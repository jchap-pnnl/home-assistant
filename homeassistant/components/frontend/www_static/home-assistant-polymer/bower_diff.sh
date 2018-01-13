#!/bin/sh
 
echo "starting bower compare..."

dirs=(bower_components/*);

for dir in ${dirs[@]}
do
    echo $(basename $dir)
done