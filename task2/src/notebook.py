from task2.src.note import Note


class Notebook:
    def __init__(self):
        self.__notes = list()

    def __add__(self, note: Note):
        if not isinstance(note, Note):
            raise TypeError(f'note cannot have {type(note)} type')
        if not note.filled():
            raise ValueError(f'note should be filled')
        if not all(old_note != note for old_note in self.__notes):
            raise ValueError(f'note {str(note)} already exists')
        self.__notes.append(note)
        return self

    def __mul__(self, key: Note):
        return self.__find(key)

    def __sub__(self, key: Note):
        found = self.__find(key)
        for entry in found:
            self.__notes.remove(entry)

    def __find(self, key: Note):
        found = self.__notes
        for argument_name in key.__dict__:
            found = self.__filter(found, key, argument_name)

        return found

    @staticmethod
    def __filter(notes: list, key: Note, argument_name: str):
        key_argument = key.__dict__[argument_name]
        if key_argument is None:
            return notes

        return list(filter(
            lambda entry: entry.__dict__[argument_name] == key_argument,
            notes
        ))

