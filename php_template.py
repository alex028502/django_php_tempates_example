import os
import subprocess
import json


def render(template, payload):

    assert os.path.isfile(template),\
        "template file %s does not exist" % template

    # thanks http://stackoverflow.com/a/5655409/5203563
    env = os.environ.copy()
    env['REQUEST_METHOD'] = "POST"
    env['SCRIPT_FILENAME'] = template
    env['REDIRECT_STATUS'] = "CGI"
    env['CONTENT_TYPE'] = "application/www-form-urlencoded"
    env['CONTENT_LENGTH'] = "%s" % len(json.dumps(payload))
    try:
        output = subprocess.check_output(
            ["php-cgi", "-dalways_populate_raw_post_data=-1"],
            input=json.dumps(payload).encode('utf-8'),
            env=env
        ).decode("utf-8").split("\n")[3:]
    except subprocess.CalledProcessError as exc:
        print("env is...")
        print(env)
        print("php output is...")
        print(exc.output)
        raise
    return "\n".join(output)
