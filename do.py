class docls(object):
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

    def __gt__(self, do):
        self.emit('rgt')
        for di in do.inst:
            self.emit(*di)
        do.inst = self.inst
        return do

    def __lt__(self, do):
        self.emit('lft')
        for di in do.inst:
            self.emit(*di)
        do.inst = self.inst
        return self

    def __rshift__(self, do):
        self.emit('lop')
        for di in do.inst:
            self.emit(*di)
        do.inst = self.inst
        return self

    def __lshift__(self, do):
        p = len(self.inst) - 1
        c = 0
        while p > -1:
            if self.inst[p][0] == 'lop':
                self.inst[p] = ('lop', c)
            p -= 1
            c += 1
        for di in do.inst:
            self.emit(*di)
        return self


def do():
    return docls()
