# -*- coding: utf-8 -*-
from spg_client.responses import ServicePanOneTimeTokenResponse
from spg_client.spg_requests import BaseRequest


class ServicePanOneTimeToken(BaseRequest):
    response_class = ServicePanOneTimeTokenResponse
    method = 'POST'
    path = '/servicepan_onetimetoken'

    _mac_fields = ['ServiceId', 'PAN', 'EMonth', 'EYear', 'SecureCode',
                   'CardHolder', 'CustomFields']
    _mac_val_or_ignore_fields = []

    def __init__(self, card, custom_fields=None):
        """ Создание одноразового токена для данных карты
        card (Card obj): обьект класса Card

        CustomFields (dict): Опционально. дополнительные поля транзакции
        """
        self.card = card
        self.custom_fields = custom_fields

    def _params(self):
        return {'PAN': self.card.pan,
                'EMonth': self.card.month,
                'EYear': self.card.year,
                'CardHolder': self.card.card_holder,
                'SecureCode': self.card.secure_code,
                'CustomFields': self.custom_fields}
