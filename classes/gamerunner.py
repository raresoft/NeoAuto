#Run a game if we need to handles:
import time
from logwriter import logwriter
from classes.cliffhanger import cliffhanger

#Cliffhanger

class gamerunner:


    def __init__(self,acc,settingsmanager,mobilehandler):
        self.settingsmanager = settingsmanager
        self.loadsettings()
        self.acc = acc
        self.mobilehandler = mobilehandler

        self.loghandler = logwriter(acc,settingsmanager)
        self.cliffhangerhandler = cliffhanger(self.acc,self.settingsmanager,self.mobilehandler)
    def loadsettings(self):

        #On off switches from config file
        self.lastcliffhangertime = self.settingsmanager.getvalue("timecache","cliffhangertime")

    def rungames(self):
        #Run any game we need to
        doneone=0
        self.loadsettings()
        if self.cliffhangerhandler.cliffhangeron == 'on':
            if (time.time() - float(self.lastcliffhangertime) > 86400):
                self.cliffhangerhandler.tick()


