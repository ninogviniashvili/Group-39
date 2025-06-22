# 1

def insert_at(lst, index, item):
    lst.insert(index, item)
    return lst

my_list = [1, 2, 3, 4]
result = insert_at(my_list, 2, 99)
print(result)


# 2

def append_items(lst, items):
    lst.extend(items)
    return lst

my_list = [1, 2, 3]
new_items = [4, 5, 6]
result = append_items(my_list, new_items)
print(result)


# 3

def append_list(original, to_append):
    original.extend(to_append)
    return original

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = append_list(list1, list2)
print(result)
