
# 字符串
print('----字符串----')
str = "字符串"
print(str)
print(len(str))
print(str.find("字"))
print(str.replace("字", "z"))
print(str.split("字"))

strs = ''''
    1
    2'''
print(strs)

# int类型
int = 10
print('----int类型----')
print(int)
print(int.bit_length())

# float类型
float = 10.0
print('----float类型----')
print(float)
if float == 10:
    print("是整数")
else:
    print("不是整数")

# bool类型
print('----bool类型----')
bool = True
print(bool)
if bool:
    print("是真")
else:
    print("是假")


# complex类型
print('----complex类型----')
complex = 1 + 2j
print(complex)


# bytes类型
print('----bytes类型----')
bytes = b"abc"
print(bytes)
print(bytes.decode("utf-8"))
print(bytes.decode("utf-8").encode("utf-8"))


# list类型
print('----list类型----')
list = [1, 2, 3, 4, 5]
print(list)
print(list[0])
print(list[0:3])



# 列表
print('----列表----')
list = [1, 2, 3, 4, 5]
print(list)
print(list[0])
print(list[0:2])
list.append(6)
print(list)
list.insert(0, 0)
print(list)
list.pop(0)
print(list)
list.remove(5)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.clear()
print(list)


# 元组
print('----元组----')
tuple = (1, 2, 3, 4, 5)
print(tuple)
print(tuple[0])
print(tuple[0:2])
print(tuple.index(1))
print(tuple.count(1))

print(tuple.__add__((6, 7, 8)))


# 字典
print('----字典----')
dict = {"name": "张三", "age": 18}
print(dict["name"])
print(dict.get("name"))
dict["name"] = "李四"
print(dict)

# 集合
print('----集合----')
set = {1, 2, 3, 4, 5}
print(set)
set.add(6)
print(set)
set.remove(6)
print(set)
set.clear()
print(set)

# 集合运算
print('----集合运算----')
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
