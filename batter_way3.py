def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # str 인스턴스


print(repr(to_str(b'foo')))
print(to_str(b'foo'))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
        print(1)
    else:
        value = bytes_or_str
        print(2)
    return value #bytes 인스턴스

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))

#'안녕'.encode()
# 'hello'.encode()


with open('data.bin', 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')
