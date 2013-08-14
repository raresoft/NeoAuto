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

from classes.InventoryManager import InventoryManager


from pyamf.remoting.client import RemotingService #Pyamf class used for amf request (slightly edited)
from classes.NeoAccount import NeoAccount
from classes.settings import settings
from classes.dailys import dailys
from classes.habi import habi
######################################################End Imports##################################################


strcookie= []
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CJ))


debugmode =1


if debugmode == 1:
    neouser = ""
    neopass = ""

 

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


settigsfile =  settingsmanager.getvalue("Settings","selllist")
inventorymanager = InventoryManager(acc,settigsfile,settingsmanager)
#we logged into a account so lets load settings...
#settingsmanager.loadsettings() #Loads the current accounts settings from the /cache/folder or makes a new file if one doesn't exist...

lastlogintime = time.time()

pyamfhandler = RemotingService('http://habitarium.neopets.com/amfphp/gateway.php')
#print neouser
habihander = habi(acc,pyamfhandler) #Setup habi hander module
dailyshander =  dailys(acc,settingsmanager) #Setup dailys hander module
test = 1
while test ==1:
    if dailyshander.DoTick() == 0:# Nothing was done
      
        if inventorymanager.checktick() == 1:#Check if a Deposit all tick is needed  , return 0 if not
            #Nothing done fall back to next task
            print "Processed SDB tick"
              
        else:
            #We did nothing at all , fallback to habi
           #print "Should do habi here"
           habihander.DoLoop()
    time.sleep(10)
    print "tick"
