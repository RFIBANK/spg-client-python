# -*- coding: utf-8 -*-
from spg_client.spg_requests import BasePay


# одностадийный платеж - 'payment' - обычный платеж
class Pay(BasePay):
    pay_type = 'payment'

    def __init__(self, card, order_id, amount, description, email=None,
                 phone=None, currency='RUB', channel=None):
        """
        Одностадийное проведение платежа. Обычный платеж.
        Args:
            card (namedtuple): Card

            order_id : Уникальный идентификатор транзакции в системе
            Партнера cтрока, 6-19 цифр

            amount (int): сумма к оплате. 1-14 цифр, может содержать десятичный
            разделитель в виде точки

            currency (str): Валюта в формате ISO (USD, EUR, RUB).
            3 буквы (a-zA-Z)

            channel (str): Код канала (банка), по которому предпочтительно
            проводить транзакцию. Cтрока, 2-20 символов ('short_name' из
            таблицы gate)

            email (str): Email покупателя, обязательно для рекуррентных
            платежей. Этот email не должен передаваться в банк, это email
            для информирования Покупателя - сохраняется в транзакции.
            Cтрока, 5-80 символов

            phone (str): В МН формате +7 999 123 12 12 (без пробелов).
            до 20 цифр, впереди ‘+’

            description (str): Описание транзакции. Cтрока, 1-50 символов,
                латиница.
        """
        self.card = card
        self.order_id = order_id
        self.amount = amount
        self.currency = currency
        self.description = description
        self.recurrent_type = None
        self.recurrent_period = None
        self.custom_fields = None
        self.channel = channel
        self.email = email
        self.phone = phone

    def _params(self):
        return {
            # значения карты
            'PAN': self.card.pan,
            'EMonth': self.card.month,
            'EYear': self.card.year,
            'CardHolder': self.card.card_holder,
            'SecureCode': self.card.secure_code,
            'CVC2ReasonCode': self.card.cvc2reason_code,
            # остальные параметры
            'OrderId': self.order_id,
            'Amount': self.amount,
            'Currency': self.currency,
            'Channel': self.channel,
            'EMail': self.email,
            'Phone': self.phone,
            'Description': self.description,
            'CustomFields': self.custom_fields,
            'Type': self.pay_type,
            'RecurrentType': self.recurrent_type,
            'RecurrentPeriod': self.recurrent_period,
        }
