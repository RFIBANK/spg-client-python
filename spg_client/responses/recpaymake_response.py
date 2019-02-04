# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class RecPayMakeResponse(BaseResponse):
    _fields = [
        'Success', 'RcStatus', 'OrderId', 'TrId', 'LimitCntLeft',
        'LimitAmountLeft', 'ValidThru', 'RRN', 'Auth', 'MAC'
    ]
    _mac_fields = [
        'Success', 'RcStatus', 'ErrCode', 'ErrMessage', 'OrderId', 'TrId',
        'LimitCntLeft', 'LimitAmountLeft', 'ValidThru', 'RRN', 'Auth'
    ]
