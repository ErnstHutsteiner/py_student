from errors import errors

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class Freezererror(Error):
    def __init__(self, error_code):
        self.error_code = error_code
        self.message = errors[error_code]

class Validationerror(Error):
    def __init__(self, error_code):
        self.error_code = error_code
        self.message = "ungülitige Werteingabe"

