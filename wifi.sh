#!/bin/bash
kill $(ps -e |grep wpa |grep -oP '\d{3,}')
wpa_supplicant -B -D wext -i wlan0 -c /etc/wpa_supplicant.conf
dhclient wlan0 -v
ping 8.8.8.8 -c 3