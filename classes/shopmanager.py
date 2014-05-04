
#Import Needed Classes:
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range







#Begin Class
class shopManager:


    def __init__(self,acc,settingsmanager):
        self.acc = acc


    def dotick(self):
        #print self.selllist
        html = self.acc.get("http://www.neopets.com/market.phtml?type=your")
        if html.find("You don't have your own shop yet!") > 1:
            print "no shop"
            postdata = {'shop_name': "NeoShop", "shop_world": "0" ,  "description": "Welcome to my shop thankyou for stopping by",  "remLen": "3957","shopekeeper_name": "greeter","shopekeeper_greeting": "hello there"}
            html = self.acc.post("http://www.neopets.com/process_market.phtml",postdata)
            print "shop created"




