#Find duplicates in list using set

def find_duplicates(nums):
    seen =  set()
    duplicates = set()


    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


#Example usage
print(find_duplicates([1,2,5,1,7,1,8,2]))
print(find_duplicates(['a','b','c','d','a','c']))