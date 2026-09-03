#!/usr/bin/env bash
x () {
    local here=$1
    source $here/vendor.d/bash_colors.sh
    for name in $(ls $here | sort | grep ^[0-9]); do
        source $1/$name
    done
}
x $(dirname ${BASH_SOURCE[0]})
