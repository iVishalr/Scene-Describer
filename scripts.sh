#!/bin/sh
python3 frameExtraction.py $1
th eval.lua -model ./model.t7 -image_folder ../data -gpuid -1 -dump_images 0 -dump_path 0
python3 predict.py "$2"
