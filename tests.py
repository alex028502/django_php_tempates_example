from django.test import TestCase
from django.test import Client

from comments.models import Comment


class TestComments(TestCase):
    def setUp(self):
        self.c = Client()

    def test_items_in_list(self):
        Comment(name="Mikey", message="Good morning!").save()
        Comment(name="Billy", message="Good morning to you too!").save()

        response = self.c.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            self._comment_fragment(),
            response.content.decode('UTF-8')
        )
        self.assertIn("Mikey", response.content.decode('UTF-8'))
        self.assertIn("Billy", response.content.decode('UTF-8'))
        self.assertIn("Good morning", response.content.decode('UTF-8'))
        self.assertIn(self._form_fragement(), response.content.decode('UTF-8'))

        self.assertNotIn(
            self._no_comments_message_fragement(),
            response.content.decode('UTF-8')
        )
        self.assertNotIn(
            self._required_message_fragement(),
            response.content.decode('UTF-8')
        )

    def test_no_items_in_list(self):
        response = self.c.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            self._comment_fragment(),
            response.content.decode('UTF-8')
        )
        self.assertIn(
            self._no_comments_message_fragement(),
            response.content.decode('UTF-8')
        )
        self.assertIn(self._form_fragement(), response.content.decode('UTF-8'))
        self.assertNotIn(
            self._required_message_fragement(),
            response.content.decode('UTF-8')
        )

    def test_add_first_comment(self):
        location = "/"

        response = self.c.post(
            location,
            {"name": "Don", "message": "message from test"}
        )
        self.assertEqual(response['Location'], location)
        self.assertEqual(response.content, b"")
        self.assertEqual(response.status_code, 302)

        response = self.c.get(location)
        self.assertEqual(response.status_code, 200)
        self.assertIn("<pre", response.content.decode('UTF-8'))
        self.assertIn("Don", response.content.decode('UTF-8'))
        self.assertIn("<form", response.content.decode('UTF-8'))
        self.assertNotIn(
            self._required_message_fragement(),
            response.content.decode('UTF-8')
        )

    def test_incorrect_form(self):
        # this won't really happen with HTML5 required
        response = self.c.post(
            "/",
            {"name": "", "message": "message from test"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("<pre", response.content.decode('UTF-8'))
        self.assertIn("<form", response.content.decode('UTF-8'))
        self.assertIn(
            self._required_message_fragement(),
            response.content.decode('UTF-8')
        )

    def _form_fragement(self):
        return "<form"

    def _comment_fragment(self):
        return "<pre"

    def _no_comments_message_fragement(self):
        return "no comments"

    def _required_message_fragement(self):
        return "is required"
