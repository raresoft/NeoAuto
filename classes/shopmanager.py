
#Import Needed Classes:
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range







#Begin Class
class shopmanager:


    def __init__(self,acc,settingsmanager):
        self.acc = acc
        self.settingsmanager= settingsmanager
        self.withdrawtill = self.settingsmanager.getvalue("shop","withdrawtill")
        self.lasttilltime = self.settingsmanager.getvalue('timecache','lasttilltime')
        self.autoprice_on = self.settingsmanager.getvalue("shop","autoprice")
        self.autoprice_file = self.settingsmanager.getvalue("shop","autoprice_file")

        self.lastpricetime = self.settingsmanager.getvalue('timecache','lastpricetime')



        self.buylist = self.fetchfilterlist(self.autoprice_file)
        if self.withdrawtill == 'on':
            #If withdraw from till is on , make sure we own a shop on run , to prevent any issues
            self.checkshop()
        if self.autoprice_on == 'on':
            #If Auto price is on , make sure we own a shop on run , to prevent any issues
            self.checkshop()



    def striphtml(self,html):
        #Getting stuff from this page is tricky , so instead of using the entire html string i do some things to it and return only the relevant part


        startpos1 = html.find('<b>Rm</b></td>')
        startpos2 = html.find('=remove_all')
        html = html[startpos1:startpos2]


        #We are going to extract each item at '><b> , the first item will be a item in our shops stocks name
        #The second item is a invalid tag "STOCK" , we dont want this tag and will remove it from the html string to fix later extractions

        startpos = 0 #Pos to search from initially


        itemcount=0
        postdata = {}
        postdata["type"] = "update_prices"
        postdata["order_by"] = ""
        postdata["view"] = ""
        postdata["lim"] = "30"
        #print html
        finalhtml = html
        thestartpos = 0

        while not html.find("'><b>",thestartpos)== -1:

            itemcount = itemcount +1


            startpos1 = html.find("'><b>",thestartpos) +5
            endpos1 = html.find('</b>',startpos1) #Item id end


            itemname= html[startpos1:endpos1]

            if itemcount == 2:

                replacestr = "'><b>" + itemname + '</b>'
                finalhtml = finalhtml.replace(replacestr,"")
                itemcount = 0
            thestartpos = endpos1

        return finalhtml

    def filtermatch(self,itemname):
        #Checks if a item is found in users text file
        theret = ["-1"]
        for x in self.buylist:
            y = x.split(':')
            if y[0] == itemname:
                theret = y


        return theret




    def fetchfilterlist(self,thefolder):
       #Load the sell list
        f = open(thefolder  )
        lines = f.readlines()
        f.close()
        lines2=[]
        for x in lines:
            lines2.append(x.replace("\n",""))

        return lines2



    def priceitems(self):
        self.buylist = self.fetchfilterlist(self.autoprice_file)
        html = self.acc.get("http://www.neopets.com/market.phtml?type=your")
        html = self.acc.cleanhtml
        print "Getting current stock list"
        self.lastpricetime = time.time()
        self.settingsmanager.setvalue("timecache","lastpricetime" , self.lastpricetime )




        if html.find("no items in your") > 1:
            print "no stock in your shop"
            return
        else:


            html= self.striphtml(html)




            thestartpos = html.find("<b>Rm</b>") + 5
            itemcount=-1
            postdata = {}
            postdata["type"] = "update_prices"
            postdata["order_by"] = ""
            postdata["view"] = ""
            postdata["lim"] = "30"


            while not html.find("'><b>",thestartpos)== -1:


                #Start itemname
                startpos1 = html.find("'><b>",thestartpos) +5
                endpos1 = html.find('</b>',startpos1) #Item id end



                itemname= html[startpos1:endpos1]

                thestartpos = endpos1

             #   continue

                startpos2 = html.find("obj_id_",endpos1)
                startpos3 = html.find("value='",startpos2) +7
                endpos2 = html.find("'",startpos3) #Item id end
                itemid= html[startpos3:endpos2]

                startpos4 = html.find("oldcost_",endpos2)
                startpos5 = html.find("value='",startpos4) +7
                endpos3 = html.find("'",startpos5) #Item cost end
                itemoldcost= html[startpos5:endpos3]

                startpos6 = html.find("back_to_inv[",endpos2)
                startpos7 = html.find("]",startpos6) +1

                back2invname= html[startpos6:startpos7]

                #thestartpos = html.find('<b>Special</b>' , startpos7)




                postdata["obj_id_" + str(itemcount)] = itemid
                postdata["old_cost_" + str(itemcount)] = itemoldcost

                postdata[back2invname] = "0"

                thenewcost=0

                theresult = self.filtermatch(itemname)
                if not theresult[0]   == "-1":

                    itemprice =theresult[1]
                    postdata["cost_" + str(itemcount)] = itemprice

                    print "Auto Pricer , priced " + itemname + ' at ' + str(itemprice) + ' Neopoints'
                else:

                    postdata["obj_id_" + str(itemcount)] = itemid
                    postdata["old_cost_" + str(itemcount)] = itemoldcost
                    postdata["cost_" + str(itemcount)] = itemoldcost
                    postdata[back2invname] = "0"





            html=self.acc.post("http://www.neopets.com/process_market.phtml",postdata)














    def checktill(self):

        html = self.acc.get('http://www.neopets.com/market.phtml?type=till')

        #Get raw amount from html
        pos1 = html.find('You currently have ')+22 #We skip the html bold tag here wich is why we are +3 more than the letter count
        pos2 = html.find('NP',pos1)


        tillamount_raw = html[pos1:pos2] #This is the amount of np , but including the commas. We cant use math functions with commas so... remove
        tillamount_clean = tillamount_raw.replace(",","")
        if int(tillamount_clean) > 0:
            print "Withdrawing " + tillamount_raw + " neopoints, from your shop till!"
            postdata = {'type' : 'withdraw' ,
                'amount' : tillamount_clean}

            html=self.acc.post('http://www.neopets.com/process_market.phtml',postdata,'http://www.neopets.com/market.phtml?type=till')

        self.lasttilltime = time.time()
        self.settingsmanager.setvalue("timecache","lasttilltime" , self.lasttilltime )


    def checkshop(self):
        #Create a shop if needed
        html = self.acc.get("http://www.neopets.com/market.phtml?type=your")
        if html.find("You don't have your own shop yet!") > 1:
            print "no shop"
            postdata = {'shop_name': "NeoShop", "shop_world": "0" ,  "description": "Welcome to my shop",  "remLen": "3957","shopekeeper_name": "greeter","shopekeeper_greeting": "hello there"}
            html = self.acc.post("http://www.neopets.com/process_market.phtml",postdata)
            print "shop created"



