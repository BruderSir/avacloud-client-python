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


class GrossPriceComponentDto(object):
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
        'tax_rate': 'float',
        'deduction_factor': 'float',
        'total_net': 'float',
        'total_deducted': 'float',
        'total_tax': 'float',
        'total_gross': 'float',
        'total_gross_deducted': 'float',
        'total_tax_deducted': 'float'
    }

    attribute_map = {
        'tax_rate': 'taxRate',
        'deduction_factor': 'deductionFactor',
        'total_net': 'totalNet',
        'total_deducted': 'totalDeducted',
        'total_tax': 'totalTax',
        'total_gross': 'totalGross',
        'total_gross_deducted': 'totalGrossDeducted',
        'total_tax_deducted': 'totalTaxDeducted'
    }

    def __init__(self, tax_rate=None, deduction_factor=None, total_net=None, total_deducted=None, total_tax=None, total_gross=None, total_gross_deducted=None, total_tax_deducted=None, _configuration=None):  # noqa: E501
        """GrossPriceComponentDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._tax_rate = None
        self._deduction_factor = None
        self._total_net = None
        self._total_deducted = None
        self._total_tax = None
        self._total_gross = None
        self._total_gross_deducted = None
        self._total_tax_deducted = None
        self.discriminator = None

        self.tax_rate = tax_rate
        self.deduction_factor = deduction_factor
        self.total_net = total_net
        self.total_deducted = total_deducted
        self.total_tax = total_tax
        self.total_gross = total_gross
        self.total_gross_deducted = total_gross_deducted
        self.total_tax_deducted = total_tax_deducted

    @property
    def tax_rate(self):
        """Gets the tax_rate of this GrossPriceComponentDto.  # noqa: E501

        This components tax rate.  # noqa: E501

        :return: The tax_rate of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this GrossPriceComponentDto.

        This components tax rate.  # noqa: E501

        :param tax_rate: The tax_rate of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and tax_rate is None:
            raise ValueError("Invalid value for `tax_rate`, must not be `None`")  # noqa: E501

        self._tax_rate = tax_rate

    @property
    def deduction_factor(self):
        """Gets the deduction_factor of this GrossPriceComponentDto.  # noqa: E501

        This is the factor of applied deductions for this component  # noqa: E501

        :return: The deduction_factor of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._deduction_factor

    @deduction_factor.setter
    def deduction_factor(self, deduction_factor):
        """Sets the deduction_factor of this GrossPriceComponentDto.

        This is the factor of applied deductions for this component  # noqa: E501

        :param deduction_factor: The deduction_factor of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and deduction_factor is None:
            raise ValueError("Invalid value for `deduction_factor`, must not be `None`")  # noqa: E501

        self._deduction_factor = deduction_factor

    @property
    def total_net(self):
        """Gets the total_net of this GrossPriceComponentDto.  # noqa: E501

        The total net price for all components of a given tax rate.  # noqa: E501

        :return: The total_net of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._total_net

    @total_net.setter
    def total_net(self, total_net):
        """Sets the total_net of this GrossPriceComponentDto.

        The total net price for all components of a given tax rate.  # noqa: E501

        :param total_net: The total_net of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total_net is None:
            raise ValueError("Invalid value for `total_net`, must not be `None`")  # noqa: E501

        self._total_net = total_net

    @property
    def total_deducted(self):
        """Gets the total_deducted of this GrossPriceComponentDto.  # noqa: E501

        The resulting price component after applied deductions  # noqa: E501

        :return: The total_deducted of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._total_deducted

    @total_deducted.setter
    def total_deducted(self, total_deducted):
        """Sets the total_deducted of this GrossPriceComponentDto.

        The resulting price component after applied deductions  # noqa: E501

        :param total_deducted: The total_deducted of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total_deducted is None:
            raise ValueError("Invalid value for `total_deducted`, must not be `None`")  # noqa: E501

        self._total_deducted = total_deducted

    @property
    def total_tax(self):
        """Gets the total_tax of this GrossPriceComponentDto.  # noqa: E501

        The total tax amount for all components of a given tax rate.  # noqa: E501

        :return: The total_tax of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this GrossPriceComponentDto.

        The total tax amount for all components of a given tax rate.  # noqa: E501

        :param total_tax: The total_tax of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total_tax is None:
            raise ValueError("Invalid value for `total_tax`, must not be `None`")  # noqa: E501

        self._total_tax = total_tax

    @property
    def total_gross(self):
        """Gets the total_gross of this GrossPriceComponentDto.  # noqa: E501

        The total gross price for all components of a given tax rate.  # noqa: E501

        :return: The total_gross of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._total_gross

    @total_gross.setter
    def total_gross(self, total_gross):
        """Sets the total_gross of this GrossPriceComponentDto.

        The total gross price for all components of a given tax rate.  # noqa: E501

        :param total_gross: The total_gross of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total_gross is None:
            raise ValueError("Invalid value for `total_gross`, must not be `None`")  # noqa: E501

        self._total_gross = total_gross

    @property
    def total_gross_deducted(self):
        """Gets the total_gross_deducted of this GrossPriceComponentDto.  # noqa: E501

        The total gross price for all components of a given tax rate, after applied deductions.  # noqa: E501

        :return: The total_gross_deducted of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._total_gross_deducted

    @total_gross_deducted.setter
    def total_gross_deducted(self, total_gross_deducted):
        """Sets the total_gross_deducted of this GrossPriceComponentDto.

        The total gross price for all components of a given tax rate, after applied deductions.  # noqa: E501

        :param total_gross_deducted: The total_gross_deducted of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total_gross_deducted is None:
            raise ValueError("Invalid value for `total_gross_deducted`, must not be `None`")  # noqa: E501

        self._total_gross_deducted = total_gross_deducted

    @property
    def total_tax_deducted(self):
        """Gets the total_tax_deducted of this GrossPriceComponentDto.  # noqa: E501

        The total tax amount for all components of a given tax rate, after applied deductions.  # noqa: E501

        :return: The total_tax_deducted of this GrossPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._total_tax_deducted

    @total_tax_deducted.setter
    def total_tax_deducted(self, total_tax_deducted):
        """Sets the total_tax_deducted of this GrossPriceComponentDto.

        The total tax amount for all components of a given tax rate, after applied deductions.  # noqa: E501

        :param total_tax_deducted: The total_tax_deducted of this GrossPriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total_tax_deducted is None:
            raise ValueError("Invalid value for `total_tax_deducted`, must not be `None`")  # noqa: E501

        self._total_tax_deducted = total_tax_deducted

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
        if issubclass(GrossPriceComponentDto, dict):
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
        if not isinstance(other, GrossPriceComponentDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GrossPriceComponentDto):
            return True

        return self.to_dict() != other.to_dict()
