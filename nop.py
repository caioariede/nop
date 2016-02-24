from collections import namedtuple


class nopcls(object):
    def __init__(self):
        self.inst = []
        self.input_func = input

    def __str__(self):
        s = namedtuple('scope', 'pos max_pos stack write_stack')
        s.pos = 0
        s.max_pos = 9
        s.stack = [0] * 10
        s.write_stack = []

        def run(i):
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
                s.stack[s.pos] = ord(self.input_func())
            elif i[0] == 'wrt':
                s.write_stack.append(s.stack[s.pos])
            elif i[0] == 'lop':
                lopinsts = []
                for x in range(i[1]):
                    lopinsts.append(it.next())
                while s.stack[s.pos] > 0:
                    for lopi in lopinsts:
                        run(lopi)

        it = iter(self.inst)
        while True:
            try:
                run(it.next())
            except StopIteration:
                break

        return ''.join(map(chr, s.write_stack))

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
        p = len(self.inst) - 1
        c = 0
        while p > -1:
            if self.inst[p][0] == 'lop':
                self.inst[p] = ('lop', c)
            p -= 1
            c += 1
        for di in nop.inst:
            self.emit(*di)
        return self

    def __xor__(self, nop):
        self.emit('wrt')
        return self

    def emit(self, *inst):
        self.inst.append(inst)


def nop():
    return nopcls()
