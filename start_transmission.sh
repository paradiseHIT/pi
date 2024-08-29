#!/bin/bash

trans_ps=`ps aux | grep transmission-daemon | grep -v grep | awk '{print $2}'`
if [ "x$trans_ps" = "x" ]
then
  sudo -u debian-transmission /usr/bin/transmission-daemon -f --log-error -e /tmp/transmission-daemon.log > /tmp/start_transmission.log
fi
