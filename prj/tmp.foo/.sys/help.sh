foo () { while read line; do echo "   $1 $line"; done }

clr_bold USAGE:
for name in $(ls -a $my_bin); do
    path=$my_bin/$name
    [ ! -f $path ] && continue
    echo $name  | foo $(clr_bold $my_name)
done
#ls $my_bin | grep ^[a-z]*$                | foo $(clr_bold $my_name)
echo "-h or --h (for more subcommands)"  | foo $(clr_bold $my_name)

echo
clr_bold ABOUT:
cat $my_here/config/__doc__  | foo

echo
clr_bold ENVIRONMENT:
set | grep ^my     | foo
