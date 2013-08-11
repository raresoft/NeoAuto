import urllib2, urllib, cookielib
import StringIO, gzip


class NeoAccount:

    d = 'http://www.neopets.com'
    headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1'),
                ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                ('Accept-Language', 'en-us,en;q=0.5'),
                ('Accept-Encoding', 'gzip, deflate')]
    
    def __init__(self, user, pw, proxy = None):
        self.user = user
        self.pw = pw
        self.proxy = proxy
        self.referer = ''
        
        self.cj = cookielib.LWPCookieJar()
        self.cookie_handler = urllib2.HTTPCookieProcessor(self.cj)
        
        if proxy != None:
            proxy_handler = urllib2.ProxyHandler({'http': 'http://' + proxy + '/'})
            self.opener = urllib2.build_opener(proxy_handler, self.cookie_handler)
        else:
            self.opener = urllib2.build_opener(self.cookie_handler)

    def __str__(self):
        return '%s:%s' % (self.user, self.pw)


    def getimg(self, url, referer = '', readable = False):
        fulloutput = ""
        if url[0] == '/':
            url = self.d + url

        self.opener.addheaders =  self.headers
        res = self.opener.open(url).readall()
        fulloutput =res
        res2 = self.opener.open(url).readall()

        
        fulloutput =fulloutput + res2
        return fulloutput


    def get3(self, url, referer = '', readable = True):
        if url[0] == '/':
            url = self.d + url
        if referer == '':
            referer = self.referer
        self.opener.addheaders = [('Referer', referer)]  + self.headers 
        
        #data1 = urllib.urlopen(url).read()
        req = urllib2.Request(url)
        req.addheaders = [('Referer', referer)]  + self.headers
        
        req.HTTPCookieProcessor = self.cj

        resp = urllib2.urlopen(req)
        data1 = resp.read()
        #self.referer = res.geturl()

        #data1 = res.read(1024*1024)
       
#file = cStringIO.StringIO(urllib.urlopen(URL).read())
#img = Image.open(file)       


        
        #res5 = res.read()        
        return data1 

    def get2(self, url, referer = '', readable = True):
        if url[0] == '/':
            url = self.d + url
        if referer == '':
            referer = self.referer
        self.opener.addheaders = [('Referer', referer)]  + self.headers
        res = self.opener.open(url)
        self.referer = res.geturl()
        return res

    def get(self, url, referer = '', readable = True):
        if url[0] == '/':
            url = self.d + url
        if referer == '':
            referer = self.referer
        self.opener.addheaders = [('Referer', referer)]  + self.headers
        res = self.opener.open(url)
        self.referer = res.geturl()
        if readable:
            return self.readable(res)
        else:
            return res

    def post(self, url, data, referer = '', readable = True):
        if url[0] == '/':
            url = self.d + url
        if referer == '':
            referer = self.referer
        self.opener.addheaders = [('Content-Type', 'application/x-www-form-urlencoded'),
                                  ('Referer', referer)] + self.headers
        res = self.opener.open(url, urllib.urlencode(data))
        self.referer = res.geturl()
        if readable:
            return self.readable(res)
        else:
            return res

    def amf(self, packet, gateway = 'http://services.neopets.com/amfphp/gateway.php', referer = ''):
        if referer == '':
            referer = self.referer
        self.opener.addheaders = [('Content-Type', 'application/x-amf'),
                                  ('Referer', referer)] + self.headers
        res = self.opener.open(gateway, packet)
        return res.read()

    def login(self):
        res = self.get('/index.phtml')
        res = self.post('/login.phtml', {'username': self.user,
                                         'password': self.pw,
                                         'destination': "/index.phtml"}, readable = False)
        print res.geturl()
        if 'badpassword' in res.geturl():
            return False, 'Bad password'
        elif 'hello' in res.geturl():
            return False, 'Birthday locked'
        elif 'login' in res.geturl():
            return False, 'Frozen'
        elif 'index' in res.geturl():
            return True, 'Logged in'

    def readable(self, data):
        if 'gzip' in str(data.info()):
            return gzip.GzipFile(fileobj=StringIO.StringIO(data.read())).read()
        else:
            return data.read()
