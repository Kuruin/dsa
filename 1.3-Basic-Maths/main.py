from math import log, sqrt


class basicMaths:
    def countDigits(self, n):
        count = 0
        while (n > 0):
            lastDigit = n % 10
            print(lastDigit)
            n //= 10
            count += 1
        print(f"The total digits are {count}")

    def optimalCountDigits(self, n):
        count = int(log(n, 10) + 1)
        print(count)

    def reverseNumber(self, n):
        sum = 0
        while (n > 0):
            lastDigit = n % 10
            sum = sum * 10 + lastDigit
            n //= 10
        print(sum)

    def palindrome(self, n):
        number = n
        reverseNumber = 0
        while (n > 0):
            lastDigit = n % 10
            reverseNumber = reverseNumber * 10 + lastDigit
            n //= 10
        print(reverseNumber)
        if number == reverseNumber:
            print("It is a palindrome number")
        else:
            print("Not a palindrome number")

    def armstrong(self, n):
        input = n
        sum = 0
        count = int(log(n, 10) + 1)
        while (n > 0):
            lastDigit = n % 10
            sum += (lastDigit ** count)
            n //= 10
        if sum == input:
            print(f"{input} is a Armstrong number")
        else:
            print(f"{input} is not a armstrong number")

    def allDivisors(self, n):
        divisors = []
        divisors1 = []

        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        print(divisors)

        # or you can loop till j*j + 1 (for i = 1; i<= j * j; j ++ )
        for j in range(1, int(sqrt(n) + 1)):
            if n % j == 0:
                divisors1.append(j)

                if j != n//j:
                    divisors1.append(n//j)

        divisors1.sort()
        print(divisors1, " This is optimal ")

    def primeNumbers(self, n):
        # or just keep a count variable to track the number of factors
        p_list = []
        for i in range(1, int(sqrt(n) + 1)):
            if n % i == 0:
                p_list.append(i)

                if i != n//i:
                    p_list.append(n//i)
        p_list.sort()
        if (len(p_list) == 2):
            print(f"Prime Number")
        else:
            print("Not a prime number")

    def gcd_hcf(self, n1, n2):
        gcd = 1
        min = n1 if n1 < n2 else n2  # so it start from the top and goes down
        for i in range(min, 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
                break
        print(gcd)

    # eucledian distance


obj = basicMaths()
obj.gcd_hcf(15, 20)
