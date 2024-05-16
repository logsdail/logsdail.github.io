#!/bin/bash

rm -rf build/html/images build/html/sources build/html/static
mv build/html/_sources build/html/sources
mv build/html/_static build/html/static
mv build/html/_images build/html/images
sed -e "s/_static/static/g" -e "s/_sources/sources/g" -e "s/_images/images/g" build/html/index.html > temp
mv temp build/html/index.html
cp Map2.png conference_photo.jpg build/html/images
# This adds a nofollow, so the search engines don't track the content
# I know the layout looks strange but that's what you need to do on OS X
sed -i='' '6i\
    <meta name="robots" content="noindex, nofollow">\
' build/html/index.html
cp -r presentations build/html/

#mv build/html/index.html ../../
#cp -r build/html/static ../../
#cp -r build/html/sources ../../
