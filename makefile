install: requirements.txt virtualenv
	virtualenv/bin/pip install -r $<
virtualenv:
	virtualenv -p python3 $@
