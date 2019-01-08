# coding: utf-8

"""
    AVACloud API 1.4.1

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import avacloud_client_python
from avacloud_client_python.api.excel_conversion_api import ExcelConversionApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestExcelConversionApi(unittest.TestCase):
    """ExcelConversionApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.excel_conversion_api.ExcelConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_excel_conversion_convert_to_ava(self):
        """Test case for excel_conversion_convert_to_ava

        Converts Excel files to Dangl.AVA projects.  # noqa: E501
        """
        pass

    def test_excel_conversion_convert_to_excel(self):
        """Test case for excel_conversion_convert_to_excel

        Converts Excel files to Excel files. Used, for example, when elements were added in excel to generate or modify a project. The Excel file can then be shared containing the full project with all formattings, formulas and styles applied.  # noqa: E501
        """
        pass

    def test_excel_conversion_convert_to_gaeb(self):
        """Test case for excel_conversion_convert_to_gaeb

        Converts Excel files to GAEB files.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
