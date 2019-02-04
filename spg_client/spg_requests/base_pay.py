# -*- coding: utf-8 -*-

from spg_client.responses import PayResponse
from .base import BaseRequest


class BasePay(BaseRequest):  # одностадийный платеж
    """
    Базовый класс, для одностадийных платежей
    Типы одностадийних платежей(наследуются от этого класса):
        1) “payment” - обычный платеж
        2) “recurrentrequest” - рекуррентый платеж, первый или последующие
        (для сервисов с is_recurrent_available=1)
        3) “payservice” - оплата услуг (используются доп параметры из
        CustomFields)
        4) “transfer” - перевод с карты на карту (требуется PaymentTo)
    """
    response_class = PayResponse
    method = 'POST'
    path = '/pay'
    pay_type: str

    _mac_fields = [
        'ServiceId', 'Type', 'PAN', 'EMonth', 'EYear', 'CardHolder',
        'SecureCode', 'CVC2ReasonCode', 'OrderId', 'Amount', 'Currency',
        'Channel', 'EMail', 'Phone', 'Description', 'CustomFields',
        'RecurrentType', 'RecurrentPeriod', 'PaymentTo', 'AsyncWaitingUrl'
    ]

    # список полей при отсутствии значений которых '-' в МАС не ставится
    _mac_val_or_ignore_fields = ['PaymentTo', 'AsyncWaitingUrl']

    def _params(self):
        pass
