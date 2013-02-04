# -*- encoding: utf-8 -*-
__author__ = 'Сергей'

from django.test import TestCase, Client

class PagesCheck(TestCase):
    def testCodes(self):
        test_client = Client()
        pages = ["/","/places","/place/1"]
        for page in pages:
            response = test_client.get(page,follow=True)
            self.assertEqual(response.status_code,200)

