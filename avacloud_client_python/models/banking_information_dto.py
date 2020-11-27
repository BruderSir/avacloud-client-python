# coding: utf-8

"""
    AVACloud API 1.17.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BankingInformationDto(object):
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
        'id': 'str',
        'name': 'str',
        'iban': 'str',
        'account_number': 'str',
        'bic': 'str',
        'routing_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'iban': 'iban',
        'account_number': 'accountNumber',
        'bic': 'bic',
        'routing_number': 'routingNumber'
    }

    def __init__(self, id=None, name=None, iban=None, account_number=None, bic=None, routing_number=None):  # noqa: E501
        """BankingInformationDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._iban = None
        self._account_number = None
        self._bic = None
        self._routing_number = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if iban is not None:
            self.iban = iban
        if account_number is not None:
            self.account_number = account_number
        if bic is not None:
            self.bic = bic
        if routing_number is not None:
            self.routing_number = routing_number

    @property
    def id(self):
        """Gets the id of this BankingInformationDto.  # noqa: E501

        Elements GUID identifier.  # noqa: E501

        :return: The id of this BankingInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BankingInformationDto.

        Elements GUID identifier.  # noqa: E501

        :param id: The id of this BankingInformationDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this BankingInformationDto.  # noqa: E501

        The name of the bank.  # noqa: E501

        :return: The name of this BankingInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingInformationDto.

        The name of the bank.  # noqa: E501

        :param name: The name of this BankingInformationDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def iban(self):
        """Gets the iban of this BankingInformationDto.  # noqa: E501

        The international identifier for the bank account.  # noqa: E501

        :return: The iban of this BankingInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this BankingInformationDto.

        The international identifier for the bank account.  # noqa: E501

        :param iban: The iban of this BankingInformationDto.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def account_number(self):
        """Gets the account_number of this BankingInformationDto.  # noqa: E501

        The account number. Typically no longer used since the introduction of IBAN within the SEPA area.  # noqa: E501

        :return: The account_number of this BankingInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BankingInformationDto.

        The account number. Typically no longer used since the introduction of IBAN within the SEPA area.  # noqa: E501

        :param account_number: The account_number of this BankingInformationDto.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def bic(self):
        """Gets the bic of this BankingInformationDto.  # noqa: E501

        The international bank identifier.  # noqa: E501

        :return: The bic of this BankingInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this BankingInformationDto.

        The international bank identifier.  # noqa: E501

        :param bic: The bic of this BankingInformationDto.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def routing_number(self):
        """Gets the routing_number of this BankingInformationDto.  # noqa: E501

        The routing number for the bank. Typically no longer used since the introduction of IBAN within the SEPA area.  # noqa: E501

        :return: The routing_number of this BankingInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """Sets the routing_number of this BankingInformationDto.

        The routing number for the bank. Typically no longer used since the introduction of IBAN within the SEPA area.  # noqa: E501

        :param routing_number: The routing_number of this BankingInformationDto.  # noqa: E501
        :type: str
        """

        self._routing_number = routing_number

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
        if issubclass(BankingInformationDto, dict):
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
        if not isinstance(other, BankingInformationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other