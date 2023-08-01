#!/bin/bash

mkdir -p out

for example in examples/*; do
    if [ -f "$example" ]; then
        filename=$(basename "$example")
        python3 preprocessor.py "$example" > "out/$filename"
    fi
done
