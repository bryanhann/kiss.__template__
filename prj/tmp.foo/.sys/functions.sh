
rename_fn() {
    # Found online
    local old_name="$1"
    local new_name="$2"
    
    # Verify the source function exists
    declare -f "$old_name" > /dev/null || return 1
    
    # Copy definition and delete the old one
    eval "function $(printf %q "$new_name") \
                   $(declare -f "$old_name" | tail -n +2)" \
                   && unset -f "$old_name"
}


rename_all_fn () {
    prename=$(echo $my_name | tr '.' '-' )
    prefix=my-
    for name in $(declare -f | grep ^$prefix); do
        left=${name:0:${#prefix}}
        right=${name:${#prefix}}
        [ ! "$left" == "$prefix" ] && continue
        rename_fn $name $prename-$right
    done
}

rename_all_exp () {
    local line
    local name=$(echo $my_name | tr '.' '_')
    for line in $(set | grep ^my_exp_); do
        export ${name}_${line:9}
    done
}

fix () {
    local mytmp=~/.tmp/$RANDOM.$RANDOM
    mkdir -p $mytmp
    cat $1 | sed "s/my_/${my_uname}_/g"  | sed "s/my-/${my_dname}-/g" > $mytmp/o
#    cat $mytmp/o
    source $mytmp/o
    rm $mytmp/o
    rmdir $mytmp
}


