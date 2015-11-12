#!/bin/bash

if test $# -ne 3 
then
 echo -n "ERROR. " 
 echo "Usage: $0 my_robot.py my_other_robot.py"
 exit 1;
fi 

python rgkit/rgkit/run.py $1 $2
