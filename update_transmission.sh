#!/bin/bash

public_ip=`curl http://members.3322.org/dyndns/getip`
sudo rm -f /tmp/tm.json
sudo cat /etc/transmission-daemon/settings.json.template | sed "s/\[public_ip\]/$public_ip/g" > /tmp/tm.json
sudo cp /tmp/tm.json /etc/transmission-daemon/settings.json

sudo service transmission-daemon reload
