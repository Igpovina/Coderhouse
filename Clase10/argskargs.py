# *args y **kargs
def conversion(*nums):
  if len(nums) == 1:
    return nums[0]/1000, nums[0]/10, nums[0]
  else:
    return (nums[0]*1000+(nums[1]*10)+(nums[2]))
print(conversion(5,3,1))