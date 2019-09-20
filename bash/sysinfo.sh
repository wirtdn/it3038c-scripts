#!/bin/bash
#"This script will email us our user, IP, hostname and today's date"
emailaddress=wirtdn@mail.uc.edu
p=$(printf "User \t%s\n" $USER)
a=$(ip a|grep 'dynamic ens192' | awk '{print$2}')
d=$(date +"%m-%d-%y")

 mail -s "IT3038c Linux IP" $emailaddress <<< $(echo \n $p)$(echo \n Hostname $HOSTNAME)$(echo \n IP $a)$(echo \n DATE $d)


