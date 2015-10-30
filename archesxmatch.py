#!/usr/bin/python
import requests as rq
from hashlib import sha1
import base64
from configobj import ConfigObj
from time import sleep

class ArchesXMatch(object):
    #HOST = "http://cdsxmatch.u-strasbg.fr"
    HOST = "http://serendib.unistra.fr"
    URL = "%s/ARCHESWebService/XMatchARCHES" % HOST
    COOKIE = ".logcookie"

    def __init__(self):
        self.echo = True
        self.logged_in = False

    def get_pwd(self, pwd):
        """
        Encode password.
        """
        return base64.b64encode(sha1(pwd).hexdigest())

    def login(self, login, password=''):
        """
        Login to XMatch server and save cookies.
        """
        data = {'cmd': 'login',
                'username': login,
                'password': self.get_pwd(password)}
        req = rq.post(self.URL, data=data)
        self.cookies = req.cookies
        if self.echo and req.status_code == 200:
            self.logged_in = True
            print req.content
        return req

    def post(self, data, use_cookies=True, files=None):
        """
        General post method.
        """
        if use_cookies:
            req = rq.post(self.URL, data=data,
                          cookies=self.cookies, files=files)
        else:
            req = rq.post(self.URL, data=data, files=files)
        if files is not None:
            for f in files.values():
                f.close()
        if req.status_code == 200:
            # Everything's fine.
            self.content = req.content
            if self.echo:
                print self.content
        return req

    def list(self):
        """
        List files on the server.
        """
        return self.post({'cmd': "ls"})

    def upload(self, filename):
        """
        Upload a file to the server.
        """
        filehandler = open(filename)
        result = self.post(data={'cmd': 'put'},
                         files={filename: filehandler})
        filehandler.close()
        return result

    def xmatch(self, scriptname):
        """
        Run XMatch script.
        """
        if self.echo:
            print 'Running script %s' % scriptname
        if type(scriptname) == str:
            script = open(scriptname, 'r')
        else:
            script = scriptname
        result = self.post(data={'cmd': 'xmatch'},
                         files={'script': script})
        script.close()
        return result

    def download(self, filename, destination=None):
        """
        Download file from the server.
        """
        if self.echo:
            print 'Downloading file %s' % filename
        if destination is None:
            dest_file = filename
        else:
            dest_file = destination
        echo = self.echo
        self.echo = False
        for iretry in range(3):
            req = self.post({'cmd': "get", "fileName": filename})
            if req.status_code == 200:
                savetofile = open(dest_file, 'w')
                savetofile.write(req.content)
                savetofile.close()
            else:
                print 'Error downloading file %s. Response: %s' % (
                    filename, req.status_code)
                #if req.status_code != 400:
                #    self.echo = echo
                #    return req.status_code
                #else:
                print 'Retry in %s second...' % 2**iretry
                sleep(2**iretry)
        self.echo = echo
        if self.echo:
            print 'Downloading finished'
        return req

    def remove(self, filename):
        """
        Delete file on the server.
        """
        return self.post({'cmd': 'rm', 'fileName': filename})

    def quit(self):
        """
        Quit session.
        """
        self.logged_in = False
        return self.post({'cmd': "quit"})

if __name__ == '__main__':
    ax = ArchesXMatch()
    settings = ConfigObj('archesxmatch.ini')
    REQ = ax.login(settings['username'], settings['password'])
    #ax.xmatch(sys.argv[1])
    ax.list()
    #ax.download(sys.argv[2])
    ax.quit()
