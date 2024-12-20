from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class IsItAPhoneNumber:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "The name must be only digit and can start with +"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        for i in range(len(value)):
            if i == 0 and value[i] == '+':
                continue
            if not value[i].isdigit():
                raise ValidationError(self.message)