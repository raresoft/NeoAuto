#Import Needed Classes:
import os #Used for normalizing pyton strings like folders wich use "/" in folder instead of "\" when running on windows debug server
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range
from pyamf.remoting.client import RemotingService #Pyamf class used for amf request (slightly edited)


class mobileservices:
    #Initialize this class
    def __init__(self,acc,settingsmanager):
        self.usemobileservices = settingsmanager.getvalue("Settings","usemobileservices")

        if   self.usemobileservices == 'on':
            self.acc = acc
            self.pyamfhandler = RemotingService('http://www.neopets.com/amfphp/gateway.php')
            self.pyamfhandler.opener =self.acc.opener.open
            self.token = self.domobilelogin()
            print "Mobile login token = " + str(self.token)

    def getnp(self):
        #Get Np on hand
        MobileService = self.pyamfhandler.getService('MobileService')
        html = MobileService.getUser(self.acc.user,self.token)
        thenp = html['neopoints']

        return thenp

    def domobilelogin(self):
        #print self.acc.user
        #print self.acc.pw
        print "Performing mobile auth"
        MobileService = self.pyamfhandler.getService('MobileService')
        html = MobileService.auth(self.acc.user,self.acc.pw)
        #print html
        self.activepetname =html['user']['active_pet']

        return html['token']



    def setactivepet(self,petname):


        PetService = self.pyamfhandler.getService('PetService')

        #activepetname
        html = PetService.setActivePet(petname,self.acc.user,self.token)

        return html



    def getpetlist(self):


        MobileService = self.pyamfhandler.getService('MobileService')

        html = MobileService.getPets(self.acc.user,self.token)

        return html

