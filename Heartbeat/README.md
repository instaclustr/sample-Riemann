# Simple Heartbeat monitoring with Riemann

This example illustrates how to use Riemann to monitor the heartbeats of some remote hosts, and trigger an alert when no heartbeat is recieved anymore.
A detailed explanation of this example can be found [there](https://www.instaclustr.com/monitoring-cassandra-and-it-infrastructure-with-riemann/)

#1. Set up the server #
To set up the server, you need to install Riemann. Check first if your distribution provides it already. For example, on a debian based distro:

```
#!bash

apt-get install riemann

```
On a redhat based system, this is usually done with

```
#!bash

yum install riemann

```
In case it is not found, you can follow the manual installation procedure [there](http://riemann.io/quickstart.html).

Once you have Riemann installed, you can clone this repository, and go to the folder ./Heartbeat, If you have pagerduty, you can set your key by editing the file riemann.config. If you don't, no worries, the message will be printed out on the terminal anyway. Starting the server is done with the command (as root):

```
#!bash

riemann ./riemann.config
```
If everything goes well, you will see on your terminal:

```
#!

main - riemann.core - Hyperspace core online
```
Riemann is now listening, by default on port 5555.

#2. Set up the client #
In this example the client uses the Riemann python client 'bernhard'. You will need python, pip, and you will need to install bernhard (as root) with pip. For example

```
#!bash
apt-get install python python-pip

pip install bernhard
```

Once installed, you can use the client.py script provided in this repo to send Heartbeat events:

```
#!bash

./client.py
```

The client will send Heartbeat events to Riemann every 5 seconds, and will stop after a minute (type ctrl+c if you are impatient!). Shortly after the client stoped, Riemann will trigger an alert: printing the event on stdout, and if you provided a valid pagerduty key, it will trigger a pagerduty alert.
If you want to test it on a separate physical host, you will need to modify client.py and provide the IP of your server, and you will need to open port 5555 on your server.

# Resources #
[Riemann web site](http://riemann.io)

[Bernhard github page](https://github.com/banjiewen/bernhard)

[Detailed explanation of this example](https://www.instaclustr.com/monitoring-cassandra-and-it-infrastructure-with-riemann/)
