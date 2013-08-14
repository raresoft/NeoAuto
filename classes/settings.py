



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
            print "creating new cache file based on ./cache/default.cfg"

            default_ancor_on = self.getDefaultvalue('Dailys','ancor_on')
            default_lastsnowagertime = self.getDefaultvalue('timecache','lastsnowagertime')
            default_snowager_on = self.getDefaultvalue('Dailys','snowager_on')
            
            default_lastbagatelletime = self.getDefaultvalue('timecache','lastbagatelletime')

            default_lasttombolatime = self.getDefaultvalue('timecache','lasttombolatime')
            default_lasttombtime = self.getDefaultvalue('timecache','lasttombtime')
            default_lastcocotime = self.getDefaultvalue('timecache','lastcocotime')
            default_lastshrinetime = self.getDefaultvalue('timecache','lastshrinetime')
            default_lastanchortime = self.getDefaultvalue('timecache','lastanchortime')
            default_lastfruittime = self.getDefaultvalue('timecache','lastfruittime')

            default_lastSDBtime = self.getDefaultvalue('timecache','lastSDBtime')

            
            default_coco_on = self.getDefaultvalue('Dailys','coco_on')
            default_shrine_on = self.getDefaultvalue('Dailys','shrine_on')
            default_tombola_on = self.getDefaultvalue('Dailys','tombola_on')
            
            default_dtomb_on = self.getDefaultvalue('Dailys','dtomb_on')

            default_selllist = self.getDefaultvalue('Settings','selllist')
            default_baga_on = self.getDefaultvalue('Dailys','baga_on')
            default_fruit_on = self.getDefaultvalue('Dailys','fruit_on')
          
            # add the settings to the structure of the file, and lets write it out...
            confighandler.add_section('Dailys')
            confighandler.add_section('timecache')
            confighandler.add_section('Settings')
            #default value set low to make sure a trigger exetues on first run
            confighandler.set('Settings',"selllist", default_selllist)
           # confighandler.set('Settings',"selllist", default_selllist)
            confighandler.set('timecache',"lastanchortime", default_lastanchortime)
            confighandler.set('timecache','lastfruittime', default_lastfruittime)
            
            confighandler.set('timecache','lastcocotime', default_lastcocotime)
            confighandler.set('timecache','lastsnowagertime', default_lastsnowagertime)
            confighandler.set('timecache','lasttombtime', default_lasttombtime)
            confighandler.set('timecache','lastshrinetime', default_lastshrinetime )
            confighandler.set('timecache','lasttombolatime', default_lasttombolatime)
            confighandler.set('timecache','lastbagatelletime', default_lastbagatelletime)
            
            confighandler.set('Dailys','shrine_on', default_shrine_on)
            confighandler.set('Dailys','ancor_on', default_ancor_on)
            confighandler.set('Dailys','snowager_on', default_snowager_on)
            confighandler.set('Dailys','coco_on', default_coco_on)
            confighandler.set('Dailys','tombola_on', default_tombola_on)
            confighandler.set('Dailys','dtomb_on', default_dtomb_on)
            confighandler.set('Dailys','baga_on', default_baga_on)
            confighandler.set('Dailys','fruit_on', default_fruit_on)

            confighandler.set('timecache','lastSDBtime', default_lastSDBtime)
            
            with open("./cache/" + username + ".cfg",'w') as cfgfile:
                confighandler.write(cfgfile)
                cfgfile.close()

    def getDefaultvalue(self,Section,value):
        config2 = ConfigParser.ConfigParser()
        config2.read("./cache/default.cfg")
#print os.path.isfile("../cache/default.cfg")
        # Set the third, optional argument of get to 1 if you wish to use raw mode.
        return config2.get(Section, value, 0) 


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




