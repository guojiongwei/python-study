# r: 读取文件
# w: 写入文件
# a: 追加文件
# r+: 读取和追加文件
# w+: 读取和写入文件
# encoding: 编码格式

file = open('./demo.txt', 'r+', encoding='utf-8')

def read_file():
    # 读取文件
    print(file.read())

def read_file_line():
    # 读取文件
    print(file.readline())

def read_file_lines():
    # 读取文件
    print(file.readlines())

def write_file():
    # 写入文件
    file.write('hello world')

def close_file():
    # 关闭文件
    file.close()

try:
    read_file()
    read_file_line()
    read_file_lines()
    write_file()
    read_file()
except BaseException as e:
    print('error', e)
finally:
    close_file()
