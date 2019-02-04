# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class Status3dsResponse(BaseResponse):
    _fields = [
        'OrderId', 'Status', 'Success', 'MAC'
    ]
    _mac_fields = [
        'OrderId', 'Status', 'Success', 'ErrCode', 'ErrMessage'
    ]
