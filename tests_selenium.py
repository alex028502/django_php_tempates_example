import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


class SeleniumTestCase(StaticLiveServerTestCase):
    def test_e2e(self):
        driver = webdriver.Chrome()
        driver.get(self.live_server_url)
        self.assertEqual("Comments", driver.title)
        self.assertIn(self._no_comments_fragement(), driver.find_element_by_tag_name("body").get_attribute('innerHTML'))

        driver.find_element_by_name("name").send_keys("Andy")

        driver.find_element_by_xpath("//input[@type='submit']").click()

        # because we have the required attribute, we won't actually submit the form
        # and we won't get any error messages in the html
        self.assertIn(self._no_comments_fragement(), driver.find_element_by_tag_name("body").get_attribute('innerHTML'))

        driver.find_element_by_name("message").send_keys(self._message())

        driver.find_element_by_xpath("//input[@type='submit']").click()

        self.assertNotIn(self._no_comments_fragement(), driver.find_element_by_tag_name("body").get_attribute('innerHTML'))

        self.assertIn(self._message(), driver.find_element_by_tag_name("body").get_attribute('innerHTML'))

    def _no_comments_fragement(self):
        return "no comments"

    def _message(self):
        return "This is a test"
