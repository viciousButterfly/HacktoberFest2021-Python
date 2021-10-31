#!/usr/bin/python

class CharDistance(str):
    _keyboard_array = [
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\''],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
        ['', '', ' ', ' ', ' ', ' ', ' ', '', '']
    ]

    _shift_keyboard_array = [
        ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
        ['', '', ' ', ' ', ' ', ' ', ' ', '', '']
    ]

    def __or__(self, a):
        """Used to cast a string to CharDistance()"""
        return CharDistance(a)

    def __and__(self, b):
        try:
            return CharDistance(self).get(self, b)
        except Exception: # noqa
            return 1

    def array_from_char(self, c):
        if True in [c in r for r in self._keyboard_array]:
            return self._keyboard_array
        elif True in [c in r for r in self._shift_keyboard_array]:
            return self._shift_keyboard_array
        else:
            raise ValueError(c + " not found in any keyboard layouts")

    @staticmethod
    def get_char_coord(c, array):
        for r in array:
            if c in r:
                row = array.index(r)
                column = r.index(c)
                return row, column
        raise ValueError(c + " not found in given keyboard layout")

    def get(self, c1, c2):
        """Returns the euclidean distance between two characters"""
        coord1 = self.get_char_coord(c1, self.array_from_char(c1))
        coord2 = self.get_char_coord(c2, self.array_from_char(c2))
        return ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2) ** 0.5


def test(a, b):
    print((CharDistance() | a) & b)
    print(CharDistance(a) & b)


if __name__ == '__main__':
    test('a', 'b')
