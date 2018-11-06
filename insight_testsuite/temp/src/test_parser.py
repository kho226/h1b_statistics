"""
Author: Kyle Ong
Date: 11/05/2018

Test cases for Parser class
"""
import unittest
from unittest import TestCase
from parser import Parser


class ParserTestCase(TestCase):

    def setUp(self):
        line = ';LCA_CASE_NUMBER;STATUS;LCA_CASE_SUBMIT;DECISION_DATE;'\
            'VISA_CLASS;LCA_CASE_EMPLOYMENT_START_DATE;'\
            'LCA_CASE_EMPLOYMENT_END_DATE;'\
            'LCA_CASE_EMPLOYER_NAME;LCA_CASE_EMPLOYER_ADDRESS;'\
            'LCA_CASE_EMPLOYER_CITY;LCA_CASE_EMPLOYER_STATE;'\
            'LCA_CASE_EMPLOYER_POSTAL_CODE;LCA_CASE_SOC_CODE;'\
            'LCA_CASE_SOC_NAME;LCA_CASE_JOB_TITLE;'\
            'LCA_CASE_WAGE_RATE_FROM;LCA_CASE_WAGE_RATE_TO;'\
            'LCA_CASE_WAGE_RATE_UNIT;FULL_TIME_POS;TOTAL_WORKERS;'\
            'LCA_CASE_WORKLOC1_CITY;LCA_CASE_WORKLOC1_STATE;PW_1;'\
            'PW_UNIT_1;PW_SOURCE_1;OTHER_WAGE_SOURCE_1;'\
            'YR_SOURCE_PUB_1;LCA_CASE_WORKLOC2_CITY;'\
            'LCA_CASE_WORKLOC2_STATE;PW_2;PW_UNIT_2;PW_SOURCE_2;'\
            'OTHER_WAGE_SOURCE_2;YR_SOURCE_PUB_2;LCA_CASE_NAICS_CODE'

        self.parsed = line.split(";")
        self.parser = Parser(self.parsed)

    def test_getLocations(self):
        test = self.parser.locations
        expected = {
            "soc_name":  14,
            "soc_code": 13,
            "status": 2,
            "lca_case_workloc2_state": 29,
            "lca_case_workloc1_state": 22,
        }
        # print(test)
        self.assertEquals(test, expected)

    def test_isValid(self):
        test = self.parser.isValid(self.parsed)
        expected = True
        self.assertEquals(expected, test)

    def test_status(self):
        status = self.parser.status(self.parsed)
        expected = "STATUS"
        self.assertEquals(status, expected)

    def test_state1(self):
        state = self.parser.state1(self.parsed)
        expected = "LCA_CASE_WORKLOC1_STATE"
        self.assertEquals(expected, state)

    def test_state2(self):
        state = self.parser.state2(self.parsed)
        expected = "LCA_CASE_WORKLOC2_STATE"
        self.assertEquals(expected, state)

    def test_worksite(self):
        worksite = self.parser.worksite(self.parsed)
        expected = None
        self.assertEquals(expected, worksite)

    def test_isCertified(self):
        isCertified = self.parser.isCertified(self.parsed)
        expected = False
        self.assertEquals(isCertified, expected)

    def test_name(self):
        name = self.parser.name(self.parsed)
        expected = "LCA_CASE_SOC_NAME"
        self.assertEquals(name, expected)

    def test_code(self):
        code = self.parser.code(self.parsed)
        expected = "LCA_CASE_SOC_CODE"
        self.assertEquals(code, expected)


if __name__ == '__main__':
    unittest.main()
