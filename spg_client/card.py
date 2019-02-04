from utils import is_pan_valid


class Card:
    """
    PAN (int): Номер карты Visa или MasterCard. 12-19 цифр без пробелов

    month (int): Месяц истечения срока действия карты. 2 цифры с лидирующим 0

    year (int): Год истечения срока действия карты 2 цифры 2 цифры, последние
    цифры года с лидирующим нулём

    CardHolder (str): Владелец карты (с лицевой стороны карты) строка,
    максимум 30 символов [a-Z.,-]

    SecureCode (str): CVC2/CVV2 3 цифры

    CVC2ReasonCode (int): Константа "1", 1 цифра
    """

    def __init__(self, pan, month, year, card_holder, secure_code,
                 cvc2reason_code=1):
        self._pan = pan
        self.month = month
        self.year = year
        self.card_holder = card_holder
        self.secure_code = secure_code
        self.cvc2reason_code = cvc2reason_code

    @property
    def pan(self):
        return self._pan

    # для проверки корректности PAN
    @pan.setter
    def pan(self, val):
        is_pan_valid(val)
        self._pan = val
