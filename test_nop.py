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
        inst1 = list(nop() + 1 > nop() + 3)
        inst2 = list((nop() + 1 > 2) + 3)

        self.assertEqual(len(inst1), 3)
        self.assertEqual(inst1[0], ('add', 1))
        self.assertEqual(inst1[1], ('rgt', 1))
        self.assertEqual(inst1[2], ('add', 3))

        self.assertEqual(len(inst2), 3)
        self.assertEqual(inst2[0], ('add', 1))
        self.assertEqual(inst2[1], ('rgt', 2))
        self.assertEqual(inst2[2], ('add', 3))

    def test_lft(self):
        inst1 = list(nop() + 1 > nop() + 3 < nop() - 2 > nop() + 1)
        inst2 = list((((nop() + 1 > 5) + 3 < 5) - 2 > 5) + 1)

        self.assertEqual(len(inst1), 7)
        self.assertEqual(inst1[0], ('add', 1))
        self.assertEqual(inst1[1], ('rgt', 1))
        self.assertEqual(inst1[2], ('add', 3))
        self.assertEqual(inst1[3], ('lft', 1))
        self.assertEqual(inst1[4], ('sub', 2))
        self.assertEqual(inst1[5], ('rgt', 1))
        self.assertEqual(inst1[6], ('add', 1))

        self.assertEqual(len(inst2), 7)
        self.assertEqual(inst2[0], ('add', 1))
        self.assertEqual(inst2[1], ('rgt', 5))
        self.assertEqual(inst2[2], ('add', 3))
        self.assertEqual(inst2[3], ('lft', 5))
        self.assertEqual(inst2[4], ('sub', 2))
        self.assertEqual(inst2[5], ('rgt', 5))
        self.assertEqual(inst2[6], ('add', 1))

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
        self.assertEqual(inst[3], ('rgt', 1))
        self.assertEqual(inst[4], ('add', 2))
        self.assertEqual(inst[5], ('lft', 1))
        self.assertEqual(inst[6], ('add', 5))

    def test_nested_loop(self):
        inst = list(
            nop() + 2 >> (
                nop() > nop() + 4 >> (
                    nop() - 1 > nop() + 6 < nop()
                ) << nop() - 3
            ) << nop() + 5
        )

        self.assertEqual(len(inst), 11)
        self.assertEqual(inst[0], ('add', 2))
        self.assertEqual(inst[1], ('lop', 8))
        self.assertEqual(inst[2], ('rgt', 1))
        self.assertEqual(inst[3], ('add', 4))
        self.assertEqual(inst[4], ('lop', 4))
        self.assertEqual(inst[5], ('sub', 1))
        self.assertEqual(inst[6], ('rgt', 1))
        self.assertEqual(inst[7], ('add', 6))
        self.assertEqual(inst[8], ('lft', 1))
        self.assertEqual(inst[9], ('sub', 3))
        self.assertEqual(inst[10], ('add', 5))

    def test_write(self):
        inst = list(nop() > nop() + 2 < nop() + 3 ^ nop())

        self.assertEqual(len(inst), 5)
        self.assertEqual(inst[0], ('rgt', 1))
        self.assertEqual(inst[1], ('add', 2))
        self.assertEqual(inst[2], ('lft', 1))
        self.assertEqual(inst[3], ('add', 3))
        self.assertEqual(inst[4], ('wrt',))

    def test_read(self):
        inst = list(~nop() + 1 ^ nop() > ~nop() + 2)

        self.assertEqual(len(inst), 6)
        self.assertEqual(inst[0], ('red',))
        self.assertEqual(inst[1], ('add', 1))
        self.assertEqual(inst[2], ('wrt',))
        self.assertEqual(inst[3], ('rgt', 1))
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

    def test_nested_loop(self):
        res = (
            nop() + 2 >> (
                nop() > nop() + 24 >> (
                    nop() - 1 > nop() + 1 < nop()
                ) << nop() < nop() - 1
            ) << (nop() > 2) + 5 ^ nop()
        )

        self.assertEqual(str(res), '5')

    def test_read(self):
        res = ~nop() - 32 ^ nop()
        res.input_func = lambda: 'a'

        self.assertEqual(str(res), 'A')


if __name__ == '__main__':
    unittest.main()
