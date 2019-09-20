#!/bin/bash
#This script will email me my IP,Server name, Bash Version, Time and Date.
emailaddress=wirtdn@mail.uc.edu
a=$(ip a|grep 'dynamic ens192' | awk '{print$2}')
s=$(echo $HOSTNAME)
b=$(echo $BASH_VERSION)
d=$(date +"%d-%m-%y")
t=$(date +"%H:%M:%S")


mail -s "IT3038C Lab2" $emailaddress <<< $(echo  $a 		   $s		    $b 		   $d		    $t)
