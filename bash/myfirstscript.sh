#!/bin/bash
echo 'This is a script. Hello!'
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working dir: $PWD
echo Session Length: $Seconds
echo Home Dir: $HOME

a=$(ip a | grep 'dynamic ens192' | awk '{print$2}')
echo My IP is $a
