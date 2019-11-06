import keyword

print(keyword.kwlist)

a = 'abc'.encode('ascii')
b = '中文'.encode('utf-8')
c = '中文'
d = b.decode('utf-8',errors='ignore')#忽视无法解码的字节
print(a)
print(b)
print(c)
print(d)