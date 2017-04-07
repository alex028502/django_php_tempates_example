#!/usr/bin/env bash

# list all files that need to be style checked
# this includes files that were generated with the project

find . -name "*.py" | git check-ignore --stdin -v -n | grep :: | awk '{ print $2 }'
