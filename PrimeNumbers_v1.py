class PrimeNumbers:
    def __init__(self, range, range_max=None):
        self.xnumber = 1
        self.prime_numbers_list = [2]
        if range_max == None and type(range) == int:
            self.range_min = None
            self.n_of_pn(range)
        elif range_max != None and (type(range) == int and type(range_max) == int):
            self.range_min = range
            self.range(range_max)
        else:
            raise SyntaxError("The range must be an integer")

    def n_of_pn(self, range):  # n_of_pn stands for number of prime numbers!
        pnumber = 2*self.xnumber + 1
        while range > len(self.prime_numbers_list):
            for num in self.prime_numbers_list:
                if pnumber % num == 0:
                    break
            else:
                self.prime_numbers_list.append(pnumber)
            self.xnumber += 1
            pnumber = 2*self.xnumber + 1

    def range(self, range):
        pnumber = 2*self.xnumber + 1
        while range >= pnumber:
            for num in self.prime_numbers_list:
                if pnumber % num == 0:
                    break
            else:
                self.prime_numbers_list.append(pnumber)
            self.xnumber += 1
            pnumber = 2*self.xnumber + 1

    def __str__(self):
        if self.range_min == None:
            return str(self.prime_numbers_list)
        else:
            return str([num for num in self.prime_numbers_list if num >= self.range_min])

    def __len__(self):
        return len(self.prime_numbers_list)

    def __iter__(self):
        return iter(self.prime_numbers_list)


print(PrimeNumbers(10))
print(PrimeNumbers(100, 200))
