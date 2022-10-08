#=== ALL TABLE FOR DES ===

# Table of Position of 64 bits at initial level: Initial Permutation Table
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

# inverse initial Permutation Table
inverse_initial_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                        39, 7, 47, 15, 55, 23, 63, 31,
                        38, 6, 46, 14, 54, 22, 62, 30,
                        37, 5, 45, 13, 53, 21, 61, 29,
                        36, 4, 44, 12, 52, 20, 60, 28,
                        35, 3, 43, 11, 51, 19, 59, 27,
                        34, 2, 42, 10, 50, 18, 58, 26,
                        33, 1, 41, 9, 49, 17, 57, 25]
 
# Expansion Permutation Table
exp_perm = [32,  1,  2,  3,  4,  5, 
             4,  5,  6,  7,  8,  9, 
             8,  9, 10, 11, 12, 13, 
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]
 
# Straight Permutation Table
perm = [16,  7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2,  8, 24, 14,
       32, 27,  3,  9,
       19, 13, 30,  6,
       22, 11,  4, 25]
 
# S-box Table
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

#permuted choice one (PC-1)
pc1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
 
# permutated choice two (PC-2)
pc2 = [14, 17, 11, 24,  1,  5,  3, 28,
       15,  6, 21, 10, 23, 19, 12,  4,
       26,  8, 16,  7, 27, 20, 13,  2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]

# Number of bit shifts
shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]
 
#Function bantuan

def decimalToBiner(num, bit=0):
    biner = bin(num)[2::]
    zeros = bit - len(biner)

    return "0" * zeros + biner

def charToBinary(char):
    return decimalToBiner(ord(char), 8)      #convert to ascii number lalu dijadikan binary, remove 2 char paling depan dan tambahkan 0 dipaling depan supaya menjadi 8 bit

def stringToBinary(text):
    result = ""
    for char in text:
        result += charToBinary(char)
    
    return result

def binaryToChar(binary):
    return chr(int(binary, 2))

def binaryToString(binary):
    result = ""
    for i in range(int(len(binary)/8)):
        start = i * 8
        end = start + 8
        result += binaryToChar(binary[start:end])
    
    return result

def permute(origin, arrPermute):
    result = ""
    for index in arrPermute:
        result += origin[index-1]

    return result

def shiftLeft(arr, n):
    return arr[n:] + arr[:n]

def xor(p, q):
    result = ""
    for i in range(len(p)):
        if p[i] == q[i]:
            result += "0"
        else:
            result += "1"

    return result

#input key sudah dalam bentuk binary, return berupa binary juga
def generate_subkeys(binKey):
    subkeys = []            #the result

    #dipermutasi dengan PC-1, dari 64 bit jadi 56 bit
    pc1Key = permute(binKey, pc1)
    # print(pc1Key)

    mid = int(len(pc1Key))//2
    LKey = pc1Key[:mid]
    RKey = pc1Key[mid:]
    
    for i in range(16):
        #dilakukan shift left sebanyak 1/2 sesuai tabel
        LKey = shiftLeft(LKey, shift_table[i])
        RKey = shiftLeft(RKey, shift_table[i])

        #digabung kembali
        combine = LKey + RKey

        #dipermutasi dengan PC-2, dari 56 jadi 48 bit
        pc2Key = permute(combine, pc2)

        subkeys.append(pc2Key)

    return subkeys

def sboxSub(biner):
    result = ""

    for i in range(len(biner)//6):
        start = i * 6
        end = start + 6

        partial = biner[start:end]          #biner yang dibagi setiap 6 bit

        row = int(partial[0]+partial[-1], 2) #row = nilai desimal dari gabungan biner pertama dan terakhir
        col = int(partial[1:-1], 2)          #col == nilai desimal dari 4 bit ditengah

        sboxValue = sbox[i][row][col]
        sboxBiner = decimalToBiner(sboxValue, 4)
        # print(sboxBiner)

        result += sboxBiner
    
    return result

def feistelChiper(RText, subkey):
    #di expand dari 32 menjadi 48 bit
    expandText = permute(RText, exp_perm)   
    # print("Expaned RText: " + expandText)

    XORResult = xor(expandText, subkey)
    # print("ExpandexText XOR Subkey: " + XORResult)

    #di sbox supaya dari 48 jadi 32 bit lagi
    sboxResult = sboxSub(XORResult)
    # print("S-Box Result: " + sboxResult)

    #permutasi dengan Permutation Fuction
    permResult = permute(sboxResult, perm)
    # print("Permutation Result: " + permResult)

    return permResult

#input plain text dan key sudah dalam bentuk binary, return berupa binary juga
def des_encryption(binText, binKey):
    #GENERETE SUB KEYS
    subkeys = generate_subkeys(binKey)

    #lakukan permutasi dengan initial permutation (IP)
    ipText = permute(binText, initial_perm)
    print("Hasil Initial Permutaion: " + ipText)
    print("Hasil Initial Permutaion: " + binaryToString(ipText))
    print()

    #split jadi kiri dan kanan
    mid = int(len(ipText))//2
    LText = ipText[:mid]
    RText = ipText[mid:]
    print("L0: " + LText + " R0: " + RText)
    print("L0: " + binaryToString(LText) + " R0: " + binaryToString(RText))
    print()
    
    for i in range(16):
        round = str(i+1)
        print("===== ROUND " + round + " =====")
        newLText = RText
        newRText = xor(LText, feistelChiper(RText, subkeys[i]))

        #replace bagian kiri dan kanan yang baru
        LText = newLText
        RText = newRText

        #print
        
        #binary form
        print("Round %2s = L%2s: %32s ===== R%2s: %32s ===== Key: %48s" % (round, round, (LText), round, (RText), (subkeys[i])))
        #ascii form
        print("Round %2s = L%2s: %4s ===== R%2s: %4s ===== Key: %4s" % (round, round, binaryToString(LText), round, binaryToString(RText), binaryToString(subkeys[i])))
        # print("Round %2s = L%2s: %4s ===== R%2s: %4s ===== Key: %4s" % (round, round, binToHexa(LText), round, binToHexa(RText), binToHexa(subkeys[i])))
        print()

    combine = LText + RText

    #permutasi dengan inverse initial permutation
    ipInverseText = permute(combine, inverse_initial_perm)
    # print("Inverse Initial Permutation: " + ipInverseText)

    #the final result
    chiperText = ipInverseText
    return chiperText

#input chiper text dan key sudah dalam bentuk binary, return berupa binary juga
def des_decryption(binText, binKey):
    #GENERETE SUB KEYS
    subkeys = generate_subkeys(binKey)[::-1]           #Key16 jadi Key1

    #lakukan permutasi dengan initial permutation (IP)
    ipText = permute(binText, initial_perm)
    print("Hasil Initial Permutaion: " + ipText)
    print("Hasil Initial Permutaion: " + binaryToString(ipText))
    print()

    #split jadi kiri dan kanan
    mid = int(len(ipText))//2
    LText = ipText[:mid]
    RText = ipText[mid:]
    print("L0: " + LText + " R0: " + RText)
    print("L0: " + binaryToString(LText) + " R0: " + binaryToString(RText))
    print()
    
    for i in range(16):
        round = str(i+1)
        print("===== ROUND " + round + " =====")

        newLText = xor(RText, feistelChiper(LText, subkeys[i]))
        newRText = LText

        #replace bagian kiri dan kanan yang baru
        LText = newLText
        RText = newRText

        #print
        
        #binary form
        print("Round %2s = L%2s: %32s ===== R%2s: %32s ===== Key: %48s" % (round, round, (LText), round, (RText), (subkeys[i])))
        #ascii form
        print("Round %2s = L%2s: %4s ===== R%2s: %4s ===== Key: %4s" % (round, round, binaryToString(LText), round, binaryToString(RText), binaryToString(subkeys[i])))
        print()

    combine = LText + RText

    #permutasi dengan inverse initial permutation
    ipInverseText = permute(combine, inverse_initial_perm)
    # print("Inverse Initial Permutation: " + ipInverseText)

    #the final result
    plainText = ipInverseText
    return plainText


##MAIN PROGRAM

#PLAIN TEXT

#=== INPUT ===
while(True):
    plainText = input("Plain Text: ")

    if len(plainText) == 8:
        break
    else:
        print("Panjang harus 8 karakter")

while(True):
    key = input("Key: ")

    if len(key) == 8:
        break
    else:
        print("Panjang harus 8 karakter")


#convert ascii to biner
binText = stringToBinary(plainText)
# print("Binary Plain Text: " + binText)

# convert dardi ascii ke biner
binKey = stringToBinary(key)
# print("Binary Key: " + binKey)

encrypted = des_encryption(binText, binKey)

print("\n==============================================")
print("Chiper Text: " + binaryToString(encrypted))
print("==============================================\n")

decrypted = des_decryption(encrypted, binKey)
print("\n==============================================")
print("Plain Text: " + binaryToString(decrypted))
print("==============================================\n")