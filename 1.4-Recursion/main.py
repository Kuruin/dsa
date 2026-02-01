from math import factorial


class Recursion:

    def printName(self, n, text, count):
        if count == n:
            return
        print(text)
        self.printName(n, text, count + 1)

    def forwardNumber(self, n, current):
        if current > n:
            return
        print(current, end=" ")
        # call recursive function first for backtracking
        self.forwardNumber(n, current+1)

    def reverseNumber(self, n):
        if n < 1:
            return
        # call recursive function first for backtracking
        print(n, end=" ")
        self.reverseNumber(n-1)

    def sumOfN(self, current, n, sum):
        if current == 1:
            print(n * (n+1) // 2)  # or use this formula

        if current > n:
            print(sum)
            return
        self.sumOfN(current + 1, n, sum + current)

        # better version

        if n == 1:
            return 1
        # return N + self.sumOfN(n-1) # this is functional way

    def sumOfn1(self, n, sum):
        if n < 1:
            print(sum)
            return
        self.sumOfn1(n-1, sum+n)  # this is parameterized way

    def factorial1(self, n, fact):
        if n < 1:
            print(fact)
            return
        self.factorial1(n-1, fact * n)

    def factorial2(self, n):
        if n == 0:
            return 1
        return n * self.factorial2(n-1)


if __name__ == "__main__":
    sol = Recursion()
    sol.factorial2(5)
