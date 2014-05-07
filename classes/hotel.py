#Auto hotel class - RareDareDevil Aka Darkbyte:
#This class just places pets in the hotel if needed , this is usefull for keepgn pets healthy / happy.
#We can do activepet only or all pets on the account , hotels are super cheap for a weeks stay its like 90np..
#Having healthy/full pets for battling ect is s must so this is very usefull along side auto battle.
import time

class hotel:

    def __init__(self,acc,settingsmanager,mobilehandler):
        self.acc = acc
        self.settingsmanager = settingsmanager
        self.mobilehandler = mobilehandler
        self.autohotel_on = self.settingsmanager.getvalue("hotel","autohotel")
        self.hotelmode = self.settingsmanager.getvalue("hotel","mode")
        self.lasthoteltime = self.settingsmanager.getvalue("timecache","lasthoteltime")



    def putpetinhotel(self,petname):
        #Stick a pet in a hotel , cheapest hotel (addons ect make no difference)
        postdata = {'pet_name' : petname ,
                    'hotel_rate' : '5',
                    'nights' : '28'}
        self.acc.post('http://www.neopets.com/book_neolodge.phtml' ,postdata , 'www.neopets.com/book_neolodge.phtml' )

    def dotick(self):


        self.lasthoteltime = time.time()
        self.settingsmanager.setvalue("timecache","lasthoteltime" , self.lasthoteltime )
        print 'Running Auto hotel'
        if self.hotelmode == 'activepet':
            #We are only sticking the active pet in a hotel...
            petname = self.mobilehandler.activepetname
            self.putpetinhotel(petname)

        else:
            #Put all pets in the hotel
            petlist =  self.mobilehandler.getpetlist()
            for pet in petlist:
                petname = pet['name']
                self.putpetinhotel(petname)
