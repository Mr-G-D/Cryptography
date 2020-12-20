from Crypto.Cipher import AES
key = " Be quick about "
plain = b'hell'
Cipher = AES.new(key,AES.MODE_CBC)
cipherText = Cipher.encrypt(plain)
result = cipherText.encode('hex')
print(result)

plainText = Cipher.decrypt(cipherText)
print (plainText)
