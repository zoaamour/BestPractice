import time
import threading
import requests
import pandas as pd

from loguru import logger
from faker import Faker
from bs4 import BeautifulSoup


def craw_url(url):
	global df
	fake = Faker()
	headers = {'User-Agent': fake.user_agent()}
	r = requests.get(url, headers=headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	review_list = soup.find_all(class_="main review-item")

	for ri in range(len(review_list)):
		rank = review_list[ri].select('span')[0].get('title')
		time1 = review_list[ri].select('span')[1].get('content')
		title = review_list[ri].select('h2>a')[0].text
		df = df.append({'时间': time1,
						'评分': rank,
						'标题': title, }, ignore_index=True)

	logger.info("-> 爬取完成")


if __name__ == '__main__':

	start = time.perf_counter()
	df = pd.DataFrame(columns=['时间', '评分', '标题'])

	url_list = [
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=0',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=20',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=40',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=60',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=80',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=100',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=120',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=140',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=160',
		'https://movie.douban.com/subject/1652587/reviews?sort=time&start=180']
	thread_list = []
	for i in url_list:
		thread = threading.Thread(target=craw_url, args=[i])
		thread.start()
		thread_list.append(thread)

	for t in thread_list:
		t.join()

	finish = time.perf_counter()

	logger.info(f"全部任务执行完成，耗时 {round(finish - start, 2)} 秒")