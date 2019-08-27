# coding: utf-8

"""
    AVACloud API 1.9.1

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.9.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoginPost(object):
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
        'identifier': 'str',
        'password': 'str',
        'stay_signed_in': 'bool'
    }

    attribute_map = {
        'identifier': 'identifier',
        'password': 'password',
        'stay_signed_in': 'staySignedIn'
    }

    def __init__(self, identifier=None, password=None, stay_signed_in=None):  # noqa: E501
        """LoginPost - a model defined in Swagger"""  # noqa: E501

        self._identifier = None
        self._password = None
        self._stay_signed_in = None
        self.discriminator = None

        self.identifier = identifier
        self.password = password
        self.stay_signed_in = stay_signed_in

    @property
    def identifier(self):
        """Gets the identifier of this LoginPost.  # noqa: E501


        :return: The identifier of this LoginPost.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this LoginPost.


        :param identifier: The identifier of this LoginPost.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501
        if identifier is not None and len(identifier) < 1:
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._identifier = identifier

    @property
    def password(self):
        """Gets the password of this LoginPost.  # noqa: E501


        :return: The password of this LoginPost.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LoginPost.


        :param password: The password of this LoginPost.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) < 1:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def stay_signed_in(self):
        """Gets the stay_signed_in of this LoginPost.  # noqa: E501


        :return: The stay_signed_in of this LoginPost.  # noqa: E501
        :rtype: bool
        """
        return self._stay_signed_in

    @stay_signed_in.setter
    def stay_signed_in(self, stay_signed_in):
        """Sets the stay_signed_in of this LoginPost.


        :param stay_signed_in: The stay_signed_in of this LoginPost.  # noqa: E501
        :type: bool
        """
        if stay_signed_in is None:
            raise ValueError("Invalid value for `stay_signed_in`, must not be `None`")  # noqa: E501

        self._stay_signed_in = stay_signed_in

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
        if issubclass(LoginPost, dict):
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
        if not isinstance(other, LoginPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
