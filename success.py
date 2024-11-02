Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums=[29,75,40,78,91,30,45]
>>> nums[0]
29
>>> nums[2:]
[40, 78, 91, 30, 45]
>>> nums[3]
78
>>> nums[:-1]
[29, 75, 40, 78, 91, 30]
>>> names=['nelly','vanessa','maxensia']
>>> names
['nelly', 'vanessa', 'maxensia']
>>> values= [9.5,'vanessa',91,'nelly']
>>> mil=[nums,names]
>>> mil
[[29, 75, 40, 78, 91, 30, 45], ['nelly', 'vanessa', 'maxensia']]
>>> nums.append(78)
>>> nums
[29, 75, 40, 78, 91, 30, 45, 78]
>>> nums.insert(2,94)
>>> nums
[29, 75, 94, 40, 78, 91, 30, 45, 78]
>>> nums.remove(91)
>>> nums
[29, 75, 94, 40, 78, 30, 45, 78]
>>> nums.pop()
78
>>> nums.pop(1)
75
>>> nums.extend([29,89,40])
>>> nums
[29, 94, 40, 78, 30, 45, 29, 89, 40]
>>> min(nums)
29
>>> max(nums)
94
>>> sum(nums)
474
>>> nums.sort()
>>> nums
[29, 29, 30, 40, 40, 45, 78, 89, 94]
