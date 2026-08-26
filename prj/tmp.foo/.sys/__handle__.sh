source ${my_sys}/init.sh

bash0=${BASH_SOURCE[1]}
base=$(basename $bash0)

[ "$base" == "$1" ] && shift

[ -d $bash0.d ] && [ -f $bash0.d/$1 ] && {
    export PATH=$bash0.d/.bin:$PATH
    #$my_dot $bash0.d/"$@"
    $bash0.d/"$@"
    return $?
}

[ -d $bash0.d ] && {
    [ ! .$1 == . ] && echo not found: $1
    for name in $(ls $bash0.d); do
        [ ! -f $bash0.d/$name ] && continue
        clr_bold "try: $base $name"
    done
    return $?
}

