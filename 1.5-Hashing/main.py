class Hashing:
    def number_hashing(self, arr, input, len):
        hash_arr = [0] * int(len(arr))
        # or define the max array length, for the 12th index,
        #   hash_arr = [0] * 13, if the problem states len of arr is 10^5 then arr[0] * 10^5
        # int max size arr is 10^6 inside main, but globally it can go till 10^7
        for i in arr:
            hash_arr[i] += 1
        for i in input:
            try:
                print(hash_arr[i])
            except IndexError:
                print(0)

    def character_hashing(self, arr, input):
        hash_arr = [0] * 256
        for i in arr:
            hash_arr[ord(i)] += 1
        for i in input:
            print(hash_arr[ord(i)])

    def character_hashing2(self, arr, input):
        hash_arr = [0] * 26  # only for small alphabets
        for i in arr:
            map = ord(i) - ord('a')
            hash_arr[map] += 1
        for i in input:
            print(hash_arr[ord(i) - ord('a')])

    def hashing_with_dict(self, arr):
        maxValue = 0
        maxKey = 1
        lowValue = 1000000
        lowKey = 1
        hash_dict = {}
        for i in arr:
            ### or ####
            #  hash_dict[i] = hash_dict.get(i, 0)+1
            if i in hash_dict:
                hash_dict[i] += 1
            else:
                hash_dict[i] = 1
        for key, value in hash_dict.items():
            print(f"{key} has appeared {value} times")
            if maxValue < value:
                maxValue = value
                maxKey = key

            if value < lowValue:
                lowValue = value
                lowKey = key
        print(
            f"The max time occuring element is {maxKey} and it comes {maxValue}")
        print(
            f"The min time occuring element is {lowKey} and it comes {lowValue}")


solution = Hashing()
solution.hashing_with_dict([2, 2, 3, 4, 4, 2])
