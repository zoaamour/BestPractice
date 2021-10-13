import speedtest
# 全局取消证书验证
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
test = speedtest.Speedtest()
down = test.download()
upload = test.upload()
print(f"上传速度：{round(upload/(1024 * 1024),2)} Mbps")
print(f"下载速度：{round(down/(1024 * 1024),2)} Mbps")