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

from avacloud_client_python.models.price_rounding_mode_dto import PriceRoundingModeDto  # noqa: F401,E501
from avacloud_client_python.models.project_information_dto import ProjectInformationDto  # noqa: F401,E501
from avacloud_client_python.models.service_specification_dto import ServiceSpecificationDto  # noqa: F401,E501


class ProjectDto(object):
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
        'price_accuracy': 'int',
        'force_strict_totals': 'bool',
        'price_rounding_mode': 'PriceRoundingModeDto',
        'project_information': 'ProjectInformationDto',
        'service_specifications': 'list[ServiceSpecificationDto]',
        'gaeb_xml_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'price_accuracy': 'priceAccuracy',
        'force_strict_totals': 'forceStrictTotals',
        'price_rounding_mode': 'priceRoundingMode',
        'project_information': 'projectInformation',
        'service_specifications': 'serviceSpecifications',
        'gaeb_xml_id': 'gaebXmlId'
    }

    def __init__(self, id=None, price_accuracy=None, force_strict_totals=None, price_rounding_mode=None, project_information=None, service_specifications=None, gaeb_xml_id=None):  # noqa: E501
        """ProjectDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._price_accuracy = None
        self._force_strict_totals = None
        self._price_rounding_mode = None
        self._project_information = None
        self._service_specifications = None
        self._gaeb_xml_id = None
        self.discriminator = None

        self.id = id
        self.price_accuracy = price_accuracy
        self.force_strict_totals = force_strict_totals
        self.price_rounding_mode = price_rounding_mode
        if project_information is not None:
            self.project_information = project_information
        if service_specifications is not None:
            self.service_specifications = service_specifications
        if gaeb_xml_id is not None:
            self.gaeb_xml_id = gaeb_xml_id

    @property
    def id(self):
        """Gets the id of this ProjectDto.  # noqa: E501

        Elements GUID identifier.  # noqa: E501

        :return: The id of this ProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectDto.

        Elements GUID identifier.  # noqa: E501

        :param id: The id of this ProjectDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def price_accuracy(self):
        """Gets the price_accuracy of this ProjectDto.  # noqa: E501

        This property controls the accuracy of all price properties, meaning how many decimal places are preserved in calculations. It defaults to DEFAULT_PRICE_ACCURACY. Please see the Dangl.AVA documentation for further information about decimal precision.  # noqa: E501

        :return: The price_accuracy of this ProjectDto.  # noqa: E501
        :rtype: int
        """
        return self._price_accuracy

    @price_accuracy.setter
    def price_accuracy(self, price_accuracy):
        """Sets the price_accuracy of this ProjectDto.

        This property controls the accuracy of all price properties, meaning how many decimal places are preserved in calculations. It defaults to DEFAULT_PRICE_ACCURACY. Please see the Dangl.AVA documentation for further information about decimal precision.  # noqa: E501

        :param price_accuracy: The price_accuracy of this ProjectDto.  # noqa: E501
        :type: int
        """
        if price_accuracy is None:
            raise ValueError("Invalid value for `price_accuracy`, must not be `None`")  # noqa: E501

        self._price_accuracy = price_accuracy

    @property
    def force_strict_totals(self):
        """Gets the force_strict_totals of this ProjectDto.  # noqa: E501

        This forces total prices to be the strict product of quantities times unit price in positions. It is enabled by default. If this is disabled, both the unit price and the total price of positions is calculated from the non-rounded values. Please see the documentation for a more detailed explanation of this setting.  # noqa: E501

        :return: The force_strict_totals of this ProjectDto.  # noqa: E501
        :rtype: bool
        """
        return self._force_strict_totals

    @force_strict_totals.setter
    def force_strict_totals(self, force_strict_totals):
        """Sets the force_strict_totals of this ProjectDto.

        This forces total prices to be the strict product of quantities times unit price in positions. It is enabled by default. If this is disabled, both the unit price and the total price of positions is calculated from the non-rounded values. Please see the documentation for a more detailed explanation of this setting.  # noqa: E501

        :param force_strict_totals: The force_strict_totals of this ProjectDto.  # noqa: E501
        :type: bool
        """
        if force_strict_totals is None:
            raise ValueError("Invalid value for `force_strict_totals`, must not be `None`")  # noqa: E501

        self._force_strict_totals = force_strict_totals

    @property
    def price_rounding_mode(self):
        """Gets the price_rounding_mode of this ProjectDto.  # noqa: E501

        This property controls the rounding mode of all price properties, meaning how rounding of decimal places is performed in price calculations. It defaults to DEFAULT_ROUNDING_MODE. Please see the Dangl.AVA documentation for further information about decimal precision.  # noqa: E501

        :return: The price_rounding_mode of this ProjectDto.  # noqa: E501
        :rtype: PriceRoundingModeDto
        """
        return self._price_rounding_mode

    @price_rounding_mode.setter
    def price_rounding_mode(self, price_rounding_mode):
        """Sets the price_rounding_mode of this ProjectDto.

        This property controls the rounding mode of all price properties, meaning how rounding of decimal places is performed in price calculations. It defaults to DEFAULT_ROUNDING_MODE. Please see the Dangl.AVA documentation for further information about decimal precision.  # noqa: E501

        :param price_rounding_mode: The price_rounding_mode of this ProjectDto.  # noqa: E501
        :type: PriceRoundingModeDto
        """
        if price_rounding_mode is None:
            raise ValueError("Invalid value for `price_rounding_mode`, must not be `None`")  # noqa: E501

        self._price_rounding_mode = price_rounding_mode

    @property
    def project_information(self):
        """Gets the project_information of this ProjectDto.  # noqa: E501

        The ProjectInformation contains information that describes the project and its structure.  # noqa: E501

        :return: The project_information of this ProjectDto.  # noqa: E501
        :rtype: ProjectInformationDto
        """
        return self._project_information

    @project_information.setter
    def project_information(self, project_information):
        """Sets the project_information of this ProjectDto.

        The ProjectInformation contains information that describes the project and its structure.  # noqa: E501

        :param project_information: The project_information of this ProjectDto.  # noqa: E501
        :type: ProjectInformationDto
        """

        self._project_information = project_information

    @property
    def service_specifications(self):
        """Gets the service_specifications of this ProjectDto.  # noqa: E501

        The ServiceSpecifications in this Project.  # noqa: E501

        :return: The service_specifications of this ProjectDto.  # noqa: E501
        :rtype: list[ServiceSpecificationDto]
        """
        return self._service_specifications

    @service_specifications.setter
    def service_specifications(self, service_specifications):
        """Sets the service_specifications of this ProjectDto.

        The ServiceSpecifications in this Project.  # noqa: E501

        :param service_specifications: The service_specifications of this ProjectDto.  # noqa: E501
        :type: list[ServiceSpecificationDto]
        """

        self._service_specifications = service_specifications

    @property
    def gaeb_xml_id(self):
        """Gets the gaeb_xml_id of this ProjectDto.  # noqa: E501

        This is used to store the GAEB XML Id within this Project. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization.  # noqa: E501

        :return: The gaeb_xml_id of this ProjectDto.  # noqa: E501
        :rtype: str
        """
        return self._gaeb_xml_id

    @gaeb_xml_id.setter
    def gaeb_xml_id(self, gaeb_xml_id):
        """Sets the gaeb_xml_id of this ProjectDto.

        This is used to store the GAEB XML Id within this Project. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization.  # noqa: E501

        :param gaeb_xml_id: The gaeb_xml_id of this ProjectDto.  # noqa: E501
        :type: str
        """

        self._gaeb_xml_id = gaeb_xml_id

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
        if issubclass(ProjectDto, dict):
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
        if not isinstance(other, ProjectDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
