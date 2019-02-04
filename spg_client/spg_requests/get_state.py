# -*- coding: utf-8 -*-
from spg_client.responses import GetstateResponse
from spg_client.spg_requests.base import BaseRequest


class GetState(BaseRequest):
    response_class = GetstateResponse
    method = 'POST'
    path = '/getstate'
    _mac_fields = ['ServiceId', 'OrderId']
    _mac_val_or_ignore_fields = []

    def __init__(self, order_id):
        """
        Получение статуса платежа
        Args:
            OrderId (str): Уникальный идентификатор транзакции в системе
                Партнера cтрока, 6-19 цифр
        """
        self.order_id = order_id

    def _params(self):
        return {'OrderId': self.order_id}
