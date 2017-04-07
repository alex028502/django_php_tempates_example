#!/usr/bin/env bash

# to make sure..
# -we have installed php-cgi and not just php
# -we have php 7 and not 5
# -php cgi is on 7 (since it might be possible to upgrade php but not upgrade php-cgi)

php-cgi --version | grep "PHP 7"
