#!/bin/bash

mkdir -p out


./preprocessor --input_file examples/example1.jazz --output_file out/example1.jazz
./preprocessor --input_file examples/example2.jazz --output_file out/example2.jazz
./preprocessor --input_file examples/example3.jazz --output_file out/example3.jazz
./preprocessor --input_file examples/example4.jazz --output_file out/example4.jazz
./preprocessor --input_file examples/example5.jazz --output_file out/example5.jazz
./preprocessor --input_file examples/example6.jazz --output_file out/example6.jazz