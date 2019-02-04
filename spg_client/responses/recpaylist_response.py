# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class RecPayListResponse(BaseResponse):
    _fields = [
        'Success', 'MAC'
    ]
    _mac_fields = ['Success', 'ErrCode', 'ErrMessage']
