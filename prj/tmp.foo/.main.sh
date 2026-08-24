#!/usr/bin/env bash
. $(dirname $(readlink ${BASH_SOURCE[0]}))/.sys/first "$@"
. $my_sys/main "$@"
. $my_sys/last

# clear spurious paramaters
while [ ! -z $1 ]; do
    shift
done
