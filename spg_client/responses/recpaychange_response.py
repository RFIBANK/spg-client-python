# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class RecPayChangeResponse(BaseResponse):
    _fields = ['Success', 'RcStatus', 'OrderId', 'MAC']

    _mac_fields = ['Success', 'RcStatus', 'ErrCode', 'ErrMessage', 'OrderId']
