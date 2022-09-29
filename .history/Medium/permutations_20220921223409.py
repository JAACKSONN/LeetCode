def permute(nums):
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]  # nums[:] is a deep copy

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

res = (permute([1,2,3,4,5,6]))
for item in res:
    plan = f'{item[0]} {item[1]} {item[2]} {item[3]} {item[4]} {item[5]}'
    print(plan)
    print()
