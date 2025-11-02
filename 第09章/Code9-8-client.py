import socket

# 创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
sk.connect(('127.0.0.1', 9999))

# 发送和接收数据
while True:
    send_data = input('请输入要发送的内容（输入"exit"退出）：')
    if send_data == 'exit':
        break
    # 发送数据到服务器
    sk.send(send_data.encode('utf-8'))
    # 等待服务器响应
    accept_data = sk.recv(1024)
    # 打印服务器的响应
    print('收到回复：', repr(accept_data.decode('utf-8')))

# 关闭连接
sk.close()

