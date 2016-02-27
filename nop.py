import sys

from collections import namedtuple


class nopcls(object):
    def __init__(self):
        self.inst = []
        try:
            self.input_func = raw_input
        except:
            self.input_func = input

    def run(self, stdout=None):
        s = namedtuple('scope', 'pos max_pos stack write_stack')
        s.pos = 0
        s.max_pos = 9
        s.stack = [0] * 10
        s.write_stack = []

        def run(it, stdout):
            try:
                i = it.next()
            except StopIteration:
                return

            if i[0] == 'add':
                s.stack[s.pos] += i[1]
            elif i[0] == 'sub':
                s.stack[s.pos] -= i[1]
            elif i[0] == 'lft':
                s.pos -= 1
            elif i[0] == 'rgt':
                s.pos += 1
                if s.pos > s.max_pos:
                    s.max_pos += 10
                    s.stack += [0] * 10
            elif i[0] == 'red':
                try:
                    r = self.input_func()
                except EOFError:
                    return
                if r:
                    s.stack[s.pos] = ord(r)
            elif i[0] == 'wrt':
                stdout(chr(s.stack[s.pos]))
                s.write_stack.append(s.stack[s.pos])

            if i[0] == 'lop':
                lopinsts = []
                for x in range(i[1]):
                    lopinsts.append(it.next())
                while s.stack[s.pos] > 0:
                    run(iter(lopinsts), stdout)

            run(it, stdout)

        if stdout is None:
            def stdout(s):
                pass
        else:
            if not callable(stdout):
                stdout = sys.stdout.write

        try:
            run(iter(self.inst), stdout)
        except KeyboardInterrupt:
            pass

        return s

    def __str__(self):
        return ''.join(map(chr, self.run().write_stack))

    def __iter__(self):
        for i in self.inst:
            yield i

    def __invert__(self):
        self.emit('red')
        return self

    def __add__(self, num):
        self.emit('add', num)
        return self

    def __sub__(self, num):
        self.emit('sub', num)
        return self

    def __gt__(self, nop):
        self.emit('rgt')
        for di in nop.inst:
            self.emit(*di)
        nop.inst = self.inst
        return nop

    def __lt__(self, nop):
        self.emit('lft')
        for di in nop.inst:
            self.emit(*di)
        nop.inst = self.inst
        return self

    def __rshift__(self, nop):
        self.emit('lop')
        for di in nop.inst:
            self.emit(*di)
        nop.inst = self.inst
        return self

    def __lshift__(self, nop):
        for i, inst in enumerate(self.inst):
            if inst[0] == 'lop':
                break

        self.inst[i] = ('lop', len(self.inst) - (i+1))

        for di in nop.inst:
            self.emit(*di)

        return self

    def __xor__(self, nop):
        self.emit('wrt')
        for di in nop.inst:
            self.emit(*di)
        nop.inst = self.inst
        return self

    def emit(self, *inst):
        self.inst.append(inst)


def nop():
    return nopcls()
