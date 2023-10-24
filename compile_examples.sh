#!/bin/bash

for i in {1..7}
do
  python3 preprocessor --input_file examples/example$i.jazz --output_file examples/example"$i"_resolved.jazz --workers 4
done