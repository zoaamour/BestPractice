'''
百度API查询经纬度
python coords.py
'''
import click
import requests
import re


@click.command()
@click.option('--addr', prompt='查询经纬度\n输入地址')
def main(addr):
    # https://api.map.baidu.com/geocoding/v3/?address=北京市海淀区上地十街10号&output=json&ak=您的ak&callback=showLocation //GET请求
    ak = 'TQt8mXNaNXRye0laIvRPGY7BGQN8cAkX'
    rep = requests.get(
        f'https://api.map.baidu.com/geocoding/v3/?address={addr}&output=json&ak={ak}&callback=showLocation')
    print(re.findall(r'"lng":(.*),"lat":(.*?)}', rep.text))


if __name__ == "__main__":
    main()