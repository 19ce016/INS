import hashlib
import rsa

message = input("Enter Message TO Be Sent: ")
print("Encryption Process...")
print()
publicKey, privateKey = rsa.newkeys(1024)

def encrypt(message):
    private_key = hashlib.sha256(message.encode("utf-8")).hexdigest()
    print("Alice -> Hash Value: ", end=" ")
    print(private_key)
    hashMessage = str(private_key)+', '+message
    print("\nConcatenation of Message & Hash Vaue: \n", end=" ")
    print(hashMessage)
    return rsa.encrypt(hashMessage.encode(), publicKey)

def decrypt(enc):
    decMessage = rsa.decrypt(enc, privateKey).decode()
    print("Decrypted Message: ", end=" ")
    print(decMessage)
    hash,m = decMessage.split(', ')
    print("\nAlice -> Hash Value: ", end=" ")
    print(hash)
    print("\nMessage: ", end=" ")
    print(m)
    return hash,hashlib.sha256(m.encode("utf-8")).hexdigest()

encrypted = encrypt(message)
print("\nEncrypted Message: \n", end=" ")
print(encrypted)
print()
print("---------------------------------------------------------------------------------------------------")
print("Decryption Process...")
print()

hash,mhash = decrypt(encrypted)
print("\nBob -> Hash Value: ", end=" ")
print(mhash)
if(str(hash) == str(mhash)):
    print("\nMessage Received Successfully! \n Hence, Communication Successful!")
else:
    print("Altered Message! Message Might be tampered!")
