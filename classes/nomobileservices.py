#This module is a clone of mobileservices.py but without using the mobile functions
#This is used if mobileservices is off

#Import Needed Classes:
import os #Used for normalizing pyton strings like folders wich use "/" in folder instead of "\" when running on windows debug server
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range
from pyamf.remoting.client import RemotingService #Pyamf class used for amf request (slightly edited)


class nomobileservices:

    def getactivepet(self):


        CustomPetService = self.pyamfhandler.getService('CustomPetService')

        html = CustomPetService.getUserData(self.acc.user)

        return html['active_pet']




    def __init__(self,acc,settingsmanager):
        self.acc = acc
        self.pyamfhandler = RemotingService('http://www.neopets.com/amfphp/gateway.php')
        self.pyamfhandler.opener =self.acc.opener.open



        self.activepetname =self.getactivepet()







    def getnp(self):
        #Get Np on hand
        retnp = 0
        temphtml = self.acc.get('http://www.neopets.com/objects.phtml')


        if temphtml.find("id='npanchor") > 1:
            startpos = temphtml.find("id='npanchor")
            startpos2 = self.acc.cleanhtml.find("'>",startpos) +2
            endpos = temphtml.find('</a>',startpos2)
            tempnp = temphtml[startpos2:endpos]

            tempnp = tempnp.replace(',','')
            retnp =tempnp
        return retnp


    def getpetlist(self):


        PetService = self.pyamfhandler.getService('PetService')

        html = PetService.getAllPets(self.acc.user)

        return html

    def setactivepet(self,petname):

        html = self.acc.get('http://www.neopets.com/process_changepet.phtml?new_active_pet=' + petname,'http://www.neopets.com/quickref.phtml')




