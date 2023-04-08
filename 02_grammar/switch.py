str = 'b'

def function_a():
    print('a')

# switch语法
switch = {
    'a': function_a,
    'b': 'b',
}

print(switch.get(str, 'default'))
str = 'a'
switch.get(str)()