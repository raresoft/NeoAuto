#Auto Battle by raredaredevil aka DarkByte
#Currently targeted towards  punchbag bob only





class battle:
    def __init__(self,acc,mobilehandler,settingsmanager):
        self.acc = acc
        self.mobilehandler = mobilehandler

    def geteligibalstate(self):
        #Returns a list:
        #['Petname']['Eligibal to battle']
        #For all pets
        #If the target pet is not eligable we can skip a tick , wait for auto hotel if its enabled to do its thing
        #and await next time when our pet should be full stats and now eligable to battle.

        print 'Getting Eligibale list'


    def startbattle(enemyname):
        #Start a battle with X enemy and load battle logic from ./list/battle/logic/enemyname.txt
        print "Loading battle logic for " + enemyname


