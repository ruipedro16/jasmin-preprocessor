#!/bin/bash 

mkdir -p jpp_examples/asm
mkdir -p jpp_examples/jazz

for file in jpp_examples/*.jpp; do
    filename=$(basename "$file" .jpp)
    ./preprocessor --input_file $file --output_file "jpp_examples/jazz/$filename.jazz"
done

for file in jpp_examples/jazz/*; do
    filename=$(basename "$file" .jpp)
    jasminc $file -o "jpp_examples/asm/$filename.s" || (echo "Failed compiling $file" ; exit 1)
done
