# -*- coding: utf-8 -*-
from spg_client.spg_requests import BaseRequest
from spg_client.responses.recpaymake_response import RecPayMakeResponse


class RecPayMake(BaseRequest):
    response_class = RecPayMakeResponse
    method = 'POST'
    path = '/recpaymake'
    _mac_fields = ['ServiceId', 'OrderId', 'PaymentId', 'Amount', 'Desс']

    def __init__(self, order_id, payment_id, amount, desc=None):
        """
         Изменение суммы заблокированных средств
        Args:
            order_id (str): уникальный идентификатор транзакции в
                системе Партнера
            payment_id (str): Уникальный идентификатор списания. Используется
                как order_id для рекурентной операции.
            amount (str): Сумма к оплате.

            desc (str): ОПЦИОНАЛЬНО - Описание рекуррентного платежа.
        """
        self.order_id = order_id
        self.payment_id = payment_id
        self.amount = amount
        self.desc = desc

    def _params(self):
        return {'OrderId': self.order_id,
                'PaymentId': self.payment_id,
                'Amount': self.amount,
                'Desс': self.desc}
