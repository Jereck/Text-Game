class GameUnitError(Exception):
    """The custom error class"""
    def __init__(self, message="", code=000):
        super().__init__(message)
        self.error_message = '~'*50 + '\n'
        self.error_dict = {
            000: "Error-000: Unexpected Error",
            101: "Error-101: Health Meter Error",
            102: "Error-102: Attack Error. Ignored",
        }

        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~'*50
