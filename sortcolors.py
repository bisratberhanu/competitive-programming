def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list=nums.copy()
        nums.clear()
        for i in list:
            if i==0:
                nums.append(0)
        for i in list:
            if i==1:
                nums.append(1)
        for i in list:
            if i==2:
                nums.append(2)
                