#!/bin/bash

mkdir -p out


python3 preprocessor.py --input_file examples/example1.jazz --output_file out/example1.jazz
python3 preprocessor.py --input_file examples/example2.jazz --output_file out/example2.jazz
python3 preprocessor.py --input_file examples/example3.jazz --output_file out/example3.jazz
python3 preprocessor.py --input_file examples/example4.jazz --output_file out/example4.jazz
python3 preprocessor.py --input_file examples/example5.jazz --output_file out/example5.jazz
python3 preprocessor.py --input_file examples/example6.jazz --output_file out/example6.jazz