# -*- coding: utf-8 -*-
from spg_client.responses import UnblockResponse
from spg_client.spg_requests import BaseRequest


class Unblock(BaseRequest):
    response_class = UnblockResponse
    method = 'POST'
    path = '/unblock'

    _mac_fields = ['ServiceId', 'OrderId', 'Amount']
    _mac_val_or_ignore_fields = []

    def __init__(self, order_id, amount):
        """ Изменение суммы заблокированных средств
        OrderId (str): Уникальный идентификатор транзакции в системе Партнера
        cтрока, 6-19 цифр

        Amount (str): Cумма, которую следует разблокировать (В текущей версии
        протокола операция может быть выполнена только один раз)
        """
        self.order_id = order_id
        self.amount = amount

    def _params(self):
        return {'OrderId': self.order_id,
                'Amount': self.amount}
