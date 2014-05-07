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
        self.invenotrymanageron =self.settingsmanager.getvalue("Settings","autodeposititems")
        self.lastsdbticktime = self.settingsmanager.getvalue("timecache","lastsdbtime")

    def checktick(self):
        #Checks if a sdb tick is needed


        self.lastsdbticktime = time.time()
        self.settingsmanager.setvalue("timecache","lastsdbtime" , self.lastsdbticktime )
        self.Depositall()

        return


    def getrawfilterlist(self):
        #Just returns the filter list array

        return self.filterlist



    def fetchfilterlist(self,thefolder):

        f = open(thefolder  )
        lines = f.readlines()
        f.close()
        lines2=[]
        for x in lines:
            lines2.append(x.replace("\n",""))

            #self.getitemfilter_byname("lucodestrong")
        return lines2


    def GetItemFilterByname(self,itemname):
        #Gets the filter type for a certain item.

        self.filterlist = self.getrawfilterlist()
        #Loop each item in the filter list to find its name...
        thereturn = None #Return none if no filter
        for items in self.filterlist:
            splititems =  items.split(':'); #Split the current item at ":"
            currentitemname = splititems[0] #Itemname
            currentitemfilter = splititems[1]
            if (currentitemname == itemname): #Clash found

                thereturn = splititems[1]
        return thereturn #Return either "None" or the filter if the item matched a filter

    def test(self):

        self.filterlist = self.getrawfilterlist()
        #Loop each item in the filter list to find its name...
        for items in self.filterlist:
            print items.split(':');
        print self.GetItemFilterByname("Lu CodeStone")
        print self.filterlist

    def Depositall(self):
        html=self.acc.get("http://www.neopets.com/quickstock.phtml","http://www.neopets.com/quickstock.phtml")
        arrynum=1
        self.itemcollection=[]
        startopos3 = 0
        postdata = {}
        postdata["buyitem"] = "0"

        self.lastsdbticktime = time.time()
        self.settingsmanager.setvalue("timecache","lastsdbtime" , self.lastsdbticktime )

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


                            if thefilter == "shop": #The filter in lowercase to prevent a mismatch

                                postdata["id_arr[" + str(arrynum) + "]"] = html[startpos2:endpos]
                                postdata["radio_arr[" + str(arrynum) + "]"] = "stock" #This items going to the users shop
                                self.itemcollection = self.itemcollection + ["&id_arr[" + str(arrynum) + "]=" + html[startpos2:endpos] + "&radio_arr[" + str(arrynum) + "]=deposit"]
                                arrynum = arrynum + 1

                            elif thefilter == "donate": #donate item to  money tree
                                postdata["id_arr[" + str(arrynum) + "]"] = html[startpos2:endpos]
                                postdata["radio_arr[" + str(arrynum) + "]"] = "donate" #This items going to the users shop
                                self.itemcollection = self.itemcollection + ["&id_arr[" + str(arrynum) + "]=" + html[startpos2:endpos] + "&radio_arr[" + str(arrynum) + "]=deposit"]
                                arrynum = arrynum + 1
                            elif thefilter == "discard": #discard item
                                postdata["id_arr[" + str(arrynum) + "]"] = html[startpos2:endpos]
                                postdata["radio_arr[" + str(arrynum) + "]"] = "discard" #This items going to the users shop
                                self.itemcollection = self.itemcollection + ["&id_arr[" + str(arrynum) + "]=" + html[startpos2:endpos] + "&radio_arr[" + str(arrynum) + "]=deposit"]
                                arrynum = arrynum + 1

                        else:


                            print thefilter
                                #None set , so send to sdb
                            postdata["id_arr[" + str(arrynum) + "]"] = html[startpos2:endpos]
                            postdata["radio_arr[" + str(arrynum) + "]"] = "deposit"
                            self.itemcollection = self.itemcollection + ["&id_arr[" + str(arrynum) + "]=" + html[startpos2:endpos] + "&radio_arr[" + str(arrynum) + "]=deposit"]
                            arrynum = arrynum + 1


        #print postdata
        html = self.acc.post(outputurl, postdata ,"http://www.neopets.com/quickstock.phtml")
        #print html














