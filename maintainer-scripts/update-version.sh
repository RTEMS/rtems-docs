#!/bin/sh

old="'4\.11\.0'"
new="'4\.11\.99'"

for i in */conf.py ; do
  sed -i "s/\(version\|release\) = $old/\1 = $new/g" $i
done
