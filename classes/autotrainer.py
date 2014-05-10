#train pets in acadamy (level 40-)




class autotrainer:
    def __init__(self,acc,mobilehandler,settingsmanager,inventorymanager):
        self.acc = acc
       # self.mobilehandler = mobilehandler
        self.settingsmanager = settingsmanager
        self.mobilehandler =mobilehandler
        self.trainingon = self.settingsmanager.getvalue("trainer","trainpets")
        self.trainingstat =  self.settingsmanager.getvalue("trainer","trainstat")
        self.trainmode =  self.settingsmanager.getvalue("trainer","trainmode")

        self.inventorymanager = inventorymanager


    def gettrainingstatus(self,html):

        retlist = []
        petlist = self.mobilehandler.getpetlist()
        for pet in petlist:

            petname= pet['name']

            pos1=html.find('<b>'+str(petname) + ' (')
            pos2 = html.find('</td>',pos1)
            extractedhtml = html[pos1:pos2]


            pos3 = html.find('<b>'+str(petname) + ' (')
            pos4 = html.find('</td></tr>',pos3) + 5
            pos5 =html.find('</td></tr>',pos4)




            extractedhtml2 =html[pos3:pos5]


            if extractedhtml2.find('Time till course finish') > 1:
                tempitem =[petname,'studying']
                retlist.append(tempitem)


            elif extractedhtml2.find('Course Finished!') >1:
                tempitem =[petname,'finished']
                retlist.append(tempitem)



            elif extractedhtml2.find('is not on a course') >1:
                tempitem =[petname,'none']
                retlist.append(tempitem)


            elif extractedhtml2.find('is currently studying Level') >1:
                tempitem =[petname,'level']
                retlist.append(tempitem)




        return retlist



    def getpayitem(self,html,petname):
        #Get the item needed to pay for a course
        pos1 = html.find('<b>'+str(petname)+' (')
        pos2 = html.find('</table>',pos1)
        temphtml = html[pos1:pos2]
        pos3=temphtml.find('<td><b>') +  7
        pos4=temphtml.find('</b>',pos3)
        return temphtml[pos3:pos4]

    def paycourse(self,html,petname):
       # Pay for a course
        postdata = {'pet_name' : petname , 'type' : 'pay'}
        html = self.acc.post('http://www.neopets.com/pirates/process_academy.phtml',postdata,'http://www.neopets.com/pirates/academy.phtml',)
       # print html




    def dopettick(self,targetpetname):
        #Do a tick for X petname
            statushtml = self.acc.get('http://www.neopets.com/pirates/academy.phtml?type=status')

           # print statushtml
            trainstatus = self.gettrainingstatus(statushtml)

            for item in trainstatus:
                petname = item[0]
                trainmode = item[1]


                if petname == targetpetname:


                    if trainmode == 'studying':
                        print  targetpetname + ' is  already studying...'
                        return

                    elif trainmode == 'finished':
                        print 'Finishing course for : ' + targetpetname
                        postdata = {'type' : 'complete',
                                    'pet_name': targetpetname}
                        finalhtml = self.acc.post('http://www.neopets.com/pirates/process_academy.phtml',postdata)



                    elif trainmode == 'none':
                        print 'Starting course...'

                        trainstat = str(self.trainingstat)
                        trainstat = trainstat.lower()

                        if trainstat == 'level':
                            print petname + ' is not on a course , starting course in ' + self.trainingstat

                            postdata = {'type' : 'start',
                                        'course_type' : 'Level',
                                        'pet_name' : str(petname)}

                            statushtml = self.acc.post('http://www.neopets.com/pirates/process_academy.phtml',postdata,'http://www.neopets.com/pirates/academy.phtml?type=courses',postdata)
                            print  self.mobilehandler.activepetname + ' Starting a course'

                        if trainstat == 'stenghth':
                            print petname + ' is not on a course , starting course in ' + self.trainingstat

                            postdata = {'type' : 'start',
                                        'course_type' : 'Strength',
                                        'pet_name' : str(petname)}

                            statushtml = self.acc.post('http://www.neopets.com/pirates/process_academy.phtml',postdata,'http://www.neopets.com/pirates/academy.phtml?type=courses',postdata)
                            print  self.mobilehandler.activepetname + ' Starting a course'



                        if trainstat == 'agility':
                            print petname + ' is not on a course , starting course in ' + self.trainingstat

                            postdata = {'type' : 'defence',
                                        'course_type' : 'Agility',
                                        'pet_name' : str(petname)}

                            statushtml = self.acc.post('http://www.neopets.com/pirates/process_academy.phtml',postdata,'http://www.neopets.com/pirates/academy.phtml?type=courses',postdata)
                            print  self.mobilehandler.activepetname + ' Starting a course'
                        if trainstat == 'endurance':
                            print petname + ' is not on a course , starting course in ' + self.trainingstat

                            postdata = {'type' : 'defence',
                                        'course_type' : 'Endurance',
                                        'pet_name' : str(petname)}

                            statushtml = self.acc.post('http://www.neopets.com/pirates/process_academy.phtml',postdata,'http://www.neopets.com/pirates/academy.phtml?type=courses',postdata)
                            print  self.mobilehandler.activepetname + ' Starting a course'


                    else:
                        #A train mode is set , get the item needed to pay for a course
                        thepayitem = self.getpayitem(statushtml,petname)

                        if self.inventorymanager.searchinvenotry(thepayitem) == True:
                            print thepayitem + ' found in inventory... , using to pay for course..'
                            self.paycourse(statushtml,petname)
                            return
                        else:
                            #Item was not found in inventory , search sdb for it

                            self.inventorymanager.removefromsdb(thepayitem)

                            self.inventorymanager.searchinvenotry(thepayitem)
                            if self.inventorymanager.searchinvenotry(thepayitem) == True:
                                print thepayitem + ' found in inventory... , using to pay for course..'
                                self.paycourse(statushtml,petname)
                                return



    def dotick(self):
        #modes are;
        #activepet
        #allpets
        #list?

        themode = self.trainmode.lower()
        if themode == 'activepet':
            #train the active pet
            self.dopettick(self.mobilehandler.activepetname)


        else:
            #Train all pets

            userpets = self.mobilehandler.getpetlist()
            for pet in userpets:
                petname= pet['name']
                self.dopettick(petname)

