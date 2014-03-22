# -*- coding: utf-8 -*-
import os
import argparse
import sys
import socket
import time
import datetime
import urllib2
import signal

def signal_handler(signal, frame):
        print '\033[0m'
        sys.exit(0)
        
signal.signal(signal.SIGINT, signal_handler)

class alertmewhenthissitegoesdown:
    def __init__(self, inputargs):
        prog="alertmewhenthissitegoesdown.py"
        version=0.1
        description = prog + " " + str(version) + "\nAlert me, when this site goes down."
        epilog = """
    Sample usage:
      python alertmewhenthissitegoesdown.py http://xxx.xxx/xxx.xxx 

    """
        parser = argparse.ArgumentParser(description=description, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter, prog=prog)
        parser.add_argument("url",
            metavar="URL", action="store", default="",
            help='url to check')
        parser.add_argument("--timeout",
            metavar="S", action="store", default=10, type=int,
            help='timeout in S seconds (default: %(default)s)')
        parser.add_argument("--repeat",
            metavar="S", action="store", default=60, type=int,
            help='check it again after S seconds (default: %(default)s)')
        parser.add_argument("--times",
            metavar="NUM", action="store", default=3, type=int,
            help='alert only NUM times in a row (default: %(default)s)')
        self.options = parser.parse_args(args=inputargs)
        self.counter=0
        self.process()



    def process(self):
        socket.setdefaulttimeout(60)
        while True:
            start=time.time()
            print datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S'),

            req = urllib2.Request(self.options.url)
            try:
                response = urllib2.urlopen(req)
            except urllib2.URLError as e:
                print '\033[91m',
                end=time.time()
                print ("{:6.2f}".format(end-start)),
                if hasattr(e, 'reason'):
                    print "We failed to reach a server. Reason: ", e.reason,
                    self.alert()
                elif hasattr(e, 'code'):
                    print "The server couldn\'t fulfill the request. Error code: ", e.code,
                    self.alert()
            except  Exception, e:
                print '\033[91m',
                end=time.time()
                print ("{:6.2f}".format(end-start)),
                print "We failed to reach a server. Reason: %s"  % e,
                self.alert()
            else:
                response.read()
                end=time.time()
                if (end-start)>self.options.timeout:
                    print '\033[91m',
                else:
                    print '\033[92m',
                print ("{:6.2f}".format(end-start)),
                asterisk="*"*int(round((end-start)/0.25,0))
                if len(asterisk)>80:
                    asterisk="*"*80
                print asterisk,
                if (end-start)>self.options.timeout:
                    self.alert()
                else:
                    self.counter=0
            print '\033[0m'
            time.sleep(self.options.repeat)



    def alert(self):
        if self.counter<self.options.times:
            self.counter+=1
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1, 444))



if __name__ == "__main__":
    alertmewhenthissitegoesdown(sys.argv[1:])

