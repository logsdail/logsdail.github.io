#!/bin/bash

convert -scale 400x -strip -interlace Plane -gaussian-blur 0.05 -quality 85% $1 new_$1
