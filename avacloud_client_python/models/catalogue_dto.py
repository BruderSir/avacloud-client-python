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


class CatalogueDto(object):
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
        'gaeb_xml_id': 'str',
        'name': 'str',
        'description': 'str',
        'catalogue_type': 'CatalogueTypeDto'
    }

    attribute_map = {
        'id': 'id',
        'gaeb_xml_id': 'gaebXmlId',
        'name': 'name',
        'description': 'description',
        'catalogue_type': 'catalogueType'
    }

    def __init__(self, id=None, gaeb_xml_id=None, name=None, description=None, catalogue_type=None, _configuration=None):  # noqa: E501
        """CatalogueDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._gaeb_xml_id = None
        self._name = None
        self._description = None
        self._catalogue_type = None
        self.discriminator = None

        self.id = id
        if gaeb_xml_id is not None:
            self.gaeb_xml_id = gaeb_xml_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.catalogue_type = catalogue_type

    @property
    def id(self):
        """Gets the id of this CatalogueDto.  # noqa: E501

        Elements GUID identifier.  # noqa: E501

        :return: The id of this CatalogueDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CatalogueDto.

        Elements GUID identifier.  # noqa: E501

        :param id: The id of this CatalogueDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def gaeb_xml_id(self):
        """Gets the gaeb_xml_id of this CatalogueDto.  # noqa: E501

        This is used to store the GAEB XML Id within this Catalogue. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization.  # noqa: E501

        :return: The gaeb_xml_id of this CatalogueDto.  # noqa: E501
        :rtype: str
        """
        return self._gaeb_xml_id

    @gaeb_xml_id.setter
    def gaeb_xml_id(self, gaeb_xml_id):
        """Sets the gaeb_xml_id of this CatalogueDto.

        This is used to store the GAEB XML Id within this Catalogue. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization.  # noqa: E501

        :param gaeb_xml_id: The gaeb_xml_id of this CatalogueDto.  # noqa: E501
        :type: str
        """

        self._gaeb_xml_id = gaeb_xml_id

    @property
    def name(self):
        """Gets the name of this CatalogueDto.  # noqa: E501

        The name that is given for this catalogue.  # noqa: E501

        :return: The name of this CatalogueDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CatalogueDto.

        The name that is given for this catalogue.  # noqa: E501

        :param name: The name of this CatalogueDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CatalogueDto.  # noqa: E501

        Additional information about this catalogue.  # noqa: E501

        :return: The description of this CatalogueDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CatalogueDto.

        Additional information about this catalogue.  # noqa: E501

        :param description: The description of this CatalogueDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def catalogue_type(self):
        """Gets the catalogue_type of this CatalogueDto.  # noqa: E501

        If given, this gives a classification for the contents of the catalogue  # noqa: E501

        :return: The catalogue_type of this CatalogueDto.  # noqa: E501
        :rtype: CatalogueTypeDto
        """
        return self._catalogue_type

    @catalogue_type.setter
    def catalogue_type(self, catalogue_type):
        """Sets the catalogue_type of this CatalogueDto.

        If given, this gives a classification for the contents of the catalogue  # noqa: E501

        :param catalogue_type: The catalogue_type of this CatalogueDto.  # noqa: E501
        :type: CatalogueTypeDto
        """
        if self._configuration.client_side_validation and catalogue_type is None:
            raise ValueError("Invalid value for `catalogue_type`, must not be `None`")  # noqa: E501

        self._catalogue_type = catalogue_type

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
        if issubclass(CatalogueDto, dict):
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
        if not isinstance(other, CatalogueDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogueDto):
            return True

        return self.to_dict() != other.to_dict()
