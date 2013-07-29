import string


class MinBraid():

    def __init__ (self, s, c):
        self.strands = s
        self.crossings = c
        self.universe = CartesianProduct(*[range(1, s)]*c)

    def minbraid(self):
        self.universe = self.filter1()
        self.universe = self.filter2()
        self.universe = self.filter3()
        self.universe = self.filter4()
        return self.universe

    def minbraid_str(self, l):
        ans = []
        for i in l:
            if i % 2 == 1:
                ans.append(chr(i+64))
            elif i % 2 == 0:
                ans.append(chr(i+96))
        return ans

    def filter1(self):
        return [i for i in self.universe if i[0] == 1]

    def filter2(self):
        return filter(self.filter2_help, self.universe)

    def filter2_help(self, l):
        s = range(1, self.strands)
        for i in s:
            if l.count(i) < 2:
                return False

        return True

    def filter3(self):
        return self.universe

    def filter4(self):
        return self.universe

    def smaller(self, b1, b2):
        if len(b1) != len(b2):
            return False

        for i in range(0, len(b1)):
            if b1[i] > b2[i]:
                return b2

        return b1

    def alternating(self, u):
        braid = self.minbraid_str(u)

        upper = [string.ascii_uppercase[i] for i in range(0, 26, 2)]
        lower = [string.ascii_lowercase[i] for i in range(1, 26, 2)]

        for i in braid:
            if i in upper:
                if not self.odd(i):
                    return False
            elif i in lower:
                if not self.even(i):
                    return False

        return True

    def even(self, c):
        n = ord(string.lower(c))-97
        if n % 2 == 0:
            return False
        else:
            return True

    def odd(self, c):
        return not self.even(c)

    def bincode(self, l):
        s = self.minbraid_str(l)
        bc = 0

        for i in s:
            if self.even(i) and i in string.ascii_uppercase:
                bc = bc + 1

        return bc

b = MinBraid(3, 4)
