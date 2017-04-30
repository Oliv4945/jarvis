import logging
import time
from threading import Thread, Event

#import fix_import
from respeaker import Microphone


def task(quit_event):
    mic = Microphone(quit_event=quit_event)

    while not quit_event.is_set():
        if mic.wakeup('jarvis'):
            print('Jarvis')
            quit_event.set()

def main():
    #logging.basicConfig(level=logging.DEBUG)

    quit_event = Event()
    thread = Thread(target=task, args=(quit_event,))
    thread.start()
    while True:
        try:
            time.sleep(1)
            if quit_event.is_set():
                raise KeyboardInterrupt()
        except KeyboardInterrupt:
            #print('Quit')
            quit_event.set()
            break
    thread.join()

if __name__ == '__main__':
    main()

