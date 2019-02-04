# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class PayResponse(BaseResponse):
    _fields = [
        'Success', 'OrderId', 'Operation', 'Amount', 'Currency', 'Status',
        'GateAmount', 'GateCurrency', 'IsAsync', 'StatusType', 'RRN', 'Auth',
        'MAC'
    ]
    _mac_fields = [
        'Success', 'OrderId', 'Operation', 'Amount', 'Currency', 'GateAmount',
        'GateCurrency', 'IsAsync', 'Status', 'StatusType', 'ErrCode',
        'ErrMessage'
    ]
