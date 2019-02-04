# -*- coding: utf-8 -*-
import abc

from utils import is_pan_valid


class BaseRequest:
    _mac_fields: list
    _mac_val_or_ignore_fields: list

    @property
    def mac_fields(self):
        mac_fields = list(self._mac_fields)
        for field in self._mac_val_or_ignore_fields:
            if self.params.get(field, None) is None:
                mac_fields.remove(field)
        return mac_fields

    @abc.abstractmethod
    def _params(self):
        pass

    @property
    def params(self):
        params = self._params()
        # тут можно сделать проверку на корректность необходимых параметров
        if params.get('PaymentTo', None):
            is_pan_valid(params['PaymentTo'])
        return params
