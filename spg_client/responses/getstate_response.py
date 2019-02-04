# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class GetstateResponse(BaseResponse):
    _fields = [
        'Success', 'OrderId', 'Operation', 'Amount', 'Currency', 'GateAmount',
        'GateCurrency', 'Status', 'StatusType', 'RRN', 'Auth', 'MAC'
    ]
    _mac_fields = [
        'Success', 'OrderId', 'Operation', 'Amount', 'Currency', 'GateAmount',
        'GateCurrency', 'Status', 'StatusType', 'ErrCode', 'ErrMessage',
    ]
