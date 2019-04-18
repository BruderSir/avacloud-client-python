# coding: utf-8

"""
    AVACloud API 1.7.5

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.7.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.models.i_element_dto import IElementDto  # noqa: F401,E501
from avacloud_client_python.models.note_text_dto import NoteTextDto  # noqa: F401,E501


class ExecutionDescriptionDto(IElementDto):
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
        'blocks': 'list[NoteTextDto]',
        'label': 'str',
        'identifier': 'str',
        'element_type': 'str'
    }

    attribute_map = {
        'blocks': 'blocks',
        'label': 'label',
        'identifier': 'identifier',
        'element_type': 'elementType'
    }

    def __init__(self, blocks=None, label=None, identifier=None, element_type=None):  # noqa: E501
        """ExecutionDescriptionDto - a model defined in Swagger"""  # noqa: E501

        self._blocks = None
        self._label = None
        self._identifier = None
        self._element_type = None
        self.discriminator = None

        if blocks is not None:
            self.blocks = blocks
        if label is not None:
            self.label = label
        if identifier is not None:
            self.identifier = identifier
        if element_type is not None:
            self.element_type = element_type

    @property
    def blocks(self):
        """Gets the blocks of this ExecutionDescriptionDto.  # noqa: E501

        Blocks within an ExecutionDescription contain the actual information.               # noqa: E501

        :return: The blocks of this ExecutionDescriptionDto.  # noqa: E501
        :rtype: list[NoteTextDto]
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """Sets the blocks of this ExecutionDescriptionDto.

        Blocks within an ExecutionDescription contain the actual information.               # noqa: E501

        :param blocks: The blocks of this ExecutionDescriptionDto.  # noqa: E501
        :type: list[NoteTextDto]
        """

        self._blocks = blocks

    @property
    def label(self):
        """Gets the label of this ExecutionDescriptionDto.  # noqa: E501

        Labels this ExecutionDescription.               # noqa: E501

        :return: The label of this ExecutionDescriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ExecutionDescriptionDto.

        Labels this ExecutionDescription.               # noqa: E501

        :param label: The label of this ExecutionDescriptionDto.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def identifier(self):
        """Gets the identifier of this ExecutionDescriptionDto.  # noqa: E501

        Uniquely identifies this ExecutionDescription.               # noqa: E501

        :return: The identifier of this ExecutionDescriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ExecutionDescriptionDto.

        Uniquely identifies this ExecutionDescription.               # noqa: E501

        :param identifier: The identifier of this ExecutionDescriptionDto.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def element_type(self):
        """Gets the element_type of this ExecutionDescriptionDto.  # noqa: E501


        :return: The element_type of this ExecutionDescriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this ExecutionDescriptionDto.


        :param element_type: The element_type of this ExecutionDescriptionDto.  # noqa: E501
        :type: str
        """

        self._element_type = element_type

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
        if issubclass(ExecutionDescriptionDto, dict):
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
        if not isinstance(other, ExecutionDescriptionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
