from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mysecretpassword'

cipher = AES.new(key,AES.MODE_CBC)

plaintext = input()

cipherText = cipher.encrypt(pad(plaintext,AES.block_size))

print(cipherText)