#Import Needed Classes:
import os #Used for normalizing pyton strings like folders wich use "/" in folder instead of "\" when running on windows debug server
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range 
#import sqllink # Sql link used to connect to the sql database


class dailys:
    #Initialize this class
    def __init__(self,acc,settingsmanager):
        self.settingsmanager = settingsmanager
        self.loadsettings()
        self.acc = acc
    def loadsettings(self):
        
        #On off switches
        self.anchoron = self.settingsmanager.getvalue("Dailys","ancor_on")
        self.snowageron = self.settingsmanager.getvalue("Dailys","snowager_on")
        self.fruiton = self.settingsmanager.getvalue("Dailys","fruit_on")        
        self.tombolaon = self.settingsmanager.getvalue("Dailys","tombola_on")  
        self.shrinon = self.settingsmanager.getvalue("Dailys","shrine_on")
        self.cocoon = self.settingsmanager.getvalue("Dailys","coco_on")
        self.dtombon = self.settingsmanager.getvalue("Dailys","dtomb_on")
        self.bagaon = self.settingsmanager.getvalue("Dailys","baga_on")

        

        #Dailys times  fruit_on
        self.bagatelletime = self.settingsmanager.getvalue("Dailys","lastbagatelletime")        
        self.lasttombtime = self.settingsmanager.getvalue("Dailys","lasttombtime") 
        self.lastocotime = self.settingsmanager.getvalue("Dailys","lastcocotime") 
        self.lastshrinetime = self.settingsmanager.getvalue("Dailys","lastshrinetime") 
        self.tombolatime = self.settingsmanager.getvalue("Dailys","lasttombolatime")           
        self.last_fruittime = self.settingsmanager.getvalue("Dailys","lastfruittime")   
        self.last_anchortime = self.settingsmanager.getvalue("Dailys","lastanchortime")
        self.lastnowagertime =  self.settingsmanager.getvalue("Dailys","lastsnowagertime")




    def process_fruitmachine(self):

        #Fruit Machine
    
        print "Fruit Machine"

        html = self.acc.get("http://www.neopets.com/desert/fruit/index.phtml","http://www.thedailyneopets.com/dailies/")
        
        startpos = html.find('"ck" value="') +12
        endpos = html.find('"',startpos)
        theck = html[startpos:endpos]
        postdata = {'spin': "1", "ck": theck}
        html = self.acc.post("http://www.neopets.com/desert/fruit/index.phtml" , postdata ,"http://www.neopets.com/desert/fruit/index.phtml")





        
    def writestringtofile(self,file_name, str_to_be_written):
        print self.outputfolder + file_name + ".htm"
        #str_to_be_written.replace(".js","")
        file_writer = open(self.outputfolder + file_name + ".htm", 'w')
        file_writer.write(str(str_to_be_written))
        #print ("String written successfully.")
        file_writer.close()

      
        
    def process_snowager(self):
        print "Checking Snowager"
        html = self.acc.get("http://www.neopets.com/winter/snowager.phtml","http://www.thedailyneopets.com/dailies/")
        if (html.find ("The Snowager is awake") == -1):       
            html = self.acc.get("http://www.neopets.com/winter/snowager2.phtml","http://www.neopets.com/winter/snowager.phtml")
          
    def process_tomb(self):

    #Deserted Tomb

        print "Checking Deserted Tomb"
        
        html = self.acc.get("http://www.neopets.com/worlds/geraptiku/process_tomb.phtml","http://www.neopets.com/worlds/geraptiku/tomb.phtml")
        



            
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
         html = self.acc.post("http://www.neopets.com/pirates/anchormanagement.phtml" , postdata ,"http://www.thedailyneopets.com/dailies/")

    def process_tombola(self):
        #Tombola
        print "Checking tombola"
        
        html = self.acc.get("http://www.neopets.com/island/tombola2.phtml","http://www.neopets.com/island/tombola.phtml")
        
        
    def process_shrine(self):
    #Coltzans Shrine
        if (time.time() - float(self.lastshrinetime) > 86400):
            print "Coltzans Shrine"
            
            html = self.acc.get("http://www.neopets.com/desert/shrine.phtml?type=approach","http://www.neopets.com/desert/shrine.phtml")


    def cocoloop(self):
        while True:
            print "Coconut shrine"
            time.sleep(2)
            randnum = random.randrange(70083,79083)
            html = self.acc.get("http://www.neopets.com/halloween/process_cocoshy.phtml?cocnut=1&r=" + str(randnum),"http://www.neopets.com/halloween/coconutshy.phtml")
            print html
            if  (html.find ("No+more+throws") == -1):
                self.lastocotime = time.time()
                break
            elif (html.find (" No+Neopoints+No+Throw")  > 1):
                self.lastocotime = time.time()
                break               
    
    def process_bagatelle(self):

        while True:
            print "Bagatelle"
        
            randnum = random.randrange(10083,49083)
            html = self.acc.get("http://www.neopets.com/halloween//process_bagatelle.phtml?r=" + str(randnum),"http://www.neopets.com/halloween/bagatelle.phtml")
            print html
            time.sleep(2)
            if html.find("+you+let+somebody+else+play") > 1:

                break
            if html.find("+afford+to+play%") > 1:

                break





    def DoTick(self):
        #Run a check of all dailys and process 1 if needed
        runone=0 #Only ever do 1 task per tick regardless of how many are needed
        #anchortime=  self.settingsmanager.getvalue("Dailys","lastanchortime")
     #   print "Ancor" + self.anchoron

        if self.snowageron ==  "on": #Snowager    
            if (time.time() - float(self.lastnowagertime) > 3600): #Snowager (every hour)
                self.process_snowager()
                runone=1
                
                self.lastnowagertime = time.time()
                self.settingsmanager.setvalue("Dailys","lastsnowagertime" , self.lastnowagertime )
                return runone
        if self.anchoron  == "on":  
            if (runone == 0):
               # print time.time() - float(self.last_anchortime) > 86400
                if (time.time() - float(self.last_anchortime) > 86400): #anchor  (24 Hours)

                    self.process_anchor()
                    self.last_anchortime = time.time()
                    self.settingsmanager.setvalue("Dailys","lastanchortime" , self.last_anchortime )
                    runone=1
                    return runone

        if self.tombolaon  =="on": #Tombola        
            if (runone == 0):
                if (time.time() - float(self.tombolatime) > 86400): #tombola  (24 Hours)
                    self.process_tombola()
                    
                    self.tombolatime = time.time()
                    self.settingsmanager.setvalue("Dailys","lasttombolatime" , self.tombolatime )
                    runone=1
        if self.fruiton  == "on":  
            if (runone == 0):
      
                if (time.time() - float(self.last_fruittime) > 86400): 
                    self.process_fruitmachine()
                  #  print "Dailys Class - Processing Anchor Management"
                    self.last_fruittime = time.time()
                    self.settingsmanager.setvalue("Dailys","lastfruittime" , self.last_fruittime )
                    runone=1
                    return runone
                
        if self.shrinon  == "on":  
            if (runone == 0):
      
                if (time.time() - float(self.lastshrinetime) > 86400): 
                    self.process_shrine()
                  
                    self.lastshrinetime = time.time()
                    self.settingsmanager.setvalue("Dailys","lastshrinetime" , self.lastshrinetime )
                    runone=1
                    return runone

        if self.cocoon  == "on":  
            if (runone == 0):
      
                if (time.time() - float(self.lastocotime) > 86400): 
                    self.cocoloop()
                  
                    self.lastocotime = time.time()
                    self.settingsmanager.setvalue("Dailys","lastcocotime" , self.lastocotime )
                    runone=1
                    return runone
                
        if self.dtombon  == "on":  
            if (runone == 0):
      
                if (time.time() - float(self.lasttombtime) > 86400): 
                    self.process_tomb()
                  
                    self.lasttombtime = time.time()
                    self.settingsmanager.setvalue("Dailys","lasttombtime" , self.lasttombtime )
                    runone=1
                    return runone 

        if self.bagaon  == "on":  
            if (runone == 0):
      
                if (time.time() - float(self.bagatelletime) > 86400): 
                    self.process_bagatelle()
                  
                    self.bagatelletime = time.time()
                    self.settingsmanager.setvalue("Dailys","lastbagatelletime" , self.bagatelletime )
                    runone=1
                    return runone 
                
        return runone   #Returns the default value 0 if we get here  so we know a daily did not run   



