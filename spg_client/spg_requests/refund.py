# -*- coding: utf-8 -*-
from spg_client.responses import RefundResponse
from spg_client.spg_requests.base import BaseRequest


class Refund(BaseRequest):
    response_class = RefundResponse
    method = 'POST'
    path = '/refund'

    _mac_fields = ['ServiceId', 'OrderId', 'Amount', 'ExtOperationId']
    _mac_val_or_ignore_fields = ['ExtOperationId']

    def __init__(self, order_id, amount, ext_operation_id=None):
        """ Возврат средств
        OrderId (str): Уникальный идентификатор транзакции в системе
        Партнера. cтрока, 6-19 цифр

        Amount (str): сумма, которую следует вернуть. 1-14 цифр, может
        содержать десятичный разделитель в виде точки.

        ExtOperationId (str): ID операции
        """
        self.order_id = order_id
        self.amount = amount
        self.ext_operation_id = ext_operation_id

    def _params(self):
        return {'OrderId': self.order_id,
                'Amount': self.amount,
                'ExtOperationId': self.ext_operation_id}
