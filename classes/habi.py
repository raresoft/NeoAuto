#------------------------------------------------
#Habi bot v2.0 Recoded
#Created by raredaredevil and a sprinkle of o.c.d
#------------------------------------------------


#Habi bot is a simulation of the packets neopets sends in a legitimate game.
#By simulating the backend packet we clone the game without ever really loading it.
#If you are intrested in how this is done , simply hook up a packet editor to a legit game
#And look at the packets it sends. All we do is simulate those packets.

#########################################################################
#2.0 Recode - Randomized map creation
            # Ranomized map selection
            # Works without resource hack (slower but it works)
            # Auto runs reshack optional for new players (option in client.py of this bot and rarebot)
            # No longer needed to load habi once on a account before using
            #Complete recode of backend
            #Auto find fix coords instead of hard coded
##########################################################################
#Import Needed Classes:
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range 
from pyamf.remoting.client import RemotingService #Pyamf class used for amf request (slightly edited)


#Setup Default vars / classes
confighandler = ConfigParser.RawConfigParser() #Used for .cfg files





#Begin Class
class habi:
    def amfgetservice(self,servicename):
    #Get amf service and update cookie after #Bugfix id 001 since reclass , fuck knows whats going on with this shite. but this rusty fix works for now
        self.gateway.opener = self.theopener
        theret= self.gateway.getService(servicename) #Get The service
        
        return theret
            






    #Initialize this class
    #def __init__(self,acc):
    
    def __init__(self,acc,thegateway):
        self.lastexp = 0

        self.LAST_EGG_CHECK_TIME = 1
        self.theopener = acc.opener.open
        self.gateway = thegateway
        self.LAST_GEM_CHECK_TIME = 1
        print "init-------------"
             
    def counthouses(self):
        #print "findNest"
        housecount=0
        for x in self.itembag:
          itemstr = str(x)

          if itemstr.find("type': u'House'") > 0:
             if itemstr.find("isBuilt': False") > 0:
                 housecount=housecount+1
        return housecount



    def checkupgrades(self,playerlevel):
        #I was going to intergrate this into the speand resource function , but it can take a long time until you get full resources. So instead its
        #a seperate function and we can check more often.



        #recoded in 1.3f to execute all in a single loop..... This stops spikes of 10% cpu usage/massive memory leaks
        #How did I ever think that last code was a good idea?
        #This functions now timed too , no point in having it every loop , we aint gonna have full resources everytime!


        print "searching for p3/building upgrades.."
        
        ret = 0 # return 0 if none done 
        upgradeservice = self.amfgetservice("UpgradeService")

        pollencount = self.resp3['resources']['pollen']
        grasscount = self.resp3['resources']['grass']
        watercount = self.resp3['resources']['water']
        mudcount = self.resp3['resources']['mud']
        stonecount = self.resp3['resources']['stone']
        woodcount = self.resp3['resources']['wood']
        #Get list of all upgrades player has....
        #first give them a default...
        got_nester_lvl_1_upgrade = 0
        got_worker_lvl_1_upgrade = 0
        got_nester_lvl_2_upgrade = 0
        got_worker_lvl_2_upgrade = 0
        got_soldier_lvl_1_upgrade = 0
        playersupgrades = upgradeservice.playerUpgrades()
        for x in  playersupgrades:
            if x["m_id"] == 1: #Level 1 worker upgrade
                got_worker_lvl_1_upgrade = 1
            if x["m_id"] == 6: #Level 1 nester upgrade
                got_nester_lvl_1_upgrade = 1
            if x["m_id"] == 7: #Level 2 nester upgrade
                got_nester_lvl_2_upgrade = 1
            if x["m_id"] == 2: #Level 2 worker upgrade
                got_worker_lvl_2_upgrade = 1

            if x["m_id"] == 11: #soldier level 1 upgrades
                got_soldier_lvl_1_upgrade = 1

                


        
        if playerlevel > 10:# dont even waste my cpu if no upgrades available for this level (11+ for upgrades)
          #  print "searching p3 upgrades"

            for x in  self.itemcollection:
                


###################################### level 1 workers
                if got_worker_lvl_1_upgrade == 0:  #only if we havent got all       
                    if (x['sceneItemType'] == "Character"):
                        #print x
                        if (x['unlockLevel']) == 1: #set to 1 if upgrade is available that made things easier eh? :D
                            if x['profession'] == "worker":
                                if pollencount > 60:
                                    if grasscount > 30:
                                        if watercount > 30:
                                            upgradeid =x['m_id']
                                            print "id=" + str(upgradeid)
                                            print "Upgraded workers from level 1 to level 2"
                                            #print pollencount

                                            
                                            upgradeservice.buyUpgrade("1",str(upgradeid))
                                            return 1

###################################### level 1 nester
                if got_nester_lvl_1_upgrade == 0:  #only if we havent got all       
                    if (x['sceneItemType'] == "Character"):
                        #print x
                        if (x['unlockLevel']) == 1: #set to 1 if upgrade is available that made things easier eh? :D
                            if x['profession'] == "nester":
                                if pollencount > 60:
                                    if grasscount > 30:
                                        if watercount > 30:
                                            upgradeid =x['m_id']
                                            print "id=" + str(upgradeid)
                                            print "Upgraded nesters from level 1 to level 2"
                                            #print pollencount

                                            
                                            upgradeservice.buyUpgrade("6",str(upgradeid))
                                            return 1






###################################### level 2 nester
                if got_nester_lvl_2_upgrade == 0:  #only if we havent got all
                    if playerlevel > 30:
                        if (x['sceneItemType'] == "Character"):
                            #print x
                            if (x['unlockLevel']) == 1: #set to 1 if upgrade is available that made things easier eh? :D
                                if x['profession'] == "nester":
                                    if pollencount > 60:
                                        if grasscount > 30:
                                            if watercount > 30:
                                                upgradeid =x['m_id']
                                                print "id=" + str(upgradeid)
                                                print "Upgraded nesters from level 2 to level 3"
                                                #print pollencount

                                                
                                                upgradeservice.buyUpgrade("7",str(upgradeid))
                                                return 1




###################################### level 2 soldiers - this only executes if the player has a soldier on stage but if so its a nice little +200 exp tweak
                if got_soldier_lvl_1_upgrade == 0:  #only if we havent got all
                    if playerlevel > 11:
                        if (x['sceneItemType'] == "Character"):
                            #print x
                            if (x['unlockLevel']) == 1: #set to 1 if upgrade is available that made things easier eh? :D
                                if x['profession'] == "soldier":
                                    if pollencount > 25:
                                        if grasscount > 50:
                                            if watercount > 25:
                                                upgradeid =x['m_id']
                                                #print "id=" + str(upgradeid)
                                                print "Upgraded soldiers from level 2 to level 3"
                                                #print pollencount

                                                
                                                upgradeservice.buyUpgrade("11",str(upgradeid))
                                                return 1













###################################### level 2 workers
                if got_worker_lvl_2_upgrade == 0:  #only if we havent got all
                    if playerlevel > 30:
                        if (x['sceneItemType'] == "Character"):
                            #print x
                            if (x['unlockLevel']) == 1: #set to 1 if upgrade is available that made things easier eh? :D
                                if x['profession'] == "worker":
                                    if pollencount > 60:
                                        if grasscount > 30:
                                            if watercount > 30:
                                                upgradeid =x['m_id']
                                                #print "id=" + str(upgradeid)
                                                print "Upgraded workers from level 2 to level 3"
                                                #print pollencount

                                                
                                                upgradeservice.buyUpgrade("2",str(upgradeid))
                                                return 1



                                         
###Now check on buildings...
                if playerlevel > 12:# dont even waste my cpu if no upgrades available for this level (13+ for building upgrades)
                   # print "checking building upgrades"

                #level 1 house....
           
                    if (x['sceneItemType'] == 'Structure'):
                        if (x['type'] == 'House'):
                            upgradeid =x['m_id']
                            if (x['itemLevel'] == 1):
                                if (mudcount > 600):
                                    if (stonecount > 1300):
                                        if (woodcount > 950):
                                            print "Upgraded House id " + str(upgradeid) + " to level 2"
                                            upgradeservice.buyUpgrade("16",str(upgradeid))
                                            return 1

            #level 2 house....
                if playerlevel > 36:

                    if (x['sceneItemType'] == 'Structure'):
                        if (x['type'] == 'House'):
                            print "rdd"
                            upgradeid =x['m_id']
                            if (x['itemLevel'] == 2):
                                if (mudcount > 850):
                                    if (stonecount > 2200):
                                        if (woodcount > 1150):
                                            print "Upgraded House id " + str(upgradeid) + " to level 3"
                                            upgradeservice.buyUpgrade("17",str(upgradeid))
                                            return 1

 ###################################

                if playerlevel > 17:
                #level 1 nest....
               
                    if (x['sceneItemType'] == 'Structure'):
                        if (x['type'] == 'Nest'):
                            upgradeid =x['m_id']
                            #print x
                            if (x['itemLevel'] == 1):
                                if (mudcount > 850):
                                    if (stonecount > 1050):
                                        if (woodcount > 800):
                                            
                                            print "Upgraded Nest id " + str(upgradeid) + " to level 2"
                                            upgradeservice.buyUpgrade("22",str(upgradeid))
                                            return 1

                if playerlevel > 40:
                #level 1 nest....
               
                    if (x['sceneItemType'] == 'Structure'):
                        if (x['type'] == 'Nest'):
                            upgradeid =x['m_id']
                            #print x
                            if (x['itemLevel'] == 2):
                                if (mudcount > 900):
                                    if (stonecount > 950):
                                        if (woodcount > 1300):
                                            
                                            print "Upgraded Nest id " + str(upgradeid) + " to level 3"
                                            upgradeservice.buyUpgrade("23",str(upgradeid))
                                            return 1      

 ###################################

                if playerlevel > 21:
                    #level 1 nest....
                    if (x['sceneItemType'] == 'Structure'):
                        if (x['type'] == 'Storage'):
                            upgradeid =x['m_id']
                            if (x['itemLevel'] == 1):
                                if (mudcount > 1250):
                                    if (stonecount > 1800):
                                        if (woodcount > 3400):
                                            print "Upgraded Storage Center id " + str(upgradeid) + " to level 2"
                                            upgradeservice.buyUpgrade("19",str(upgradeid))
                                            return 1


     ###################################    
        
    def countnest(self):
        #print "findNest"
        housecount=0
        for x in self.itembag:
          itemstr = str(x)

          if itemstr.find("type': u'Nest'") > 0:
             if itemstr.find("isBuilt': False") > 0:
                 housecount=housecount+1
        return housecount

    def findinvnest(self):
        #print "findNest"
        houseid = 0
        for x in self.itembag:
          itemstr = str(x)
          #print x
          if itemstr.find("type': u'Nest'") > 0:
             if itemstr.find("isBuilt': False") > 0:
                     #'
                 #print itemstr
                 startpos = itemstr.find("m_id': ") +7
                    #print startpos
                 #print startpos
                 endpos = itemstr.find("'uid") -2
                 houseid = itemstr[startpos:endpos]
                 #print "nest=" + str(houseid)
        return houseid

    def findinvstorage(self):
        houseid=0
        #print "findStorage"
        for x in self.itembag:
          itemstr = str(x)
          #print x
          if itemstr.find("type': u'Storage'") > 0:
              if itemstr.find("isBuilt': False") > 0:
                  startpos = itemstr.find("m_id': ") +7
                #print startpos
             #print startpos
                  endpos = itemstr.find("'uid") -2
                  houseid = itemstr[startpos:endpos]
                  #print "storage=" + str(houseid)
        return houseid






    def findnonehealthybuildings(self):
        doneone = 0;
        print "Checking for none healthy buildings..."
        for x in self.itemcollection:

            if (x['sceneItemType'] == "Structure"):
                if (x['decayLevel'] > 1): #Buildings have a heath and a decay level only use decay levels in this ver , its better this way
                    
                    buildid=x['m_id']
                    #print x
                    badx = self.getbuildingx(buildid)
                    bady = self.getbuildingy(buildid)
                    #print "badx=" + str(badx) + "bady=" + str(bady)
                    emptytile = self.getfixcoord(badx,bady)

                    builderid = self.findnonebusyworker2()
                    if not int(builderid) == -1:
                        if emptytile: #tile found
                            doneone=1
                            self.scene_service.moveItem(str(builderid),str(badx),str(bady))
                            print "set creature " + str(builderid) + " to fix unhealthy building at x = " + str(badx) + " y = " + str(bady)
                            return doneone
                #if (x['isBuilt'] == True):       
        return doneone

    def findinvhouse(self):
        #print "findhouse"
        for x in self.itembag:
          itemstr = str(x)
          #print x
          if itemstr.find("type': u'House'") > 0:
             startpos = itemstr.find("m_id': ") +7
                #print startpos
             #print startpos
             endpos = itemstr.find("'uid") -2
             houseid = itemstr[startpos:endpos]
             return houseid
             #print eggid
             #emptytile = self.findemptytilearound(6,6)
                         #scene_service.moveItem(str(x['m_id']),"3","9") ##collect wood
             #if (emptytile): #Empty tile found
             #   self.scene_service.moveItem(str(eggid),emptytile[0],emptytile[1])
             #   print "Placed bonus egg at x=" + emptytile[0] + " y = " + emptytile[1]

    def dummybuild(self):
        #Check 5 dummy build points to see if items are ready , if so remove them from stage
        item1id = 0
        for x in self.itemcollection:
            if (x['x'] == "9"):
                if (x['y'] == "8"):
                   # print x
                    if (x['sceneItemType'] == "Structure"):
                        if (x['isBuilt'] == True):
                            item1id  = x['m_id']   
                            
       #     if (x['x'] == "9"):
       #         if (x['y'] == "7"):
       #             if (x['sceneItemType'] == "Structure"):
       #                 if (x['isBuilt'] == True):
       #                     item1id  = x['m_id']                             
        if item1id > 0:
            print "Removed completed dummy build item"
            self.Inventory_Service.moveToItemBag(str(item1id))
            



    def countbuildings(self):
        #Count all buildings on the users stage
        housecount=0
        for x in self.itemcollection:
            if (x['sceneItemType'] == "Structure"):
                housecount=housecount+1
        return housecount


    def getfixcoord(self,thex,they):
        #get a empty coordinate next to the building that needs to be repaired
        #Added in v1.3 to fix bugs and decrease memory usage
        thex = str(thex)
        they = str(they)
        if thex == "1" and they == "0":
           return ["0","0"]
        elif thex == "2" and they == "0":
           return ["2","1"] #1 square in front of the house , not the side (building 3 will block that tile if its built)

        elif thex == "3" and they == "0":
           return ["3","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)
        elif thex == "4" and they == "3":
           return ["4","4"] #1 square in front of the house , not the side (building 4 will block that tile if its built)


        elif thex == "5" and they == "0":
           return ["4","0"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "6" and they == "0":
           return ["6","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "7" and they == "0":
           return ["8","0"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "8" and they == "0":
           return ["8","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)
        elif thex == "9" and they == "0":
           return ["9","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "5" and they == "2":
           return ["5","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "6" and they == "2":
           return ["6","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "7" and they == "2":
           return ["7","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "8" and they == "2":
           return ["8","3"] #1 square in front of the house , not the side (building 4 will block that tile if its built)
        elif thex == "9" and they == "2":
           return ["9","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "4" and they == "3":
           return ["4","4"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "6" and they == "4":
           return ["6","5"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "9" and they == "6":
           return ["9","7"] #1 square in front of the house , not the side (building 4 will block that tile if its built)



        elif thex == "10" and they == "0":
           return ["10","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)


        elif thex == "1" and they == "8":
           return ["0","8"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "1" and they == "7":
           return ["0","7"] #1 square in front of the house , not the side (building 4 will block that tile if its built)

        elif thex == "4" and they == "0":
           return ["4","1"] #1 square in front of the house , not the side (building 4 will block that tile if its built)
        elif thex == "9" and they == "5":
           return ["9","6"] #1 square in front of the house , not the side (building 4 will block that tile if its built)
        elif thex == "10" and they == "6":
           return ["10","5"] #1 square in front of the house , not the side (building 4 will block that tile if its built)






        
        else:
            print "Get fix coord failed for " + str(thex) + " , " + str(they) +  ". Please report this. Unless you have edited the predefined map. If so then you need to add a build point for your new coord to this function!"
            
        







    def checknonebuiltbuildings_recode(self):
        #reoded to call new functions in 1.3
        doneone=0
        buildid = self.findnonecompletebuilding()

        
        if not buildid ==-1:

            badx = self.getbuildingx(buildid)
            bady = self.getbuildingy(buildid)
            builderid = self.findnonebusyworker()
            emptytile=self.getfixcoord(badx,bady)
            if (emptytile): #Empty tile found
                 # print "builderid=" + str(builderid)
                  if  builderid > -1:


                      doneone=1
                      self.scene_service.moveItem(str(builderid),str(emptytile[0]),str(emptytile[1]))
                      print "set creature " + str(builderid) + " to build unbuilt structure at x = " + str(emptytile[0]) + " y = " + str(emptytile[1])
        return doneone







    def buildpremap_recode(self):
        #Instead of looping every item on stage and checking if item exist there , we now just count how many items on the stage the user has
        #So if we have 6 items , we know we need to build the 7th in our premap list next. This will fix buildings stacking ontop of eachover.
        #Also will decrease cpu usage
        buildingcount =  self.countbuildings()
        
        if buildingcount == 0:
            print "No buildings found , Building item 1 (Storage) at coordinate 1,0"
            buildid = self.findinvstorage()
            if buildid == 0: #No storage centers in inventory
                print "You have started habi bot without any items in your item bag , this will be slow. You should run reshack.py first! I will continue anyway... This message will dissapear after the first uilding is built"
            else:
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(1),str(0)) #Move the item onto the map


        if buildingcount == 1:
            print "Building Item 2 (House) at coordinate 2,0"
            buildid = self.findinvhouse()
            if not buildid == 0: #None  in inventory
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(2),str(0)) #Move the item onto the map



        if buildingcount == 2:
            print "Building Item 3 (Storage) at coordinate 3,0"
            buildid = self.findinvstorage()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(3),str(0)) #Move the item onto the map



        if buildingcount == 3:
            print "Building Item 4 (Storage) at coordinate 4,3"
            buildid = self.findinvstorage()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(4),str(3)) #Move the item onto the map





        if buildingcount == 4:
            print "Building Item 5 (Storage) at coordinate 5,0"
            buildid = self.findinvstorage()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(5),str(0)) #Move the item onto the map


        if buildingcount == 5:
            print "Building Item 6 (nest) at coordinate 6,0"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(6),str(0)) #Move the item onto the map


        if buildingcount == 6:
            print "Building Item 7 (nest) at coordinate 7,0"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(7),str(0)) #Move the item onto the map

        if buildingcount == 7:
            print "Building Item 8 (nest) at coordinate 8,0"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(8),str(0)) #Move the item onto the map

        if buildingcount == 8:
            print "Building Item 9 (nest) at coordinate 9,0"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(9),str(0)) #Move the item onto the map


        if buildingcount == 9:
            print "Building Item 10 (nest) at coordinate 6,4"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(6),str(4)) #Move the item onto the map

        if buildingcount == 10:
            print "Building Item 11 (nest) at coordinate 9,2"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(9),str(2)) #Move the item onto the map

        if buildingcount == 11:
            print "Building Item 12 (nest) at coordinate 8,2"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(8),str(2)) #Move the item onto the map



        if buildingcount == 12:
            print "Building Item 13 (nest) at coordinate 7,2"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(7),str(2)) #Move the item onto the map



        if buildingcount == 13:
            print "Building Item 14 (nest) at coordinate 6,2"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(6),str(2)) #Move the item onto the map


        if buildingcount == 14:
            print "Building Item 15 (nest) at coordinate 5,2"
            buildid = self.findinvnest()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(5),str(2)) #Move the item onto the map



        if buildingcount == 15:
            print "Building Item 16 (nest) at coordinate 9,8"
            buildid = self.findinvstorage()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(9),str(8)) #Move the item onto the map




        if buildingcount == 15:
            print "Building Item 16 (nest) at coordinate 10,6"
            buildid = self.findinvstorage()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(10),str(6)) #Move the item onto the map

        if buildingcount == 16:
            print "Building Item 17 (nest) at coordinate 9,5"
            buildid = self.findinvstorage()
            if  not buildid == 0: #None in invenotry
                print "Item added to stage"
                self.scene_service.moveItem(str(buildid),str(9),str(5)) #Move the item onto the map


     

    def getlowestresource(self):
        print "Finding lowest resource"
        #for x in itemcollection:
        lowestres= "none"
        lowestres = 0

        self.woodcount = self.resp3['resources']['wood']      
        # print "wood = " + str(woodcount)
        lowestrescount = self.woodcount
        lowestres= "wood"

        self.mudcount = self.resp3['resources']['mud']      
        # print "mud = " + str(mudcount)
        if ( self.mudcount < lowestrescount):
            lowestrescount = self.mudcount
            lowestres= "mud"     

        self.grasscount = self.resp3['resources']['grass']      
        # print "grass = " + str(grasscount)
        if ( self.grasscount < lowestrescount):
            lowestrescount = self.grasscount
            lowestres= "grass"

      
        self.pollencount = self.resp3['resources']['pollen']      
    # print "pollen = " + str(pollencount)
        if ( self.pollencount  < lowestrescount):
            lowestrescount = self.pollencount
            lowestres= "pollen"

      
        self.stonecount = self.resp3['resources']['stone']      
    #print "stone = " + str(stonecount)
        if ( self.stonecount < lowestrescount):
            lowestrescount = self.stonecount
            lowestres= "stone"

      
        self.watercount = self.resp3['resources']['water']      
    #print "water = " + str(watercount)

        if ( self.watercount < lowestrescount):
            lowestrescount = self.watercount
            lowestres= "water"


        return lowestres

    
    def checktennants(self,searchid):
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Character"):
             if((x['tenantOf'])== searchid['m_id']):
                maxhunger= x['maxAttributes']['hunger']
                maxrest= x['maxAttributes']['rest']
                if (int(x['hunger']) == int(maxhunger)) and (int(x['rest']) == int(maxrest)):
                   print "Moving fully healthy creature id#" + str(x['m_id']) + " out of house id#" + str(searchid['m_id'])
                   #print "id=" + str(x['m_id']) + "x=" + str(x['x']) + "y=" + str(x['y'] ) 
                   self.scene_service.moveItem(str(x['m_id']),str(8),str(8))

            

    def checkhouses(self):
          #print itemcollection
          for y in self.itemcollection:

                   self.checktennants(y)        

    def findemptyhouse(self):
      # print "finding empty house.."
       #print itemcollection
       
       for y in self.itemcollection:
          
          if (y['sceneItemType'] == 'Structure'):
             if (y['type'] == 'House'):
                maxchars=y['characterCapacity']
                tencount= self.findhousetenantcount(y['m_id'])
                #print maxchars + "vs" + tencount
                if (int(tencount) < int(maxchars)):
                   
                   #space available here so put pet into house
                   #print "putting pet into house"

                   return y

    def findhousetenantcount(self,searchid):
       counter=0
       #print searchid
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Character"):
             if((x['tenantOf'])== searchid):
             #Check pet hunger and put them in available house
                counter = counter + 1
       return counter


    def checkhungry(self):
       print "hungry check"

       
       currentmon =""
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Character"):
             if  (int(x['tenantOf']) == -1): #Not in a house already or already nesting
                   
                #print x
                if (int(x['hunger']) < 50) or (int(x['rest']) < 50):
                  
                  #print "test"
                   #Check pet hunger and put them in available house
                  currentmon = x
                 # print currentmon['m_id']
                  if (int(currentmon['m_id']) > 0):
                     currhouse=[]
                     #print "loop"
                     currhouse=self.findemptyhouse()
                    
                     if not (currhouse == None):
                        #print "true"
                       result = self.scene_service.makeTenant((str(currentmon['m_id'])),str(currhouse['m_id']))

                  #      print currentmon 
                       if (result == True):
                           #
                           print "Placed creature id#" + str(currentmon['m_id']) + " in house id#" + str(currhouse['m_id'])
                           #print "Placed creature in house"
                       break

                
    def setworkercollect(self,cid,lowestres):
        if (lowestres == "wood"):
            print str(cid) + " Is now colleting wood"
            self.scene_service.moveItem(str(cid),"9","9")
        elif (lowestres == "stone"):
            print str(cid) + " Is now colleting stone"
            self.scene_service.moveItem(str(cid),"0","4")
        elif (lowestres == "mud"):
            print str(cid) + " Is now colleting mud"
            self.scene_service.moveItem(str(cid),"9","3")
        elif (lowestres == "grass"):
            print str(cid) + " Is now colleting grass"
            self.scene_service.moveItem(str(cid),"3","2")
        elif (lowestres == "pollen"):
            print str(cid) + " Is now colleting pollen"
            self.scene_service.moveItem(str(cid),"1","0")
        elif (lowestres == "water"):
            print str(cid) + " Is now colleting water"
            self.scene_service.moveItem(str(cid),"3","3")             
        else:
            print "fix needed no tile found for " + lowestres

       #for x in self.tilecollection:
          #resmname = x['resource']
          #if (resmname.lower() == lowestres):
          #   resx = x['x']
          #   resy = x['y']
        


             
             #emptytile = self.findemptytilearound(resx,resy)
                         #scene_service.moveItem(str(x['m_id']),"3","9") ##collect wood
             #if (emptytile): #Empty tile found
             #   self.scene_service.moveItem(str(cid),str(emptytile[0]),str(emptytile[1]))
             #   print "setting worker id #" + str(cid) + " to collect " + lowestres
            #    break


    def itemexistat(self,thex,they):
        theret=False
        #print "rdd1=" + thex + "/" + they
        for x in self.itemcollection:
            if (x['x'] == str(thex)):
                if (x['y'] == str(they)):
                    #print "rdd"
                    theret = True
        return theret

    def findemptytilearound(self,thex,they):
   #Find a empty tile next to a certain tile , used to move creatures next to items ect
   #Checks tile to left , to right , above and below could be improved with diagnal but not really needed
       foundone = []   
       for x in self.tilecollection:
          #print x

       #Is this the  tile >1 of target if so is it empty?
          searchx = int(thex) - 1
          searchy = int(they)
            # print "searchx = " + searchx + "searchy = " + searchy
             #print "thex = " + x['x'] + "they = " + x['y']
             #print searchx
          #print str( x['x'])
          if(x['x'] == int(searchx)):
             #print x
             if(x['y'] == int(searchy)):
                  #print x
                  if(x['walkable'] == True):
                      if self.itemexistat(searchx,searchy) == False:
                          foundone = [searchx,searchy]
                          return foundone
                          break

          searchx = int(thex) +1
          searchy = int(they)
            # print "searchx = " + searchx + "searchy = " + searchy
             #print "thex = " + x['x'] + "they = " + x['y']
             #print searchx
          #print str( x['x'])
          if(x['x'] == int(searchx)):
             
             if(x['y'] == int(searchy)):
                  
                  if(x['walkable'] == True):
                      
                      if self.itemexistat(searchx,searchy) == False:
                          
                          foundone = [searchx,searchy]
                          return foundone
                          break


          
          searchx = int(thex)
          searchy = int(they) -1
            # print "searchx = " + searchx + "searchy = " + searchy
             #print "thex = " + x['x'] + "they = " + x['y']
             #print searchx
          #print str( x['x'])
          if(x['x'] == int(searchx)):
             #print x
             if(x['y'] == int(searchy)):
                  #print "rdd" 
                  #print self.itemexistat(searchx,searchy)
                  if(x['walkable'] == True):
                      if self.itemexistat(searchx,searchy) == False:
                          foundone = [searchx,searchy]
                          return foundone
                          break
                   
       
          searchx = int(thex)
          searchy = int(they)+1
            # print "searchx = " + searchx + "searchy = " + searchy
             #print "thex = " + x['x'] + "they = " + x['y']
             #print searchx
          #print str( x['x'])
          if(x['x'] == int(searchx)):
             #print x
             if(x['y'] == int(searchy)):
                  #print x
                  if(x['walkable'] == True):
                      if self.itemexistat(searchx,searchy) == False:
                          foundone = [searchx,searchy]
                          return foundone
                          break
       #print "found=" + str(foundone)
       return foundone


        
    def getbuildingx(self,buildingid):
       #Get building X coord (should be updated to single function for both coords)
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Structure"):
             if (x['m_id'] == buildingid):
                return (x['x'])
          
    def getbuildingy(self,buildingid):
       #Get building Y coord (should be updated to single function for both coords)
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Structure"):
             if (x['m_id'] == buildingid):
                return (x['y'])
        
    def findlowhpbuilding(self):
       theret=-1
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Structure"):
             #print x['isBuilt']
             if (x['isBuilt'] == True):
                if (x['health'] < 50):
                   theret=(x['m_id'])
                   return theret
                   break
         
       return theret

    def countpets(self):
       counter=0
       #print searchid
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Character"):
             counter = counter + 1
       return counter


    def checkeggs50(self,playerlevel):
        
       print "Searching for any eggs on stage (level 50 logic)..."
       for x in self.itemcollection:
         # print x['sceneItemType']
          petcount= self.countpets()
          maxpetcount = self.resp['maxPopulation']
          if (x['profession'] == "soldier"):
             self.scene_service.discardEgg(str(x['m_id']))#Egg is a soldier , #discard
             print "Discarded Useless Egg id#" + str(x['m_id'])
             return 1 #Kill func              
          if (x['sceneItemType'] == "Egg"):
             #print x['profession']
             if not (x['species'] == None):
                #if (int(playerlevel) >49):
               #  self.scene_service.harvestEgg(str(x['m_id']))# == "True"):
                #  print "Harvested Egg id#" + str(x['m_id'])
               if (x['profession'] == "nester"): #Only if egg is not a soldier....

                     nestercount=(self.countnesters()) #Get total nester , premap only has 13 nest , so if we have more than this the nesters are useless to us
                     if (nestercount > 13): #To many nesters
                        print "Not enough nest on stage to justify another nester , discarded egg"
                        self.scene_service.discardEgg(str(x['m_id'])) # Population = max so discard
                        return 0
              
               nestercount=(self.countnesters()) #Get total nester , premap only has 13 nest , so if we have more than this the nesters are useless to us
               if (x['profession'] == "nester"): #Only if egg is a worker
                  if (nestercount < 5): #Keep 5 nesters alive for repopulating when others die , any less than 3 is pretty damn slow to repopulate  is my preference
                      (self.scene_service.hatchEgg(str(x['m_id'])))#Hatch the egg
                      print "hatched nester egg (less than 5 nesters currently in stage)"
                      return 1 #Kill func



                
               if (x['profession'] == "worker"): #Only if egg is a worker
                     if (petcount < maxpetcount): #If we dont have full capacity population....
                             (self.scene_service.hatchEgg(str(x['m_id'])))#Hatch the egg
                             print "Hatched Egg id#" + str(x['m_id']) + " (" + x['profession'] + ")" 
                             return 1 #Kill func    
                     else:
                             self.scene_service.discardEgg(str(x['m_id'])) # Population = max so discard
                             print "Discarded Egg id#" + str(x['m_id']) + " due to full population"
                             return 1 #Kill func
               else:
                     self.scene_service.discardEgg(str(x['m_id']))#Egg is a soldier , #discard
                     print "Discarded Useless Egg id#" + str(x['m_id'])
                     return 1 #Kill func





    def checkeggs(self,playerlevel):
        
       print "Searching for any eggs on stage..."
       for x in self.itemcollection:

          petcount= self.countpets()
          maxpetcount = self.resp['maxPopulation']
          if (x['sceneItemType'] == "Egg"):

             if not (x['species'] == None):
                 if (x['profession'] == "soldier"):
                     self.scene_service.discardEgg(str(x['m_id']))#Egg is a soldier , #discard
                     print "Discarded Useless Egg id#" + str(x['m_id'])
                     return 1 #Kill func 
                 if (x['profession'] == "nester"): #Only if egg is not a soldier....

                     nestercount=(self.countnesters()) #Get total nester , premap only has 13 nest , so if we have more than this the nesters are useless to us
                     if (nestercount > 13): #To many nesters
                        print "Not enough nest on stage to justify another nester , discarded egg"
                        self.scene_service.discardEgg(str(x['m_id'])) # Population = max so discard
                        return 0



                            
                 if not(x['profession'] == "soldier"): #Only if egg is not a soldier....
                     if (petcount < maxpetcount): #If we dont have full capacity population....
                         (self.scene_service.hatchEgg(str(x['m_id'])))#Hatch the egg
                         print "Hatched Egg id#" + str(x['m_id']) + " (" + x['profession'] + ")" 
                         return 0


                     
                     else:

                         
                         self.scene_service.discardEgg(str(x['m_id'])) # Population = max so discard

                         print "Discarded Egg id#" + str(x['m_id']) + " due to full population"
                 else:
                     self.scene_service.discardEgg(str(x['m_id']))#Egg is a soldier , #discard
                     print "Discarded Useless Solidier Egg id#" + str(x['m_id'])


    def checknesters(self):

       for x in self.itemcollection:
          
          if (x['sceneItemType'] == "Character"):
             
             if  (str(x['profession']) == "nester"):
                
                if (int(x['tenantOf'] == -1)): #Nester is not busy


                                
                    if (int(x['hunger']) > 50) and (int(x['rest']) > 50):
                        nestid= self.finemptynest()


                        if not (nestid == -1):
                           result = self.scene_service.makeTenant((str(x['m_id'])),str(nestid))
                           print "Placed inactive nester id#" + str(x['m_id']) + " in nest id#" + str(nestid)
                           break

    def finemptynest(self):
       ret=-1
       for x in self.itemcollection:
          if (x['sceneItemType'] == 'Structure'):

             if (x['type'] == 'Nest'):
                 

                if (str(x['isBuilt']) == 'True'):
                    if (int(x['health']) > 50):

                       tencount = self.findhousetenantcount(x['m_id'])

                       if (tencount == 0):
                          ret = x['m_id']
       return ret         




    def findnonecompletebuilding(self):
       theret=-1
       for x in self.itemcollection:
          if (x['sceneItemType'] == "Structure"):

             if (x['isBuilt'] == False):

                theret=(x['m_id'])
                return theret
                break
             
       return theret


    def checkgems(self):
       print "Looking for any gems on stage..."
       for x in self.itemcollection:

          if (x['sceneItemType'] == "Gem"):
            
             if str((self.scene_service.collectGem(str(x['m_id']))) == "True"):
                print "Collected gem id#" + str(x['m_id'])


    def checkinveggs(self):
        #Amf is broke so get the packet to a string , use string manipulation to parse the id
       for x in self.itembag:
          itemstr = str(x)
          if itemstr.find("sceneItemType': u'Egg'") > 0:
             startpos = itemstr.find("m_id': ") +7

             endpos = itemstr.find("'uid") -2
             eggid = itemstr[startpos:endpos]

             emptytile = self.findemptytilearound(6,6)

             if (emptytile): #Empty tile found
                self.scene_service.moveItem(str(eggid),emptytile[0],emptytile[1])
                print "Placed egg from inventory at x=" + str(emptytile[0]) + " y = " + str(emptytile[1])
                #break


    def trashbuy(self):
        #fallback to this function if nothing to upgrade , this just buys storage centers


       self.stonecount = self.resp3['resources']['stone']
       self.mudcount = self.resp3['resources']['mud']
       self.woodcount = self.resp3['resources']['wood']
       if mudcount > 3000:
          if stonecount > 3000:
             if woodcount > 3000:
                self.store_service = self.gateway.getService('StoreService')
                self.theopener = self.gateway.opener
                self.gateway.opener = self.theopener
                self.store_service.buyItem("20")
                self.theopener = self.gateway.opener
                self.gateway.opener = self.theopener
                print "speant some resources"        

    def speandresources(self):
        #print self.countnest()
        self.stonecount = self.resp3['resources']['stone']
        self.mudcount = self.resp3['resources']['mud']
        self.woodcount = self.resp3['resources']['wood']
        self.store_service = self.gateway.getService('StoreService')
        if self.mudcount > 6000:
           if self.stonecount > 6000:
              if self.woodcount > 6000:
                if self.mudcount > 6000:
                   if self.stonecount > 6000:
                      if self.woodcount > 6000:
                          
                          if self.countnest() < 1:
                              #We have less than 1 nest in inventory so buy new nest
                              self.store_service.buyItem("22")
                              print "less than 1 nest in inventory so buying one"

                          elif self.counthouses() < 1:
                              print "less than 1 house in inventory so buying one"
                              self.store_service.buyItem("15")
                          else:
                              print "No items to buy and all upgrades done , so speanding trash resources"
                              self.store_service.buyItem("20")

    def findnonebusypet(self):
        theid=-1 
        for x in  self.itemcollection:
                    
            if (x['sceneItemType'] == "Character"):
                if  (x['tenantOf'] == -1):
                    theid=x['m_id']
                            
        return theid


    def findnonebusyworker(self):
        theid=-1 
        for x in  self.itemcollection:
                    
            if (x['sceneItemType'] == "Character"):
             if  (x['profession'] == "worker"):
                #print "1"
                if  (x['tenantOf'] == -1):
                    #print "2"
                    if (x['health'] > 50):
                        theid=x['m_id']
                            
        return theid

    def countnesters(self):
        ret = 0
        for x in  self.itemcollection:
            
                    
            if (x['sceneItemType'] == "Character"):
             if  (x['profession'] == "nester"):        
                ret = ret+1
        return ret
    
    def findnonebusyworker2(self):
        theid=-1 
        for x in  self.itemcollection:
                    
            if (x['sceneItemType'] == "Character"):
             if  (x['profession'] == "worker"):
                #print "1"
                if  (x['tenantOf'] == -1):
                    if  (x['tenantOf'] == -1):
                        #print "2"
                        if (x['attachedTo'] == -1):
                            theid=x['m_id']
                            #print x
                            
        return theid
    def checknonebuiltbuildings(self):
        doneone=0
        buildid = self.findnonecompletebuilding()
       # print "buildid= " + str(buildid)
        if(buildid > -1):
          #getbuildingx(badid,itemcollection)
          badx = self.getbuildingx(buildid)
          bady = self.getbuildingy(buildid)

          #print "x=" + badx +  "y=" + bady
          emptytile = self.findemptytilearound(badx,bady)
         
          builderid = self.findnonebusyworker2()




          
          if (emptytile): #Empty tile found
             # print "builderid=" + str(builderid)
              if  builderid > -1:

    
                  doneone=1
                  self.scene_service.moveItem(str(builderid),str(emptytile[0]),str(emptytile[1]))
                  print "set creature to fix build unbuilt structure at x = " + str(emptytile[0]) + " y = " + str(emptytile[1])
          return doneone



        
    def checkworkers(self):
        workerid=self.findnonebusyworker2()
        doneone=0
        if  workerid > -1:

            print "finding lowest res"
            lowestres =  self.getlowestresource()
            if not (lowestres == "none"):

                print "lowest res = " + lowestres
                self.setworkercollect(workerid,lowestres)
                         
    def DoLoop(self):
    # try:



       self.gateway.opener = self.theopener     
       self.player_service = self.amfgetservice("PlayerService")
       self.event_service = self.amfgetservice("EventService")
       self.scene_service = self.amfgetservice("SceneService")
       self.Inventory_Service = self.amfgetservice("InventoryService")
       self.resp = self.player_service.playerinfo()
       playerlevel =self.resp['habitariumLevel']


       
       #Detect a brand new player and set them up , stops the user needing to do it manually
       if int(self.resp['isSetup']) == 0:
           print "New habi detected , sending setup packet...."
           #print self.player_service.setupHabitarium(0)
           self.player_service.skillSetup() #Sets up a brand new habi
           print "choosing a new habi"
           self.scene_service.setupHabitarium("0")
           print "Setting tutorial to complete..."
           self.player_service.setTutorialProgress("-1")
           print "Sending Update..."
           self.event_service.update('40','40')
               
           print "resetting player"
           self.player_service.reset()
           print "choosing a new habi"
           self.scene_service.setupHabitarium("0")
           print "Setting tutorial to complete..."
           self.player_service.setTutorialProgress("-1")
           print "Sending Update..."
           self.event_service.update('40','40')
           temp= self.event_service.simulate()
           time.sleep(2)
           self.checkgems()
           self.event_service.update('40','40')
           self.store_service.buyItem("15") 
           temp= self.event_service.simulate()

           
           return 1


                  



              
       self.itemcollection= self.scene_service.sceneItems()
       self.resp2= self.event_service.simulate() 
       self.tilecollection = self.resp2['map']['tiles']
       self.resp3= self.event_service.update('40','40')
       
       self.itembag = self.Inventory_Service.itemBag()

       
       maxxp=self.resp2['player']['levelInfo']['nextXP']
       thisexp =   self.resp2['player']['xp']  - self.lastexp 
       print "Tick - " + str(self.resp['neoUsername']) + " | Level=" + str(self.resp['habitariumLevel']) + "| +exp = " +  str(thisexp) + "| total exp = " + str(self.resp2['player']['xp']) + "/" + str(maxxp) 
       self.lastexp = self.resp2['player']['xp']
       if (self.resp2['player']['xp'] > maxxp):
          print "leveled up sending next level gains"
          self.player_service.nextLevelGains()
       playerid =  self.resp2['player']['m_id']

       self.speandresources() #Speand resources when 10k+ resources (even at level 1 a player has enough storage centeres for this , kickstart exploit handles that)
       self.buildpremap_recode() # Build a optimized map using items in bacpack
       self.checknesters() #Check for none busy nesters and place them on a nest
       #self.dummybuild() # We use 4 tiles in premap as dummy build tiles , to build trash items and earn +200exp , this functions removes them if they are finished building (allows new ones to be placed)
       #print str(self.checknonebuiltbuildings_recode())
       if self.checknonebuiltbuildings_recode() == 0: #Check for unbuilt buildings
           if self.findnonehealthybuildings() == 0:
               self.checkworkers() #Check for workers with no jobs set only if all buildings done.
       self.checkhungry() #Check hungry/low hp pets and bed them
       self.checkhouses() #Check for full houses with healed pets and move them out
       self.checkupgrades(playerlevel) # Check for upgrades based on current player level.


                 



         #Egg check delayed:
       if (time.time() - float(self.LAST_EGG_CHECK_TIME) > 120): #2 mins
           self.LAST_EGG_CHECK_TIME = time.time() #Update time
           self.checkinveggs() 

           if int(playerlevel) == 50:
               self.checkeggs50(playerlevel) #Special logic if we are 50 , we want to filter out soldiers and nesters now
           else:           
               self.checkeggs(playerlevel) #Check for eggs/discard(+200exp them)
         #Gem check delayed:
       if (time.time() - float(self.LAST_GEM_CHECK_TIME) > 120): #2 mins
           self.LAST_GEM_CHECK_TIME = time.time() #Update time
           self.checkgems() #Check for any gems and collect them

     



       print "tick complete"



    # except:
    
   #     time.sleep(10)
