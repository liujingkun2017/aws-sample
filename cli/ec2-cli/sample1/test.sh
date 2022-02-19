
rrr='
ddd
ff
ee
'
for line in $rrr
do

  if [ "$line" = "" ]; then

      echo "empty string"
  fi

  echo  $line;
done