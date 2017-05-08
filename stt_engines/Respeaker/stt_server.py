#!/usr/bin/python
"""
Web server to enable easy intergration of Respeaker python
library inside Jarvis.
Should disapear in favor of dedicated code
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import argparse # manage program arguments
import socket
import signal
import urlparse
import sys
from respeaker import Microphone
from respeaker.bing_speech_api import BingSpeechAPI
import logging
from threading import Event

class respeakerSTT():
    def __init__(self, quit_event, key):
        self.mic = Microphone(quit_event=quit_event)
        self.bing = BingSpeechAPI(key=key)

    def hotword(self, hotword):
        print('Starting detecting with:', hotword)
        if self.mic.wakeup(hotword):
            print('Detected hotword:', hotword)
            return hotword

    def rec(self, language):
        print('Waiting for order')
        data = self.mic.listen()
        try:
            text = self.bing.recognize(data, language)
            if text:
                print('Recognized %s' % text)
                return text
        except Exception as e:
            print(e.message)

# Clean program exit
def clean_exit (signum, frame):
    print 'Stopping HTTP server'
    quit_event.set()
    http_server.server_close()
    sys.exit(0)

def handle_request(self, data):
    if "hotword" in data:
        hotword = data['hotword'].lower()
        detected = respeaker.hotword(hotword)
        if detected  == hotword:
            self.send_response(200)
        else:
            self.send_response(400)                                             
        self.send_header('Content-type', 'text/html')                       
        self.end_headers()                                                  
        self.wfile.write(detected)

    elif "action" in data:
        if data['action'] == 'rec':
            detected = respeaker.rec(data.get('language', 'fr-FR'))
            if detected:
                self.send_response(200)
            else:
                self.send_response(408)
            self.send_header('Content-type', 'text/html') 
            self.end_headers()                            
            self.wfile.write(detected)

class requestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self._set_headers()
    
    def do_GET(self):
        url = urlparse.urlparse(self.path)
        data = dict(urlparse.parse_qsl(url.query))
        try:
            handle_request (self, data)
        except Exception as e:
            self.send_response(400)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            print "ERROR:", e
            pass
        
if __name__ == '__main__':
    # TODO
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Respeaker HTTP service')
    parser.add_argument('-b', '--bingKey', help='Bing API key')
    parser.add_argument('-p', '--port', help='Listening port (default: 8082)', type=int, default=8082)
    # parser.add_argument('-s', '--ssl', help='Use SSL', action='store_true')
    args = parser.parse_args()

    quit_event = Event()
    respeaker = respeakerSTT(quit_event, args.bingKey)

    try:
        http_server = HTTPServer(('', args.port), requestHandler)
        # if args.ssl:
        #     http_server.socket = ssl.wrap_socket (http_server.socket, certfile='./server.pem', server_side=True)
        for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
            signal.signal(sig, clean_exit)
        print('Start forever')
        http_server.serve_forever()
    except socket.error, msg:
        print 'ERROR: ', msg
        sys.exit(1)
    except KeyboardInterrupt:
        pass

