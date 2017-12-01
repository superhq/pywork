# coding:utf-8
#from Cryptodome.Cipher import  AES
import hashlib


m = hashlib.md5()
m.update(b'123456')
digest = m.hexdigest()
print(digest.upper())
#cipher = AES.new(b'sunrunvas', AES.MODE_EAX)

#print(cipher)