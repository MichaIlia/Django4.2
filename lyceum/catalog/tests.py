from http import HTTPStatus

from django.test import Client, TestCase

import parameterized


class StaticURlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class StaticURL(TestCase):
    @parameterized.parameterized.expand([
        ('0', HTTPStatus.OK),
        ('1', HTTPStatus.OK),
        ('01', HTTPStatus.OK),
        ('010', HTTPStatus.OK),
        ('10', HTTPStatus.OK),
        ('100', HTTPStatus.OK),
        ('abcd', HTTPStatus.NOT_FOUND),
        ('aa4a', HTTPStatus.NOT_FOUND),
        ('232%', HTTPStatus.NOT_FOUND),
        ('-0', HTTPStatus.NOT_FOUND),
        ('-1', HTTPStatus.NOT_FOUND),
    ])
    def test_catalog_ilo(self, ilo, expected_status):
        status_code = Client().get(f'/catalog/{ilo}/').status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f'/catalog/{ilo}/ get not {expected_status}',
        )


class StaticURLTest(TestCase):
    @parameterized.parameterized.expand([
        ('0', HTTPStatus.NOT_FOUND),
        ('1', HTTPStatus.OK),
        ('01', HTTPStatus.NOT_FOUND),
        ('010', HTTPStatus.NOT_FOUND),
        ('10', HTTPStatus.OK),
        ('100', HTTPStatus.OK),
        ('abcd', HTTPStatus.NOT_FOUND),
        ('aa4a', HTTPStatus.NOT_FOUND),
        ('232%', HTTPStatus.NOT_FOUND),
        ('-0', HTTPStatus.NOT_FOUND),
        ('-1', HTTPStatus.NOT_FOUND),
    ])
    def test_catalog_plo(self, plo, expected_status):
        status_code = Client().get(f'/catalog/re/{plo}/').status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f'/catalog/re/{plo}/ get not {expected_status}',
        )


class StaticUrlTest(TestCase):
    @parameterized.parameterized.expand([
        ('0', HTTPStatus.NOT_FOUND),
        ('1', HTTPStatus.OK),
        ('01', HTTPStatus.NOT_FOUND),
        ('010', HTTPStatus.NOT_FOUND),
        ('10', HTTPStatus.OK),
        ('100', HTTPStatus.OK),
        ('abcd', HTTPStatus.NOT_FOUND),
        ('aa4a', HTTPStatus.NOT_FOUND),
        ('232%', HTTPStatus.NOT_FOUND),
        ('-0', HTTPStatus.NOT_FOUND),
        ('-1', HTTPStatus.NOT_FOUND),
     ])
    def test_catalog_ujo(self, ujo, expected_status):
        status_code = Client().get(
            f'/catalog/converter/{ujo}/').status_code

        self.assertEqual(
            status_code,
            expected_status,
            msg=f'/catalog/converter/{ujo}/ get not {expected_status}',
         )
