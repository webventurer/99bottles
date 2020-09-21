import inspect
import unittest

import bottles


class BottleNumberTest(unittest.TestCase):
    def test_returns_correct_class_for_given_number(self):
        self.assertEqual(
            type(bottles.BottleNumber.from_number(0)), bottles.BottleNumber0,
        )
        self.assertEqual(
            type(bottles.BottleNumber.from_number(1)), bottles.BottleNumber1,
        )
        self.assertEqual(
            type(bottles.BottleNumber.from_number(6)), bottles.BottleNumber6,
        )
        self.assertEqual(
            type(bottles.BottleNumber.from_number(2)), bottles.BottleNumber,
        )


class BottleVerseTest(unittest.TestCase):
    def test_common_rule_upper_bound(self):
        expected = (
            "99 bottles of beer on the wall, "
            + "99 bottles of beer.\n"
            + "Take one down and pass it around, "
            + "98 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, bottles.BottleVerse.from_number(99))

    def test_common_rule_lower_bound(self):
        expected = (
            "3 bottles of beer on the wall, "
            + "3 bottles of beer.\n"
            + "Take one down and pass it around, "
            + "2 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, bottles.BottleVerse.from_number(3))

    def test_verse_7(self):
        expected = (
            "7 bottles of beer on the wall, "
            + "7 bottles of beer.\n"
            + "Take one down and pass it around, "
            + "1 six-pack of beer on the wall.\n"
        )
        self.assertEqual(expected, bottles.BottleVerse.from_number(7))

    def test_verse_6(self):
        expected = (
            "1 six-pack of beer on the wall, "
            + "1 six-pack of beer.\n"
            + "Take one down and pass it around, "
            + "5 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, bottles.BottleVerse.from_number(6))

    def test_verse_2(self):
        expected = (
            "2 bottles of beer on the wall, "
            + "2 bottles of beer.\n"
            + "Take one down and pass it around, "
            + "1 bottle of beer on the wall.\n"
        )
        self.assertEqual(expected, bottles.BottleVerse.from_number(2))

    def test_verse_1(self):
        expected = (
            "1 bottle of beer on the wall, "
            + "1 bottle of beer.\n"
            + "Take it down and pass it around, "
            + "no more bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, bottles.BottleVerse.from_number(1))

    def test_verse_0(self):
        expected = (
            "No more bottles of beer on the wall, "
            + "no more bottles of beer.\n"
            + "Go to the store and buy some more, "
            + "99 bottles of beer on the wall.\n"
        )
        self.assertEqual(expected, bottles.BottleVerse.from_number(0))


class VerseFake:
    @classmethod
    def from_number(cls, number):
        return f"This is verse {number}. \n"


class CountdownSongTest(unittest.TestCase):
    def test_verse(self):
        expected = "This is verse 500. \n"
        self.assertEqual(expected, bottles.CountdownSong(VerseFake).verse(500))

    def test_verses(self):
        expected = (
            "This is verse 99. \n"
            + "\n"
            + "This is verse 98. \n"
        )
        self.assertEqual(
            expected,
            bottles.CountdownSong(VerseFake).verses(99, 98))

    def test_song(self):
        expected = (
            "This is verse 47. \n"
            + "\n"
            + "This is verse 46. \n"
            + "\n"
            + "This is verse 45. \n"
        )
        self.assertEqual(
            expected, bottles.CountdownSong(VerseFake, 47, 45).song(),
        )


if __name__ == "__main__":
    unittest.main()
