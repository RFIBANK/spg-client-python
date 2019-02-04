# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class UnblockResponse(BaseResponse):
    _fields = [
        'Success', 'OrderId', 'Operation', 'IsAsync', 'Status', 'StatusType',
        'NewAmount', 'MAC'
    ]
    _mac_fields = [
        'Success', 'OrderId', 'Operation', 'IsAsync', 'Status', 'StatusType',
        'ErrCode', 'ErrMessage', 'NewAmount'
    ]
