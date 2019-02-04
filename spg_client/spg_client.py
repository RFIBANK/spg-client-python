# -*- coding: utf-8 -*-
# TODO python2 compatible
import copy
import requests

from requests import exceptions as requests_exceptions

import exceptions
from utils import parse_xml, calculate_mac, check_mac_equivalence


class SpgClient:
    read_timeout = 35
    connect_timeout = 38

    def __init__(self, service_id, secret, base_url):
        """
        Args:
            service_id (str): идентификатор сервиса
            secret (str): секретный ключ сервиса
        """
        self.service_id = service_id
        self.secret = secret
        self.base_url = base_url

    def perform(self, request):
        url = self.base_url + request.path

        params = copy.deepcopy(request.params)
        params['ServiceId'] = self.service_id
        request_mac = calculate_mac(
            self.secret, *[params.get(f) for f in request.mac_fields])
        params['MAC'] = request_mac

        try:
            response = requests.request(
                request.method,
                url,
                data=params,
                timeout=(self.connect_timeout, self.read_timeout)
            )
        except requests_exceptions.RequestException as exc:
            msg = "Connection with url {} refused.".format(self.base_url)
            raise exceptions.ConnectionError(msg, exc)

        return self.check_response(response, request)

    def check_response(self, response, request):
        xml_root = parse_xml(response.content)
        response = request.response_class(xml_root)

        calculated_mac = calculate_mac(
            self.secret, *[None if not hasattr(response, field) or
                           getattr(response, field) == ''
                           else getattr(response, field)
                           for field in response.mac_fields]
        )
        check_mac_equivalence(response.MAC, calculated_mac)
        return response
