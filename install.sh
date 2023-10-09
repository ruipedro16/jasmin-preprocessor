#!/usr/bin/env bash

#
# install.sh - Installation script for the Jasmin preprocessor
#
# Usage: sudo ./install.sh
#

# Run sudo apt install python3.10 if not installed
if ! command -v python3 >/dev/null; then
    echo "Python not installed."
    exit 1
fi

chmod +x preprocessor # Make sure the script is executable
cp {preprocessor,generic_fn.py,typed_generic_fn.py,task.py,utils.py} /usr/local/bin
