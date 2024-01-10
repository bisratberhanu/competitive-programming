class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter_list=[]
        left=0
        right=k-1
        while right<len(blocks):
            new_string=blocks[left:right+1]
            counter=0
            for letter in new_string:
                if letter=='W':
                    counter+=1
            counter_list.append(counter)
            right+=1
            left+=1
        return min(counter_list)
