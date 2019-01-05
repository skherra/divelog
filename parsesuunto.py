from bs4 import BeautifulSoup
from img import pngprofile
import os
import glob
import logging
from datetime import date
import yaml
import re
import sys

logging.basicConfig(filename='{}.log'.format(date.today()), level=logging.DEBUG, format='%(asctime)s :: %(levelname)s :: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )

#Parse le SML SUUNTO et genere le Markedown en resultat
def wlogbook(pathsamples,pathlogs,listdir, suunto):
    for x in range(len(listdir)):
        os.chdir(pathsamples)
        fp = open(listdir[x]).read().lower()
        soup = BeautifulSoup(fp, 'lxml')

        airstart=""
        conso=""
        deco=""
        #Particularites du SML EONCORE
        if (suunto == "EONCORE"):
            if (soup.find("startpressure") == None):
                airstart=0
            else :
                airstart= float(soup.find("startpressure").string) / 100000
            if (soup.find("endpressure") == None):
                airstop =0
            else :
                airstop = float(soup.find("endpressure").string) / 100000
            conso=airstart-airstop
        #Particularites du SML D6I
        if (suunto == "D6I"):
            if (soup.find("usedpressure") == None):
                conso = 0
            else :
                conso=float(soup.find("usedpressure").string) / 100000
            if (soup.find("tankpressure") == None):
                airstart = 0
            else :
                airstart=float(soup.find("tankpressure").string) / 100000
        duree = round(float(soup.find("duration").string)/60, 2)
        oxygen = round(float(soup.find('oxygen').string)*100)

        #Format du nom de fichier MD
        date = soup.find('datetime').string[:16]
        year = date[:4]
        month = date[5:7]
        day =date[8:10]
        hour =date[11:13]
        minute = date[14:]
        datefile = year+month+day+"_"+hour+"-"+minute

        #new deco
        notifyall = soup.findAll("notify")

        for i in range(len(notifyall)):
            if (notifyall[i].type != None ):
                if (notifyall[i].type.string == "deco"):
                    deco = notifyall[i].type.string

        os.chdir(pathlogs)
        logBook = datefile+"_"+suunto+".md"
        filename = datefile+"_"+suunto
        logBook = filename+".md"

        #si le fichier existe deja skip
        if (logBook in os.listdir(pathlogs)):
            logging.warning("file {} already exist in {}".format(logBook, pathlogs))
        else :
            pngprofile(soup, datefile+"_"+suunto, suunto)
            file = open(logBook, 'w', encoding='utf-8')
            file.write("**DateTime :** {}".format(datefile))
            file.write("\n")
            file.write("**Dive Number :**")
            file.write("\n")
            file.write("**Country :**")
            file.write("\n")
            file.write("**Dive site :**")
            file.write("\n")
            surfacetime = ""
            if (soup.find('surfacetime') != None):
                surfacetime = round(float(soup.find('surfacetime').string)/3600)
            file.write("**Surface Time :** {} h".format(surfacetime))
            file.write("\n")
            #new deco
            if (deco != ""):
                file.write("**Plongée avec deco**")
                file.write("\n")
            file.write("**Duration :** {} min".format(duree))
            file.write("\n")
            file.write("**Dive Mode :** {} {} %".format(soup.find('divemode').string ,oxygen))
            file.write("\n")
            file.write("**Air :** {} bar".format(round(airstart, 1)))
            file.write("\n")
            file.write("**Consommation :** {} bar".format(round(conso)))
            file.write("\n")
            file.write("**Profondeur Max :** {} m".format(round(float(soup.find('max').string))))
            file.write("\n")
            file.write("**Profondeur Moyenne :** {} m".format(round(float(soup.find('avg').string))))
            file.write("\n")
            file.write("**Current :**")
            file.write("\n")
            file.write("**Visibility :**")
            file.write("\n")
            file.write("**Weight (kg) :**")
            file.write("\n")
            file.write("**Tank (Alu-Steel) :**")
            file.write("\n")
            file.write("**Weetsuit (mm) :**")
            file.write("\n")
            file.write("\n")
            file.write("---------------------------------------------")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("![ ]("+"./"+filename+".png"+")")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("---------------------------------------------")
            file.write("\n")
            file.write("**Description :**")
            file.write("\n")
            file.write("**Fishs :**")
            logging.info("New file {} updated in {}".format(logBook, pathlogs))

#Appel la fonction wlogbook
def  call_wlogbook(pathlogsuunto, pathsamplesuunto, modele):
    pathlogs = config[pathlogsuunto]
    pathsamples = config[pathsamplesuunto]
    os.chdir(pathsamples)
    listdir=glob.glob('*.sml')
    wlogbook(pathsamples, pathlogs, listdir, modele)

if __name__ == '__main__':
    config = yaml.load(open('config.yaml'))
    if (len(sys.argv) > 1):
        ordi = sys.argv[1]
        if (ordi == "D6I"):
            call_wlogbook("LOGSD6I", "SAMPLESD6I", "D6I")

        elif (ordi == "EONCORE"):
            call_wlogbook("LOGSEONCORE", "SAMPLESEONCORE", "EONCORE")
    else :
        call_wlogbook("LOGSD6I", "SAMPLESD6I", "D6I")
        call_wlogbook("LOGSEONCORE", "SAMPLESEONCORE", "EONCORE")
