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


class ValidationCheckResult(object):
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
        'severity': 'ValidationSeverity',
        'check_type': 'ValidationCheckType',
        'message': 'str',
        'object_validation_check_details': 'ObjectValidationCheckDetails',
        'xml_schema_validation_check_details': 'XmlSchemaValidationCheckDetails',
        'project_validation_check_details': 'ProjectValidationCheckDetails'
    }

    attribute_map = {
        'severity': 'severity',
        'check_type': 'checkType',
        'message': 'message',
        'object_validation_check_details': 'objectValidationCheckDetails',
        'xml_schema_validation_check_details': 'xmlSchemaValidationCheckDetails',
        'project_validation_check_details': 'projectValidationCheckDetails'
    }

    def __init__(self, severity=None, check_type=None, message=None, object_validation_check_details=None, xml_schema_validation_check_details=None, project_validation_check_details=None, _configuration=None):  # noqa: E501
        """ValidationCheckResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._severity = None
        self._check_type = None
        self._message = None
        self._object_validation_check_details = None
        self._xml_schema_validation_check_details = None
        self._project_validation_check_details = None
        self.discriminator = None

        self.severity = severity
        self.check_type = check_type
        if message is not None:
            self.message = message
        if object_validation_check_details is not None:
            self.object_validation_check_details = object_validation_check_details
        if xml_schema_validation_check_details is not None:
            self.xml_schema_validation_check_details = xml_schema_validation_check_details
        if project_validation_check_details is not None:
            self.project_validation_check_details = project_validation_check_details

    @property
    def severity(self):
        """Gets the severity of this ValidationCheckResult.  # noqa: E501

        The severity for this check. Usually, low severity checks do not impact data exchange with third party applications  # noqa: E501

        :return: The severity of this ValidationCheckResult.  # noqa: E501
        :rtype: ValidationSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ValidationCheckResult.

        The severity for this check. Usually, low severity checks do not impact data exchange with third party applications  # noqa: E501

        :param severity: The severity of this ValidationCheckResult.  # noqa: E501
        :type: ValidationSeverity
        """
        if self._configuration.client_side_validation and severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def check_type(self):
        """Gets the check_type of this ValidationCheckResult.  # noqa: E501

        The actual check that is represented by this result. Additional information may be found in other properties of this class, depending on the check.  # noqa: E501

        :return: The check_type of this ValidationCheckResult.  # noqa: E501
        :rtype: ValidationCheckType
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this ValidationCheckResult.

        The actual check that is represented by this result. Additional information may be found in other properties of this class, depending on the check.  # noqa: E501

        :param check_type: The check_type of this ValidationCheckResult.  # noqa: E501
        :type: ValidationCheckType
        """
        if self._configuration.client_side_validation and check_type is None:
            raise ValueError("Invalid value for `check_type`, must not be `None`")  # noqa: E501

        self._check_type = check_type

    @property
    def message(self):
        """Gets the message of this ValidationCheckResult.  # noqa: E501

        A human readable message describing the result of the check.  # noqa: E501

        :return: The message of this ValidationCheckResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationCheckResult.

        A human readable message describing the result of the check.  # noqa: E501

        :param message: The message of this ValidationCheckResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def object_validation_check_details(self):
        """Gets the object_validation_check_details of this ValidationCheckResult.  # noqa: E501

        For CheckType of types ObjectValidation  # noqa: E501

        :return: The object_validation_check_details of this ValidationCheckResult.  # noqa: E501
        :rtype: ObjectValidationCheckDetails
        """
        return self._object_validation_check_details

    @object_validation_check_details.setter
    def object_validation_check_details(self, object_validation_check_details):
        """Sets the object_validation_check_details of this ValidationCheckResult.

        For CheckType of types ObjectValidation  # noqa: E501

        :param object_validation_check_details: The object_validation_check_details of this ValidationCheckResult.  # noqa: E501
        :type: ObjectValidationCheckDetails
        """

        self._object_validation_check_details = object_validation_check_details

    @property
    def xml_schema_validation_check_details(self):
        """Gets the xml_schema_validation_check_details of this ValidationCheckResult.  # noqa: E501

        For CheckType of types XmlSchemaCheck  # noqa: E501

        :return: The xml_schema_validation_check_details of this ValidationCheckResult.  # noqa: E501
        :rtype: XmlSchemaValidationCheckDetails
        """
        return self._xml_schema_validation_check_details

    @xml_schema_validation_check_details.setter
    def xml_schema_validation_check_details(self, xml_schema_validation_check_details):
        """Sets the xml_schema_validation_check_details of this ValidationCheckResult.

        For CheckType of types XmlSchemaCheck  # noqa: E501

        :param xml_schema_validation_check_details: The xml_schema_validation_check_details of this ValidationCheckResult.  # noqa: E501
        :type: XmlSchemaValidationCheckDetails
        """

        self._xml_schema_validation_check_details = xml_schema_validation_check_details

    @property
    def project_validation_check_details(self):
        """Gets the project_validation_check_details of this ValidationCheckResult.  # noqa: E501

        For CheckType of types ProjectValidation  # noqa: E501

        :return: The project_validation_check_details of this ValidationCheckResult.  # noqa: E501
        :rtype: ProjectValidationCheckDetails
        """
        return self._project_validation_check_details

    @project_validation_check_details.setter
    def project_validation_check_details(self, project_validation_check_details):
        """Sets the project_validation_check_details of this ValidationCheckResult.

        For CheckType of types ProjectValidation  # noqa: E501

        :param project_validation_check_details: The project_validation_check_details of this ValidationCheckResult.  # noqa: E501
        :type: ProjectValidationCheckDetails
        """

        self._project_validation_check_details = project_validation_check_details

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
        if issubclass(ValidationCheckResult, dict):
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
        if not isinstance(other, ValidationCheckResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidationCheckResult):
            return True

        return self.to_dict() != other.to_dict()
