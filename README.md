**README**

Ce script permet de parser des sml de type Suunto D6I et Suunto Eon Core (à exporter depuis l'application SUUNTO) et de fournir des Markedown de logsbook synthétiques des informations de la plongée.

**PRE-REQUIS & DEPENDANCES**

Installer python > 3.6 [Doc Python](https://www.python.org/downloads/)
Installer pip [Doc Pip](https://pip.pypa.io/en/stable/installing/)
Installer PyYaml [Doc PyYaml](https://pyyaml.org/)
Installer Beautifulsoup [Doc BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Installer bs4 [Doc BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Installer le parseur lxml
Installer matplotlib [Doc Matplotib](https://matplotlib.org/)

**Tests**
Testé sous Mac OS  et Windows 10

**CONFIG**

Le fichier config.yaml est à configurer :
2 imputs et 2 outputs avec un chemin de type D:\Projets\Python\sample ...  

LOGSD6I : Fichier Markedown en sortie du parser pour un sml LOGSD6I
LOGSEONCORE : Fichier Markedown en sortie du parser pour un sml LOGSEONCORE
SAMPLESD6I : SML source de l'ordinateur D6I
SAMPLESEONCORE : SML source de l'ordinateur EON CORE

**INPUT**

Prend les sml sources. Ne regénère pas un Markdown si le fichier est déjà existant.

**OUTPUT**

Génère des fichiers Markedown.

**EXEMPLE**

--sreanshot--

**EXECUTION**

A exécuter avec python3
Arguments :
 python parsesuunto.py  -- génère les sml des deux ordinateurs
 python parsesuunto.py D6I -- génère les sml du D6I
 python parsesuunto.py EONCORE -- génère les sml du EON Core

 **NOTE**
 
 Développé en amateur par des créateurs de bulles

 **NewRelease**
 
 2019-01 : Mention de pallier de déco obligatoire
