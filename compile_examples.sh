#!/bin/bash

mkdir -p out

for example in examples/example{1,5}.jazz; do
    if [ -f "$example" ]; then
        filename=$(basename "$example")
        python3 preprocessor.py --input_file "$example" --output_file "out/$filename"
    fi
done

# _keccak1600.jinc has the parameters in another file, but all functions are in the same file
python3 preprocessor.py --input_file examples/sphincs+/_keccak1600.jinc --search_path examples/sphincs+/* --output_file out/_keccak1600.jinc
