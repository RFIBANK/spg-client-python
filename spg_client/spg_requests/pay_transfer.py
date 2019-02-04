# -*- coding: utf-8 -*-
from spg_client.spg_requests import BasePay


class PayTransfer(BasePay):  # одностадийный платеж - 'transfer'
    pay_type = 'transfer'

    def __init__(self, card, payment_to, order_id, amount, description,
                 async_waiting_url=None, email=None, phone=None, currency='RUB',
                 channel=None):
        """
        doc
        """
        self.card = card
        self.payment_to = payment_to
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
        self.payment_to = None
        self.async_waiting_url = async_waiting_url

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
            'PaymentTo': self.payment_to,
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
