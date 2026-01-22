class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()

    def pattern2(self, n):
        for i in range(n):
            print("* " * (i+1))

    def pattern3(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1, end=" ")
            print()

    def pattern4(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1, end=" ")
            print()

    def pattern5(self, n):
        for i in range(n, 0, -1):
            print("* "*i)

        # or

        # for i in range(n):
        #     for j in range(n, i, -1):
        #         print("*", end=" ")
        #     print()

    def pattern6(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()

    def pattern7(self, n):
        for i in range(n):
            for j in range(n-1, i, -1):
                print(" ", end="")
            print("*" * (2*i + 1), end=" ")
            for j in range(n-1, i, -1):
                print(" ", end="")
            print()

    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            print("*" * ((2*n) - (2*i+1)), end="")
            for j in range(i):
                print(" ", end="")
            print()

    def pattern9(self, n):
        for i in range(n):
            for j in range(n-1, i, -1):
                print(" ", end="")
            print("*" * (2*i + 1), end=" ")
            for j in range(n-1, i, -1):
                print(" ", end="")
            print()
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            print("*" * ((2*n) - (2*i+1)), end="")
            for j in range(i):
                print(" ", end="")
            print()

    def pattern10(self, n):
        for i in range(n-1):
            print("*" * (i + 1))

        print("*" * n)

        for i in range(n-1, 0, -1):
            print("*" * i)

    def pattern11(self, n):
        for i in range(n):
            if i % 2 == 0:
                start = 1
            else:
                start = 0
            for j in range(start, start+1):
                for k in range(i+1):
                    print(start, end=" ")
                    start = 1 - start
            print()

    def pattern12(self, n):
        # THIS IS MY LOGIC

        # for i in range(n):
        #     for j in range(i+1):
        #         print(j+1, end="")

        #     for k in range(n-1, i, -1):
        #         print(" ", end="")

        #     for j in range(i, n-1):
        #         print(" ", end="")

        #     for k in range(i+1, 0, -1):
        #         print(k, end="")
        #     print()

        # This is the more optimal one
        space = 2 * (n-1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end='')

            for k in range(1, space+1):
                print(" ", end="")

            for j in range(i, 0, -1):
                print(j, end='')
            print()
            space -= 2

    def pattern13(self, n):
        last = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(last, end=' ')
                last += 1
            print()

    def pattern14(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(chr(64 + j), end=" ")
            print()

    def pattern15(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(chr(64 + j), end=" ")
            print()

    def pattern16(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(chr(64 + i), end=' ')
            print()

    def pattern17(self, n):
        ch = ord("A")
        for i in range(n):
            for j in range(n-1, i, -1):
                print(" ", end="")

            for k in range(0, i+1):
                print(chr(65 + k), end="")

            for m in range(i-1, -1, -1):
                print(chr(ch + m), end="")

            for j in range(n-1, i, -1):
                print(" ", end="")
            print()

        for i in range(n):
            breakpoint = 2*i+1 // 2
            for j in range(n-1, i, -1):
                print("-", end='')

            for k in range(0, (2*i+1)):
                print(chr(ch), end="")

            for j in range(n-1, i, -1):
                print("-", end='')
            print()
            # something with this approach
 ###############################################

    def pattern18(self, n):
        for i in range(n):
            for j in range(ord('A') + n - 1 - i, ord('A') + n):
                print(chr(j), end=" ")
            print()

    def pattern19(self, n):
        spaces = 0
        for i in range(n):
            for j in range(n-i):
                print("*", end=" ")

            for k in range(spaces):
                print(" ", end=" ")

            for j in range(n-i):
                print("*", end=" ")
            spaces += 2
            print()

        spaces = 2 * n - 2
        for i in range(n):

            # stars
            for j in range(i+1):
                print("*", end=" ")

            # space
            for j in range(spaces):
                print(" ", end=" ")
            # stars
            for j in range(i+1):
                print("*", end=" ")

            spaces -= 2
            print()

    def pattern20(self, n):
        # my bruteforce approach
        space = 2 * n - 2
        for i in range(n):
            # stars
            for j in range(i+1):
                print("*", end=" ")

            # space
            for j in range(space):
                print(" ", end=" ")

            # stars
            for j in range(i+1):
                print("*", end=" ")
            space -= 2
            print()
        space = 2
        for i in range(n-1):
            # stars
            for j in range(n-i-1):
                print("*", end=" ")
            # space
            for j in range(space):
                print(" ", end=" ")
            # stars
            for j in range(n-i-1):
                print("*", end=" ")
            space += 2
            print()

        print()
        for i in range(2*n-1):
            stars = i+1
            if (i > n):
                stars = (2 * n) - i
            # stars

            for i in range(stars):
                print("*", end=" ")
            # spaces
            # stars
            print()

    def pattern21(self, n):
        for i in range(n):
            for j in range(n):
                if (i == 0 or j == 0 or i == n-1 or j == n-1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


sol = Solution()
sol.pattern21(4)
