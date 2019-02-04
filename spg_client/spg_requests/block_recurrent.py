# -*- coding: utf-8 -*-
from spg_client.responses import BlockResponse
from spg_client.spg_requests.base import BaseRequest


class BlockRecurrentFirst(BaseRequest):
    response_class = BlockResponse
    method = 'POST'
    path = '/block'
    _mac_fields = [
        'ServiceId', 'PAN', 'EMonth', 'EYear', 'CardHolder', 'SecureCode',
        'CVC2ReasonCode', 'OrderId', 'Amount', 'Currency', 'Channel',
        'EMail', 'Phone', 'Description', 'CustomFields', 'Type',
        'RecurrentType', 'RecurrentPeriod'
    ]

    _mac_val_or_ignore_fields = ['Type', 'RecurrentType', 'RecurrentPeriod']

    def __init__(self, card, order_id, amount, description,
                 payment_type='recurrentrequest', recurrent_type='first',
                 recurrent_period='byrequest', custom_fields=None, email=None,
                 phone=None, currency='RUB', channel=None):
        """
        Args:
            card(namedtuple): Card
            order_id (str): Уникальный идентификатор транзакции в системе
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
            custom_fields (str): dict
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
        self.card = card
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
            # данные карты
            'PAN': self.card.pan,
            'EMonth': self.card.month,
            'EYear': self.card.year,
            'CardHolder': self.card.card_holder,
            'SecureCode': self.card.secure_code,
            'CVC2ReasonCode': self.card.cvc2reason_code,
            # данные остальные
            'Amount': self.amount,
            'Currency': self.currency,
            'OrderId': self.order_id,
            'Description': self.description,
            'Type': self.payment_type,
            'Channel': self.channel,
            'EMail': self.email,
            'Phone': self.phone,
            'CustomFields': self.custom_fields,
            'RecurrentType': self.recurrent_type,
            'RecurrentPeriod': self.recurrent_period,
        }
