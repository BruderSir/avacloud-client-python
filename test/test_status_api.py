# coding: utf-8

"""
    AVACloud API 1.7.5

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.7.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import avacloud_client_python
from avacloud_client_python.api.status_api import StatusApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.status_api.StatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_status_get_status(self):
        """Test case for status_get_status

        Reports the health status of the AVACloud API  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
