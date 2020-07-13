#!/bin/bash

# Ensure directory was passed
if [ $# -ne 1 ]; then
	echo "Please pass a directory"
	exit 1
fi
if ! [ -d "$1" ]; then
	echo "Could not find directory $1"
	exit 1
fi

export DYLD_LIBRARY_PATH=/anaconda3/lib/
mv "$1/element.in" "$1/element_o.in"
cp ./element.in $1
cp ./element6 $1
cd $1
rm *.aei
./element6
cd $OLDPWD
python convert_mercury_rebound.py $1
rm "$1/element.in"
mv "$1/element_o.in" "$1/element.in"

