#!/bin/bash

mkdir -p out

for example in examples/example{1,6}.jazz; do
    if [ -f "$example" ]; then
        filename=$(basename "$example")
        python3 preprocessor.py --input_file "$example" --output_file "out/$filename"
    fi
done
