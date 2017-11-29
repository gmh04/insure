from django.core import management
from django.test import TestCase

import json

from insure import settings

class ApiTest(TestCase):
    fixtures = ['risk/fixtures/data.json',]

    def test_api(self):
        # with no risk defined
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'msg': 'Risk needs to be defined'}
        )

        # check automobiles have 5 entries including non generic fields
        response = self.client.get('/api/automobiles')
        content = json.loads(str(response.content, encoding='utf8'))['fields']
        self.assertTrue(len(content), 5)
        self.assertEquals(content[3]['value'], 'ford,seat,kia')

        # entry with no non generic fields with have the 3 common enties
        response = self.client.get('/api/other')
        content = json.loads(str(response.content, encoding='utf8'))['fields']
        self.assertTrue(len(content), 3)

        # post returns 501
        response = self.client.post('/api/other')
        self.assertEqual(response.status_code, 501)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'msg': 'To be implemented'}
        )
