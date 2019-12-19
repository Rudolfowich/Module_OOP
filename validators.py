from abc import ABC, abstractmethod


class AbstractValidator(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def is_valid(self, value):
        pass


class TextValidator(AbstractValidator):
    def __init__(self, min_length = 16, max_length = 256):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__()

    def is_valid(self, value):
        super().is_valid(value)
        if self.min_length <= len(value) <= self.max_length:
            return True
        else:
            return False


class IntegerValidator(AbstractValidator):
    def __init__(self, min_value=32, max_value=1024):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__()

    def is_valid(self, value):
        super().is_valid(value)
        if self.min_value <= value <= self.max_value:
            return True
        else:
            return False


