# Scout Crooke, 11/25/19, this prgram works on unit 6 daily exercises

names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen", "Jackie",
         "Kurt", "Linda"]

print(names[3:5])
print(names[1:6])
print(names[5:12])
print(names[5:])
print(names[11])
print(names[-1])
print(names[1:8:2])
print(names[0:12:2])
print(names[:12:2])
print(names[11:8:-1])
print(names[::-1])
print(names[11::-1])


def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


print(are_duplicates([100, 2, 3, 4, 5, 100]))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def add_numbers(nums):
    total = 0
    for x in nums:
        total = total + x
    return total


print(add_numbers(nums))


def has22(nums):
    for x in range(len(nums) - 1):
        if nums[x] == 2 and nums[x + 1] == 2:
            return True
        else:
            return False


print(has22([1, 2, 3, 4, 5, 2]))


def is_sorted(nums):
    for x in range(len(nums)):
        if nums[x] <= nums[x + 1]:
            return True
        else:
            return False


print(is_sorted([1, 2, 3, 4, 3]))




