#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Made by Michael Kaplan
#Before running install requirements.txt




from zabbix_api import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

#define params
group = 25 #edit group id, you can find it using zabbix-cli
templete = 11433 #edit templete id you can find it using zabbix-cli



#Zabbix api configuration
zapi = ZabbixAPI("ZABBIXURL")
zapi.session.verify = False
zapi.login(user="APIUSER", password="ZabbixPASS")
##Progress bar
file = csv.reader(open('aps.csv'))
lines = sum(1 for line in file)
bar = ProgressBar(maxval=lines,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0
#progress bar
f = csv.reader(open('sample.csv'), delimiter=';') #Change the file name to that one you intend to use 

for [hostname,ip,macadd] in f: #edit colums to be readed and set variables for parameters
    zapi.host.create({
        "host": hostname ,
        "interfaces":[{
            "type": 2,
            "main": 1,
            "useip": 1,
            "ip": ip,
            "dns": "",
            "port": 161
        }],
        "groups":[{
            "groupid": group,
        }],
        "templates":[{
            "templateid": templete,
        }],
        "inventory": {
        "macaddress_a": macadd,
        },
        }
    )

    i += 1
    bar.update(i)

print ("\n Done")
        
