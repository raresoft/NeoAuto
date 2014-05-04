#NeoAccount was originally created by ikakk
#Recoded and stripped by RareDareDevil:



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
        self.cleanhtml = ''

        self.cj = cookielib.LWPCookieJar()
        self.cookie_handler = urllib2.HTTPCookieProcessor(self.cj)

        if proxy != None:
            proxy_handler = urllib2.ProxyHandler({'http': 'http://' + proxy + '/'})
            self.opener = urllib2.build_opener(proxy_handler, self.cookie_handler)
        else:
            self.opener = urllib2.build_opener(self.cookie_handler)

    def __str__(self):
        return '%s:%s' % (self.user, self.pw)







    def get(self, url, referer = '', readable = True):
        if url[0] == '/':
            url = self.d + url
        if referer == '':
            referer = self.referer
        self.opener.addheaders = [('Referer', referer)] + self.headers
        res = self.opener.open(url)
        self.referer = res.geturl()
        if readable:
            theret = self.readable(res)
            self.cleanhtml = theret.replace('"',"'")
            return theret
        else:
            theret = str(res)
            self.cleanhtml = theret.replace('"',"'")
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
            theret = self.readable(res)
            self.cleanhtml = theret.replace('"',"'")
            return theret
        else:
            theret = str(res)
            self.cleanhtml = theret.replace('"',"'")
            return res


    def login(self):
        res = self.get('/index.phtml')
        res = self.post('/login.phtml', {'username': self.user,
                                         'password': self.pw,
                                         'destination': "/index.phtml"}, readable = False)
       # print res.geturl()
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