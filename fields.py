from abc import ABC, abstractmethod
from validators import TextValidator, IntegerValidator


class AbstractField(ABC):
    @abstractmethod
    def __init__(self, validators=None):
        pass

    @abstractmethod
    def is_valid(self, value):
        pass


class CharField(AbstractField):
    def __init__(self, validators=None):
        self.default_validator = [TextValidator(0, 999)]
        self.all_validators = self.default_validator
        if isinstance(validators, list) and validators:
            self.all_validators += validators
        super().__init__()

    def is_valid(self, value):
        return all(TextValidator.is_valid(value) for TextValidator in self.all_validators)


class TextField(AbstractField):
    def __init__(self, validators=None):
        self.default_validator = [TextValidator(1001, 3000)]
        self.all_validators = self.default_validator
        if isinstance(validators, list) and validators:
            self.all_validators += validators
        super().__init__()

    def is_valid(self, value):
        return all(TextValidator.is_valid(value) for TextValidator in self.all_validators)


class IntegerField(AbstractField):
    def __init__(self, validators=None):
        self.default_validator = [IntegerValidator(128, 1024)]
        self.all_validators = self.default_validator
        if isinstance(validators, list) and validators:
            self.all_validators += validators
        super().__init__()

    def is_valid(self, value):
        return all(IntegerValidator.is_valid(value) for IntegerValidator in self.all_validators)