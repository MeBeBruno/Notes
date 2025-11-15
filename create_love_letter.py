from base64 import b64encode, b64decode

def encrypt(password: str, message: str = input("Enter message: ")) -> str:
	encrypted = ""
	for char in range(len(message)):
		encrypted += chr(ord(message[char]) ^ ord(password[char % len(password)]))
	return b64encode(encrypted)

def decrypt(password: str, encryptedb64: str) -> str:
	encrypted = b64decode(encryptedb64)
	decrypted = ""
	for char in range(len(encrypted)):
		decrypted += chr(ord(encrypted[char]) ^ ord(password[char % len(password)]))
	return decrypted