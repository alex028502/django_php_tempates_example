import os
import json

from unittest import TestCase

from php_template import render


class TestTemplates(TestCase):
    def test_json(self):
        test_data = json.loads(content_of_file_in_directory('json/data.json'))
        result = render(
            template=absolute_path_of_file_in_directory('json/template.php'),
            payload=test_data
        )
        expected_result =\
            content_of_file_in_directory('json/expected_result.html')
        self.assertEqual(result, expected_result)


def content_of_file_in_directory(filename):
    return open(absolute_path_of_file_in_directory(filename=filename)).read()


def absolute_path_of_file_in_directory(filename):
    return os.path.join(os.path.dirname(__file__), filename)
