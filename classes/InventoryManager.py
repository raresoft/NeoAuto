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
        self.lastsdbticktime = self.settingsmanager.getvalue("timecache","lastsdbticktime")
        self.maxspeand = self.settingsmanager.getvalue("trainer","maxspeand")

    def searchinvenotry(self,itemname):
        html = self.acc.get('http://www.neopets.com/quickstock.phtml')
        if html.find(itemname) > 1:
            return True
        else:
            return False




    def findlowestshopwizprice(self,itemname,maxspeand=9999):
        #Search shop wizard for a item , get the first results buy url
        #print "test= " + maxspeand
        itemname = itemname.replace('+' , ' ' ) #We want spaces in the itemname this time around , not + symbols (neopets programmers are inconsistant with this)


        postdata = {}
        postdata["type"] = "process_wizard"
        postdata["feedset"] = "0"
        postdata["shopwizard"] = itemname
        postdata["table"] = "shop"
        postdata["criteria"] = "exact"
        postdata["min_price"] = "0"
        postdata["max_price"] = str(maxspeand)


        html=self.acc.post("http://www.neopets.com/market.phtml" , postdata , "http://www.neopets.com/market.phtml?type=wizard")
      #  html = self.acc.post('http://www.neopets.com/market.phtml',postdata,'http://www.neopets.com/market.phtml?type=wizard')
        if html.find('browseshop.phtml?owner=') > 1:
            #A item was found matching our search , get the first entrys buy url
            pos1 = html.find('browseshop.phtml?owner=')
            pos2 = self.acc.cleanhtml.find("'",pos1)
            buyurl = 'http://www.neopets.com/' + html[pos1:pos2]
            return buyurl
        else:
            print "item not found on shop wizard"
            return ''
    def shopwizardbuy(self,buyurl,itemname):
        #We are on a users shop page , from here we get the first item from the html (the matching item from shop wiz , and buy it)
        #Return 1 on success
        html = self.acc.get(buyurl)
        itemname = itemname.replace('+' ,' ')
        if not html.find(itemname) > 1: #Make sure item is still there , so we dont buy a invalid item
            print 'ret'
            return 0
        finalbuyurlpos1 = html.find('buy_item.phtml?lower=0')
        finalbuyurlpos2 = self.acc.cleanhtml.find("'",finalbuyurlpos1)
        finalbuyurl = 'http://www.neopets.com/' + html[finalbuyurlpos1:finalbuyurlpos2]
        finalhtml = self.acc.get(finalbuyurl,buyurl)
        if not html.find('Item not found') > 1: #We got the item.. (More checks needed here for not enough np ect)
            return 1
        else:
            #We did not get the item
            return 0


        print finalhtml


    def removefromsdb(self,itemname):
        #Search for a item by name and if found remove it from sdb to inventory
        itemname = itemname.replace(' ', '+')
        html = self.acc.get('http://www.neopets.com/safetydeposit.phtml?obj_name=' + itemname + '&category=0' , 'http://http://www.neopets.com/safetydeposit.phtml')
        if html.find('Not finding any items with that') > 1:
            print "ITEM NOT FOUND IN SDB"
            theret = self.findlowestshopwizprice(itemname,self.maxspeand)
            if not theret == "":
                print "Buying item from show wizard..."
                if (self.shopwizardbuy(theret,itemname)) == 1:
                    self.searchinvenotry(itemname)
                    #We got a item , search invenotry for it
            #print htmlhttp://www.neopets.com/safetydeposit.phtml
        else:
            print itemname + ' found in sdb'
            #Get the item id...
            pos1 = html.find('onClick=passPin')
            pos2 = html.find (',',pos1) + 1
            pos3 = html.find (',',pos2)
            itemid = html[pos2:pos3]

            #Is pin needed:
            if html.find('PIN number') > 1:
                html = self.acc.get('http://www.neopets.com/process_safetydeposit.phtml?remove_one_object=' + itemid  + '&offset=0&obj_name=' + itemname + '&catergory=0&pin=' + self.acc.neopin)
            else:
                #no pin needed
                html = self.acc.get('http://www.neopets.com/process_safetydeposit.phtml?remove_one_object=' + itemid  + '&offset=0&obj_name=' + itemname + '&catergory=0&pin=')





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
        self.settingsmanager.setvalue("timecache","lastsdbticktime" , self.lastsdbticktime )

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

                        thefilter = self.GetItemFilterByname(theitemname)

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














