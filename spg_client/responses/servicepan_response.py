# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class ServicePanOneTimeTokenResponse(BaseResponse):
    _fields = [
        'Success', 'Token', 'MAC'
    ]

    _mac_fields = [
        'Success', 'Token', 'ErrCode', 'ErrMessage'
    ]
