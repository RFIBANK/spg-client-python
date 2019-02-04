# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class ChargeResponse(BaseResponse):
    _fields = [
        'Success', 'OrderId', 'Operation', 'IsAsync', 'Status', 'StatusType',
        'RRN', 'Auth', 'MAC'
    ]
    _mac_fields = [
        'Success', 'OrderId', 'Operation', 'IsAsync', 'Status', 'StatusType',
        'ErrCode', 'ErrMessage'
    ]
