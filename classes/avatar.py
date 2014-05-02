#Automatically get avatars (clickables,some harder ones ect)

#Will get one avatar each tick
import random
import time
class avatar:

    def __init__(self,acc,settingsmanager,mobilehandler):
        self.settingsmanager = settingsmanager
        #self.loadsettings()
        self.acc = acc
        self.mobilehandler = mobilehandler
        self.avataron = self.settingsmanager.getvalue('misc','avatargrabber')
        self.lastavatartime = self.settingsmanager.getvalue('timecache','avatartime')

    def getneededavatars(self):
        #Get a randomized list of the avatars we still need (out of the ones we can automate)
        html = self.acc.get('http://www.neopets.com/neoboards/preferences.phtml')
        theret = []
        if html.find('Xweetok - Faerie') < 1:
            theret.append('Xweetok - Faerie')

        if html.find('Grarrl - Darigan') < 1:
            theret.append('Grarrl - Darigan')

        if html.find('Ruki - Desert') < 1:
            theret.append('Ruki - Desert')
        if html.find('Peophin - Faerie') < 1:
            theret.append('Peophin - Faerie')

        if html.find('Tuskaninny - Relax') < 1:
            theret.append('Tuskaninny - Relax')

        if html.find('Ixi - Disco') < 1:
            theret.append('Ixi - Disco')

        if html.find('Acara - Roberta of Brightvale') < 1:
            theret.append('Acara - Roberta of Brightvale')

        if html.find('Quiggle - Mutant') < 1:
            theret.append('Quiggle - Mutant')
        if html.find('JubJub - Tyrannian') < 1:
            theret.append('JubJub - Tyrannian')
        if html.find('Yurble - Forefitor') < 1:
            theret.append('Yurble - Forefitor')
        if html.find('Lupe - King Altador') < 1:
            theret.append('Lupe - King Altador')
        if html.find('Chomby - Colourful') < 1:
            theret.append('Chomby - Colourful')

 #       if html.find('Mynci - Halloween') < 1:
 #           theret.append('Mynci - Halloween')

        if html.find('Tonu - Mutant') < 1:
            theret.append('Tonu - Mutant')
        if html.find('Lenny - Mutant') < 1:
            theret.append('Lenny - Mutant')

        if html.find('Anubis') < 1:
            theret.append('Anubis')

 #       if html.find('Elephante - To War!') < 1:
#            theret.append('Elephante - To War!')
        if html.find('Aisha - Disco') < 1:
            theret.append('Aisha - Disco')
        if html.find('Snuffly') < 1:
            theret.append('Snuffly')
        if html.find('Bruce - Mutant') < 1:
            theret.append('Bruce - Mutant')
        if html.find('Usul - Royal Boy') < 1:
            theret.append('Usul - Royal Boy')
        if html.find('Cyodrake') < 1:
            theret.append('Cyodrake')

        if html.find('Bori - Grumpy') < 1:
            theret.append('Bori - Grumpy')
        if html.find('Scarabug') < 1:
            theret.append('Scarabug')
        if html.find('Jetsam - Bah!') < 1:
            theret.append('Jetsam - Bah!')

        if html.find('Faerie Pteri') < 1:
            theret.append('Faerie Pteri')

        if html.find('Grarrl - Galem Darkhand') < 1:
            theret.append('Grarrl - Galem Darkhand')
        if html.find('Poogle - Pirate') < 1:
            theret.append('Poogle - Pirate')

        if html.find('Spardel') < 1:
            theret.append('Spardel')
        if html.find('Meerca - Halloween') < 1:
            theret.append('Meerca - Halloween')

        if html.find('Wocky - Camouflage') < 1:
            theret.append('Wocky - Camouflage')

        if html.find('Peophin - Purple') < 1:
            theret.append('Peophin - Purple')

        if html.find('Ixi - Sophie the Swamp Witch') < 1:
            theret.append('Ixi - Sophie the Swamp Witch')

        if html.find('Flotsam - Rainbow') < 1:
            theret.append('Flotsam - Rainbow')
        if html.find('Acara - Angry Prince') < 1:
            theret.append('Acara - Angry Prince')
        if html.find('Kau - Starry') < 1:
            theret.append('Kau - Starry')
        if html.find('Baby Nimmo') < 1:
            theret.append('Baby Nimmo')
        if html.find('Quiggle - Cheesy Grin') < 1:
            theret.append('Quiggle - Cheesy Grin')
        if html.find('Yarrble!') < 1:
            theret.append('Yarrble!')

        if html.find('Acara - Angry Prince') < 1:
            theret.append('Acara - Angry Prince!')

        if html.find('Aisha - Disco') < 1:
            theret.append('Aisha - Disco')

        if html.find('Angelpuss - Angel') < 1:
            theret.append('Angelpuss - Angel')
        if html.find('Zomutt') < 1:
            theret.append('Zomutt')

        if html.find('Usukicon - Usuls') < 1:
            theret.append('Usukicon - Usuls')

        if html.find('Who Me?') < 1:
            theret.append('Who Me?')

        if html.find('Baby Buzz') < 1:
            theret.append('Baby Buzz')
        if html.find('Baby Pteri - Cracked') < 1:
            theret.append('Baby Pteri - Cracked')

        if html.find('Captain Scarblade') < 1:
            theret.append('Captain Scarblade')


        if html.find('Clay - Ouch!') < 1:
            theret.append('Clay - Ouch!')

        if html.find('Colourful Korbat') < 1:
            theret.append('Colourful Korbat')
        if html.find('Uni - Nightsteed') < 1:
            theret.append('Uni - Nightsteed')

        if html.find('Darigan Peophin') < 1:
            theret.append('Darigan Peophin')

        if html.find('Defenders of Neopia - Aisha') < 1:
            theret.append('Defenders of Neopia - Aisha')
        if html.find('Defenders of Neopia - Lupe') < 1:
            theret.append('Defenders of Neopia - Lupe')
        if html.find('Faellie - It') < 1:
            theret.append('Faellie - It')
        if html.find('Goldy') < 1:
            theret.append('Goldy')
        if html.find('Good or Bad?') < 1:
            theret.append('Good or Bad?')
        if html.find('Moach') < 1:
            theret.append('Moach')
        if html.find('Moehog - Avast!') < 1:
            theret.append('Moehog - Avast!')
        if html.find('The Darkest Faerie') < 1:
            theret.append('The Darkest Faerie')
        if html.find('Spotted Gelert') < 1:
            theret.append('Spotted Gelert')
        if html.find('SlugaWOO!') < 1:
            theret.append('SlugaWOO!')
        if html.find('Raindorf') < 1:
            theret.append('Raindorf')
        if html.find('Pirate! - Shoyru') < 1:
            theret.append('Pirate! - Shoyru')
        if html.find('Grey Faerie') < 1:
            theret.append('Grey Faerie')
        if html.find('Grundo - Faerie') < 1:
            theret.append('Grundo - Faerie')
        if html.find('Fiery Pteri') < 1:
            theret.append('Fiery Pteri')

        if html.find('Hissi - Ice') < 1:
            theret.append('Hissi - Ice')
        if html.find('Jeran - Hero') < 1:
            theret.append('Jeran - Hero')
        if html.find('Kass Minion') < 1:
            theret.append('Kass Minion')
        if html.find('Kougra - Baby') < 1:
            theret.append('Kougra - Baby')
        if html.find('Korbat - Royal') < 1:
            theret.append('Korbat - Royal')
        if html.find('Maraquan Chomby') < 1:
            theret.append('Maraquan Chomby')

        if html.find('Maraquan Krawk') < 1:
            theret.append('Maraquan Krawk')
        if html.find('Mutant Draik - Back Off!') < 1:
            theret.append('Mutant Draik - Back Off!')
        if html.find('Niptor') < 1:
            theret.append('Niptor')
        if html.find('Not For Wreathale') < 1:
            theret.append('Not For Wreathale')

        if html.find('OHEMGEE!!!') < 1:
            theret.append('OHEMGEE!!!')


        if html.find('Pirate! - Aisha') < 1:
            theret.append('Pirate! - Aisha')
        if html.find('Pirate! - Krawk') < 1:
            theret.append('Pirate! - Krawk')

        if html.find('Pirate! - Scorchio') < 1:
            theret.append('Pirate! - Scorchio')



        return theret

    def getavatar(self):
        randavs = self.getneededavatars()
        if randavs == []:
            print 'Got you all the avatars I can for now! Turning off.. '
            self.settingsmanager.setvalue("misc","avatargrabber" , 'off' )

            self.avataron = 'off'

            return
        random.shuffle(randavs)



        self.lastavatartime = time.time()
        self.settingsmanager.setvalue("timecache","avatartime" , self.lastavatartime )



        if randavs[0] == 'Pirate! - Scorchio':
            html = self.acc.get('http://www.neopets.com/pirates/academy.phtml?room=2149')

        if randavs[0] == 'Pirate! - Krawk':
            html = self.acc.get('http://www.neopets.com/pirates/academy.phtml?room=2')

        if randavs[0] == 'Pirate! - Aisha':
            html = self.acc.get('http://www.neopets.com/pirates/academy.phtml?room=45')

        if randavs[0] == 'OHEMGEE!!!':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Snowien')

        if randavs[0] == 'Not For Wreathale':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=neopetsrmg')


        if randavs[0] == 'Niptor':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Jiryra')



        if randavs[0] == 'Mutant Draik - Back Off!':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Nannias')



        if randavs[0] == 'Maraquan Krawk':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Lumidi')


        if randavs[0] == 'Maraquan Chomby':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Paqua')



        if randavs[0] == 'Korbat - Royal':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=LittleAriadne')
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Warh')


        if randavs[0] == 'Kougra - Baby':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Avatay')



        if randavs[0] == 'Kass Minion':
            html = self.acc.get('http://www.neopets.com/evil/showcreature.phtml?villain=16')



        if randavs[0] == 'Jeran - Hero':
            html = self.acc.get('http://www.neopets.com/medieval/plot_bfm.phtml?current_day=7')


        if randavs[0] == 'Hissi - Ice':
            html = self.acc.get('http://neopets.com/search.phtml?selected_type=pet&string=axeci')

        if randavs[0] == 'Fiery Pteri':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Astro_febuary')

        if randavs[0] == 'Grundo - Faerie':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Frizzlets')
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=LillytheGrundo')
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=BluGru_')


        if randavs[0] == 'Pirate! - Shoyru':
            html = self.acc.get('http://www.neopets.com/pirates/academy.phtml?room=15')


        if randavs[0] == 'Raindorf':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Emaden')
        if randavs[0] == 'Grey Faerie':
            html = self.acc.get('http://www.neopets.com/neopedia.phtml?neopedia_id=179')



        if randavs[0] == 'SlugaWOO!':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Jessana_176')

        if randavs[0] == 'Spotted Gelert':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=WolfChild_Spirit')

        if randavs[0] == 'Moach':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Ezenthier')
        if randavs[0] == 'Moehog - Avast!':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Pirate_Hog')


        if randavs[0] == 'The Darkest Faerie':
            html = self.acc.get('http://www.neopets.com/tcg/displayCard.phtml?edid=9&id=5')

        if randavs[0] == 'Good or Bad?':
            html = self.acc.get('http://www.neopets.com/water/plot_com.phtml?chapter=5')

        if randavs[0] == 'Goldy':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Mangokicks')


        if randavs[0] == 'Faellie - It':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Deztao')

        if randavs[0] == 'Defenders of Neopia - Lupe':
            html = self.acc.get('http://www.neopets.com/games/defenders.phtml?type=old')

        if randavs[0] == 'Defenders of Neopia - Aisha':
            html = self.acc.get('http://www.neopets.com/games/process_defenders.phtml?type=enter','http://www.neopets.com/games/defenders.phtml')


        if randavs[0] == 'Darigan Peophin':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Chreos')



        if randavs[0] == 'Uni - Nightsteed':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Dusksteed')

        if randavs[0] == 'Colourful Korbat':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Korbath')


        if randavs[0] == 'Captain Scarblade':
            html = self.acc.get('http://www.neopets.com/art/misc/scarblade2.phtml')

        if randavs[0] == 'Clay - Ouch!':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=__Aman__Da__')



        if randavs[0] == 'Baby Pteri - Cracked':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=PetitOeuf')
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=rikoushin')
        if randavs[0] == 'Baby Buzz':
            html = self.acc.get('http://www.neopets.com/search.phtml?s=i%20love%20baby%20buzz!')

        if randavs[0] == 'Xweetok - Faerie':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=6Candy93')

        if randavs[0] == 'Ruki - Desert':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Meziers')

        if randavs[0] == 'Grarrl - Darigan':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Jotunheimr')

        if randavs[0] == 'Peophin - Faerie':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Kulaboo')
        if randavs[0] == 'Tuskaninny - Relax':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=kirus_')

        if randavs[0] == 'Ixi - Disco':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=ixi_329')
        if randavs[0] == 'Acara - Roberta of Brightvale':
            html = self.acc.get('http://www.neopets.com/objects.phtml?type=shop&obj_type=78')
        if randavs[0] == 'Quiggle - Mutant':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=santasmuffin')

        if randavs[0] == 'JubJub - Tyrannian':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Jesperus')

        if randavs[0] == 'Yurble - Forefitor':
            html = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1')

        if randavs[0] == 'Lupe - King Altador':
            html = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=12')

        if randavs[0] == 'Krawk - Island Fever':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Coast')

        if randavs[0] == 'Chomby - Colourful':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Urwissen')
       # if randavs[0] == 'Mynci - Halloween':
     #       html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=ebil_wire_monkey')
        if randavs[0] == 'Tonu - Mutant':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=bats850jr')

        if randavs[0] == 'Cyodrake':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=sparkey1860')

        if randavs[0] == 'Usul - Royal Boy':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=alexim')

        if randavs[0] == 'Bruce - Mutant':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Klarvus')

        if randavs[0] == 'Aisha - Disco':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Claudaisha')

  #      if randavs[0] == 'Elephante - To War!':
 #           html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=losta_potatoes')

        if randavs[0] == 'Snuffly':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=__ShadowFury__')


        if randavs[0] == 'Anubis':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Bastet1570')



        if randavs[0] == 'Lenny - Mutant':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Teratorn')

        if randavs[0] == 'Bori - Grumpy':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Carnic')



        if randavs[0] == 'Scarabug':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=lunalindy')

        if randavs[0] == 'Faerie Pteri':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Alabrisha')


        if randavs[0] == 'Jetsam - Bah!':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=_Jetty_Sammy_')

        if randavs[0] == 'Grarrl - Galem Darkhand':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=object&string=Galem+Darkhand')

        if randavs[0] == 'Poogle - Pirate':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Cirrus')

        if randavs[0] == 'Spardel':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=friskitorius')

        if randavs[0] == 'Meerca - Halloween':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Meerca')


        if randavs[0] == 'Wocky - Camouflage':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=37_coco_37')


        if randavs[0] == 'Peophin - Purple':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Sea_Queen_of_loveing')


        if randavs[0] == 'Ixi - Sophie the Swamp Witch':
            html = self.acc.get('http://www.neopets.com/halloween/costumes.phtml')




        if randavs[0] == 'Flotsam - Rainbow':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=matt_bellamy_')


        if randavs[0] == 'Acara - Angry Prince':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Trestian')


        if randavs[0] == 'Kau - Starry':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Kauarva')


        if randavs[0] == 'Baby Nimmo':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Celicer')



        if randavs[0] == 'Quiggle - Cheesy Grin':
            html = self.acc.get('http://www.neopets.com/browseshop.phtml?owner=Cosmic145236987')


        if randavs[0] == 'Yarrble!':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=yomikoza')


        if randavs[0] == 'Grarrl - Galem Darkhand':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=object&string=Galem+Darkhand')
        if randavs[0] == 'JubJub - Tyrannian':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Jubjubpigz')
     #   if randavs[0] == 'Mynci - Halloween':
          #  html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=ebil_wire_monkey')

        if randavs[0] == 'Acara - Angry Prince':
            html = self.acc.get('hhttp://www.neopets.com/petlookup.phtml?pet=Ariandes')
        if randavs[0] == 'Aisha - Disco':
            html = self.acc.get('http://neopets.com/search.phtml?selected_type=pet&string=Kaluki')
        if randavs[0] == 'Angelpuss - Angel':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=object&string=Angelpuss')


        if randavs[0] == 'Zomutt':
            html = self.acc.get('http://www.neopets.com/search.phtml?selected_type=pet&string=Corellion')


        if randavs[0] == 'Who Me?':
            html = self.acc.get('http://www.neopets.com/petlookup.phtml?pet=Camaro_envy')
        if randavs[0] == 'Usukicon - Usuls':
            html = self.acc.get('http://www.neopets.com/usuki_demo.phtml')





        print 'Grabbed avatar - ' + randavs[0]


