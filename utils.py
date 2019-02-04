# -*- coding: utf-8 -*-
import hmac
import hashlib
import sys

from xml.etree import ElementTree as ET

from exceptions import InvalidMacError


def parse_xml(string_content):
    return ET.fromstring(string_content)


def calculate_mac(secret_key, *items):
    def mac_part(item):
        if item is None:
            return '-'
        else:
            string = str(item)
            return "{0}{1}".format(len(string), string)
    mac = hmac.new(
        secret_key.encode(),
        msg="".join(mac_part(i) for i in items).encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    if sys.version_info > (3,):
        return mac.hex()
    else:
        return mac.encode('hex')


def check_mac_equivalence(spg, calculated):

    if spg != calculated:
        raise InvalidMacError(spg)


def is_pan_valid(pan):
    """
    Проверка PAN по алгоритму mod 10
    :param pan: str
    :returns: bool
    """
    digits_input = reversed([int(digit) for digit in str(pan)])
    digits_output = []
    for index, digit in enumerate(digits_input, start=1):
        if index % 2 == 0:  # check if even четный
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        digits_output.append(digit)
    return sum(digits_output) % 10 == 0


def check_pan(pan):
    """
    Проверка PAN по алгоритму mod 10
    :param pan: str
    :returns: bool
    """
    digits_input = reversed([int(digit) for digit in str(pan)])
    digits_output = []
    for index, digit in enumerate(digits_input, start=1):
        if index % 2 == 0:  # check if even четный
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        digits_output.append(digit)
    return sum(digits_output) % 10 == 0
