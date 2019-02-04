# -*- coding: utf-8 -*-
from spg_client.spg_requests import BaseRequest
from spg_client.responses import PayResponse


class PayToken(BaseRequest):
    response_class = PayResponse
    method = 'POST'
    path = '/paytoken'
    pay_token_type = 'payment'

    _mac_fields = [
        'ServiceId', 'Type', 'CardToken', 'PaymentToToken', 'OrderId',
        'Amount', 'Currency', 'Channel', 'EMail', 'Phone', 'Description',
        'CustomFields', 'RecurrentType', 'RecurrentPeriod'
    ]
    _mac_val_or_ignore_fields = []

    def __init__(self, card_token, order_id, amount, description,
                 payment_to_token=None, email=None, phone=None, currency='RUB',
                 channel=None):
        """
        Одностадийное проведение платежа. Обычный платеж.
        Args:
            card (namedtuple): Card
            order_id: Уникальный идентификатор транзакции в системе
                Партнера cтрока, 6-19 цифр
            amount (int): сумма к оплате. 1-14 цифр, может содержать
                десятичный разделитель в виде точки
            currency (str): Валюта в формате ISO (USD, EUR, RUB).
                3 буквы (a-zA-Z)
            channel (str): Код канала (банка), по которому предпочтительно
                проводить транзакцию. Cтрока, 2-20 символов
                ('short_name' из таблицы gate)
            email (str): Email покупателя, обязательно для рекуррентных
                платежей. Этот email не должен передаваться в банк, это email
                для информирования Покупателя - сохраняется в транзакции.
                Cтрока, 5-80 символов
            phone (str): В МН формате +7 999 123 12 12 (без пробелов).
                до 20 цифр, впереди ‘+’
            description (str): Описание транзакции. Cтрока, 1-50 символов,
                латиница.
        """
        self.card_token = card_token
        self.amount = amount
        self.currency = currency
        self.order_id = order_id
        self.description = description
        self.payment_type = self.pay_token_type
        self.recurrent_type = None
        self.recurrent_period = None
        self.custom_fields = None
        self.channel = channel
        self.email = email
        self.phone = phone
        self.payment_to_token = payment_to_token

    def _params(self):
        return {
            'CardToken': self.card_token,
            'OrderId': self.order_id,
            'Amount': self.amount,
            'Currency': self.currency,
            'Channel': self.channel,
            'EMail': self.email,
            'Phone': self.phone,
            'Description': self.description,
            'CustomFields': self.custom_fields,
            'Type': self.payment_type,
            'PaymentToToken': self.payment_to_token,
            'RecurrentType': self.recurrent_type,
            'RecurrentPeriod': self.recurrent_period,
        }
