#Use http://timezonedb.com/api , currently just gets nst time
#I will recode this later to only use the api once to find the offset value
#Date and time handling is fucking messy , i have to deal with timezones and shit so its easier to just use
#a third party api , could probly sync with windows time servers or something but its hassle right now.

import datetime
import json
import time
class nsthandler():

    def __init__(self,acc):
        self.acc = acc

    def getNst(self):
        #Get posix timestamp for nst
        html = self.acc.get('http://api.timezonedb.com/?zone=America/Phoenix&format=json&key=FGWOF0NHG2ZE')
        jsondata = json.loads(html)
        return jsondata['timestamp']


    def getreadabletime(self):
        #Returns a more readable time
        thetime = self.getNst()

        date = datetime.datetime.utcfromtimestamp(thetime)
        strdate = str(date)
        strdate = strdate.replace('-' , ':')
        datelist = strdate.split(' ')
        return datelist

