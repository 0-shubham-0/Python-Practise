list_a = ["Hello", 2, 15, "World", 5.5, 'd', [1, 'y'], True]
for_int = 0
for_str = 0
for_float = 0
for_char = 0
for_bool = 0
for_list = 0
print(list_a)
for value in list_a:
    datatype = type(value)
    if datatype == int:
        for_int = for_int + 1

    elif datatype == str and len(value) == 1:
        for_char = for_char + 1

    elif datatype == str:
        for_str = for_str + 1

    elif datatype == float:
        for_float = for_float + 1

    elif datatype == bool:
        for_bool = for_bool + 1

    elif datatype == list:
        for_list = for_list + 1


print("No of times Intger Datatype present ", for_int)
print("No of times String Datatype present ", for_str)
print("No of times Float Datatype present ", for_float)
print("No of times Boolean Datatype present ", for_bool)
print("No of times char Datatype present ", for_char)
print("No of times List Datatype present ", for_list)
