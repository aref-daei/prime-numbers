# Version 2 of PrimeNumbers is 14 times faster than version 1!
class PrimeNumbers:
    def __init__(self, __start: int, __stop: int = ...) -> None:
        self.__start = __start
        self.__stop = __stop
        self.__primenums = self.__calculator()

    def __calculator(self) -> list:
        if self.__stop is Ellipsis:
            stop = self.__start
        else:
            stop = self.__stop
        xnumber = 1
        prime_nums = [2]
        pnumber = 2*xnumber + 1
        while stop >= pnumber:
            for num in prime_nums:
                if num**2 >= pnumber:
                    indnum = num
                    break
            for num in prime_nums[:prime_nums.index(indnum)+1]:
                if pnumber % num == 0:
                    break
            else:
                prime_nums.append(pnumber)
            xnumber += 1
            pnumber = 2*xnumber + 1
        if self.__stop is Ellipsis:
            return prime_nums
        return [num for num in prime_nums if num >= self.__start]

    def value(self) -> list:
        return self.__primenums

    def __iter__(self):
        return iter(self.__primenums)

    def __len__(self):
        return len(self.__primenums)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < len(self):
                return self.__primenums[index]
            raise IndexError("PrimeNumbers object index out of range")
        elif isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            return self.__primenums[start:stop:step]
        else:
            raise TypeError("PrimeNumbers indices must be integers or slices")

    def __repr__(self) -> str:
        return f"PrimeNumbers(start={self.__start}, stop={self.__stop}) -> return {self.__primenums}"

    def __str__(self) -> str:
        return f"Prime Numbers: {self.__primenums}"


print(PrimeNumbers(100))
print(PrimeNumbers(100, 200))
print(PrimeNumbers(100)[::-1])
print(PrimeNumbers(100).value())
