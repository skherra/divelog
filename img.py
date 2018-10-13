from bs4 import BeautifulSoup
import logging
from datetime import date
import yaml
import re
import matplotlib
import matplotlib.pyplot as plt



logging.basicConfig(filename='{}.log'.format(date.today()), level=logging.DEBUG, format='%(asctime)s :: %(levelname)s :: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )

#Genere un png avec trois graphs profondeur, conso et temperature
def pngprofile(soup, filename, suunto):
    depth = soup.find_all("depth")
    time = soup.find_all("time")
    temp = soup.find_all("temperature")

    if (suunto == "EONCORE"):
        pres = soup.find_all("pressure")

    if (suunto == "D6I"):
        pres = soup.find_all("tankpressure")

    i = 1
    x = 0
    d= []
    t =[]
    p =[]
    c=  []

    while i < len(depth):
        d.append(round(float(depth[i].string)*-1,2))
        t.append(round(float(time[i].string)/60,2))
        c.append(round(float(temp[x].string)-273.15,1))
        #Particularites EONCORE + traitements si zero valeurs remontees
        if (suunto == "EONCORE"):
            if (x+60 <= len(pres)):
                if (pres[x+60].string == None):
                    p.append(0)
                else:
                    p.append(float(pres[(x)+60].string)/ 100000)
            else:
                p.append(0)
        #Particularites D6I + traitements si zero valeurs remontees
        if (suunto == "D6I"):
            if (x < len(pres)):
                p.append(float(pres[x].string)/ 100000)
            else:
                p.append(0)

        i +=1
        x +=1

    plt.clf()
    plt.figure(1)
    plt.subplot(311)
    plt.plot(t, d, 'xkcd:sky blue')
    plt.title("Diving Profile")
    plt.ylabel('Deep (m)')

    plt.subplot(312)
    plt.plot(t, c, 'tab:orange')
    plt.ylabel('Temperature (C)')

    plt.subplot(313)
    plt.plot( t, p, 'tab:green')
    plt.ylabel('Pressure (Bar)')
    plt.xlabel('Time (min)')

    #plt.show() - debugg
    plt.savefig("{}.png".format(filename))
