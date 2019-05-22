# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureWorkloadErrorInfo(Model):
    """Azure storage specific error information.

    :param error_code: Error code.
    :type error_code: int
    :param error_string: Localized error string.
    :type error_string: str
    :param error_title: Title: Typically, the entity that the error pertains
     to.
    :type error_title: str
    :param recommendations: List of localized recommendations for above error
     code.
    :type recommendations: list[str]
    :param additional_details: Additional details for above error code.
    :type additional_details: str
    """

    _attribute_map = {
        'error_code': {'key': 'errorCode', 'type': 'int'},
        'error_string': {'key': 'errorString', 'type': 'str'},
        'error_title': {'key': 'errorTitle', 'type': 'str'},
        'recommendations': {'key': 'recommendations', 'type': '[str]'},
        'additional_details': {'key': 'additionalDetails', 'type': 'str'},
    }

    def __init__(self, *, error_code: int=None, error_string: str=None, error_title: str=None, recommendations=None, additional_details: str=None, **kwargs) -> None:
        super(AzureWorkloadErrorInfo, self).__init__(**kwargs)
        self.error_code = error_code
        self.error_string = error_string
        self.error_title = error_title
        self.recommendations = recommendations
        self.additional_details = additional_details