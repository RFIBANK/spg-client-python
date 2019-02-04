# -*- coding: utf-8 -*-
import exceptions

FIELDS_3DS_RESPONSE = ['ACSUrl', 'PaReq', 'ThreeDSKey']


class BaseResponse(object):
    # включается в MAC только при наличии, при отсутствии "-" в MAC не
    # ставится
    _mac_ignore_fields = ['CustomForm']
    _fields: list

    def __init__(self, root):
        if root.find('ErrMessage') is not None:
            raise exceptions.InvalidResponseError('{}\n ErrCode: {}'.format(
                root.find('ErrMessage').text, root.find('ErrCode').text
                )
            )
        # block, pay
        if root.find('Success').text == '3DS':
            self._fields += FIELDS_3DS_RESPONSE

        # TODO
        if root.find('Success').text == '3DSCustomForm':
            pass

        for field in self._fields:
            if root.find(field) is not None:
                value = root.find(field).text
            else:
                value = None
            setattr(self, field, value)

    # TEST
    @property
    def mac_fields(self):

        if getattr(self, 'Success') == '3DS':
            self._mac_fields += FIELDS_3DS_RESPONSE
            self._fields += FIELDS_3DS_RESPONSE

        mac_fields = list(self._mac_fields)

        for field in self._mac_ignore_fields:
            if hasattr(self, field) and getattr(self, field) is None:
                mac_fields.remove(field)

        return mac_fields
