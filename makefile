runserver: virtualenv check-for-php migrate
	$</bin/python ./manage.py $@
test: virtualenv check-for-php check-for-chromedriver
	$</bin/python ./manage.py $@ --failfast
migrate: virtualenv
	$</bin/python ./manage.py $@
check-for-chromedriver:
	which chromedriver
check-for-php:
	which php
virtualenv: requirements.txt
	virtualenv -p python3 $@
	virtualenv/bin/pip install -r $<
	touch $@
