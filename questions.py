tup1: tuple[int] = (99,)

tup2: tuple[int, int, int] = (77, 88, 99)


def get_tup_length(t):
    return len(t)


def get_two_tup_together(t1, t2):
    return t1 + t2


def get_tup_common(tuple1, tuple2):
    common = tuple(set(tuple1) & set(tuple2))
    return common


t1: tuple[int, int, int, int] = (1, 2, 3, 4)
t2: tuple[int, int, int, int] = (3, 4, 5, 6)
result = get_tup_common(t1, t2)
print(result)


def get_tup_diff(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    diff = (set1 ^ set2)
    return diff


t1: tuple[int, int, int, int] = (1, 2, 3, 4)
t2: tuple[int, int, int, int] = (3, 4, 5, 6)
result = get_tup_diff(t1, t2)
print(result)


def get_tup_get_index(tup, index1):
    if index1 < 0 or index1 >= len(tup):
        return None
    return tup[index1]


def get_reversed_tup(tup):
    return tup[::-1]


def get_tup_get_num(tup, num1):
    return tup * num1


tup3 = (2, 1)
num = 3
result = get_tup_get_num(tup3, num)
print(result)


def get_tup_get_num2(tup, num2):
    return tuple(x for x in tup if x != num2)


my_tuple = (10, 8, 5, 5, 3, 2, 50, 10, 30, 40)
number_to_remove = 10
result = get_tup_get_num2(my_tuple, number_to_remove)
print(result)


def get_tup(tup):
    l1 = []
    for i in tup:
        if i not in l1:
            l1.append(i)
    return tuple(l1)


def name_score_tup():
    names1 = []
    while True:
        name: str = input("enter name: ")
        if name == "done":
            break
        names1.append(name)
    grades = []
    while True:
        grade: int = int(input("enter grade: "))
        if grade == -999:
            break
        grades.append(grade)

    result1 = tuple(zip(names1, grades))
    return result1
result = name_score_tup()
print(result)

# the diff between tuple and list is that you can change every existing value with another in list and in tuples you can't

data_tuple = (
{"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
)
data_tuple[0] ["age"] = 31
data_tuple[0] .clear()
print(data_tuple)

# it's working because the index[0] that started with name... and ends with "New York", and
# in the end you "cleaning" what's in index[0], what's left is: ({}, 1000, 'secret-code')