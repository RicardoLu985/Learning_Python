import socket

# 创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('0.0.0.0', 9999))
sk.listen(5)

print("等待客户端连接...")
conn, addr = sk.accept()
print('连接地址：', addr)

# 接收数据
while True:
    accept_data = conn.recv(1024)
    print('收到数据:', accept_data.decode('utf-8'))
    send_data = input('请输入要回复的内容（输入"exit"退出）：')
    if send_data == 'exit':
        break
    conn.send(send_data.encode('utf-8'))

# 关闭连接
conn.close()
sk.close()



