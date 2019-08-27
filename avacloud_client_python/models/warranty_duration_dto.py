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

from avacloud_client_python.models.duration_unit_dto import DurationUnitDto  # noqa: F401,E501


class WarrantyDurationDto(object):
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
        'duration': 'int',
        'unit': 'DurationUnitDto'
    }

    attribute_map = {
        'duration': 'duration',
        'unit': 'unit'
    }

    def __init__(self, duration=None, unit=None):  # noqa: E501
        """WarrantyDurationDto - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._unit = None
        self.discriminator = None

        self.duration = duration
        self.unit = unit

    @property
    def duration(self):
        """Gets the duration of this WarrantyDurationDto.  # noqa: E501

        The scalar value of the duration. This value must be equal to or bigger than zero (&gt;= 0). Negative values can not be set and will be ignored.  # noqa: E501

        :return: The duration of this WarrantyDurationDto.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this WarrantyDurationDto.

        The scalar value of the duration. This value must be equal to or bigger than zero (&gt;= 0). Negative values can not be set and will be ignored.  # noqa: E501

        :param duration: The duration of this WarrantyDurationDto.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def unit(self):
        """Gets the unit of this WarrantyDurationDto.  # noqa: E501

        The unit of the duration  # noqa: E501

        :return: The unit of this WarrantyDurationDto.  # noqa: E501
        :rtype: DurationUnitDto
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this WarrantyDurationDto.

        The unit of the duration  # noqa: E501

        :param unit: The unit of this WarrantyDurationDto.  # noqa: E501
        :type: DurationUnitDto
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

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
        if issubclass(WarrantyDurationDto, dict):
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
        if not isinstance(other, WarrantyDurationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
