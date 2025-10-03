#This program flatten's list using recursive method to handle depth

def flatten(nested):
    flat = []

    for items in nested:
        if isinstance(items, list):
            flat.extend(flatten(items))
        else:
            flat.append(items)

    return flat

#Example
print(flatten([[1,2],[3,4]]))
print(flatten([[1],2,3,[4,5], [6,7]]))
print(flatten([['a'],'b','c',['d','e']]))