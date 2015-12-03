#!/usr/bin/env python
import bernhard
import time
import signal
import sys
import uuid


# Catching gracefully ctrl+c
def signal_handler(signal, frame):
    print "System down"
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Generate a random hostname.
my_hostname = uuid.uuid4()

# Creating a default event.
event = {
    'host': str(my_hostname),
    'service': "Heartbeat",
}

# Starting a Riemann client.
client = bernhard.Client(host="localhost")

print "System up"
print "My hostname is '" + str(my_hostname) + "'"
print('Press Ctrl+C to stop, or wait 1 min')

for i in range(1, 13):
    print "Sending Heartbeat " + str(i)
    client.send(event)
    time.sleep(5)
print "System down"
