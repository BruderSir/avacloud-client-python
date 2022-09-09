# coding: utf-8

"""
    AVACloud API 1.30.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.30.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class TokenResponseGet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token': 'str',
        'error': 'str',
        'error_description': 'str',
        'expires_in': 'int',
        'http_error_reason': 'str',
        'http_status_code': 'HttpStatusCode',
        'identity_token': 'str',
        'is_error': 'bool',
        'refresh_token': 'str',
        'token_type': 'str',
        'error_type': 'ResponseErrorType'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'error': 'error',
        'error_description': 'errorDescription',
        'expires_in': 'expiresIn',
        'http_error_reason': 'httpErrorReason',
        'http_status_code': 'httpStatusCode',
        'identity_token': 'identityToken',
        'is_error': 'isError',
        'refresh_token': 'refreshToken',
        'token_type': 'tokenType',
        'error_type': 'errorType'
    }

    def __init__(self, access_token=None, error=None, error_description=None, expires_in=None, http_error_reason=None, http_status_code=None, identity_token=None, is_error=None, refresh_token=None, token_type=None, error_type=None, _configuration=None):  # noqa: E501
        """TokenResponseGet - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._error = None
        self._error_description = None
        self._expires_in = None
        self._http_error_reason = None
        self._http_status_code = None
        self._identity_token = None
        self._is_error = None
        self._refresh_token = None
        self._token_type = None
        self._error_type = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if error is not None:
            self.error = error
        if error_description is not None:
            self.error_description = error_description
        self.expires_in = expires_in
        if http_error_reason is not None:
            self.http_error_reason = http_error_reason
        self.http_status_code = http_status_code
        if identity_token is not None:
            self.identity_token = identity_token
        self.is_error = is_error
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if token_type is not None:
            self.token_type = token_type
        self.error_type = error_type

    @property
    def access_token(self):
        """Gets the access_token of this TokenResponseGet.  # noqa: E501


        :return: The access_token of this TokenResponseGet.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TokenResponseGet.


        :param access_token: The access_token of this TokenResponseGet.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def error(self):
        """Gets the error of this TokenResponseGet.  # noqa: E501


        :return: The error of this TokenResponseGet.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TokenResponseGet.


        :param error: The error of this TokenResponseGet.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_description(self):
        """Gets the error_description of this TokenResponseGet.  # noqa: E501


        :return: The error_description of this TokenResponseGet.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this TokenResponseGet.


        :param error_description: The error_description of this TokenResponseGet.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

    @property
    def expires_in(self):
        """Gets the expires_in of this TokenResponseGet.  # noqa: E501


        :return: The expires_in of this TokenResponseGet.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this TokenResponseGet.


        :param expires_in: The expires_in of this TokenResponseGet.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and expires_in is None:
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

    @property
    def http_error_reason(self):
        """Gets the http_error_reason of this TokenResponseGet.  # noqa: E501


        :return: The http_error_reason of this TokenResponseGet.  # noqa: E501
        :rtype: str
        """
        return self._http_error_reason

    @http_error_reason.setter
    def http_error_reason(self, http_error_reason):
        """Sets the http_error_reason of this TokenResponseGet.


        :param http_error_reason: The http_error_reason of this TokenResponseGet.  # noqa: E501
        :type: str
        """

        self._http_error_reason = http_error_reason

    @property
    def http_status_code(self):
        """Gets the http_status_code of this TokenResponseGet.  # noqa: E501


        :return: The http_status_code of this TokenResponseGet.  # noqa: E501
        :rtype: HttpStatusCode
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this TokenResponseGet.


        :param http_status_code: The http_status_code of this TokenResponseGet.  # noqa: E501
        :type: HttpStatusCode
        """
        if self._configuration.client_side_validation and http_status_code is None:
            raise ValueError("Invalid value for `http_status_code`, must not be `None`")  # noqa: E501

        self._http_status_code = http_status_code

    @property
    def identity_token(self):
        """Gets the identity_token of this TokenResponseGet.  # noqa: E501


        :return: The identity_token of this TokenResponseGet.  # noqa: E501
        :rtype: str
        """
        return self._identity_token

    @identity_token.setter
    def identity_token(self, identity_token):
        """Sets the identity_token of this TokenResponseGet.


        :param identity_token: The identity_token of this TokenResponseGet.  # noqa: E501
        :type: str
        """

        self._identity_token = identity_token

    @property
    def is_error(self):
        """Gets the is_error of this TokenResponseGet.  # noqa: E501


        :return: The is_error of this TokenResponseGet.  # noqa: E501
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        """Sets the is_error of this TokenResponseGet.


        :param is_error: The is_error of this TokenResponseGet.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_error is None:
            raise ValueError("Invalid value for `is_error`, must not be `None`")  # noqa: E501

        self._is_error = is_error

    @property
    def refresh_token(self):
        """Gets the refresh_token of this TokenResponseGet.  # noqa: E501


        :return: The refresh_token of this TokenResponseGet.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this TokenResponseGet.


        :param refresh_token: The refresh_token of this TokenResponseGet.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def token_type(self):
        """Gets the token_type of this TokenResponseGet.  # noqa: E501


        :return: The token_type of this TokenResponseGet.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this TokenResponseGet.


        :param token_type: The token_type of this TokenResponseGet.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def error_type(self):
        """Gets the error_type of this TokenResponseGet.  # noqa: E501


        :return: The error_type of this TokenResponseGet.  # noqa: E501
        :rtype: ResponseErrorType
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this TokenResponseGet.


        :param error_type: The error_type of this TokenResponseGet.  # noqa: E501
        :type: ResponseErrorType
        """
        if self._configuration.client_side_validation and error_type is None:
            raise ValueError("Invalid value for `error_type`, must not be `None`")  # noqa: E501

        self._error_type = error_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TokenResponseGet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TokenResponseGet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenResponseGet):
            return True

        return self.to_dict() != other.to_dict()
