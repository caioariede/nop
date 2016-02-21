class docls(object):
    def __init__(self):
        self.inst = []
        self.loop = False

    def __iter__(self):
        for i in self.inst:
            yield i

    def emit(self, *inst):
        # print(self.loop, inst)
        self.inst.append(inst)

    def reemit(self, *inst):
        inst = list(inst)
        inst[-1] = self.loop
        self.emit(*inst)

    def __add__(self, num):
        self.emit('add', num, self.loop)
        return self

    def __sub__(self, num):
        self.emit('sub', num, self.loop)
        return self

    def __gt__(self, do):
        self.emit('rgt', None, self.loop)
        for di in do.inst:
            self.reemit(*di)
        do.inst = self.inst
        do.loop = self.loop
        return do

    def __lt__(self, do):
        self.emit('lft', None, self.loop)
        for di in do.inst:
            self.reemit(*di)
        do.inst = self.inst
        do.loop = self.loop
        return do

    def __or__(self, do):
        self.loop = True
        for di in do.inst:
            self.reemit(*di)
        do.inst = self.inst
        return self


def do():
    return docls()
