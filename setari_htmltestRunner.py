import unittest
from unittest import TestCase
from teste_herokuapp import HerokuappTest
from teste_emag import EmagTest
import HtmlTestRunner




class TestSuite(TestCase):
    def test_suite(self):
        tests=unittest.TestSuite()
        tests.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(HerokuappTest),
                        unittest.defaultTestLoader.loadTestsFromTestCase(EmagTest)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='First suite test',
            report_name='Test result',

        )
        runner.run(tests)
