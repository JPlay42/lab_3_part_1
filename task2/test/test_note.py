import unittest
from datetime import datetime

from task2.src.note import Note


class NoteTest(unittest.TestCase):

    def test_part(self):
        self.assertEqual(Note.part(),
                         Note(None, None, None, None))

        self.assertEqual(Note.part(name='Nick'),
                         Note('Nick', None, None, None))

        self.assertEqual(Note.part(surname='Pylypchuk'),
                         Note(None, 'Pylypchuk', None, None))

        self.assertEqual(Note.part('Nick', 'Pylypchuk'),
                         Note('Nick', 'Pylypchuk', None, None))

        self.assertEqual(Note.part(phone='380987654321'),
                         Note(None, None, '380987654321', None))

        self.assertEqual(Note.part(birthdate=datetime(2000, 1, 1)),
                         Note(None, None, None, datetime(2000, 1, 1)))

    def test_filled(self):
        self.assertFalse(Note.part().filled())
        self.assertFalse(self._default_note(name=None).filled())
        self.assertFalse(self._default_note(surname=None).filled())
        self.assertFalse(self._default_note(phone=None).filled())
        self.assertFalse(self._default_note(birthdate=None).filled())
        self.assertTrue(self._default_note().filled())

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            self._default_note(name=123)
        with self.assertRaises(ValueError):
            self._default_note(name='')

    def test_surname_validation(self):
        with self.assertRaises(TypeError):
            self._default_note(surname=123)
        with self.assertRaises(ValueError):
            self._default_note(surname='')

    def test_phone_validation(self):
        with self.assertRaises(TypeError):
            self._default_note(phone=12345)
        with self.assertRaises(ValueError):
            self._default_note(phone='definitely not number123')

    def test_birthdate_validation(self):
        with self.assertRaises(TypeError):
            self._default_note(birthdate='not a date')

    @staticmethod
    def _default_note(name: str | None = 'Nick',
                      surname: str | None = 'Pylypchuk',
                      phone: str | None = '380987654321',
                      birthdate: datetime | None = datetime(2000, 1, 1)):
        return Note(name, surname, phone, birthdate)


if __name__ == '__main__':
    unittest.main()
