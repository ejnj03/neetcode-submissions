class Solution:
    def reverseBits(self, n: int) -> int:
        #ith bit gets placed at 32 - i th position
        i = 0 #dt from mid (i = 15/16th digit)
        mid = 15
        num = 0
        print(f'{n:032b}')
        while True:
            if i >= 16:
                break
            #32 - ith bit at ith position
            mask1 = ((1 << mid + i + 1) & n) >> 2 * i + 1
            mask2 = ((1 << mid - i) & n) << 2 * i + 1
            num |= mask1 | mask2
            i += 1
            print(f'{num:032b}')
        print(bin(964176192))
        return num
