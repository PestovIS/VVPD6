from unittest import TestCase, main
from functions4.fun1 import is_gray
from functions4.fun2 import to_gray


class is_gray_test(TestCase):
    def test_NoFormatStr(self):
        self.assertEqual(is_gray('asdfg'), None)

    def test_NoFormatStr2(self):
        self.assertEqual(is_gray('#A9A9AG'), None)

    def test_NoStr(self):
        self.assertEqual(is_gray(1234), None)

    def test_GrayColor(self):
        self.assertEqual(is_gray('#A9A9A9'), True)

    def test_NoGrayColor(self):
        self.assertEqual(is_gray('#A9A9FF'), False)


class to_gray_test(TestCase):
    def test_NoFormatStr(self):
        self.assertEqual(to_gray('asdfg'), None)

    def test_NoFormatStr2(self):
        self.assertEqual(to_gray('#A9A9AG'), None)

    def test_NoStr(self):
        self.assertEqual(to_gray(1234), None)

    def test_GrayColor(self):
        self.assertEqual(to_gray('#A9A9A9'), None)

    def test_NoGrayColor(self):
        self.assertEqual(to_gray('#945412'), (0, 64, 130))


if __name__ == '__main__':
    main()
