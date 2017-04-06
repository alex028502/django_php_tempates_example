#!/usr/bin/env bash

find . -name "*.py" | git check-ignore --stdin -v -n | grep :: | awk '{ print $2 }' | xargs pep8
