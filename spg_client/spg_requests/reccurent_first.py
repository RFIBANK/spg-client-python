# -*- coding: utf-8 -*-
from spg_client.spg_requests import BasePay


class RecurrentFirst(BasePay):  # рекуррентный одностадийный платеж
    pay_type = 'recurrentrequest'

    def __init__(self, card, order_id, amount, description,
                 recurrent_type='first', recurrent_period='byrequest',
                 email=None, phone=None, currency='RUB', channel=None):
        """
        doc
        """
        self.card = card
        self.order_id = order_id
        self.amount = amount
        self.currency = currency
        self.description = description
        self.recurrent_type = recurrent_type
        self.recurrent_period = recurrent_period
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
