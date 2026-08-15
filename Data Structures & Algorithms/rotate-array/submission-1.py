class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #idxs which contain the updated item (correct)
        updated = set()
        #the idx of the val we need to move

        for n in range(len(nums) - 1):
            if n in updated:
                continue
            to_move = nums[n]
            dest = (n + k) % len(nums)
            while True:
                if dest in updated: #if we've already run it
                    break
                updated.add(dest)
                next_move = nums[dest]
                next_dest = (dest + k) % len(nums)
                nums[dest] = to_move
                to_move, dest = next_move, next_dest
        
