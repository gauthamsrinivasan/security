import hashlib
sha1 = hashlib.sha1()
sha1.update('helloworld'.encode('utf-8'))
print(sha1.hexdigest())