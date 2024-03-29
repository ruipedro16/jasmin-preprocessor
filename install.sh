#!/usr/bin/env bash

#
# install.sh - Installation script for the Jasmin preprocessor
#
# Usage: sudo ./install.sh
#        sudo ./install.sh ../scripts/
#

# Run sudo apt install python3.10 if not installed
if ! command -v python3 >/dev/null; then
    echo "Python not installed."
    exit 1
fi

# Check if $1 (destination) is provided
if [ -z "$1" ]; then
    destination="/usr/local/bin"
else
    destination="$1"
fi

chmod +x preprocessor # Make sure the script is executable
cp {preprocessor,env.py,generic_fn.py,regex.py,task.py,utils.py} "$destination"

cp jpp "$destination"
