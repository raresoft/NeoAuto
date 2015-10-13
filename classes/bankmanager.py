

class bankmanager:
    def __init__(self,acc,mobilehandler,settingsmanager):
        self.acc = acc
        self.mobilehandler = mobilehandler
        self.checknp_on = settingsmanager.getvalue("bank","checknp_on")
        self.minnponhand = settingsmanager.getvalue("bank","minnponhand")
        self.withdrawamount = settingsmanager.getvalue("bank","withdrawamount")


        testhtml = self.acc.get('http://www.neopets.com/bank.phtml')
        if testhtml.find("I see you don't currently") >1 :
            print 'Bank account not found , so opening one...'
            postdata = {"type" : "new_account",
            "name" : self.acc.user,
            "add1" : 'home',
            "employment" : 'Chia Custodian',
            "salary" : '10,000 NP and below',
            "account_type" : '0',
            "initial_deposit" : '1',
            }
            html=self.acc.post('http://www.neopets.com/process_bank.phtml',postdata,'http://www.neopets.com/bank.phtml')
            if (html.find("Activation Code!") > 1):
                #Account is not activated , so diasble bank functions
                print "Bank Account cannot be created , you must activate your account first! Bank functions have been disabled"
                self.checknp_on = "off"
            
    def deopsitall(self):
        currentnp = self.mobilehandler.getnp()
        self.depositnp(currentnp)


    def depositnp(self,amount):
        postdata = {'type' : 'deposit' , 'amount' : str(amount)}
        #print postdata
        self.acc.post('http://www.neopets.com/process_bank.phtml',postdata,'http://www.neopets.com/bank.phtml')


    def withdrawnp(self,amount):





       html1=self.acc.get('http://www.neopets.com/bank.phtml') #We use this to see if a pin is set
       postdata={}
       if html1.find('Enter your') > 1:
            postdata = {'type' : 'withdraw' , 'amount' : str(amount) , 'pin' : self.acc.neopin}
       else:
            #no pin set
            postdata = {'type' : 'withdraw' , 'amount' : str(amount)}



       self.acc.post('http://www.neopets.com/process_bank.phtml',postdata,'http://www.neopets.com/bank.phtml')

    def checknpbalance(self):
        #Check players current np is more than minamum....

        if self.checknp_on == 'on':
            currentnp = self.mobilehandler.getnp()

            #Is current np  < minnponhand
            if int(currentnp) < int(self.minnponhand ):
                print 'Not enough np on hand , withdrawing ' + self.withdrawamount + ' np'
                self.withdrawnp(self.withdrawamount)




