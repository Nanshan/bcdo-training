#!/bin/bash
IFS=' ' read -a words <<< "$@"
len=${#words[@]}
firstN=${words[0]}
#echo $len
#echo $firstN
if [ $firstN -lt $len ]
then
   echo ${words[$firstN]}
else
   echo "noting to print out "
fi
