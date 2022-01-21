import socket


# 封装成函数，方便 Python 的程序调用
def get_host_ip():
	skt = None
	try:
		# AF_INET用于跨机器之间的通信
		# SOCK_DGRAM数据报套接字，UDP
		skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		skt.connect(('8.8.8.8', 80))
		ip = skt.getsockname()[0]
	finally:
		skt.close()
	return ip


def main():
	print(f"您当前的主机名为: {socket.gethostname()}")
	print(f'当前IP为： {get_host_ip()}')
	print('\n')


if __name__ == '__main__':
	main()
