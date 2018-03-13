import unittest
import os
import wordcounter


class TestCounter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_file = 'temp_file.txt'

    def setUp(self):
        pass
        # self.temp_file = 'temp_file.txt'

    def tearDown(self):
        os.remove('temp_file.txt')

    def _build(self, content):
        tf = open(self.temp_file, 'w')
        tf.write(content)
        tf.close()

    # def _destroy(self):
    #     os.remove('temp_file.txt')

    def test_parse1(self):
        self._build('a b cc\nddd')
        lines, n_lines, words, chars = wordcounter.count_else(self.temp_file)
        # self._destroy()

        self.assertEqual(lines, 2)
        self.assertEqual(n_lines, 2)
        self.assertEqual(words, 4)
        self.assertEqual(chars, 10)

    def test_parse2(self):
        self._build('a\nb\ncc\nddd\ne')
        lines, n_lines, words, chars = wordcounter.count_else(self.temp_file)
        # self._destroy()

        self.assertEqual(lines, 5)
        self.assertEqual(n_lines, 5)
        self.assertEqual(words, 5)
        self.assertEqual(chars, 12)

    def test_parse3(self):
        self._build('a\n\nb\ncc\nddd\ne')
        lines, n_lines, words, chars = wordcounter.count_else(self.temp_file)
        # self._destroy()

        self.assertEqual(lines, 6)
        self.assertEqual(n_lines, 5)
        self.assertEqual(words, 5)
        self.assertEqual(chars, 13)

    def test_parse4(self):
        self._build(' a b c ')
        lines, n_lines, words, chars = wordcounter.count_else(self.temp_file)
        # self._destroy()

        self.assertEqual(lines, 1)
        self.assertEqual(n_lines, 1)
        self.assertEqual(words, 3)
        self.assertEqual(chars, 7)


if __name__ == '__main__':
    unittest.main()
