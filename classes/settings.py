



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



            default_autoprice_file = self.getDefaultvalue('shop','autoprice_file')
            default_autoprice = self.getDefaultvalue('shop','autoprice')
            default_withdrawtill = self.getDefaultvalue('shop','withdrawtill')
            default_lastsnowagertime = self.getDefaultvalue('timecache','lastsnowagertime')
            default_snowager_on = self.getDefaultvalue('Dailys','snowager_on')
            default_Wheel_medio_on = self.getDefaultvalue('Dailys','Wheel_medio_on')
            default_wheel_knolon_on = self.getDefaultvalue('Dailys','wheel_knolon_on')
            default_Qasalan_on = self.getDefaultvalue('Dailys','Qasalan_on')

            default_loglevel = self.getDefaultvalue('misc','loglevel')
            default_avatargrabber = self.getDefaultvalue('misc','avatargrabber')



            default_ancor_on = self.getDefaultvalue('Dailys','ancor_on')

            default_lastQasatime = self.getDefaultvalue('timecache','lastQasatime')
            default_minnponhand = self.getDefaultvalue('bank','minnponhand')

            default_withdrawamount = self.getDefaultvalue('bank','withdrawamount')
            default_traineron = self.getDefaultvalue('trainer','trainpets')

            default_lastshoptime = self.getDefaultvalue('timecache','lasttilltime')

            default_lastpricetime = self.getDefaultvalue('timecache','lastpricetime')


            default_lastavatartime = self.getDefaultvalue('timecache','avatartime')

            default_lastbagatelletime = self.getDefaultvalue('timecache','lastbagatelletime')
            default_nextscratchtime = self.getDefaultvalue('timecache','nextscratchtime')
            default_lastknoltime = self.getDefaultvalue('timecache','lastknoltime')
            default_lastmediotime = self.getDefaultvalue('timecache','lastmediotime')



            default_fishing_on = self.getDefaultvalue('Dailys','fishing_on')
            default_lastfishingtime = self.getDefaultvalue('timecache','lastfishingtime')




            default_lasttombolatime = self.getDefaultvalue('timecache','lasttombolatime')
            default_lasttombtime = self.getDefaultvalue('timecache','lasttombtime')
            default_lastcocotime = self.getDefaultvalue('timecache','lastcocotime')
            default_lastcliffhangertime = self.getDefaultvalue('timecache','cliffhangertime')

            default_lastshrinetime = self.getDefaultvalue('timecache','lastshrinetime')
            default_lastanchortime = self.getDefaultvalue('timecache','lastanchortime')
            default_lastfruittime = self.getDefaultvalue('timecache','lastfruittime')


            default_usemobileservices = self.getDefaultvalue('Settings','usemobileservices')

            default_sellist = self.getDefaultvalue('Settings','depositlist')
            default_lastSDBtime = self.getDefaultvalue('timecache','lastSDBtime')

            default_withdrawamount = self.getDefaultvalue('bank','withdrawamount')



            default_minnponhand = self.getDefaultvalue('bank','minnponhand')
            default_coco_on = self.getDefaultvalue('Dailys','coco_on')
            default_shrine_on = self.getDefaultvalue('Dailys','shrine_on')
            default_tombola_on = self.getDefaultvalue('Dailys','tombola_on')
            default_dtomb_on = self.getDefaultvalue('Dailys','dtomb_on')
            default_depositlist = self.getDefaultvalue('Settings','depositlist')

            default_baga_on = self.getDefaultvalue('Dailys','baga_on')
            default_scratch_on = self.getDefaultvalue("Dailys","scratch_on")
            default_fruit_on = self.getDefaultvalue('Dailys','fruit_on')
            default_scratch_mode = self.getDefaultvalue('Scratchcard','scratch_mode')
            default_lastalton = self.getDefaultvalue('misc','altador_on')
            default_altador_stage = self.getDefaultvalue('misc','altador_stage')

            default_bankon = self.getDefaultvalue('bank','checknp_on')
            default_cliffhangeron = self.getDefaultvalue('games','cliffhangeron')






            # add the settings to the structure of the file, and lets write it out...
            confighandler.add_section('Dailys')

            confighandler.add_section('Settings')
            confighandler.add_section('misc')
            confighandler.add_section('bank')
            confighandler.add_section('trainer')

            confighandler.add_section('games')
            confighandler.add_section('shop')


            confighandler.add_section('nq2')
            confighandler.add_section('Scratchcard')
            confighandler.add_section('timecache')
            #elf.altador_on = self.getvalue("misc","altador_on")


            #default value set low to make sure a trigger exetues on first run
            #confighandler.set('Settings',"depositlist", default_depositlist)

            confighandler.set('timecache',"lastanchortime", default_lastanchortime)
            confighandler.set('timecache','lastfruittime', default_lastfruittime)
            confighandler.set('timecache','lastcocotime', default_lastcocotime)

            confighandler.set('timecache','cliffhangertime', default_lastcliffhangertime)
            confighandler.set('shop','withdrawtill', default_withdrawtill)
            confighandler.set('shop','autoprice', default_autoprice)
            confighandler.set('shop','autoprice_file', default_autoprice_file)

            confighandler.set('timecache','lastsnowagertime', default_lastsnowagertime)
            confighandler.set('timecache','lasttombtime', default_lasttombtime)
            confighandler.set('timecache','lastshrinetime', default_lastshrinetime )
            confighandler.set('timecache','lasttombolatime', default_lasttombolatime)
            confighandler.set('timecache','lastbagatelletime', default_lastbagatelletime)
            confighandler.set('timecache','lasttilltime', default_lastshoptime)

            confighandler.set('timecache','lastpricetime', default_lastpricetime)
            confighandler.set('timecache','lastQasatime', default_lastQasatime)
            confighandler.set('timecache','avatartime', default_lastavatartime)
            confighandler.set('bank','minnponhand', default_minnponhand)
            confighandler.set('bank','withdrawamount', default_withdrawamount)
            confighandler.set('trainer','trainpets', default_traineron)




            confighandler.set('timecache','nextscratchtime', default_nextscratchtime)
            confighandler.set('timecache','lastmediotime', default_lastmediotime)
            confighandler.set('timecache','lastfishingtime', default_lastfishingtime)


            confighandler.set('timecache','lastknoltime', default_lastknoltime)



            confighandler.set('nq2','nq2stage', "1")
            confighandler.set('nq2','nq2waypoint_x', "13")
            confighandler.set('nq2','nq2waypoint_y', "4")
            confighandler.set('Dailys','shrine_on', default_shrine_on)
            confighandler.set('Dailys','ancor_on', default_ancor_on)
            confighandler.set('misc','loglevel', default_loglevel)
            confighandler.set('misc','avatargrabber', default_avatargrabber)


            confighandler.set('Dailys','snowager_on', default_snowager_on)
            confighandler.set('Dailys','wheel_knolon_on', default_wheel_knolon_on)
            confighandler.set('Dailys','Qasalan_on', default_Qasalan_on)






            confighandler.set('Dailys','fishing_on', default_fishing_on)
            confighandler.set('Dailys','Wheel_medio_on', default_Wheel_medio_on)
            confighandler.set('Dailys','coco_on', default_coco_on)
            confighandler.set('Dailys','tombola_on', default_tombola_on)
            confighandler.set('Dailys','dtomb_on', default_dtomb_on)
            confighandler.set('Dailys','baga_on', default_baga_on)
            confighandler.set('Dailys','scratch_on', default_scratch_on)


            confighandler.set('misc','altador_stage', default_altador_stage)
            confighandler.set('bank','checknp_on', default_bankon)
            confighandler.set('games','cliffhangeron', default_cliffhangeron)


            confighandler.set('misc','altador_on', default_lastalton)
            confighandler.set('Dailys','fruit_on', default_fruit_on)
            confighandler.set('Settings','depositlist', default_depositlist)
            confighandler.set('Settings','usemobileservices', default_usemobileservices)


            confighandler.set('Scratchcard','scratch_mode', default_scratch_mode)


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




