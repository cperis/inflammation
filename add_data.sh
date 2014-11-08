type=`python assign_drug.py $2`
dest=`echo data/$2/$1/$1-$type.dat`
cp $2 $dest
git add $dest
MSG="Add file $dest"
git commit -m $MSG
echo "New file added to the report: $dest"
