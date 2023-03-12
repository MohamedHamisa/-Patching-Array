    def minPatches(self, nums, n):
        miss_num = []
        patch, miss, i = 0, 1, 0
        while miss <= n:
            # when do we need to patch?
            # 1. when miss is smaller than nums[i]
            # 2. when nums fully used to check miss
            #--------------------------------------------------------------------------------------
            # if nums is fully checked, it means that miss is greater than max(nums), we need patch.
            # if miss is less than nums[i], we need patch.
            if len(nums) <= i or miss < nums[i]:
                miss += miss
                patch += 1
            else:
                miss += nums[i]
                i += 1
        return patch
       

