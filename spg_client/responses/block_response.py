# -*- coding: utf-8 -*-
from .base_response import BaseResponse


class BlockResponse(BaseResponse):
    _fields = [
        'Success', 'OrderId', 'Operation', 'Amount', 'Currency', 'GateAmount',
        'GateCurrency', 'IsAsync', 'Status', 'StatusType', 'MAC'
    ]
    # pay, paytoken, payapple, block, blocktoken, blockapple, ack3ds
    _mac_fields = [
        'Success', 'OrderId', 'Operation', 'Amount', 'Currency', 'GateAmount',
        'GateCurrency', 'IsAsync', 'Status', 'StatusType', 'ErrCode',
        'ErrMessage'
    ]
