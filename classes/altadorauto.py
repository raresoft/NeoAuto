#Simple alatador auto script , needs polishing

#Import Needed Classes:
import os #Used for normalizing pyton strings like folders wich use "/" in folder instead of "\" when running on windows debug server
import ConfigParser # Config parser class (.cfg files)
import time #Time module , used for sleeping
import random #used to randomise numbers and get a random number between a range
from pyamf.remoting.client import RemotingService #Pyamf class used for amf request (slightly edited)


class altador:
    #Initialize this class
    def __init__(self,acc,settingsmanager,bankhandler):
        self.settingsmanager = settingsmanager

        self.loadsettings()
        self.acc = acc
        self.pyamfhandler = RemotingService('http://www.neopets.com/amfphp/gateway.php')
        self.pyamfhandler.opener =self.acc.opener.open
        self.bankhandler = bankhandler


    def resetstones(self):
        html = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1')
        if html.find('gear0_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=0')
        if html.find('gear1_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=1')
        if html.find('gear2_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=2')
        if html.find('gear3_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=3')
        if html.find('gear4_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=4')
        if html.find('gear5_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=5')
        if html.find('gear6_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=6')
        if html.find('gear7_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=7')
        if html.find('gear8_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=8')
        if html.find('gear9_jammed.gif')>1:
            self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=9')




    def getwaiturl(self,html):
         #in step 12.106 gets the next check url from the source code html
        thelink1pos = html.find('?ppheal=1&sthv=')
        thelink2pos = html.find('"',thelink1pos)
        urldata = html[thelink1pos:thelink2pos]


        finalurl = 'http://www.neopets.com/altador/petpet.phtml' + urldata
        return finalurl

    def calcpetactionurl(self,html):
        #in step 12.106 this will get the correct action url from the html of a page with the sick pet on
       finalurl = ''

       if html.find('A Skeith knocks on the door just then') > 1:
           #We have completed this shit



           pos2 = html.find('pchv=')
           pos3 = html.find('"',pos2)
           urldata = html[pos2:pos3]
           clickurl ='http://www.neopets.com/altador/petpet.phtml?'+urldata

           html7 =self.acc.get(clickurl,'http://www.neopets.com/altador/colosseum.phtml')





           return "-1"

       if html.find('petpet_act_c_5f4438778c.gif') > 1: #Paw on mouth
                thelink1pos = html.find('action=meds')
                thelink2pos = html.find('"',thelink1pos)
                urldata = html[thelink1pos:thelink2pos]
                imgid=1
                #print urldata


       if html.find('petpet_act_b_ffabe6bc57.gif') > 1: #Tongue
            thelink1pos = html.find('action=feed')
            thelink2pos = html.find('"',thelink1pos)
            urldata = html[thelink1pos:thelink2pos]
            imgid=2
            #print urldata


       if html.find('petpet_act_d_42b934a33b.gif') > 1: #Headdown
            thelink1pos = html.find('action=wait')
            thelink2pos = html.find('"',thelink1pos)
            urldata = html[thelink1pos:thelink2pos]
            imgid=3
           # print urldata


       if html.find('petpet_act_a_2a605ae262.gif') > 1: #paw up
            thelink1pos = html.find('action=bind')
            thelink2pos = html.find('"',thelink1pos)
            imgid=4
            urldata = html[thelink1pos:thelink2pos]


       finalurl = 'http://www.neopets.com/altador/petpet.phtml?ppheal=1&' + urldata

       return finalurl







    def writestringtofile(self,file_name, str_to_be_written):
        #print self.outputfolder + file_name + ".htm"
        outputfolder = './logs/'
        #str_to_be_written.replace(".js","")
        file_writer = open(outputfolder + file_name + ".htm", 'w')
        file_writer.write(str(str_to_be_written))
        #print ("String written successfully.")
        file_writer.close()



    def loadsettings(self):

        #On off switches from config file
        self.altadoron = self.settingsmanager.getvalue("misc","altador_on")
        self.atadorstage = self.settingsmanager.getvalue("misc","altador_stage")
       # self.snowageron = self.settingsmanager.getvalue("Dailys","snowager_on")


    def checkforoil(self,html):
        #Check statues html for oil found and grab it if its there
                foundoil = 0
                if html.find('statue_base_oil') > 1:
                    print 'oil found'
                    pos1=html.find('soh=')
                    pos2 = html.find("'",pos1)
                    graburl1 = html[pos1:pos2]
                    graburl = 'http://www.neopets.com/altador/hallofheroes.phtml?'+ graburl1
                    print 'Grabbing oil from url : ' + graburl
                    html =self.acc.get(graburl , 'http://www.neopets.com/altador/hallofheroes.phtml?janitor=1')
                    foundoil=1


                return foundoil



    def detectpostion(self):
        #Detect the position of a game in progress (simple code)
        html = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml')
        theret = '0'
        if html.find('stairs=1') > 1:
            #Stairs found on hall of heroes page , so stage is at least 2
            theret = '1.13'
        else:
            #Stairs not found , set stage to 0
            theret = '0'
            return '0'

        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=6')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)
        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=6&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_06') > 1:
            #Light found above statue 1
            theret = '4.28'


        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=9')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)

        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=9&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_09') > 1:
            #Light found above statue 1
            theret = '5.34'






        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=2')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)

        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=2&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_02') > 1:
            #Light found above statue
            theret = '6.43'





        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=4')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)

        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=4&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_04') > 1:
            #Light found above statue
            theret = '7.52'




        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=11')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)
    
        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=11&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_11') > 1:
            #Light found above statue
            theret = '8.61'









        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=7')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)

        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=7&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_07') > 1:
            #Light found above statue
            theret = '8.65'






        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=5')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)
        
        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=5&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_05') > 1:
            #Light found above statue
            theret = '10.78'




        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=10')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)
        
        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=10&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_10') > 1:
            #Light found above statue
            theret = '10.85'








        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=3')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)
        
        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=3&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_03') > 1:
            #Light found above statue
            theret = '11.95'







        html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=8')


        pos1=html2.find('look_up=')
        pos2 = self.acc.cleanhtml.find("'",pos1)
        
        graburl1 = html2[pos1:pos2]
        graburl ='http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=8&' + graburl1

        html3 = self.acc.get(graburl)
        if html3.find('ceil_light_08') > 1:
            #Light found above statue
            theret = '13.111'




        self.settingsmanager.setvalue('misc','altador_stage',theret)
        self.atadorstage = theret
        return theret

    def DoTick(self):
        #Run a check of all dailys and process 1 if needed
        runone=0 #Only ever do 1 task per tick regardless of how many are needed
        #anchortime=  self.settingsmanager.getvalue("Dailys","lastanchortime")
     #   print "Ancor" + self.anchoron

        #print "altador tick"
        checkhtml = self.acc.get('http://www.neopets.com/userlookup.phtml?user=' + self.acc.user)
        if checkhtml.find('altador_trophy.gif') > 1:
            print 'Altador is complete so turning off altador bot'
            self.settingsmanager.setvalue('misc','altador_on', 'off')
            return 999

        if self.altadoron == 'on':
            print self.atadorstage
            if self.atadorstage == '0':
                print "Altador plot running past game detection logic..."

                theret = self.detectpostion()
                if not theret == '0': #Position changed
                    return


                print 'Altador bot advancing to stage 1.3'


                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1','www.neopets.com/altador/hallofheroes.phtml')
                self.settingsmanager.setvalue('misc','altador_stage', '1.3')
                self.atadorstage = '1.3'
            if self.atadorstage == '1.3':
                print 'Altador bot advancing to stage 1.4'
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1&acpcont=1','http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1')
                self.settingsmanager.setvalue('misc','altador_stage', '1.4')
                self.atadorstage = '1.4'

            if self.atadorstage == '1.4':
                print 'Altador bot advancing to stage 1.6'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1&acpcont=1','http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1')
                self.settingsmanager.setvalue('misc','altador_stage', '1.6')
                self.atadorstage = '1.6'

            if self.atadorstage == '1.6':
                print 'Altador bot advancing to stage 1.7'
                html =self.acc.get('http://www.neopets.com/altador/quarry.phtml?get_rock=1&acpcont=1','http://www.neopets.com/altador/quarry.phtml?get_rock=1')
                self.settingsmanager.setvalue('misc','altador_stage', '1.7')
                self.atadorstage = '1.7'



        if self.atadorstage == '1.7':
                print 'Altador bot advancing to stage 1.8'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1&acpcont=1','http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1')

                self.settingsmanager.setvalue('misc','altador_stage', '1.8')
                self.atadorstage = '1.8'


        if self.atadorstage == '1.8':
                print 'Altador bot advancing to stage 1.9'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1&examine_book=1','http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1')

                self.settingsmanager.setvalue('misc','altador_stage', '1.10')
                self.atadorstage = '1.10'


        if self.atadorstage == '1.10':
                print 'Altador bot advancing to stage 1.11'
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1','http://www.neopets.com/altador/hallofheroes.phtml')

                self.settingsmanager.setvalue('misc','altador_stage', '1.11')
                self.atadorstage = '1.11'






        if self.atadorstage == '1.11':
                print 'Altador bot advancing to stage 1.12 - this may takeafew mins'



                print 'Altador bot advancing to stage 1.12 - this may takeafew mins'
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=1','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return





                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=2','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=3','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=4','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=5','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=6','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=7','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=8','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=9','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=10','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=11','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=12','http://www.neopets.com/altador/hallofheroes.phtml')
                theret = self.checkforoil(html)

                if theret == 1:
                    self.settingsmanager.setvalue('misc','altador_stage', '1.12')
                    self.atadorstage = '1.12'
                    return

                #If we got here code failed , set stage to 0 and retry
                self.settingsmanager.setvalue('misc','altador_stage', '0')
                self.atadorstage = '0'
        if self.atadorstage == '1.12':
                print 'Altador bot advancing to stage 1.13'
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1&acpcont=1','http://www.neopets.com/altador/hallofheroes.phtml?janitor=1')
                theret = self.detectpostion()
                if not theret == '1.13': #We shwatch spiderman
               # should have 1.13 here , if not passed code failed so go back to stage 0
                    self.settingsmanager.setvalue('misc','altador_stage', '0')
                    self.atadorstage = '0'
                    return


        if self.atadorstage == '1.13':
                print 'Altador bot advancing to stage 2.15'
                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1','http://www.neopets.com/altador/hallofheroes.phtml')

                self.settingsmanager.setvalue('misc','altador_stage', '2.15')
                self.atadorstage = '2.15'

        if self.atadorstage == '2.15':
                print 'Altador bot advancing to stage 2.17'
                postdata = {'board' :'6', 'join_club' : '1'}
                html =self.acc.post('http://www.neopets.com/altador/archives.phtml',postdata,'http://www.neopets.com/altador/archives.phtml?board=6')



                self.settingsmanager.setvalue('misc','altador_stage', '2.17')
                self.atadorstage = '2.17'

        if self.atadorstage == '2.17':
                print 'Altador bot advancing to stage 3.20'

                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?stairs=1&telescope=1','http://www.neopets.com/altador/hallofheroes.phtml')

                self.settingsmanager.setvalue('misc','altador_stage', '3.20')
                self.atadorstage = '3.20'



        if self.atadorstage == '3.20':
                print 'Altador bot advancing to stage 3.21'

                html =self.acc.get('http://www.neopets.com/altador/tomb.phtml','http://thedailyneopets.com/altador-plot/part3/')
                cleanhtml = self.acc.cleanhtml
                pos1=html.find('/altador/tomb.phtml?thv=')
                pos2 = cleanhtml.find("'",pos1)
                graburl1 = cleanhtml[pos1:pos2]
                graburl = 'http://www.neopets.com' + graburl1



                html =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')




                self.settingsmanager.setvalue('misc','altador_stage', '3.21')
                self.atadorstage = '3.21'



        if self.atadorstage == '3.21':
                print 'Altador bot advancing to stage 3.22'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1','http://thedailyneopets.com/altador-plot/part3/')

                self.settingsmanager.setvalue('misc','altador_stage', '3.22')
                self.atadorstage = '3.22'

        if self.atadorstage == '3.22':
                print 'Altador bot advancing to stage 4.28'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part3/')
                postdata = {'name' :'Sleeper', 'data' : html}
                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                theret = self.detectpostion()
                if not theret == '4.28': #We should have 4.28 here , if not passed code failed so go back to stage 1.13
                    self.settingsmanager.setvalue('misc','altador_stage', '1.13')
                    self.atadorstage = '1.13'
                    return





        if self.atadorstage == '4.28':
                print 'Altador bot advancing to stage 4.29'

                html =self.acc.get('http://www.neopets.com/altador/clouds.phtml','http://thedailyneopets.com/altador-plot/part4/')
                cleanhtml = self.acc.cleanhtml
                pos1=html.find('chv=')
                pos2 = cleanhtml.find("'",pos1)
                graburl1 = html[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/clouds.phtml?' + graburl1


                html =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')




                self.settingsmanager.setvalue('misc','altador_stage', '4.29')
                self.atadorstage = '4.29'



        if self.atadorstage == '4.29':
                print 'Altador bot advancing to stage 5.34'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part3/')
                postdata = {'name' :'Dreamer', 'data' : html}
                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                theret = self.detectpostion()
                if not theret == '5.34': #We should have 5.34 here , if not passed code failed so go back to stage 4.28
                    self.settingsmanager.setvalue('misc','altador_stage', '4.28')
                    self.atadorstage = '4.28'
                    return




        if self.atadorstage == '5.34':
                print 'Altador bot advancing to stage 5.35'

                html =self.acc.get('http://www.neopets.com/altador/tomb.phtml','http://thedailyneopets.com/altador-plot/part5/')
                pos1=html.find('acvhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/tomb.phtml?' + graburl1



                html =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')



                self.settingsmanager.setvalue('misc','altador_stage', '5.35')
                self.atadorstage = '5.35'


        if self.atadorstage == '5.35':
                print 'Altador bot advancing to stage 5.36'

                html =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=11','http://thedailyneopets.com/altador-plot/part5/')
                pos1=html.find('vwhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=11&' + graburl1


                html2 =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')

                pos1=html2.find('view_statue_id=11&vwhv=')
                pos2 = html2.find('"',pos1)
                graburl1 = html2[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/hallofheroes.phtml?' + graburl1


                html2 =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')



                self.settingsmanager.setvalue('misc','altador_stage', '5.36')
                self.atadorstage = '5.36'

        if self.atadorstage == '5.36':
                print 'Altador bot advancing to stage 5.37'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1','http://www.neopets.com/altador/archives.phtml')

                self.settingsmanager.setvalue('misc','altador_stage', '5.37')
                self.atadorstage = '5.37'




        if self.atadorstage == '5.37':
                print 'Altador bot advancing to stage 6.43'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'First to Rise', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                theret = self.detectpostion()
                if not theret == '6.43': #We should have 5.34  here , if not passed code failed so go back to stage 6.43
                    self.settingsmanager.setvalue('misc','altador_stage', '5.34')
                    self.atadorstage = '5.34'
                    return



        if self.atadorstage == '6.43':
                print 'Altador bot advancing to stage 6.47'

                html =self.acc.get('http://www.neopets.com/altador/farm.phtml','http://thedailyneopets.com/altador-plot/part6/')


                pos1=html.find('windmill=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/farm.phtml?' + graburl1


                html2 =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')
                pos1=html2.find('windmill=')
                pos2 = html2.find('"',pos1)
                graburl1 = html2[pos1:pos2]


                graburl = 'http://www.neopets.com/altador/farm.phtml?' + graburl1




               # print graburl

                html3 =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')


                pos1=html3.find('&umhv=')

                pos3 = html3.find('?windmill=',pos1)

                pos2 = html3.find('"',pos3)
                graburl1 = html3[pos3:pos2]

                graburl = 'http://www.neopets.com/altador/farm.phtml' + graburl1

                html4 =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')
                pos1=html4.find('windmill=')
                pos2 = html4.find('"',pos1)
                graburl1 = html4[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/farm.phtml?' + graburl1
                html5 =self.acc.get(graburl,'http://www.neopets.com/altador/tomb.phtml')

                #print graburl




                self.settingsmanager.setvalue('misc','altador_stage', '6.47')
                self.atadorstage = '6.47'

        if self.atadorstage == '6.47':
                print 'Altador bot advancing to stage 6.48'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1','http://thedailyneopets.com/altador-plot/part3/')

                self.settingsmanager.setvalue('misc','altador_stage', '6.48')
                self.atadorstage = '6.48'


        if self.atadorstage == '6.48':
                print 'Altador bot advancing to stage 7.52'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'Farmer', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')

                theret = self.detectpostion()
                if not theret == '7.52': #We should have 6.43  here , if not passed code failed so go back to stage 6.43
                    self.settingsmanager.setvalue('misc','altador_stage', '6.43')
                    self.atadorstage = '6.43 '
                    return


        if self.atadorstage == '7.52':
                print 'Altador bot advancing to stage 7.55'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?board=7','http://www.neopets.com/altador/archives.phtml')
                pos1=html.find('swhv')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/archives.phtml?board=7&' + graburl1


                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')





                self.settingsmanager.setvalue('misc','altador_stage', '7.55')
                self.atadorstage = '7.55'

        if self.atadorstage == '7.55':
                print 'Altador bot advancing to stage 7.56'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1','http://thedailyneopets.com/altador-plot/part3/')

                self.settingsmanager.setvalue('misc','altador_stage', '7.56')
                self.atadorstage = '7.56'

        if self.atadorstage == '7.56':

                print 'Altador bot advancing to stage 8.61'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'Dancer', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')
                theret = self.detectpostion()
                if not theret == '8.61': #We should have 6.43  here , if not passed code failed so go back to stage 6.43
                    self.settingsmanager.setvalue('misc','altador_stage', '7.52')
                    self.atadorstage = '7.52 '
                    return



        if self.atadorstage == '8.61':

                print 'Altador bot advancing to stage 8.63'



                html =self.acc.get('http://www.neopets.com/altador/docks.phtml','http://www.neopets.com/altador/archives.phtml')
                pos1=html.find('wchv')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl = 'http://www.neopets.com/altador/docks.phtml?' + graburl1


                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')

                self.settingsmanager.setvalue('misc','altador_stage', '8.63')
                self.atadorstage = '8.63'

        if self.atadorstage == '8.63':
                print 'Altador bot advancing to stage 8.64'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1','http://thedailyneopets.com/altador-plot/part3/')

                self.settingsmanager.setvalue('misc','altador_stage', '8.64')
                self.atadorstage = '8.64'


        if self.atadorstage == '8.64':

                print 'Altador bot advancing to stage 8.65'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'Wave', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]

                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')

                theret = self.detectpostion()

                if not theret == '8.65': #We should have 6.43  here , if not passed code failed so go back to stage 6.43
                    self.settingsmanager.setvalue('misc','altador_stage', '8.61')
                    self.atadorstage = '8.61'
                    return





        if self.atadorstage == '8.65':
                print 'Altador bot advancing to stage 9.71'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?board=6','http://thedailyneopets.com/altador-plot/part3/')

                self.settingsmanager.setvalue('misc','altador_stage', '9.71')
                self.atadorstage = '9.71'



        if self.atadorstage == '9.71':

                print 'Altador bot advancing to stage 9.74 - these stages can take a few minutes..'



                html =self.acc.get('http://www.neopets.com/altador/colosseum.phtml','http://www.neopets.com/altador/archives.phtml')
                endpos1=0
                while not (html.find("pchv",endpos1))== -1:


                    startpos2 = html.find("pchv",endpos1)

                    endpos2 = html.find('"',startpos2) #Item id end
                    theoii= html[startpos2:endpos2]
                    theurl = 'http://www.neopets.com/altador/colosseum.phtml?' +  theoii
                    endpos1 = endpos2

                    html2 =self.acc.get(theurl,'http://www.neopets.com/altador/colosseum.phtml')
                  #  print theurl
                    if html2.find('interested in joining...') > 1:
                        print 'door found'
                        break
                pos1=html2.find('pchv')

                pos2 = html2.find('value=',pos1)+7
                pos3 = html2.find('"',pos2)
                theoi = html2[pos2:pos3]

                theurl ='http://www.neopets.com/altador/colosseum.phtml?pchv='+theoi +'&pc_go=1'

                html5 =self.acc.get(theurl,'http://www.neopets.com/altador/colosseum.phtml')



                url1pos1=html5.find('punch1=')+7
                url1pos2=html5.find('"',url1pos1)
                theoi = html5[url1pos1:url1pos2]





                url2pos1=html5.find('punch1=',url1pos2) +7
                url2pos2=html5.find('"',url2pos1)



                theoi2 = html5[url2pos1:url2pos2]




                url3pos1=html5.find('punch1=',url2pos2) +7
                url3pos2=html5.find('"',url3pos1)


                theoi3 = html5[url3pos1:url3pos2]

                #Extract all 3 punch oiis , add them as punch1,punch2,punch3 later


                finalpos1=html5.find('pchv') +5
                finalpos2=html5.find('&',finalpos1)



                pchv = html5[finalpos1:finalpos2]


                print 'pchv =' + pchv

                thelist = ['1.1.1','1.1.2','1.1.3','1.2.1','1.2.2','1.2.3','1.3.1','1.3.2','1.3.3' , '2.1.1', '2.1.2', '2.1.3', '2.2.1', '2.2.2', '2.2.3', '2.3.1', '2.3.2', '2.3.3', '3.1.1', '3.1.2', '3.1.3', '3.2.1', '3.2.2', '3.2.3', '3.3.1', '3.3.2', '3.3.3']
                for combo in thelist:



                    finalurl = 'http://www.neopets.com/altador/colosseum.phtml?pchv=' + pchv + '&pc_go=1'
                    letters = combo.split('.')
                    letternum = 1
                    for letter in letters:
                        if letter == '1':
                            if letternum == 1:
                                letter1urlstuff = '&punch1=' + theoi
                            elif letternum == 2:
                                letter2urlstuff = '&punch2=' + theoi
                            elif letternum == 3:
                                letter3urlstuff = '&punch3=' + theoi


                        elif letter == '2':
                            if letternum == 1:
                                letter1urlstuff = '&punch1=' + theoi2
                            elif letternum == 2:
                                letter2urlstuff = '&punch2=' + theoi2
                            elif letternum == 3:
                                letter3urlstuff = '&punch3=' + theoi2

                        elif letter == '3':
                            if letternum == 1:
                                letter1urlstuff = '&punch1=' + theoi3
                            elif letternum == 2:
                                letter2urlstuff = '&punch2=' + theoi3
                            elif letternum == 3:
                                letter3urlstuff = '&punch3=' + theoi3


                        letternum =letternum +1






                    finalurl = finalurl + letter1urlstuff + letter2urlstuff + letter3urlstuff


                    html5 =self.acc.get(finalurl,'http://www.neopets.com/altador/colosseum.phtml')

                    if html5.find('gchv') > 1:
                        break



                cuppos1=html5.find('gchv')
                cuppos2=html5.find('"',cuppos1)
                cuphash= '&' + html5[cuppos1:cuppos2]
                #cup is available
                atfuckinglasturl = 'http://www.neopets.com/altador/colosseum.phtml?pchv=' + pchv + cuphash + '&pc_go=1'
                html7 =self.acc.get(atfuckinglasturl,'http://www.neopets.com/altador/colosseum.phtml')


                cuppos1=html7.find('gchv')
                cuppos2=html7.find('"',cuppos1)
                cuphash= '&' + html7[cuppos1:cuppos2]
                #cup crest thing... available click it and be done with this tedious step!

                omgthatwasnoteventhelastoneurl =  'http://www.neopets.com/altador/colosseum.phtml?pchv=' + pchv + cuphash + '&pc_go=1'
                html8 =self.acc.get(omgthatwasnoteventhelastoneurl,'http://www.neopets.com/altador/colosseum.phtml')

                self.settingsmanager.setvalue('misc','altador_stage', '9.74')
                self.atadorstage = '9.74'

        if self.atadorstage == '9.74':
                print 'Altador bot advancing to stage 10.78'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'Gladiator', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                theret = self.detectpostion()

                if not theret == '10.78': #We should have 6.43  here , if not passed code failed so go back to stage 6.43
                    self.settingsmanager.setvalue('misc','altador_stage', '8.61')
                    self.atadorstage = '8.65'
                    return



        if self.atadorstage == '10.78':
                print 'Altador bot advancing to stage 10.80'
                urllist = "http://www.neopets.com/objects.phtml?type=shop&obj_type=94|http://www.neopets.com/objects.phtml?type=shop&obj_type=95|http://www.neopets.com/objects.phtml?type=shop&obj_type=96"
                urlary = urllist.split('|')
                for urltarget in urlary:

                    html = self.acc.get(urltarget,'http://thedailyneopets.com/altador-plot/part10')
                    #set inflation value
                    posinflation1 = html.find('ly at <b>') +9
                    posinflation2 = html.find('%',posinflation1)
                    inlfationraw = html[posinflation1:posinflation2] #inflation with .
                    fixedinflation=inlfationraw.replace('.','')
                    self.bankhandler.deopsitall()
                    self.bankhandler.withdrawnp(fixedinflation)


                    html = self.acc.get(urltarget,'http://thedailyneopets.com/altador-plot/part10')

                    if html.find('Altadorian Scales') > 1:
                        print 'scales found'

                        posscales1 = html.find('gohv')
                        posscales2 = html.find('"',posscales1)
                        scalesraw = html[posscales1:posscales2] #inflation with .

                        html = self.acc.get('http://www.neopets.com/altador/index.phtml?' + scalesraw,'http://thedailyneopets.com/altador-plot/part10')

                    if html.find('Altadorian Chocolate Coin') > 1:
                        print 'Chocolate Coin found'

                        posscales1 = html.find('gohv')
                        posscales2 = html.find('"',posscales1)
                        scalesraw = html[posscales1:posscales2] #inflation with .

                        html = self.acc.get('http://www.neopets.com/altador/index.phtml?' + scalesraw,'http://thedailyneopets.com/altador-plot/part10')



                    if html.find('Coin Purse') > 1:
                        print 'Coin Purse'

                        posscales1 = html.find('gohv')
                        posscales2 = html.find('"',posscales1)
                        scalesraw = html[posscales1:posscales2] #inflation with .



                        html = self.acc.get('http://www.neopets.com/altador/index.phtml?' + scalesraw,'http://thedailyneopets.com/altador-plot/part10')


                self.settingsmanager.setvalue('misc','altador_stage', '10.80')
                self.atadorstage = '10.80'


        if self.atadorstage == '10.80':
                print 'Altador bot advancing to stage 10.81'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1&acpcont=1','http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1')

                self.settingsmanager.setvalue('misc','altador_stage', '10.81')
                self.atadorstage = '10.81'



        if self.atadorstage == '10.81':
                print 'Altador bot advancing to stage 10.85'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'Collector', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                theret = self.detectpostion()

                if not theret == '10.85': #We should have 6.43  here , if not passed code failed so go back to stage 6.43
                    self.settingsmanager.setvalue('misc','altador_stage', '10.78')
                    self.atadorstage = '10.78'
                    return







        if self.atadorstage == '10.85':
                print 'Altador bot advancing to stage 10.86'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?lclenny=1','http://thedailyneopets.com/altador-plot/part11/')

                self.settingsmanager.setvalue('misc','altador_stage', '10.86')
                self.atadorstage = '10.86'

        if self.atadorstage == '10.86':
                print 'Altador bot advancing to stage 10.88'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1','http://thedailyneopets.com/altador-plot/part11/')

                pos1=html.find('distract=')
                pos2 = html.find('"',pos1)

                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?archivist=1&' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')



                pos1=html.find('steal=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?archivist=1&' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')
                self.settingsmanager.setvalue('misc','altador_stage', '10.88')
                self.atadorstage = '10.88'

        if self.atadorstage == '10.88':
                print 'Altador bot advancing to stage 10.89'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?lclenny=1','http://thedailyneopets.com/altador-plot/part11/')

                self.settingsmanager.setvalue('misc','altador_stage', '10.89')
                self.atadorstage = '10.89'


        if self.atadorstage == '10.89':
                print 'Altador bot advancing to stage 11.92'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml','http://thedailyneopets.com/altador-plot/part11/')
                pos1=html.find('goarch=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?' + graburl1









                pos1=html.find('goarch=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')






                #grab door 1 and visit...
                pos1=html.find('goarch=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?' + graburl1

                door1html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')
               # print graburl


                #grab door 2 and visit...
                pos1=door1html.find('goarch=')
                pos2 = door1html.find('"',pos1)
                graburl1 = door1html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?' + graburl1

                door2html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')
                #print graburl

                #grab door 3 (last one) and visit...
                pos1=door2html.find('goarch=')
                pos2 = door2html.find('"',pos1)
                graburl1 = door2html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?' + graburl1


                door3html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                #door3html now has the link to click the closet door...




                posstart1 =door3html.find('goarch=') + 5 #Skip the first link , we want link 4
                posstart2=door3html.find('goarch=',posstart1) + 5 #Skip the second link , we want link 4
                posstart3=door3html.find('goarch=',posstart2) + 5 #Skip the second link , we want link 4
                pos1=door3html.find('goarch=',posstart3)
                pos2 = door3html.find('"',pos1)
                graburl1 = door3html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?' + graburl1

                finaldoorhtml =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')



                pos1=finaldoorhtml.find('getting his replacements')

                pos2 = finaldoorhtml.find('value=',pos1)+7
                pos3 = finaldoorhtml.find('"',pos2)
                theoi = finaldoorhtml[pos2:pos3]



                postdata = {'hide_box' : '1' , 'closet' : theoi}
                graburl ='http://www.neopets.com/altador/archives.phtml?'

                lasthtml = self.acc.post(graburl,postdata)






                self.settingsmanager.setvalue('misc','altador_stage', '11.92')
                self.atadorstage = '11.92'

        if self.atadorstage == '11.92':
                print 'Altador bot advancing to stage 11.93'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1','http://thedailyneopets.com/altador-plot/part11/')

                pos1=html.find('distract=')
                pos2 = html.find('"',pos1)

                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?archivist=1&' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                pos1=html.find('steal=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?archivist=1&' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')


                self.settingsmanager.setvalue('misc','altador_stage', '11.93')
                self.atadorstage = '11.93'

        if self.atadorstage == '11.93':


                print 'Altador bot advancing to stage 11.94'
                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?lclenny=1&acpcont=1','http://thedailyneopets.com/altador-plot/part11/')

                pos1=html.find('acpcont=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]

                graburl ='http://www.neopets.com/altador/archives.phtml?lclenny=1&' + graburl1
                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')

                self.settingsmanager.setvalue('misc','altador_stage', '10.94')
                self.atadorstage = '11.94'


        if self.atadorstage == '11.94':
                print 'Altador bot advancing to stage 11.95'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'Thief', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1





                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')



                html = self.acc.get('http://www.neopets.com/altador/archives.phtml?board=6')




                theret = self.detectpostion()

                if not theret == '11.95': #We should have 6.43  here , if not passed code failed so go back to stage 6.43
                    self.settingsmanager.setvalue('misc','altador_stage', '10.85')
                    self.atadorstage = '10.85'
                    return








        if self.atadorstage == '11.95':
                print 'Altador bot advancing to stage 12.99'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?board=6','http://thedailyneopets.com/altador-plot/part12/')

                self.settingsmanager.setvalue('misc','altador_stage', '12.99')
                self.atadorstage = '12.99'



        if self.atadorstage == '12.99':
                print 'Altador bot advancing to stage 12.102'

                targethtml =''
                html =self.acc.get('http://www.neopets.com/altador/farm.phtml','http://thedailyneopets.com/altador-plot/part12/')
                if html.find('pphv=') >1:
                    targethtml = html

                html =self.acc.get('http://www.neopets.com/altador/docks.phtml','http://thedailyneopets.com/altador-plot/part12/')
                if html.find('?pphv=') >1:
                    targethtml = html
                html =self.acc.get('http://www.neopets.com/altador/quarry.phtml','http://thedailyneopets.com/altador-plot/part12/')
                if html.find('?pphv=') >1:
                    targethtml = html
                pos1=targethtml.find('pphv=')
                pos2 = targethtml.find('"',pos1)
                graburl1 = targethtml[pos1:pos2]
                graburl ='http://www.neopets.com/altador/petpet.phtml?' + graburl1
                finalhtml = self.acc.get(graburl)

                self.settingsmanager.setvalue('misc','altador_stage', '12.102')
                self.atadorstage = '12.102'
      #  if self.atadorstage == '11.94':


        if self.atadorstage == '12.102':
                print 'Altador bot advancing to stage 12.103'

                html =self.acc.get('http://www.neopets.com/altador/archives.phtml?board=5','http://thedailyneopets.com/altador-plot/part12/')
                pos1=html.find('bmhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?board=5&' + graburl1
                finalhtml = self.acc.get(graburl)
                #print graburl

                #Same again with new html
                pos1=finalhtml.find('bmhv=')
                pos2 = finalhtml.find("'",pos1)
                graburl1 = finalhtml[pos1:pos2]
                graburl ='http://www.neopets.com/altador/archives.phtml?board=5&' + graburl1
                finalhtml2 = self.acc.get(graburl)


                self.settingsmanager.setvalue('misc','altador_stage', '12.103')
                self.atadorstage = '12.103'






        if self.atadorstage == '12.103':

                print 'Altador bot advancing to stage 12.105 - these stages can take a few minutes..'



                html =self.acc.get('http://www.neopets.com/altador/colosseum.phtml','http://www.neopets.com/altador/archives.phtml')
                endpos1=0
                while not (html.find("pchv",endpos1))== -1:


                    startpos2 = html.find("pchv",endpos1)

                    endpos2 = html.find('"',startpos2) #Item id end
                    theoii= html[startpos2:endpos2]
                    theurl = 'http://www.neopets.com/altador/colosseum.phtml?' +  theoii
                    endpos1 = endpos2

                    html2 =self.acc.get(theurl,'http://www.neopets.com/altador/colosseum.phtml')
                  #  print theurl
                    if html2.find('interested in joining...') > 1:
                        print 'door found'
                        break
                pos1=html2.find('pchv')

                pos2 = html2.find('value=',pos1)+7
                pos3 = html2.find('"',pos2)
                theoi = html2[pos2:pos3]

                theurl ='http://www.neopets.com/altador/colosseum.phtml?pchv='+theoi +'&pc_go=1'

                html5 =self.acc.get(theurl,'http://www.neopets.com/altador/colosseum.phtml')



                pos1=html5.find('pchv')

                pos2 = html5.find('sphv=',pos1)
                pos3 = html5.find('"',pos2)
                urldata = html5[pos2:pos3]
                pieurl ='http://www.neopets.com/altador/colosseum.phtml?pchv='+theoi +'&pc_go=1&'+urldata
                html6 =self.acc.get(pieurl,'http://www.neopets.com/altador/colosseum.phtml')

                #hit continue


                pos2 = html6.find('pchv=',pos1)
                pos3 = html6.find("'",pos2)
                urldata = html6[pos2:pos3]
                pieurlc ='http://www.neopets.com/altador/colosseum.phtml?'+urldata
                print pieurlc

                html7 =self.acc.get(pieurlc,'http://www.neopets.com/altador/colosseum.phtml')

                self.settingsmanager.setvalue('misc','altador_stage', '12.105')
                self.atadorstage = '12.105'

        if self.atadorstage == '12.105':
                print 'Altador bot advancing to stage 12.106 - This can take a while..'

                temphtml = self.acc.get('http://www.neopets.com/altador/petpet.phtml?ppheal=1')

                if temphtml.find('Bandage') >1:
                    #Already done

                    print 'Done before , skipping...'
                    self.settingsmanager.setvalue('misc','altador_stage', '12.106')

                    self.atadorstage = '12.106'

                    return

#Before we do this step , above we make sure we have nto done it before and skip if so to prevent a never ending loop
                html =self.acc.get('http://www.neopets.com/altador/tomb.phtml','http://thedailyneopets.com/altador-plot/part12/')


                pos2 = html.find('tehv=')

                pos3 = html.find('"',pos2)
                urldata = html[pos2:pos3]
                woodurl ='http://www.neopets.com/altador/tomb.phtml?'+urldata



                currhtml =''
                while not currhtml.find('tehv=') >1: #While the links not found refresh
                    currhtml =self.acc.get(woodurl)




                    time.sleep(2)

                 #We got the right url in currhtml..
                pos2 = currhtml.find('tehv=')
                pos3 = currhtml.find('"',pos2)
                urldata = currhtml[pos2:pos3]
                bandageurl ='http://www.neopets.com/altador/tomb.phtml?'+urldata
                bandagehtml =self.acc.get(bandageurl)
               # print bandagehtml



                #Collect bandage by hitting continue (same code as above repeated with bandagehtml)

                pos2 = bandagehtml.find('tehv=')
                pos3 = bandagehtml.find("'",pos2)
                urldata = bandagehtml[pos2:pos3]
                bandagecurl ='http://www.neopets.com/altador/tomb.phtml?'+urldata
                bandagechtml =self.acc.get(bandagecurl)

                self.settingsmanager.setvalue('misc','altador_stage', '12.106')
                self.atadorstage = '12.106'


        if self.atadorstage == '12.106':
                    print 'Altador bot advancing to stage 12.107 - this will take about 10 minutes in total'
                    #Final version
                    #Implements bug fix by charlieG
                    #When you first click the pet, don't click "check on pet.
                    #1:01 click the pet
                    #1:01 perform the neccasery action eg bandage




                    #Wait for "certificate" to be found in html (job done)
                    #Defaults...
                    test = 1
                    self.lastminute ='-1'
                    self.nextwaiturl=''

                    #1:01 click the pet
                    #First run , get the contents of 'http://www.neopets.com/altador/petpet.phtml?ppheal=1' Store the lastm minute
                    html =self.acc.get('http://www.neopets.com/altador/petpet.phtml?ppheal=1','http://www.neopets.com/altador/archives.phtml?archivist=1') #First html
                    peturl = self.calcpetactionurl(html)

                    if peturl == "-1":
                        #Completed
                        self.settingsmanager.setvalue('misc','altador_stage', '12.107')
                        self.atadorstage = '12.107'
                        return

                    html =self.acc.get(peturl) #First pet  action performed
                    finalurl2 = self.getwaiturl(html)
                    self.nextwaiturl = finalurl2


                    self.lastwaithtml = html
                    timehtml =self.lastwaithtml #use pageslast minute for first run
                    #pos before clock
                    startingpos = timehtml.find('"nst">')
                    #get the minute
                    startingpos2=timehtml.find(':',startingpos)+1
                    startingpos3=timehtml.find(':',startingpos2)
                    currentminute = timehtml[startingpos2:startingpos3]
                    self.lastminute = currentminute
                    print "Healing pet - m" + currentminute



                    self.nextwaiturl
                    #1:02 NOW check on th e pet pet and complete the action within the minute.
                   # print self.lastminute
                    while test ==1:
                        imgid=0

                        #get neopets time stamp from neopets homepage html , so we dont intefere with the loop

                        #If a wait url is set , visit that first
                        timehtml =self.acc.get('http://www.neopets.com','http://www.neopets.com/') #Time html
                        #pos before clock
                        startingpos = timehtml.find('"nst">')
                        #get the minute
                        startingpos2=timehtml.find(':',startingpos)+1
                        startingpos3=timehtml.find(':',startingpos2)
                        currentminute = timehtml[startingpos2:startingpos3]



                        if  str(currentminute) == str(self.lastminute): # minute as not changed since last check exit the loop until it does
                        #    print 'Waiting for next nst minute , its not yet so im halting for 15 seconds and rechecking ( I wanna catch it early)'
                            time.sleep(15)

                            continue #skip rest of code for this loop once then repeat until minute changes


                        self.lastminute = currentminute



                        self.lastwaithtml =self.acc.get(self.nextwaiturl,'http://www.neopets.com/') #Get wait url


                        print "Checking pet - m" + currentminute


                        peturl = self.calcpetactionurl(self.lastwaithtml)


                        if peturl == "-1":
                            #Completed
                            self.settingsmanager.setvalue('misc','altador_stage', '12.107')
                            self.atadorstage = '12.107'
                            return


                        html = self.acc.get(peturl)



                        print "Healing pet  - m" + currentminute
                        finalurl2 = self.getwaiturl(html)

                        self.nextwaiturl = finalurl2


                        time.sleep(15)



        if self.atadorstage == '12.107':
                print 'Altador bot advancing to stage 12.107 '


                temphtml = self.acc.get('http://www.neopets.com/altador/archives.phtml?board=6')

                temphtml = self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1')
                self.settingsmanager.setvalue('misc','altador_stage', '12.108')
                self.atadorstage = '12.108'

        if self.atadorstage == '12.108':
                print 'Altador bot advancing to stage 13.111'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part5/')
                postdata = {'name' :'Gatherer', 'data' : html}

                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')




                theret = self.detectpostion()

                if not theret == '13.111':
                    self.settingsmanager.setvalue('misc','altador_stage', '11.95')
                    self.atadorstage = '11.95'
                    return





        if self.atadorstage == '13.111':
                print 'Altador bot advancing to stage 13.114 '
                html =self.acc.get('http://www.neopets.com/altador/wall.phtml','http://www.neopets.com/altador/quarry.phtml')
                pos1=html.find('?sdhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/wall.phtml' + graburl1
                html = self.acc.get (graburl)


                #Same code for knecklace on new html , how nice
                pos1=html.find('?sdhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/wall.phtml' + graburl1
                html = self.acc.get (graburl)


                #Same code for continue button
                pos1=html.find('?sdhv=')
                pos2 = html.find("'",pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/wall.phtml' + graburl1
                html = self.acc.get (graburl)



                self.settingsmanager.setvalue('misc','altador_stage', '13.114')
                self.atadorstage = '13.114'


        if self.atadorstage == '13.114':
                print 'Altador bot advancing to stage 13.116 '


                temphtml = self.acc.get('http://www.neopets.com/altador/farm.phtml')

                temphtml = self.acc.get('http://www.neopets.com/altador/plant.phtml')




                self.settingsmanager.setvalue('misc','altador_stage', '13.116')
                self.atadorstage = '13.116'


        if self.atadorstage == '13.116':
            print 'Altador bot advancing to stage 13.118 - This stage can take a extremly long time... '
        #first check the waterpage html to make sure we have not completed this mission already - prevents unstoppable loop
            clraik_rox = True

            planthtml = self.acc.get('http://www.neopets.com/altador/plant.phtml')
            if planthtml.find('The engineers cheer') >1:
                #completed already
                print 'water plant is already in complete state before doing anything , skipping to 13.118..'
                self.settingsmanager.setvalue('misc','altador_stage', '13.118')
                self.atadorstage = '13.118'
                return

            #This step sucks I had real issues with it but it dosent make sence as to why it dosent work , in the end
            #I settled for this , I dont like it and i will try to upgrade it. This code works but it can take upto a hour
            #To find the lucky combo in theory anyway thats never happened for me but it is possible



            pageurls = ["http://www.neopets.com/altador/plant.phtml?room=1&act=r1v1",
                        "http://www.neopets.com/altador/plant.phtml?room=1&act=r1v2",
                        "http://www.neopets.com/altador/plant.phtml?room=2&act=r2v3",
                        "http://www.neopets.com/altador/plant.phtml?room=2&act=r2v4",

                        "http://www.neopets.com/altador/plant.phtml?room=2&act=r2s1",
                        "http://www.neopets.com/altador/plant.phtml?room=3&act=r3s2",
                        "http://www.neopets.com/altador/plant.phtml?room=3&act=r3s3",
                        "http://www.neopets.com/altador/plant.phtml?room=3&act=r3s4"]


            while clraik_rox == True:
                random.shuffle(pageurls)
                targeturl = pageurls[0]

                html = self.acc.get(targeturl)


                if html.find('611538397c.gif')>1:
                    self.settingsmanager.setvalue('misc','altador_stage', '13.118')
                    self.atadorstage = '13.118'
                    print 'Combo was found'

                    return







        if self.atadorstage == '13.118':
                print 'Altador bot advancing to stage 13.120'
                html =self.acc.get('http://www.neopets.com/altador/wall.phtml','http://www.neopets.com/altador/quarry.phtml')
                pos1=html.find('?sdhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/wall.phtml' + graburl1
                html = self.acc.get (graburl)


                #Same code for knecklace on new html , how nice
                pos1=html.find('?sdhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/wall.phtml' + graburl1
                html = self.acc.get (graburl)


                #Same code for continue button
                pos1=html.find('?sdhv=')
                pos2 = html.find("'",pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/wall.phtml' + graburl1
                html = self.acc.get (graburl)
                pos1=html.find('?sdhv=')
                pos2 = html.find('"',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/wall.phtml' + graburl1
                html = self.acc.get (graburl)


                graburl ='http://www.neopets.com/altador/archives.phtml?archivist=1'
                html = self.acc.get (graburl)

                graburl ='http://www.neopets.com/altador/archives.phtml?board=6'
                html = self.acc.get (graburl)

                self.settingsmanager.setvalue('misc','altador_stage', '13.120')
                self.atadorstage = '13.120'

        if self.atadorstage == '13.120':
                print 'Altador bot advancing to stage 13.122'

                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1','http://thedailyneopets.com/altador-plot/part3/')
                postdata = {'name' :'Protector', 'data' : html}
                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')

                self.settingsmanager.setvalue('misc','altador_stage', '13.122')
                self.atadorstage = '13.122'



        if self.atadorstage == '13.122':
                print 'Altador bot advancing to stage 14.124'
                html2=self.acc.get('http://www.neopets.com/altador/archives.phtml?board=6')
                pos1=html2.find('rqhv')

                pos2 = html2.find('value=',pos1)+7
                pos3 = html2.find('"',pos2)
                theoi = html2[pos2:pos3]

                theurl ='http://www.neopets.com/altador/archives.phtml?rqhv='+theoi +'&board=6'

                html5 =self.acc.get(theurl)
                #done , one set of missions left.
                self.settingsmanager.setvalue('misc','altador_stage', '14.124')
                self.atadorstage = '14.124'

        if self.atadorstage == '14.124':
                print 'Altador bot advancing to stage 14.125'
                html2=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?stairs=1')
                pos1=html2.find('trip')

                pos2 = html2.find('value=',pos1)+7
                pos3 = html2.find('"',pos2)
                theoi = html2[pos2:pos3]
                html2=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?trip=' + theoi)


                #looking over edge , click one of the buttons with the link to constalation...






                #Collect bandage by hitting continue (same code as above repeated with bandagehtml)

                pos2 = html2.find('trip=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]
                consturl ='http://www.neopets.com/altador/hallofheroes.phtml?'+urldata

                consthtml =self.acc.get(consturl)






                self.settingsmanager.setvalue('misc','altador_stage', '14.125')
                self.atadorstage = '14.125'



        if self.atadorstage == '14.125':
                print 'Altador bot advancing to stage 14.128'
                html2=self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1')
                html2=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1')
                html2=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1')
                html2=self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1')








                self.settingsmanager.setvalue('misc','altador_stage', '14.128')
                self.atadorstage = '14.128'


        if self.atadorstage == '14.128':
                print 'Altador bot advancing to stage 14.129'
                html2=self.acc.get('http://www.neopets.com/altador/quarry.phtml')



                pos2 = html2.find('brhv=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]
                consturl ='http://www.neopets.com/altador/quarry.phtml?'+urldata

                rockhtml =self.acc.get(consturl)

                #buy rock
                pos1=rockhtml.find('brhv')

                pos2 = rockhtml.find('value=',pos1)+7
                pos3 = rockhtml.find('"',pos2)
                theoi = rockhtml[pos2:pos3]
                rockhtml2=self.acc.get('http://www.neopets.com/altador/quarry.phtml?go_buy_rock=1&brhv=' + theoi)
                self.settingsmanager.setvalue('misc','altador_stage', '14.129')
                self.atadorstage = '14.129'

        if self.atadorstage == '14.129':

                print 'Altador bot advancing to stage 14.130'
                html2=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=2' , 'http://www.neopets.com/altador/hallofheroes.phtml?basement=1')
                if html2.find('gear2_jammed') > 1:
                    #remove the jammed stone if needed..
                    html2=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=2' , 'http://www.neopets.com/altador/hallofheroes.phtml?basement=1')
                self.settingsmanager.setvalue('misc','altador_stage', '14.130')
                self.atadorstage = '14.130'



        if self.atadorstage == '14.130':

                print 'Altador bot advancing to stage 14.131'
                html2=self.acc.get('http://www.neopets.com/altador/quarry.phtml')



                #Collect bandage by hitting continue (same code as above repeated with bandagehtml)

                pos2 = html2.find('trhv=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]
                rockurl ='http://www.neopets.com/altador/quarry.phtml?'+urldata

                rockhtml =self.acc.get(rockurl)

                #and again once more..

                pos2 = rockhtml.find('trhv=')
                pos3 = rockhtml.find('"',pos2)
                urldata = rockhtml[pos2:pos3]
                rockurl2 ='http://www.neopets.com/altador/quarry.phtml?'+urldata

                rockhtml2 =self.acc.get(rockurl2)

                #and again once more..

                pos2 = rockhtml2.find('trhv=')
                pos3 = rockhtml2.find('"',pos2)
                urldata = rockhtml2[pos2:pos3]
                rockurl3 ='http://www.neopets.com/altador/quarry.phtml?'+urldata

                rockhtml3 =self.acc.get(rockurl3)


                self.settingsmanager.setvalue('misc','altador_stage', '14.131')
                self.atadorstage = '14.131'

        if self.atadorstage == '14.131':
                print 'Altador bot advancing to stage 14.132'
                html2=self.acc.get('http://www.neopets.com/altador/archives.phtml?board=1&juggle=1')

                self.settingsmanager.setvalue('misc','altador_stage', '14.132')
                self.atadorstage = '14.132'


        if self.atadorstage == '14.132':
                print 'Altador bot advancing to stage 14.133'
               # html2=self.acc.get('http://www.neopets.com/altador/archives.phtml?board=1&juggle=1')
                html2=self.acc.get('http://www.neopets.com/altador/quarry.phtml')




                pos2 = html2.find('jjhv=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]
                rockurl ='http://www.neopets.com/altador/quarry.phtml?'+urldata

                rockhtml =self.acc.get(rockurl)

                pos1=rockhtml.find('jjhv')

                pos2 = rockhtml.find('value=',pos1)+7
                pos3 = rockhtml.find('"',pos2)
                theoi = rockhtml[pos2:pos3]

                pos4=rockhtml.find('r3hv',pos3)
                pos5 = rockhtml.find('value=',pos4)+7
                pos6 = rockhtml.find('"',pos5)
                theoi2 = rockhtml[pos5:pos6]

                rockhtml2=self.acc.get('http://www.neopets.com/altador/quarry.phtml?go_buy_rock=1&jjhv=' + theoi + '&r3hv=' + theoi2 )
                self.settingsmanager.setvalue('misc','altador_stage', '14.133')
                self.atadorstage = '14.133'


        if self.atadorstage == '14.133':
                print 'Altador bot advancing to stage 14.134 - can take a few minutes / attempts'

                ticker=0

                thesolution = ''
                self.resetstones()
                #Solve the roof / wheel combo
                while ticker <10:

                    html=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=' + str(ticker) )
                    newjanitorhtml =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1')

                    html=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=' + str(ticker) )
                    #print ticker
                    if newjanitorhtml.find('ceil_r20_634ded8a57') > 1:
                      #  print newjanitorhtml
                      #  print str(ticker) + ' is a valid gear'
                        thesolution = thesolution +  str(ticker)

                    if newjanitorhtml.find('ceil_r25_b87d73e953.gif')> 1:
                     #   print newjanitorhtml
                       # print str(ticker) + ' is a valid gear'
                        thesolution = thesolution +  str(ticker)


                    if newjanitorhtml.find('ceil_r30_8bfa6671f8.gif')> 1:
                        thesolution = thesolution +  str(ticker)
                    if len(thesolution) >2:
                        #found a solution , submit it... gears might break while we submit , if this happens reloop
                        print 'Trying solution..' + thesolution
                        solutionlist=list(thesolution)

                        for gearnum in solutionlist:
                            solution1 = solutionlist[0]
                            solution2 = solutionlist[1]
                            solution3 = solutionlist[2]
                            finalhtml=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=' + str(solution1) )
                            finalhtml=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=' + str(solution2) )
                            finalhtml=self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?basement=1&gear=' + str(solution3) )




                            newjanitorhtml =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1')


                            if newjanitorhtml.find('&olhv=') > 1:

                                pos2 = newjanitorhtml.find('&olhv=')
                                pos3 = newjanitorhtml.find('"',pos2)
                                urldata = newjanitorhtml[pos2:pos3]
                                finalurl ='http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1'+urldata
                                finalhtml =self.acc.get(finalurl)
                                #print finalhtml


                                self.settingsmanager.setvalue('misc','altador_stage', '14.134')
                                self.atadorstage = '14.134'
                                return

                            self.resetstones() #incase fail
                    if newjanitorhtml.find('You broke the gears') > 1:
                        print 'Janitor refreshed gears'
                        self.resetstones()
                        ticker = -1
                        thesolution=''
                    ticker = ticker + 1

        if self.atadorstage == '14.134':
                print 'Altador bot advancing to stage 14.138'


                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1')
                postdata = {'name' :'Hunter', 'data' : html}
                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('star_submit=')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl ='http://www.neopets.com/altador/astro.phtml?' + graburl1

                html =self.acc.get(graburl,'http://www.neopets.com/altador/astro.phtml?')

                self.settingsmanager.setvalue('misc','altador_stage', '14.138')
                self.atadorstage = '14.138'



        if self.atadorstage == '14.138':
                print 'Altador bot advancing to stage 14.139'


                html2 =self.acc.get('http://www.neopets.com/altador/archives.phtml?archivist=1&examine_book=1&view_page=53')

                pos2 = html2.find('dfhv=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]
                handurl ='http://www.neopets.com/altador/archives.phtml?'+urldata
                html =self.acc.get(handurl)


                self.settingsmanager.setvalue('misc','altador_stage', '14.139')
                self.atadorstage = '14.139'

        if self.atadorstage == '14.139':
                print 'Altador bot advancing to stage 15.140'


                html =self.acc.get('http://www.neopets.com/altador/astro.phtml?get_star_data=1')
                postdata = {'name' :'Sleeper', 'data' : html}
                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('data')
                pos2 = html.find('>',pos1) +1
                poa3=html.find('</textarea>',pos2)



                data1 = html[pos2:poa3]
                postdata = {'name' :'spellbook', 'data' : data1}
                html =self.acc.post('http://www.clraik.com/infamousjoe/constellation/',postdata,'www.Neoautov1.0.com')
                pos1=html.find('&arc')
                pos2 = html.find('\n',pos1)
                graburl1 = html[pos1:pos2]
                graburl = graburl1


                #got the coords in graburl


                html2 =self.acc.get('http://www.neopets.com/altador/archives.phtml')

                pos2 = html2.find('goarch=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]

                html2 = self.acc.get('http://www.neopets.com/altador/archives.phtml?' + urldata)




                pos2 = html2.find('goarch=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]
                cleanurl = urldata.replace('arcx=0&arcy=1&','')
                cleanurl = cleanurl + graburl




                html = self.acc.get('http://www.neopets.com/altador/archives.phtml?' + cleanurl)

                #extract all book urls
                booklisturls = []
                lastpos = 0
                while html.find('goarch=' , lastpos) > 1:
                    startpos = html.find('goarch=' , lastpos)
                    endpos = html.find('"',startpos)
                    theitemname = html[startpos:endpos]
                    if theitemname.find('read_book') >1:
                        booklisturls.append(theitemname)
                    lastpos = endpos

                for targeturl in booklisturls:
                    html = self.acc.get('http://www.neopets.com/altador/archives.phtml?' + targeturl)
                    if html.find('This spellbook contains')>1:
                        targeturl2 = targeturl + '&spell_id=29884'
                        html = self.acc.get('http://www.neopets.com/altador/archives.phtml?' + targeturl2)



                self.settingsmanager.setvalue('misc','altador_stage', '15.140')
                self.atadorstage = '15.140'



        if self.atadorstage == '15.140':
                print 'Altador bot advancing to stage 15.999'


                html2 =self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=6')

                pos2 = html2.find('view_statue_id=6&necklace')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]

                html2 = self.acc.get('http://www.neopets.com/altador/hallofheroes.phtml?' + urldata)


                pos2 = html2.find('ephv=')
                pos3 = html2.find("'",pos2)
                urldata = html2[pos2:pos3]

                html2 = self.acc.get('http://www.neopets.com/altador/council.phtml?' + urldata)

                self.settingsmanager.setvalue('misc','altador_stage', '15.999')
                self.atadorstage = '15.999'

        if self.atadorstage == '15.999':


                html2 = self.acc.get('http://www.neopets.com/altador/council.phtml')


                pos2 = html2.find('prhv=')
                pos3 = html2.find('"',pos2)
                urldata = html2[pos2:pos3]

                html2 = self.acc.get('http://www.neopets.com/altador/council.phtml?' + urldata)
                print 'Plot complete , setting plot mode off'


                self.settingsmanager.setvalue('misc','altador_on', 'off')
                self.loadsettings()


    def getrandwheelurl(self,timeout):
                pagehtml=''

                wheellist = ['http://www.neopets.com/altador/plant.phtml?room=2&act=r2s1',
                            'http://www.neopets.com/altador/plant.phtml?room=3&act=r3s2',
                            'http://www.neopets.com/altador/plant.phtml?room=3&act=r3s3',
                            'http://www.neopets.com/altador/plant.phtml?room=3&act=r3s4']


                while time.time() < timeout :

                    random.shuffle(wheellist)
                    pagehtml = self.acc.get(wheellist[0])

                    if (pagehtml.find('plant_saved') > 1):
                        self.settingsmanager.setvalue('misc','altador_stage', '13.118')
                        self.atadorstage = '13.118'
                        return




    def generaterandstring(self):
        memorylist=[] #Buffer for tried random values
        #Generates a random code that was never tried before
        targets=['o' , 'x'] #o = on , x = off
        targetstring=''

        pythonrox=True
        while pythonrox == True:



            while len(targetstring) < 8:
                random.shuffle(targets)#random order for the targets on/off value

                targetstring = targetstring + str(targets[0]) #Add the first random option to our final target string



            randstring = targetstring
            if not randstring in memorylist:

                memorylist.append(randstring)
                if len(memorylist)  ==255: #There are 256 , we have them all (counting from 0)  , this takes about 1 second
                    memorylist.sort() #Sort the list alpahbetically to cut down on needed changed between checks
                    return memorylist
            targetstring=''

