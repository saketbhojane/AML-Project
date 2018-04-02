mkdir $1 2> /dev/null;
python2 categorise_news_article.py $2 $1

sum=0
for file in $1*;
do
  d=$(find $file -type f | wc -l)
  if [ $d -le 10000 ] ;
  then
    # echo "$file Directory will be deleted"
    rm -rf $file;
    continue;
  fi
  echo "$file $d"
  sum=`expr $sum + $d`
done

echo "Total number of articles available for training $sum"
