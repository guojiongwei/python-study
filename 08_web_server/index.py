import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def handle_home(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return open('templates/home.html', 'rb')

# 添加数据
def handle_add(env, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])

    # 获取请求参数
    query = parse_qs(env['QUERY_STRING'])

    # 获取请求体参数
    body = env['wsgi.input'].read(int(env['CONTENT_LENGTH']))
    body = json.loads(body.decode('utf-8'))
    print(query['a'][0], body['name'], body['age'])
    return [bytes(json.dumps(body), encoding='utf-8')]

# 定义application类型
def app(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    print(method, path)
    if method == 'GET' and path == '/':
        return handle_home(environ, start_response)
    
    if method == 'POST' and path == '/add':
        return handle_add(environ, start_response)
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>404</h1>']


print('服务启动:http://127.0.0.1:8000', __name__)
# 启动服务
server = make_server('localhost', 8000, app).serve_forever()
