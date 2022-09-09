# coding: utf-8

"""
    AVACloud API 1.30.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.30.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import avacloud_client_python
from avacloud_client_python.api.ava_conversion_api import AvaConversionApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestAvaConversionApi(unittest.TestCase):
    """AvaConversionApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.ava_conversion_api.AvaConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ava_conversion_convert_to_ava(self):
        """Test case for ava_conversion_convert_to_ava

        Converts Dangl.AVA projects to Dangl.AVA. This is useful when you want to generate the calculated properties.  # noqa: E501
        """
        pass

    def test_ava_conversion_convert_to_excel(self):
        """Test case for ava_conversion_convert_to_excel

        Converts Dangl.AVA projects to Excel  # noqa: E501
        """
        pass

    def test_ava_conversion_convert_to_gaeb(self):
        """Test case for ava_conversion_convert_to_gaeb

        Converts Dangl.AVA projects to GAEB  # noqa: E501
        """
        pass

    def test_ava_conversion_convert_to_oenorm(self):
        """Test case for ava_conversion_convert_to_oenorm

        Converts Dangl.AVA projects to Oenorm  # noqa: E501
        """
        pass

    def test_ava_conversion_convert_to_reb(self):
        """Test case for ava_conversion_convert_to_reb

        Converts Dangl.AVA projects to REB  # noqa: E501
        """
        pass

    def test_ava_conversion_convert_to_sia(self):
        """Test case for ava_conversion_convert_to_sia

        Converts Dangl.AVA projects to SIA 451  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
