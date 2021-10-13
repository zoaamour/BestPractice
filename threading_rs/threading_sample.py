import logging
import time
import threading
from loguru import logger


def do_something(num):
	print(f"-> 线程{num} 启动，睡眠 {num} 秒")
	time.sleep(num)
	print(f"-> 线程{num} 结束")


def main():
	start = time.perf_counter()
	thread_list = []

	for i in range(1, 11):
		thread = threading.Thread(target=do_something, args=[i])
		thread.start()
		logger.info('thread.start')
		thread_list.append(thread)

	for t in thread_list:
		t.join()
		logger.info('t.join')

	finish = time.perf_counter()

	logger.info(f"全部任务执行完成，耗时 {round(finish - start, 2)} 秒")


if __name__ == '__main__':
	main()
