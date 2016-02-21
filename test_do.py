from do import do

import unittest


class DoTest(unittest.TestCase):
    def test_add_sub(self):
        inst = list(do() + 10 + 2 - 1 + 1)

        self.assertEqual(len(inst), 4)
        self.assertEqual(inst[0], ('add', 10, False))
        self.assertEqual(inst[1], ('add', 2, False))
        self.assertEqual(inst[2], ('sub', 1, False))
        self.assertEqual(inst[3], ('add', 1, False))

    def test_rgt(self):
        inst = list(do() + 1 > do() + 3)

        self.assertEqual(len(inst), 3)
        self.assertEqual(inst[0], ('add', 1, False))
        self.assertEqual(inst[1], ('rgt', None, False))
        self.assertEqual(inst[2], ('add', 3, False))

    def test_lft(self):
        inst = list(do() + 1 > do() + 3 < do() - 2 > do() + 1)

        self.assertEqual(len(inst), 7)
        self.assertEqual(inst[0], ('add', 1, False))
        self.assertEqual(inst[1], ('rgt', None, False))
        self.assertEqual(inst[2], ('add', 3, False))
        self.assertEqual(inst[3], ('lft', None, False))
        self.assertEqual(inst[4], ('sub', 2, False))
        self.assertEqual(inst[5], ('rgt', None, False))
        self.assertEqual(inst[6], ('add', 1, False))

    def test_loop(self):
        inst = list(do() + 2 | do() - 1 > do() + 1 < do() | do())
        print(inst)

    #     self.assertEqual(len(inst), 2)
    #     self.assertEqual(inst[0], ('add', 2))
    #     self.assertEqual(inst[1], ('lop', 4))
    #     self.assertEqual(inst[2], ('sub', 1))
    #     self.assertEqual(inst[3], ('rgt',))
    #     self.assertEqual(inst[4], ('add', 1))
    #     self.assertEqual(inst[5], ('lft',))


if __name__ == '__main__':
    unittest.main()
