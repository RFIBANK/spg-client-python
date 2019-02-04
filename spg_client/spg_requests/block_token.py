# -*- coding: utf-8 -*-
from spg_client.spg_requests import BaseRequest
from spg_client.responses import BlockResponse


class BlockToken(BaseRequest):
    response_class = BlockResponse
    method = 'POST'
    path = '/blocktoken'

    _mac_fields = [
        'ServiceId', 'CardToken', 'OrderId', 'Amount', 'Currency', 'Channel',
        'EMail', 'Phone', 'Description', 'CustomFields', 'Type',
        'RecurrentType', 'RecurrentPeriod'
    ]
    _mac_val_or_ignore_fields = ['Type', 'RecurrentType', 'RecurrentPeriod']

    def __init__(self, card_token, order_id, amount, description,
                 payment_type=None, recurrent_type=None, recurrent_period=None,
                 custom_fields=None, email=None, phone=None, currency='RUB',
                 channel=None):

        """
        Блокировка средств с токеном карты
        Args:
            CardToken (str): Одноразовый токен данных карты
            OrderId (): Уникальный идентификатор транзакции в системе
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
            custom_fields (str): Дополнительные поля транзакции
                Строка 1000 символов
            payment_typle (str): Тип операции платежа.
                Зарезервированные слова:
                “payment” - обычный платеж
                “recurrentrequest” - рекуррентый платеж, первый или
                последующие.

            recurrent_type (str): Тип рекуррентной операции.
                Зарезервированные слова или пусто
                (пусто - не рекуррент, first - первая транзакция).

            recurrent_period (str): Период рекуррентной операции
                Зарезервированные слова: byrequest.

        """
        self.card_token = card_token
        self.amount = amount
        self.currency = currency
        self.order_id = order_id
        self.description = description
        self.payment_type = payment_type
        self.recurrent_type = recurrent_type
        self.recurrent_period = recurrent_period
        self.custom_fields = custom_fields
        self.channel = channel
        self.email = email
        self.phone = phone

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
            'RecurrentType': self.recurrent_type,
            'RecurrentPeriod': self.recurrent_period,
        }
