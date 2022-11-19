import unittest

from task2.src.note import Note
from task2.src.notebook import Notebook
from task2.test.test_note import NoteTest


class NotebookTest(unittest.TestCase):
    def test_add(self):
        notebook = Notebook()
        notebook + NoteTest._default_note(surname='A')
        notebook = notebook + NoteTest._default_note(surname='B')
        with self.assertRaises(TypeError):
            notebook + 'Not a note'
        with self.assertRaises(ValueError):
            notebook + Note.part(surname='Smit')
        with self.assertRaises(ValueError):
            notebook + NoteTest._default_note(surname='B')

    def test_find(self):
        notebook = self.__default_notebook()
        notes = notebook * Note.part(surname='Smit')

        self.assertEqual(2, len(notes))
        self.assertEqual(notes[0], NoteTest._default_note('John', 'Smit'))
        self.assertEqual(notes[1], NoteTest._default_note('Will', 'Smit'))

    def test_delete(self):
        notebook = self.__default_notebook()
        key = Note.part(surname='Smit')

        found = notebook * key
        self.assertEqual(2, len(found))

        notebook - key
        found = notebook * key
        self.assertEqual(0, len(found))

    @staticmethod
    def __default_notebook():
        notebook = Notebook()
        notebook + NoteTest._default_note('John', 'Smit')
        notebook + NoteTest._default_note('John', 'Cena')
        notebook + NoteTest._default_note('Will', 'Smit')
        return notebook


if __name__ == '__main__':
    unittest.main()
