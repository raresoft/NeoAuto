#This class links to the mysql database and inserts logs / pulls data


#Import Needed Classes:
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range

from NeoAccount import NeoAccount
#Setup Default vars / classes
confighandler = ConfigParser.RawConfigParser() #Used for .cfg files





#Begin Class
class InventoryManager:


    #Initialize this class
    def __init__(self,acc,settigsfile,settingsmanager ):
        self.acc = acc
        self.settingsmanager = settingsmanager
       # self.newsql = newsql
        self.filterlist = []
        self.filterlist = self.fetchfilterlist(settigsfile)
        self.lastsdbticktime = self.settingsmanager.getvalue("timecache","lastsdbtime")

    def checktick(self):
        #Checks if a sdb tick is needed
        doneone=0
        if (time.time() - float(self.lastsdbticktime) > 3600): #SdbTime (1 hour checks)


            self.lastsdbticktime = time.time()
            self.settingsmanager.setvalue("timecache","lastsdbtime" , self.lastsdbticktime )
            self.Depositall()
            doneone=1
        return doneone


    def getrawfilterlist(self):
        #Just returns the filter list array

        return self.filterlist



    def fetchfilterlist(self,thefolder):
       # print str(thefolder)
        f = open(thefolder  )
        lines = f.readlines()
        f.close()
        lines2=[]
        for x in lines:
            lines2.append(x.replace("\n",""))
            #print "line" + x.replace("\n","")
            #self.getitemfilter_byname("lucodestrong")
        return lines2


    def GetItemFilterByname(self,itemname):
        #Gets the filter type for a certain item.
        print "Inventory manager - TEst"
        self.filterlist = self.getrawfilterlist()
        #Loop each item in the filter list to find its name...
        thereturn = None #Return none if no filter
        for items in self.filterlist:
            splititems =  items.split(':'); #Split the current item at ":"
            currentitemname = splititems[0] #Itemname
            currentitemfilter = splititems[1]
            if (currentitemname == itemname): #Clash found
                print "Clash found for item " + currentitemname
                thereturn = splititems[1]
        return thereturn #Return either "None" or the filter if the item matched a filter

    def test(self):
        print "Inventory manager - TEst"
        self.filterlist = self.getrawfilterlist()
        #Loop each item in the filter list to find its name...
        for items in self.filterlist:
            print items.split(':');
        print self.GetItemFilterByname("Lu CodeStone")
        print self.filterlist

    def Depositall(self):
        html=self.acc.get("http://www.neopets.com/quickstock.phtml?buyitem=0","http://www.neopets.com/quickstock.phtml")
        arrynum=1
        self.itemcollection=[]
        startopos3 = 0
        postdata = {}
        postdata["buyitem"] = "0"

        #self.itemdblogic(html)
        #print html
        print "Deposit all Logic"
        startopos3 = html.find('<b>Shed</b>') +7
        endpos = startopos3
        outputurl = "http://www.neopets.com/process_quickstock.phtml"
        while html.find("id_arr[",startopos3) > 1:
            theitemid="0"
            theitemname=""
            startpos = html.find("id_arr[",startopos3) #Few words before id
            startpos2 = html.find('value="',startpos) +7



            startpos4= html.find('left">',endpos) +6 #Few words before name
            startpos5= html.find('</TD>',startpos4) #Few words after name
            endpos = html.find('"',startpos2)
            theitemkey = html[startpos2:endpos]
            theitemname = html[startpos4:startpos5]
            startopos3 = endpos+10
            if not startpos5 == -1:
                ##if not theitemkey == "0":
                    if not theitemname == "":
                        print "rdd"
                        thefilter = self.GetItemFilterByname(theitemname)
                        print thefilter
                        if not thefilter == None:

                            #print "Clash Found2" + str(theitemname)



                            #Where should we send this item?
                            if thefilter == "shop": #The filter in lowercase to prevent a mismatch
                                print "clash2"
                                postdata["id_arr[" + str(arrynum) + "]"] = html[startpos2:endpos]
                                postdata["radio_arr[" + str(arrynum) + "]"] = "stock" #This items going to the users shop
                                self.itemcollection = self.itemcollection + ["&id_arr[" + str(arrynum) + "]=" + html[startpos2:endpos] + "&radio_arr[" + str(arrynum) + "]=deposit"]
                                arrynum = arrynum + 1
                        else:
                                #print "No filter , sending to sdb" + thefilter.lower
                            postdata["id_arr[" + str(arrynum) + "]"] = html[startpos2:endpos]
                            postdata["radio_arr[" + str(arrynum) + "]"] = "deposit"
                            self.itemcollection = self.itemcollection + ["&id_arr[" + str(arrynum) + "]=" + html[startpos2:endpos] + "&radio_arr[" + str(arrynum) + "]=deposit"]
                            arrynum = arrynum + 1


        #print postdata
        html = self.acc.post(outputurl, postdata ,"http://www.neopets.com/quickstock.phtml")
        #print html
        if  html.find('You are trying to move items into a shop') > 1:
            #No shop found make one...
            #print self.acc.user + "'s shop
            #print "TESSSSTT"
            postdata = {'shop_name': self.acc.user + "'s shop",
                       'shop_world': "0",
                       'description': "Welcome+to+my+shop+",
                       'remLen': "3981",
                       'shopkeeper_name': "Shoppy+McShopFace",
                       'shopkeeper_greeting': "Hello+my+freind+thankyou+for+visiting"
                        }

            html2 = self.acc.post("http://www.neopets.com/process_market.phtml", postdata ,"http://www.neopets.com/market.phtml?type=edit")
            #print html2
            if (html2.find("Neopoints to open your own shop") > 1): #Not enough np

                time.sleep(5)
               # print "NOOOOO"
                return 0 #Return 0 so we dont get stuck in a loop
            else:
                # print html2
                 time.sleep(5)
                 self.Depositall() #Recall this function now a shop is made
            #print html













