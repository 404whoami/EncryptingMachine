import math

# CAESAR CIPHER
#encryption
def Cencrypt(Ckey, message):
    key = Ckey
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

#decryption
def Cdecrypt(Ckey, message):
    key = Ckey
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


# END OF CAESAR CIPHER

#START OF TRANSPOSITION CIPHER
#Encryption

def tencrypt(tkey,message):
    key = tkey
    plain_text = message
    t = 0
    for r in range(row):
        for c, ch in enumerate(plain_text[t: t + len_key]):
            matrix[r][c] = ch
        t += len_key

    # print(matrix)
    sort_order = sorted([(ch, i) for i, ch in enumerate(key)])  # to make alphabetically order of chars
    # print(sort_order)

    cipher_text = ''
    for ch, c in sort_order:
        for r in range(row):
            cipher_text += matrix[r][c]


    print("Plain text is :", message)
    print("Cipher text is:", cipher_text)


#decrypiton

def Tdecrypt(tkey, dmessage):
    key = tkey
    cipher_text = dmessage

    matrix_new = [ ['X']*len_key for i in range(row) ]
    key_order = [ key.index(ch) for ch in sorted(list(key))]  #to make original key order when we know keyword
    # print(key_order)

    t = 0
    for c in key_order:
      for r,ch in enumerate(cipher_text[t : t+ row]):
        matrix_new[r][c] = ch
      t += row
    # print(matrix_new)

    p_text = ''
    for r in range(row):
      for c in range(len_key):
        p_text += matrix_new[r][c] if matrix_new[r][c] != 'X' else ''

    print("Cipher text is:",cipher_text)
    print("Plain text is :",p_text)



if __name__ == '__main__':

    message = input("Enter plain text (Letters only): ").lower().replace(" ", "")
    choose = int(input("we have two types of encryption & decryption form choose 1 for CAESAR  or 2 for TRANSPOSITION : "))
    if choose == 1: #CAESAR cipher
        decision = int(input("what do you want to do? \n 1.Encryption 2.Decryption "))
        if decision == 1:
            Ckey = int(input("Enter your key to encrypt  only numbers: "))
            print(Cencrypt(Ckey, message))
        if decision == 2:
            Ckey = int(input("Enter your key: "))
            print(Cdecrypt(Ckey, message))

    if choose == 2: #TRANSPOSITION cipher
        decision = int(input("what do you want to do? \n 1.Encryption 2.Decryption "))
        if decision == 1:
            tkey = input("Enter keyword text (Contains unique letters only): ").lower().replace(" ", "")
            len_key = len(tkey)
            len_plain = len(message)
            row = int(math.ceil(len_plain / len_key))
            matrix = [['X'] * len_key for i in range(row)]
            tencrypt(tkey, message)
        if decision == 2:
            tkey = input("enter key to decrypt: ")
            dmessage = message
            Tdecrypt(tkey, dmessage)