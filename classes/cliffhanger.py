#Self learning cliffhanger solver
import time
import random
from logwriter import logwriter

#If a new (unseen) clue comes up , trys random words and remembers patters it tried until it knows the entire solution
class cliffhanger:
    def __init__(self,acc,settingsmanager,mobilehandler):
        self.acc = acc
        self.cliffhangeron = settingsmanager.getvalue("games","cliffhangeron")
        self.mobilehandler = mobilehandler
        self.settingsmanager = settingsmanager
    def fetchfilterlist(self):
        thefolder = './list/cliffhanger/logic.txt'
       # print str(thefolder)
        f = open(thefolder  )
        lines = f.readlines()
        f.close()
        lines2=[]
        for x in lines:
            lines2.append(x.replace("\n",""))

        return lines2

    def gettargetpattern(self,html):
        #Get the pattern of target letters
        pos1 = html.find('YOUR PUZZLE')
        pos1a = html.find('bgcolor="skyblue',pos1)
        pos1b  = html.find('<b>',pos1a)

        pos2  = html.find('<br><br>',pos1b)




        rawdata = html[pos1b:pos2]
        #print rawdata
        #string html /spaces

        rawdata = rawdata.replace(' ','')
        rawdata = rawdata.replace('<b>','')
        rawdata = rawdata.replace('</b>','')
        rawdata = rawdata.replace('<br>',' ')
        rawdata = rawdata.replace('&nbsp;',' ')

        return rawdata

    def matchpattern(self,knownlist,targetletters):
        #First check if the strings length = same as any in text files , if not return 0 (no match found)

        theret = []
        #Get items in the knownlist that have same amount of letters as the knownlist

        targetitem =  self.getstringpattern(targetletters)

        for item in knownlist:
            if self.getstringpattern(item) ==targetitem:
                    theret.append(item)
        return theret







    def getletterlist(self,html):
        #Get none used letters from the html source not used in this version
      #  http://www.neopets.com/games/cliffhanger/process_cliffhanger.phtml?choice=

        ret = []
        posloop = 0
        while not  html.find('process_cliffhanger.phtml?choice=',posloop) == -1: #Do until we got them all
            posstart = html.find('process_cliffhanger.phtml?choice=',posloop) +33
            posend =html.find("'",posstart)
            posloop = posend + 1
            tempitem = html[posstart:posend]
            tempitem.rstrip ()
            ret.append(tempitem)



        return str(ret)




    def getstringpattern(self,targetstr):
        #Get a pattern based on the current letters in a string e.g
        #'rdd rox my sox' = 3323 because..
        #  3   3   2  3    letters in each word

        testlist = targetstr.split(' ')
        theret=[]
        for word in testlist:
            if not len(word) == 0:
                theret.append(len(word))

      #  print 'targetstr=' + targetstr + '  /n currentstr=' + str(theret)
        return str(theret)

    def startnewgame(self,html):
        #start a new game if needed (ie we are on the page with the post crap
        gameskills = ['1','2','3']
        random.shuffle(gameskills)
        theret = ''
        if html.find('Skill Level') >1:
        #We are on the right page to start a new game
            postdata = {'start_game' : 'true',
                        'game_skill' : gameskills[0]}
            theret = self.acc.post('http://www.neopets.com/games/cliffhanger/process_cliffhanger.phtml',postdata)

        return theret

    def skipoldgame(self,targetletters):
        if targetletters.find("='red'")>1:
            #A game is already in progress on load and letters have been sent , I did not code logic for this so just end the game by sending a random bad string
            print 'old game found ending'

            random.shuffle(knownlist)
            randitem = knownlist[0]# a random item in the known list
            postdata = {'solve_puzzle' : randitem}
            html=self.acc.post('http://www.neopets.com/games/cliffhanger/process_cliffhanger.phtml',postdata)
            self.startnewgame(html)


    def tick(self):
        #Play a single game till finish
        startnp = self.mobilehandler.getnp()

        print 'Cliffhanger - Tick'
        html = self.acc.get('http://www.neopets.com/games/cliffhanger/cliffhanger.phtml')

        knownlist = self.fetchfilterlist()

        targetletters = self.gettargetpattern(html)
        self.skipoldgame(targetletters)

        temp =  self.startnewgame(html)
        if not temp == '':
            html = temp
        targetletters = self.gettargetpattern(html)

        matchpatterval = self.matchpattern(knownlist,targetletters)

        if matchpatterval == []:

            print 'Uknown cliffhanger pattern , skipping..'
            random.shuffle(knownlist)
            randitem = knownlist[0]# a random item in the known list
            postdata = {'solve_puzzle' : randitem}
            html=self.acc.post('http://www.neopets.com/games/cliffhanger/process_cliffhanger.phtml',postdata)
        else:

            postdata = {'solve_puzzle' : matchpatterval[0]}
            html=self.acc.post('http://www.neopets.com/games/cliffhanger/process_cliffhanger.phtml',postdata)
            print 'solved a puzzle'
            endnp = self.mobilehandler.getnp()
            if startnp == endnp: #np did not increase
                print'Ciff hanger stopped earning np so exited'
                self.cliffhangertime = time.time()
                self.settingsmanager.setvalue("timecache","cliffhangertime" , self.cliffhangertime )
                time.sleep(10)

