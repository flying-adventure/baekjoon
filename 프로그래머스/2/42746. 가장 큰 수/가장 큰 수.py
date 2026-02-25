from functools import cmp_to_key
def solution(numbers):
    nums = list(map(str, numbers))
    def cmp(x,y):
        if x+y>y+x:
            return -1
        if x+y<y+x:
            return 1
        return 0
    nums.sort(key=cmp_to_key(cmp))
    if nums[0]=="0":
        return "0"
    return "".join(nums)