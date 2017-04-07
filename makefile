runserver: virtualenv check-for-php migrate
	$</bin/python ./manage.py $@
test: virtualenv check-for-php check-for-chromedriver
	./build/files.sh | xargs $</bin/pep8
	$</bin/python ./manage.py $@ --failfast
migrate: virtualenv
	$</bin/python ./manage.py $@
check-for-chromedriver:
	which chromedriver
check-for-php:
	./build/php-7-check.sh
virtualenv: requirements.txt
	ls $@ || virtualenv -p python3 $@
	virtualenv/bin/pip install -r $<
	touch $@
