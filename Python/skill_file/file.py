# 创建大文件

f = open("large.txt", "wb")
f.seek(1024*1024*1024)
f.write(b"\0")
f.close()