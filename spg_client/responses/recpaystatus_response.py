# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class RecPayStatusResponse(BaseResponse):
    _fields = [
        'Success', 'RcStatus', 'OrderId', 'LimitCntLeft', 'LimitAmountLeft',
        'ValidThru', 'Amount', 'Currency', 'LastPayTime', 'NextPayTime',
        'RecurrentPeriod', 'MAC'
    ]
    _mac_fields = [
        'Success', 'RcStatus', 'ErrCode', 'ErrMessage', 'OrderId',
        'LimitCntLeft', 'LimitAmountLeft', 'ValidThru', 'Amount', 'Currency',
        'LastPayTime', 'NextPayTime', 'RecurrentPeriod'
    ]
