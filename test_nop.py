from nop import nop

import unittest


class InstructionsTest(unittest.TestCase):
    def test_add_sub(self):
        inst = list(nop() + 5 + 2 - 1 + 1)

        self.assertEqual(len(inst), 4)
        self.assertEqual(inst[0], ('add', 5))
        self.assertEqual(inst[1], ('add', 2))
        self.assertEqual(inst[2], ('sub', 1))
        self.assertEqual(inst[3], ('add', 1))

    def test_rgt(self):
        inst = list(nop() + 1 > nop() + 3)

        self.assertEqual(len(inst), 3)
        self.assertEqual(inst[0], ('add', 1))
        self.assertEqual(inst[1], ('rgt',))
        self.assertEqual(inst[2], ('add', 3))

    def test_lft(self):
        inst = list(nop() + 1 > nop() + 3 < nop() - 2 > nop() + 1)

        self.assertEqual(len(inst), 7)
        self.assertEqual(inst[0], ('add', 1))
        self.assertEqual(inst[1], ('rgt',))
        self.assertEqual(inst[2], ('add', 3))
        self.assertEqual(inst[3], ('lft',))
        self.assertEqual(inst[4], ('sub', 2))
        self.assertEqual(inst[5], ('rgt',))
        self.assertEqual(inst[6], ('add', 1))

    def test_loop(self):
        inst = list(
            nop() + 2 >> (
                nop() - 1 > nop() + 2 < nop()
            ) << nop() + 5
        )

        self.assertEqual(len(inst), 7)
        self.assertEqual(inst[0], ('add', 2))
        self.assertEqual(inst[1], ('lop', 4))
        self.assertEqual(inst[2], ('sub', 1))
        self.assertEqual(inst[3], ('rgt',))
        self.assertEqual(inst[4], ('add', 2))
        self.assertEqual(inst[5], ('lft',))
        self.assertEqual(inst[6], ('add', 5))

    def test_write(self):
        inst = list(nop() > nop() + 2 < nop() + 3 ^ nop())

        self.assertEqual(len(inst), 5)
        self.assertEqual(inst[0], ('rgt',))
        self.assertEqual(inst[1], ('add', 2))
        self.assertEqual(inst[2], ('lft',))
        self.assertEqual(inst[3], ('add', 3))
        self.assertEqual(inst[4], ('wrt',))

    def test_read(self):
        inst = list(~nop() + 1 ^ nop() > ~nop() + 2)

        self.assertEqual(len(inst), 6)
        self.assertEqual(inst[0], ('red',))
        self.assertEqual(inst[1], ('add', 1))
        self.assertEqual(inst[2], ('wrt',))
        self.assertEqual(inst[3], ('rgt',))
        self.assertEqual(inst[4], ('red',))
        self.assertEqual(inst[5], ('add', 2))


class ExecutionTest(unittest.TestCase):
    def test_add_sub(self):
        res = nop() + 49 + (5 + 2 - 1 + 1) ^ nop()

        self.assertEqual(str(res), '8')

    def test_rgt(self):
        res = nop() + 1 > nop() < nop() + 49 ^ nop()

        self.assertEqual(str(res),  '2')

    def test_lft(self):
        res = nop() + 1 > nop() + 3 < nop() - 2 > nop() + 48 ^ nop()

        self.assertEqual(str(res), '3')

    def test_loop(self):
        res = (
            nop() + 49 > nop() + 52 >> (
                nop() - 1 < nop() + 1 > nop()
            ) << nop() < nop() ^ nop()
        )

        self.assertEqual(str(res), 'e')

    def test_read(self):
        res = ~nop() - 32 ^ nop()
        res.input_func = lambda: 'a'

        self.assertEqual(str(res), 'A')


if __name__ == '__main__':
    unittest.main()
