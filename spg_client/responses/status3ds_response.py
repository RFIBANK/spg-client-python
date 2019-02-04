# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class Status3dsResponse(BaseResponse):
    _fields = [
        'Success', 'OrderId', 'Status', 'MAC'
    ]
    _mac_fields = [
        'Success', 'OrderId', 'Status', 'ErrCode', 'ErrMessage'
    ]
