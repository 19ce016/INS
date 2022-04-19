import hashlib
from random import randint

if __name__ == '__main__':

    # Both the persons will be agreed upon the
    # public keys G and P
    # A prime number P is taken
    P = 23
    
    # A primitive root for P, G is taken
    G = 9
    
    
    # print('The Value of P is :%d'%(P))
    # print('The Value of G is :%d'%(G))
    
    a = 4
    # print('The Private Key a for Alice is :%d'%(a))
    
    # gets the generated key
    x = int(pow(G,a,P))
    
    # Bob will choose the private key b
    b = 3
    # print('The Private Key b for Bob is :%d'%(b))
    
    # gets the generated key
    y = int(pow(G,b,P))
    
    
    # Secret key for Alice
    ka = str(pow(y,a,P))
    
    # Secret key for Bob
    kb = str(pow(x,b,P))
    
    # print('Secret key for the Alice is : %c'%(ka))
    # print('Secret Key for the Bob is : %c'%(kb))

  
m = input("Enter the Messege: ")

#Append
appendm = ka +','+m
print(appendm)

#sha-256
hashm = hashlib.sha256(appendm.encode('utf-8')).hexdigest()
print(hashm)

#Append Mes and appendm
appendm2 = hashm +','+m
print(appendm2)

#Splitting
hash2,m2 = appendm2.split(',')
print(hash2)

# append
append2= kb+','+m
print(append2)

#hash function
hashm3 = hashlib.sha256(append2.encode('utf-8')).hexdigest()
print(hashm3)

if hashm == hashm3:
     print("Messege Integrity is Conserved.")

else:
     print("Messege Integrity is not Conserved.")
