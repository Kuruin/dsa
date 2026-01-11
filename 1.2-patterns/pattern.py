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


sol = Solution()
sol.pattern5(3)
