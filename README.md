# Would PHP make a good template language for django??

### The thinking here is...

* Python can't really be used as a template language
* PHP _is_ a template language
* Rails templates seem to be inspired by PHP
* Symfony used PHP as its template language for a long time
* If we have to use a language other than python for Django templates,
could we just use PHP?

### I'm really just...

* brushing up on Django
* finding out a little bit about how php CGI works
* trying out django's built-in selenium test setup

### How I did it

To try this out, I call the php-cgi executable from inside python.  I
pass the template variables to the template as a json payload.  I could
have also passed them in as query string, and they would have been
nicely loaded into `$_POST` for me.  However, I thought json would give
me more options, and is easier to create on the python side.

One drawback of this approach is that we can't pass in python objects.
Everything has to be turned into strings and numbers in advance.

### Why not build a django template engine?

* The php-cgi executable is happier when templates are passed in as a
file paths not strings
* I can't pass in python objects
* People seem to use http://www.makotemplates.org/ without a django
template engine, so I thought that was good enough for this experiment

### What about layout?

I still need to crack the layout problem.
I wonder if copying Symfony's patterns would make sense.

### interesting bits of code

* <a href="comments/views.py">use a form and csrf token without django templates</a>
* <a href="comments/views.py">get static file path without django templates</a>
* <a href="php_template.py">simulate cgi for php-cgi</a>
* <a href="comments/templates/comments/comments.php">a php template used in django</a>
* <a href="pep8.sh">script that checks format of non git ignored python files</a>

### So how do I run it?

There is a make file to make it easy.  This will install the virtualenv
if necessary and run the migrations.  You don't have to activate the
virtualenv.

to run the test server:
````bash
#make sure you have php installed
make runserver
````

to run the tests:
````bash
#make sure you have chromedriver and php installed
make test
````
