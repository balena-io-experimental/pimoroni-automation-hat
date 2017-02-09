#!/usr/bin/env python
# main.py

import sys, os, time, signal
import automationhat

def signal_term_handler(signal, frame):
    # handle the sigterm signal and write that to a persisted file in /data
    with open("/data/signals.log","a+") as f:
        f.write('got SIGTERM')
    print 'got SIGTERM'
    sys.exit(0)

def signal_int_handler(signal, frame):
    with open("/data/signals.log","a+") as f:
        f.write('got SIGINT')
    print 'got SIGINT'
    sys.exit(0)

def signal_kill_handler(signal, frame):
    with open("/data/signals.log","a+") as f:
        f.write('got SIGKILL')
    print 'got SIGKILL'
    sys.exit(0)

# Register our signal handlers to clean up gracefully
signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_int_handler)
signal.signal(signal.SIGHUP, signal_kill_handler)

# Print all the available RESIN_* variables in the environment.
print "RESIN envvars\n"
for key in os.environ.keys():
    if 'RESIN' in key:
        print key,os.environ[key]

# Switch on the Green Power LED on the Hat
automationhat.light.power.write(1)

while True:
    print "Toggling relay 1..."
    automationhat.relay.one.toggle()
    time.sleep(5)
