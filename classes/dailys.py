#Import Needed Classes:
import os #Used for normalizing pyton strings like folders wich use "/" in folder instead of "\" when running on windows debug server
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range
from pyamf.remoting.client import RemotingService #Pyamf class used for amf request (slightly edited)
from logwriter import logwriter

class dailys:
    #Initialize this class
    def __init__(self,acc,settingsmanager):
        self.settingsmanager = settingsmanager
        self.loadsettings()
        self.acc = acc
        self.pyamfhandler = RemotingService('http://www.neopets.com/amfphp/gateway.php')
        self.pyamfhandler.opener =self.acc.opener.open
        self.loghandler = logwriter(acc,settingsmanager)

    def loadsettings(self):

        #On off switches from config file
        self.anchoron = self.settingsmanager.getvalue("Dailys","ancor_on")
        self.snowageron = self.settingsmanager.getvalue("Dailys","snowager_on")
        self.fruiton = self.settingsmanager.getvalue("Dailys","fruit_on")
        self.tombolaon = self.settingsmanager.getvalue("Dailys","tombola_on")
        self.shrinon = self.settingsmanager.getvalue("Dailys","shrine_on")
        self.cocoon = self.settingsmanager.getvalue("Dailys","coco_on")
        self.dtombon = self.settingsmanager.getvalue("Dailys","dtomb_on")
        self.bagaon = self.settingsmanager.getvalue("Dailys","baga_on")
        self.fishingon = self.settingsmanager.getvalue("Dailys","fishing_on")
        self.scratch_on = self.settingsmanager.getvalue("Dailys","scratch_on")
        self.medio_on = self.settingsmanager.getvalue("Dailys","Wheel_medio_on")
        self.knol_on = self.settingsmanager.getvalue("Dailys","wheel_knolon_on")
        self.Qasalan_on = self.settingsmanager.getvalue("Dailys","Qasalan_on")



        #Last / next times , I should convert these to next times really to give more accuracy
        #Over things like a kiosk being closed (if its closed only delay for 15 mins for e.g and retry)
        #I have done this in some places but not all
        self.lastQasatime = self.settingsmanager.getvalue("timecache","lastQasatime")

        self.bagatelletime = self.settingsmanager.getvalue("timecache","lastbagatelletime")
        self.lasttombtime = self.settingsmanager.getvalue("timecache","lasttombtime")
        self.lastocotime = self.settingsmanager.getvalue("timecache","lastcocotime")
        self.lastshrinetime = self.settingsmanager.getvalue("timecache","lastshrinetime")
        self.tombolatime = self.settingsmanager.getvalue("timecache","lasttombolatime")
        self.last_fruittime = self.settingsmanager.getvalue("timecache","lastfruittime")
        self.last_anchortime = self.settingsmanager.getvalue("timecache","lastanchortime")
        self.lastnowagertime =  self.settingsmanager.getvalue("timecache","lastsnowagertime")
        self.nextscratchtime =  self.settingsmanager.getvalue("timecache","nextscratchtime")
        self.lastmediotime =  self.settingsmanager.getvalue("timecache","lastmediotime")
        self.lastknoltime =  self.settingsmanager.getvalue("timecache","lastknoltime")
        self.lastfishingtime=  self.settingsmanager.getvalue("timecache","lastfishingtime")





    def DoTick(self,mobilehandler):
        #Run a check of all dailys and process 1 if needed
        runone=0 #Only ever do 1 task per tick regardless of how many are needed
        #anchortime=  self.settingsmanager.getvalue("Dailys","lastanchortime")
     #   print "Ancor" + self.anchoron





        if self.scratch_on ==  "on": #scards
            if (time.time() > float(self.nextscratchtime) ): #Next time depends on card type here
                self.process_scratchcard()
                runone=1

                return runone

        if self.snowageron ==  "on": #Snowager
            if (time.time() - float(self.lastnowagertime) > 3600): #Snowager (every hour)
                self.process_snowager()
                runone=1

                self.lastnowagertime = time.time()
                self.settingsmanager.setvalue("timecache","lastsnowagertime" , self.lastnowagertime )
                return runone
        if self.anchoron  == "on":  #ancor management
            if (runone == 0):
               # print time.time() - float(self.last_anchortime) > 86400
                if (time.time() - float(self.last_anchortime) > 86400): #anchor  (24 Hours)

                    self.process_anchor()
                    self.last_anchortime = time.time()
                    self.settingsmanager.setvalue("timecache","lastanchortime" , self.last_anchortime )
                    runone=1
                    return runone

        if self.tombolaon  =="on": #Tombola
            if (runone == 0):
                if (time.time() - float(self.tombolatime) > 86400): #tombola  (24 Hours)
                    self.process_tombola()

                    self.tombolatime = time.time()
                    self.settingsmanager.setvalue("timecache","lasttombolatime" , self.tombolatime )
                    runone=1
        if self.fruiton  == "on":  #fruit machine
            if (runone == 0):

                if (time.time() - float(self.last_fruittime) > 86400):
                    self.process_fruitmachine()
                  #  print "Dailys Class - Processing Anchor Management"
                    self.last_fruittime = time.time()
                    self.settingsmanager.setvalue("timecache","lastfruittime" , self.last_fruittime )
                    runone=1
                    return runone

        if self.shrinon  == "on":  #coltzshrine
            if (runone == 0):

                if (time.time() - float(self.lastshrinetime) > 86400):
                    self.process_shrine()

                    self.lastshrinetime = time.time()
                    self.settingsmanager.setvalue("timecache","lastshrinetime" , self.lastshrinetime )
                    runone=1
                    return runone

        if self.cocoon  == "on":  #coco shrine
            if (runone == 0):

                if (time.time() - float(self.lastocotime) > 86400):
                    self.cocoloop()

                    self.lastocotime = time.time()
                    self.settingsmanager.setvalue("timecache","lastcocotime" , self.lastocotime )
                    runone=1
                    return runone

        if self.dtombon  == "on":  #deserted tomb
            if (runone == 0):

                if (time.time() - float(self.lasttombtime) > 86400):
                    self.process_tomb()

                    self.lasttombtime = time.time()
                    self.settingsmanager.setvalue("timecache","lasttombtime" , self.lasttombtime )
                    runone=1
                    return runone

        if self.medio_on  == "on":  #Wheel of medio
            if (runone == 0):
               # print 'rdd1'
                if (time.time() - float(self.lastmediotime) > 2400):
                   if self.spiwheelofmedio() ==1:
                       #Wheel was span as far as we know (no known logic for fail was hit)


                    self.lastmediotime = time.time()

                    self.settingsmanager.setvalue("timecache","lastmediotime" , self.lastmediotime )
                    runone=1
                    return runone

        if self.knol_on  == "on":  #Wheel of knol
            if (runone == 0):
                #print 'ee'
                if (time.time() - float(self.lastknoltime) > 86400):
                    self.spiwheelofknol()

                    self.lastknoltime = time.time()

                    self.settingsmanager.setvalue("timecache","lastknoltime" , self.lastknoltime )
                    runone=1
                    return runone



        if self.bagaon  == "on":  #bagatelle
            if (runone == 0):

                if (time.time() - float(self.bagatelletime) > 86400):
                    print 'Bagatell'
                    self.process_bagatelle()

                    self.bagatelletime = time.time()

                    self.settingsmanager.setvalue("timecache","lastbagatelletime" , self.bagatelletime )
                    runone=1
                    return runone


        if self.fishingon  == "on":  #fishing
            if (runone == 0):

                if (time.time() - float(self.lastfishingtime) > 43200):
                    #print 'fishing'
                    self.process_fishing(mobilehandler)

                    self.lastfishingtime = time.time()

                    self.settingsmanager.setvalue("timecache","lastfishingtime" , self.lastfishingtime )
                    runone=1
                    return runone


        if self.Qasalan_on  == "on":  #Qusa
            if (runone == 0):

                if (time.time() - float(self.lastQasatime) > 28800):
                    #print 'fishing'
                    self.process_Qasalan()

                    self.lastQasatime = time.time()

                    self.settingsmanager.setvalue("timecache","lastQasatime" , self.lastQasatime )
                    runone=1
                    return runone



        return runone   #Returns the default value 0 if we get here  so we know a daily did not run

    def spiwheelofmedio(self):
        print 'Spinning Wheel of medio'
        WheelService = self.pyamfhandler.getService('WheelService')
        html = WheelService.spinWheel("3")
        currtime = time.time()
        html = str(html)
        filename = self.acc.user





#Known logic so far...
        if html.find('<b>100 NP<br/>'):
            self.loghandler.writestringtofile(self.acc.user,'Wheel of medio - Won 100 NP',0)
            return 1
        elif html.find('<b>1,000 NP<br/>'):
            self.loghandler.writestringtofile(self.acc.user,'Wheel of medio - Won 1,000 NP',1)
            return 1
        elif html.find('Pterodactyl'):
            return 1
        elif html.find('<b>2,000 NP<br/>'):
            self.loghandler.writestringtofile(self.acc.user,'Wheel of medio - Won 2,000 NP',1)

            return 1

        elif html.find('<b>500 NP<br/>'):
            self.loghandler.writestringtofile(self.acc.user,'Wheel of medio - Won 100 NP',1)
            return 1
        elif html.find('Neopoints to spin this Wheel!'):
            #If the user has option keepnp on hand = True then this should never happen if it does , then they do not have this option on
            #and have turned off withdraw np so just exit and wait
            return 1


        else:
            #unknown result save a html snapshot
            filename = "WheelOfMedio" + self.acc.user + '_' +  str(time.time())
            self.writestringtofile(filename,html)
            return 0






    def spiwheelofextrav(self):
        print 'Spinning Wheel of extrav'
        WheelService = self.pyamfhandler.getService('WheelService')
        html = WheelService.spinWheel("6")
        filename = "WheelOfextrav" + self.acc.user + '_' +  str(time.time())
        self.writestringtofile(filename,html)


    def spiwheelofmisfort(self):
        print 'Spinning Wheel of misfort'
        WheelService = self.pyamfhandler.getService('WheelService')
        html = WheelService.spinWheel("4")
        self.writestringtofile(filename,html)
        filename = "WheelOfextrav" + self.acc.user + '_' +  str(time.time())



    def spiwheelofknol(self):
        print 'Spinning Wheel of Knol'
        WheelService = self.pyamfhandler.getService('WheelService')
        html = WheelService.spinWheel("1")
        strhtml = str(html)
        filename = "WheelOfknol" + self.acc.user + '_' +  str(time.time())


        if strhtml.find('t have enough Neopoints'):
            return 1

        if strhtml.find('Your Neopet has been healed'):
            #Not worth logging
            return 1



        self.writestringtofile(filename,strhtml)

    def spinwheelofexcite(self):
        print 'Spinning Wheel of Excitement'
        WheelService = self.pyamfhandler.getService('WheelService')
        html = WheelService.spinWheel("2")
        filename = "WheelOfexcite" + self.acc.user + '_' +  str(time.time())

        self.writestringtofile(filename,html)
    def BuyDesertScratchCard(self):
        #Buy a desert scratch card
        #http://www.neopets.com/desert/sc/kiosk.phtml
        html = self.acc.get("http://www.neopets.com/desert/sc/kiosk.phtml","http://www.neopets.com/desert/sc/kiosk.phtml")
        #print html
        pos1=  html.find('_ref_ck')
        startpos = html.find('value=',pos1) +7
        endpos = html.find("'",startpos)
        theck = html[startpos:endpos]
        postdata = {'buy': "1", "_ref_ck": theck}
        html = self.acc.post("http://www.neopets.com/desert/sc/kiosk.phtml" , postdata ,"http://www.neopets.com/desert/sc/kiosk.phtml")
        self.nextscratchtime = time.time() + 14400
        self.settingsmanager.setvalue("timecache","nextscratchtime" , self.nextscratchtime  )
        if html.find('even get a booby prize!'):

            self.loghandler.writestringtofile(self.acc.user,'Scratch buyer - got a Scorched Treasure Scratchcard',0)
            return 1





        filename = "Scratch_Desert_" + self.acc.user + '_' +  str(time.time())


        self.writestringtofile(filename,html)

        #print html


    def process_scratchcard(self):
        #Todo , add some logic here to ranomize card type
        print self.scratch_on
        self.BuyDesertScratchCard()





    def process_Qasalan(self):
        print "Qasalan"

        postdata ={'r' : str(random.randrange(0,9999))}
        html = self.acc.post("http://www.neopets.com/games/giveaway/process_giveaway.phtml",postdata,"http://images.neopets.com/games/g905_v3_99390.swf")
        filename = "Qas" + self.acc.user + '_' +  str(time.time())

        self.writestringtofile(filename,html)



    def process_fruitmachine(self):

        #Fruit Machine

        print "Fruit Machine"

        html = self.acc.get("http://www.neopets.com/desert/fruit/index.phtml","http://www.thedailyneopets.com/dailies/")

        startpos = html.find('"ck" value="') +12
        endpos = html.find('"',startpos)
        theck = html[startpos:endpos]
        postdata = {'spin': "1", "ck": theck}
        html = self.acc.post("http://www.neopets.com/desert/fruit/index.phtml" , postdata ,"http://www.neopets.com/desert/fruit/index.phtml")
        filename = "FruitMachine" + self.acc.user + '_' +  str(time.time())

        self.writestringtofile(filename,html)







    def process_snowager(self):
        print "Checking Snowager"
        html = self.acc.get("http://www.neopets.com/winter/snowager.phtml","http://www.thedailyneopets.com/dailies/")
        if (html.find ("The Snowager is awake") == -1):
            html = self.acc.get("http://www.neopets.com/winter/snowager2.phtml","http://www.neopets.com/winter/snowager.phtml")
            filename = "Snowager_" + self.acc.user + '_' +  str(time.time())

            self.writestringtofile(filename,html)
    def process_tomb(self):

    #Deserted Tomb

        print "Checking Deserted Tomb"
        html = self.acc.get("http://www.neopets.com/worlds/geraptiku/process_tomb.phtml","http://www.neopets.com/worlds/geraptiku/tomb.phtml")
        filename = "Dtomb_" + self.acc.user + '_' +  str(time.time())
        self.writestringtofile(filename,html)


    def process_anchor(self):


         #self.anchortime = time.time()
         #self.newsql.setsetting("lastanchortime",time.time()) #Save Settings


         html = self.acc.get("http://www.neopets.com/pirates/anchormanagement.phtml","http://www.thedailyneopets.com/dailies/")
         startpos = html.find("form-fire-cannon") #Few words before id
         #print startpos
         startpos2 = html.find('value="',startpos) +7
         endpos = html.find('"',startpos2)
         thekey= html[startpos2:endpos]
         postdata = {"action": thekey}
         html = self.acc.post("http://www.neopets.com/pirates/anchormanagement.phtml" , postdata )

         if html.find('Treasure Map Negg'):
            self.loghandler.writestringtofile(self.acc.user,'Anchor Management Grabbed Treasure Map Negg',0)
            return 1


         filename = "Anchor" + self.acc.user + '_' +  str(time.time())

         self.writestringtofile(filename,html)
    def process_tombola(self):
        #Tombola
        print "Checking tombola"

        html = self.acc.get("http://www.neopets.com/island/tombola2.phtml","http://www.neopets.com/island/tombola.phtml")
        if html.find('even get a booby prize!'):
            self.loghandler.writestringtofile(self.acc.user,'Tombola - no win :(',0)
            return 1


        filename = "Tombola" + self.acc.user + '_' +  str(time.time())
        self.writestringtofile(filename,html)

    def process_shrine(self):
    #Coltzans Shrine
        if (time.time() - float(self.lastshrinetime) > 86400):
            print "Coltzans Shrine"

            html = self.acc.get("http://www.neopets.com/desert/shrine.phtml?type=approach","http://www.neopets.com/desert/shrine.phtml")
            if html.find(' feels faster'):
                self.loghandler.writestringtofile(self.acc.user,'Coltzans shrine - Advanced pet speed',1)
                return 1
            filename = "shrine" + str(time.time())
            self.writestringtofile(filename,html)
    def cocoloop(self):
        Rdd=True
        while Rdd ==True:
            print "Coconut shrine"

            randnum = random.randrange(70083,79083)
            html = self.acc.get("http://www.neopets.com/halloween/process_cocoshy.phtml?cocnut=1&r=" + str(randnum),"http://www.neopets.com/halloween/coconutshy.phtml")
            print html
            if  (html.find ("No+more+throws") == -1):
               # self.lastocotime = time.time()
                break
            elif (html.find ("No+Neopoints+No+Throw")  > 1):

                break
            else:

                filename = "coco_" + self.acc.user + '_' +  str(time.time())
                self.writestringtofile(filename,html)






    def writestringtofile(self,file_name, str_to_be_written):
        #print self.outputfolder + file_name + ".htm"
        outputfolder = './logs/snapshots/'


        file_writer = open(outputfolder + file_name + ".htm", 'w')
        file_writer.write(str(str_to_be_written))
        #print ("String written successfully.")
        file_writer.close()


    def process_fishing(self,mobilehandler):
        print "getting usernames"
        userpets = mobilehandler.getpetlist()
        for pet in userpets:
            petname= pet['name']
            mobilehandler.setactivepet(petname)
            print 'Set active pet to - ' + petname
            postdata = {'go_fish': '1'}
            html = self.acc.post("http://www.neopets.com/water/fishing.phtml",postdata,'http://www.neopets.com/water/fishing.phtml')
            print "Fishing check complete for pet - "  + petname
           # print html


        print "Fishing complete for all pets , set active pet back to default - " + mobilehandler.activepetname
        mobilehandler.setactivepet(mobilehandler.activepetname)

    def process_bagatelle(self):

        while True:
            print "Bagatelle"

            randnum = random.randrange(10083,49083)
            html = self.acc.get("http://www.neopets.com/halloween//process_bagatelle.phtml?r=" + str(randnum),"http://www.neopets.com/halloween/bagatelle.phtml")




            if html.find('We+have+a+loser')>0:
                self.loghandler.writestringtofile(self.acc.user,'Bagetelle - Lost a game',0)
                return 1



            if html.find('ints=2000')>0:
                self.loghandler.writestringtofile(self.acc.user,'Bagetelle - Won 2000 np',1)
                return 1


            if html.find('ints=50')>0:
                self.loghandler.writestringtofile(self.acc.user,'Bagetelle - Won 50 np',0)
                return 1


            if html.find("+let+somebody+else") > 1:

                break

            elif html.find("+afford+to+play%") > 1:

                break
            else:
                print html
                filename = "baga" + self.acc.user + '_' +  str(time.time())
                self.writestringtofile(filename,html)






