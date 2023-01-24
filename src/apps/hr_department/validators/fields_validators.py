from apps.hr_department.validators.base import BaseValidatorForFields


class INNValidator(BaseValidatorForFields):
    def __init__(self, message=None):
        super().__init__(['inn'], self.is_inn, 'inn is not valid')

    @staticmethod
    def is_inn(inn: str):
        if len(inn) != 10:
            return False
        if not inn.isdigit():
            return False
        return True


class SNILSValidator(BaseValidatorForFields):
    def __init__(self, message=None):
        super().__init__(['snils'], self.is_snils, 'snils is not valid')

    @staticmethod
    def is_snils(snils: str):
        if len(snils) != 11:
            return False
        if not snils.isdigit():
            return False
        return True


class PassportValidator(BaseValidatorForFields):
    def __init__(self, message=None):
        super().__init__(['passport'], self.is_passport, 'passport is not valid')

    @staticmethod
    def is_passport(passport: str):
        if len(passport) != 10:
            return False
        if not passport.isdigit():
            return False
        return True
