from math import factorial
from array import array
from re import L


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

    def reverse_array(self, i, arr):  # YOU CAN USE SLICING TOOO [::-1]
        n = len(arr)
        if i >= n//2:
            print(arr)
            return
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
        self.reverse_array(i+1, arr)

    def reverse_array_approach2(self, i, r, arr):
        if i >= r:
            print(arr)
            return
        arr[i], arr[r] = arr[r], arr[i]
        self.reverse_array_approach2(i+1, r-1, arr)

    def palindrome_string(self, i, string_in):
        n = len(string_in)
        string_in = string_in.lower()
        if i >= n // 2:
            print("palindrome")
            return
        if string_in[i] != string_in[n-i-1]:
            print("Not a palindrome")
            return
        self.palindrome_string(i+1, string_in)

    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)

    def fib1(self, n):
        if n <= 1:
            print(" 0 1 ")
            return
        n1 = 0
        n2 = 1
        print(n1, n2, end=" ")
        for i in range(2, n+1):
            n3 = n1+n2
            n1 = n2
            n2 = n3
            print(n3, end=' ')


if __name__ == "__main__":
    sol = Recursion()
    test = array("i", [1, 2, 3, 4, 5])
    sol.fib1(5)
