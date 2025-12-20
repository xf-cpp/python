import socket



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1234)) # 连接服务器
    while True:
        msg = input("请输入要发送的消息：")
        s.sendall(msg.encode()) # 发送消息给服务器，b代表发送的是字节序列，而非字符串
        data = s.recv(1024)
        print(f"Recieved : {data}")




