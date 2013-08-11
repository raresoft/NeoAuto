



#Import Needed Classes:
import os #Used for normalizing pyton strings like folders wich use "/" in folder instead of "\" when running on windows debug server
import ConfigParser # Config parser class (.cfg files)
import os.path



#Setup Default vars / classes
confighandler = ConfigParser.RawConfigParser() #Used for .cfg files





#Begin Class
class settings:

    #Initialize this class
    def __init__(self,username):
        self.username =username
        #Class Entry point , make sure the config file for username exist
        if not os.path.isfile("./cache/" + username + ".cfg") :
            print "creating new cache file"


            # add the settings to the structure of the file, and lets write it out...
            confighandler.add_section('Dailys')
            #default value set low to make sure a trigger exetues on first run
            confighandler.set('Dailys','lastanchortime', 0)
            confighandler.set('Dailys','lastfruittime', 0)
            confighandler.set('Dailys','ancor_on', "on")
            confighandler.set('Dailys','lastsnowagertime', 0)
            confighandler.set('Dailys','snowager_on', "on")
            confighandler.set('Dailys','lastshrinetime', 0)
            confighandler.set('Dailys','shrine_on', "on")
            confighandler.set('Dailys','lastcocotime', 0)
            confighandler.set('Dailys','coco_on', "on")
            confighandler.set('Dailys','lasttombtime', 0)
            confighandler.set('Dailys','tombola_on', "on")
            confighandler.set('Dailys','lasttombolatime', 0)
            confighandler.set('Dailys','dtomb_on', "on")
            confighandler.set('Dailys','lastbagatelletime', 0)
            confighandler.set('Dailys','baga_on', "on")
            confighandler.set('Dailys','fruit_on', "on")            
            with open("./cache/" + username + ".cfg",'w') as cfgfile:
                confighandler.write(cfgfile)
                cfgfile.close()




    def getvalue(self,Section,value):
        config = ConfigParser.ConfigParser()
        config.read("./cache/" + self.username + ".cfg")

        # Set the third, optional argument of get to 1 if you wish to use raw mode.
        return config.get(Section, value, 0) 

    def setvalue(self,Section,value,val):
        config= ConfigParser.RawConfigParser()
        config.read(r"./cache/" + self.username + ".cfg")
        config.set(Section, value, val )
        with open(r"./cache/" + self.username + ".cfg", 'wb') as configfile:
            config.write(configfile)




