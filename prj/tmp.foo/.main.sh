#!/usr/bin/env bash
. $(dirname $(readlink ${BASH_SOURCE[0]}))/.sys/first "$@"
[ "$my_dot" == "." ] && [ "$1" == ""           ] && return
[ "$my_dot" == "." ] && [ "$1" == "--activate" ] && return
. $my_sys/main "$@"
. $my_sys/last

