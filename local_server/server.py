import http.server
import socketserver
import os

# 设置 HTTP 服务器的端口
PORT = 8001

# 配置静态文件目录
Handler = http.server.SimpleHTTPRequestHandler
os.chdir("local_server")

# 启动 HTTP 服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    #print(os.getcwd())
    # 开始监听请求
    try:
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        # 捕获键盘中断信号，关闭服务器
        print("KeyboardInterrupt: Stopping the server.")
        httpd.shutdown()
