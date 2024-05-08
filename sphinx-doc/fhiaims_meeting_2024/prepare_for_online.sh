#!/bin/bash

rm -rf build/html/images build/html/sources build/html/static
mv build/html/_sources build/html/sources
mv build/html/_static build/html/static
mv build/html/_images build/html/images
sed -e "s/_static/static/g" -e "s/_sources/sources/g" -e "s/_images/images/g" build/html/index.html > temp
mv temp build/html/index.html

#mv build/html/index.html ../../
#cp -r build/html/static ../../
#cp -r build/html/sources ../../
