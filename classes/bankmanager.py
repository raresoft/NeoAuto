

class bankmanager:
    def __init__(self,acc,mobilehandler,settingsmanager):
        self.acc = acc
        self.mobilehandler = mobilehandler
        self.checknp_on = settingsmanager.getvalue("bank","checknp_on")
        self.minnponhand = settingsmanager.getvalue("bank","minnponhand")
        self.withdrawamount = settingsmanager.getvalue("bank","withdrawamount")




    def deopsitall(self):
        currentnp = self.mobilehandler.getnp()
        self.depositnp(currentnp)


    def depositnp(self,amount):
        postdata = {'type' : 'deposit' , 'amount' : str(amount)}
        #print postdata
        self.acc.post('http://www.neopets.com/process_bank.phtml',postdata,'http://www.neopets.com/bank.phtml')


    def withdrawnp(self,amount):

        postdata = {'type' : 'withdraw' , 'amount' : str(amount)}
       # print postdata
        self.acc.post('http://www.neopets.com/process_bank.phtml',postdata,'http://www.neopets.com/bank.phtml')

    def checknpbalance(self):
        #Check players current np is more than minamum....

        if self.checknp_on == 'on':
            currentnp = self.mobilehandler.getnp()

            #Is current np  < minnponhand
            if int(currentnp) < int(self.minnponhand ):
                print 'Not enough np on hand , withdrawing ' + self.withdrawamount + ' np'
                self.withdrawnp(self.withdrawamount)




