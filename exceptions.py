# -*- coding: utf-8 -*-


class SpgError(Exception):

    def __init__(self, msg):
        super(SpgError, self).__init__(
            "Unsuccessful request to Partner API.\n{}".format(msg)
        )


class InvalidPanError(SpgError):

    def __init__(self, msg):
        super(SpgError, self).__init__(
            "Invalid PAN.\n{}".format(msg)
        )


class InvalidMacError(SpgError):

    def __init__(self, msg):
        super(SpgError, self).__init__(
            "Invalid MAC.\n{}".format(msg)
        )


class ConnectionError(SpgError):

    def __init__(self, msg, cause):
        super(SpgError, self).__init__(msg + u', caused by ' + repr(cause))


class NotFoundError(SpgError):

    def __init__(self, message):
        super(SpgError, self).__init__(
             'Not Found.\n{}'.format(message)
        )


class InvalidResponseError(SpgError):

    def __init__(self, msg):
        super(SpgError, self).__init__(msg)


class BadRequestError(SpgError):

    def __init__(self, msg):
        super(SpgError, self).__init__(
            "Bad request to Partner API.\n{}".format(msg)
        )


class ServerError(SpgError):

    def __init__(self, msg):
        super(SpgError, self).__init__(
            "Partner API returned 500 Server Error.\n{}".format(msg)
        )
