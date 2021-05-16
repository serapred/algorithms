class A(object):
    """docstring for A"""

    def __init__(self, arg):
        super(A, self).__init__()
        print('init A')
        self.arg = arg

    def m(self):
        print(f'{self.arg} in A')


class B(object):
    """docstring for B"""

    def m(self):
        super().m()
        print(f'{self.arg} in B')


class C(B, A):
    """[summary]

    [description]
    """


c = C('y')
c.m()
