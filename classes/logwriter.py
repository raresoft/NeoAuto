import datetime
import os
import time
class logwriter:
    #Write html log files / identify html results where possible

    def __init__(self,acc,settingsmanager):

        self.acc= acc
        self.logmode = settingsmanager.getvalue("misc","loglevel") #'all' / 'good' - log all things or only good things




    def writestringtofile(self,file_name, str_to_be_written,level):
        #print self.outputfolder + file_name + ".htm"
        outputfolder = './logs/'
        #str_to_be_written.replace(".js","")
        if level == 0:
            if self.logmode == 'good': #This item is not good enough , dont log it
                return
        file_writer = open(outputfolder + file_name + ".htm",  'a')
        currtime = time.time()
        filename = file_name + str((datetime.datetime.fromtimestamp(int(currtime)).strftime('%Y-%m-%d')))
        filename = filename.replace("-","_")


        newstr = '<div style="background-color:#99CCFF;width:auto;height:auto;border:1px solid #000"> ' + str(str_to_be_written) + '</div>'
        file_writer.write(newstr)

        file_writer.close()


