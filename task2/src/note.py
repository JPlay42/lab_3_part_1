from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    name: str | None
    surname: str | None
    phone: str | None
    birthdate: datetime | None

    @staticmethod
    def part(name: str | None = None,
             surname: str | None = None,
             phone: str | None = None,
             birthdate: datetime | None = None):
        return Note(name, surname, phone, birthdate)

    def __post_init__(self):
        self.__check_str_field(self.name, 'name')
        self.__check_str_field(self.surname, 'surname')

        self.__check_str_field(self.phone, 'phone number')
        if self.phone is not None and not self.phone.isdigit():
            raise ValueError('phone number can contain only digits')

        if self.birthdate is not None and not isinstance(self.birthdate, datetime):
            raise TypeError(f'birthdate cannot have {type(self.birthdate)} type')

    def filled(self) -> bool:
        return self.name is not None and \
               self.surname is not None and \
               self.phone is not None and \
               self.birthdate is not None

    @staticmethod
    def __check_str_field(field, name: str) -> None:
        if field is not None and not isinstance(field, str):
            raise TypeError(f'{name} cannot have {type(field)} type')
        if field == '':
            raise ValueError(f'{name} cannot be empty')
