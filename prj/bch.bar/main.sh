#!/usr/bin/env bash

.  $(dirname $(readlink ${BASH_SOURCE[0]}))/.sys/first "$@"
. $this_sys/main "$@"
. $this_sys/last
