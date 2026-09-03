#!/usr/bin/env bash
pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null
init=$PWD
popd > /dev/null
for x in $(ls $init| sort | grep ^[0-9]); do
    source $init/$x
done
#for x in $(ls $here | sort | grep ^[0-9]); do
#    echo source $here/$x
#    source $here/$x
#done
