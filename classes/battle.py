#Auto Battle by raredaredevil aka DarkByte
#Currently targeted towards  punchbag bob only

import json
import time
import ConfigParser # Config parser class (.cfg files)

class battle:
    def __init__(self,acc,mobilehandler,settingsmanager):
        self.acc = acc
        self.mobilehandler = mobilehandler
        self.settingsmanager = settingsmanager
        self.enemyname = self.settingsmanager.getvalue("battle","enemyname")
        self.lastbattletime = self.settingsmanager.getvalue("timecache","lastbattletime")
        self.battle_on = self.settingsmanager.getvalue("battle","battle_on")
        self.punchbag_on = self.settingsmanager.getvalue("battle","punchbagbob")


    def startpunchbag(self):
        temphtml = self.acc.get('http://www.neopets.com/userlookup.phtml?user=' + self.acc.user)
        if temphtml.find('Beating Punchbag Bob CHAMPION!!!')  >1:
            #User already has this trhopy , turn off
            print "You already have the punchbag bob trophy , disbling punchbag bob fighter "
            self.settingsmanager.setvalue("battle","punchbagbob" , 'off' )
            self.punchbag_on ='off'
            return
        else:
            print "Punchbag Tick"
            self.dotick('Punchbag Bob')

    def geteligibalstate(self):
        #Returns a list:
        #['Petname']['Eligibal to battle']
        #For all pets
        #If the target pet is not eligable we can skip a tick , wait for auto hotel if its enabled to do its thing
        #and await next time when our pet should be full stats and now eligable to battle.

        print 'Getting Eligibale list'



    def fetchfilterlist(self,thefolder):
       #Load the sell list
        f = open(thefolder  )
        lines = f.readlines()
        f.close()
        lines2=[]
        for x in lines:
            lines2.append(x.replace("\n",""))

        return lines2

    def getenemyhp(self,html):
        #Finds a item id on the battle html , by searching for a itemname
        temppos = html.find('var hud = new')

        cleanhtml = html.replace('"' , "'")
        pos1=  html.find("$('#p2hp'",temppos)
        pos2 = cleanhtml.find("l('",pos1) +3

        pos3 = cleanhtml.find("'",pos2)
        return html[pos2:pos3]


    def getitemid(self,html,itemname):
        #Finds a item id on the battle html , by searching for a itemname
        pos1= html.find(itemname)
        cleanhtml = html.replace('"' , "'")
        pos2 = cleanhtml.find("id='",pos1)+4
        pos3 = cleanhtml.find("'",pos2+2)
        return html[pos2:pos3]
    def getbestweapon(self):
        #Loads the battle list in \NeoAuto\list\battle\battleitems.txt
        #items at top get priority
        print 'Best weapon'
        html = self.acc.get('http://www.neopets.com/dome/arena.phtml')
        weaponlist = self.fetchfilterlist('./list/battle/battleitems.txt')
        pos1 = self.acc.cleanhtml.find("p1equipment'>")
        pos2 = html.find('fsright',pos1)
        trimhtml = html[pos1:pos2]
        #print trimhtml
        retlist = []
        for weapon in weaponlist:
            if trimhtml.find(weapon) > 1: #Weapon found in html , add it to list
                retlist.append(weapon)

            #We found multiple matching items in our pets eq list so use both

        return retlist

    def getbattleid(self,html):
        pos1 = html.find("battleid:'")+10

        pos2 = html.find("'",pos1+2)
        return html[pos1:pos2]



    def getbattlestep(self,html):
        pos1 = html.find("step")


        pos2 = html.find("value=",pos1) +7
        pos3 = html.find('"',pos2+1)
        return html[pos2:pos3]


    def dotick(self,enemyname =''):

        battlehtml = self.acc.get('http://www.neopets.com/dome/arena.phtml')
        if self.getbattlestate(battlehtml) == 'inbattle':
            pos1 = battlehtml.find("p2name').html")
            pos2 = battlehtml.find("('",pos1) +2
            pos3 = battlehtml.find("');",pos2)
            if enemyname == '':
                enemyname = battlehtml[pos2:pos3]
            else:
                enemyname = self.enemyname



            self.enemyconfig = ConfigParser.ConfigParser()
            print 'enemyname' + enemyname
            self.enemyconfig.read("./list/battle/logic/" + enemyname + '.cfg')
            print "Getting battle state"
            if self.getvalue("attack","attacktype") == 'weapon':
                weaponlist = self.getbestweapon()
                if len(weaponlist) > 1:
                    #More than one item found , equip first two in list (best 2) and double attack
                    print 'Sending double attack'
                    item1name = weaponlist[0]
                    item2name = weaponlist[1]


                elif len(weaponlist)  == 1:
                    item1id = self.getitemid(battlehtml,item1name)
                    item2id = ''

                else:
                    # No weapons found
                    return


                thebattleid = self.getbattleid(battlehtml)
                thestep = self.getbattlestep(battlehtml)

                postdata = {'p1s' : '',
                             'eq1' : item1id,
                              'eq2' : item2id,
                              'p1a' : '',
                               'chat' : '',
                               'action' : 'attack',
                               'ts' : time.time(),
                               'battleid' : thebattleid,
                               'step' : thestep,
                               'intro' : '0',
                               'status' : '1'
                               }

                print 'Enemy Hp = ' + self.getenemyhp(battlehtml)
                newhtml =self.acc.post('http://www.neopets.com/dome/ajax/arena.php',postdata ,'http://www.neopets.com/dome/arena.phtml')
                jsondata = json.loads(newhtml)
                if jsondata['battle']['statusmsg'] == 'Winner: ':
                    print 'Won battle...'
                    for prize in jsondata['battle']:
                        #self.battlecount = int(self.battlecount) + 1
                        #self.settingsmanager.setvalue("battle","battlecount" , self.battlecount )
                        if jsondata['battle']['prize_messages']:
                            #Reached our limit for today
                            print 'Battle limit reached for today'
                            self.lastbattletime = time.time()

                            self.settingsmanager.setvalue("timecache","lastbattletime" , self.lastbattletime )
                            return
     #   self.lasthoteltime = time.time()
     #   self.settingsmanager.setvalue("timecache","lasthoteltime" , self.lasthoteltime )

        else:

             if enemyname == '':
                enemyname = self.enemyname


             print 'enemyname' + enemyname
             self.enemyconfig = ConfigParser.ConfigParser()
             self.enemyconfig.read("./list/battle/logic/" + enemyname + '.cfg')
             if  enemyname == '':
                return
             print "./list/battle/logic/" + enemyname + '.cfg'
             starthp = self.getvalue("health","starthp")
             enemydifficulty = self.getvalue("settings","enemydifficulty")
             targetpet = self.mobilehandler.activepetname
            # print targetpet
             petdatastr=[]
             petlist = self.mobilehandler.getpetlist()
             for petstr in petlist:
                if petstr['name'] == targetpet:
                    petdatastr = petstr

             currenthp = int(petdatastr['health'])
             if currenthp > int(starthp):
                print 'Starting a battle'
                battleid = self.getbattleid2(enemyname)
                print 'petname =' + targetpet
                print 'toughness='  + enemydifficulty
                print 'Battleid =' + battleid
                postdata = {'type' : '2',
                            'pet' : targetpet,
                            'npcId' : battleid,
                            'toughness' : enemydifficulty}
                finalhtml = self.acc.post('http://www.neopets.com/dome/ajax/startFight.php',postdata)


    def getbattleid2(self,enemyname):
        #Get a battle id from the game launch page
        html = self.acc.get('http://www.neopets.com/dome/fight.phtml')
        html = self.acc.cleanhtml
        chunks =[]
        startpos =0


        while html.find("class='npcRow" , startpos) > 1:
            pos1 = html.find("class='npcRow" , startpos)
            pos2 = html.find('</tr>',pos1)
            startpos = pos2
            chunks.append(html[pos1:pos2])
        for htmlchunk in chunks:
            htmlchunk = htmlchunk.lower()
            lowerenemyname = enemyname.lower()
            if htmlchunk.find(lowerenemyname) > 0:
                pos3 = htmlchunk.find("data-oppid='") +12
                pos4 = htmlchunk.find("'" , pos3)
                battleid = htmlchunk[pos3:pos4]

                return battleid

    def getvalue(self,Section,value):


       #    self.enemyconfig.read("./cache/" + self.username + ".cfg")

        # Set the third, optional argument of get to 1 if you wish to use raw mode.
        return self.enemyconfig.get(Section, value, 0)




    def getbattlestate(self,battlehtml):
        #Start a battle with X enemy and load battle logic from ./list/battle/logic/enemyname.txt


        if battlehtml.find('p2headshot') > 1:
            #Already in battle
            return 'inbattle'




