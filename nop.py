class nopcls(object):
    def __init__(self):
        self.inst = []

    def __iter__(self):
        for i in self.inst:
            yield i

    def emit(self, *inst):
        self.inst.append(inst)

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


def nop():
    return nopcls()
