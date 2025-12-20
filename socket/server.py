import socket
import threading
# 用于记录活动连接数
active_connections = 0
# 用于线程同步的锁
lock = threading.Lock()

def handle_client(c, addr):
    global active_connections
    try:
        with lock:
            active_connections += 1
        print(f"Connected by {addr}")
        while True:
            data = c.recv(1024)
            print(f'i received {data}')  # 1024 一次性接受的最大长度 1024字节
            if not data: 
                break
            c.sendall(data)  # 数据不为空 原封不动回传数据
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        c.close()
        with lock:
            active_connections -= 1
        print(f"Connection closed by {addr}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1234)) # 绑定IP地址和端口号
    s.listen()  # 当前socket为监听状态
    print("Server is listening on port 1234...")
    try:
        while True:
            c, addr = s.accept()
            t = threading.Thread(target = handle_client, args = (c, addr))
            t.start()
            # 检查是否有活动连接，若没有则退出循环
            if active_connections == 0:
                break
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        print("Server closed.")










