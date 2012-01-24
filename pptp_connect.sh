#!/bin/bash

echo "jackylee" > sudo_pass
sudo -S /usr/sbin/pptpsetup --create lable --server 173.231.56.203 --username leafbug --password jackylee --encrypt < sudo_pass
sudo -S pppd call lable < sudo_pass
sudo -S route add default gw 192.168.0.1 < sudo_pass
sudo -S route del default gw 192.168.5.1 < sudo_pass
