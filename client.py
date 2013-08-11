######################################################
################NeoAuto BETA - RareDareDevil##########
######################################################
############Open Source Neopets Automation############
######################################################

######################################################Imports######################################################
import urllib2, re
from cookielib import CookieJar


from urllib import urlencode
import urllib
CJ=CookieJar()
import threading
import sys
import time
import random

import ConfigParser
config1 = ConfigParser.RawConfigParser()

from classes.NeoAccount import NeoAccount
from classes.settings import settings
from classes.dailys import dailys
######################################################End Imports##################################################


strcookie= []
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CJ))


debugmode =1


if debugmode == 1:
    neouser = "USERNAMEHERE"
    neopass = "PASSWORDHERE"

 

else:
   #None debug mode takes command args , usefull for vps servers ect
   #python /client.bin -username -password
    if len(sys.argv) == 1:
        print "Debug mode was turned off , but no args sent , so i fell back to debug mode."
        debugmode=1
    else:
        neouser = sys.argv[1] #or get the info from command line interface eg:
        neopass = sys.argv[2]

        


acc = NeoAccount(neouser,neopass)

acc .login()
settingsmanager = settings(acc.user)
#we logged into a account so lets load settings...
#settingsmanager.loadsettings() #Loads the current accounts settings from the /cache/folder or makes a new file if one doesn't exist...

lastlogintime = time.time()


#print neouser
dailyshander =  dailys(acc,settingsmanager) #Setup dailys hander module
test = 1
while test ==1:
    dailyshander.DoTick()
    time.sleep(10)
    print "tick"
