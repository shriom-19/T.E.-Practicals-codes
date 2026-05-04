# “Implementation of Data Encryption Standard (DES) Algorithm”



# OUTPUT-
# DES - DATA ENCRYPTION STANDARD ALGORITHM
# Enter the 64 bit plain Text (16 Characters): 0123456789ABCDEF
# Enter the 64 bit key (16 Characters): 0123456789ABCDEF

# After initial permutation: CC00CCFFF0AAF0AA
# Round 1 F0AAF0AA 5E1CEC63 0B02679B49A5
# Round 2 5E1CEC63 82E13C49 69A659256A26
# Round 3 82E13C49 499542F9 45D48AB428D2
# Round 4 499542F9 0DD64AFB 7289D2A58257
# Round 5 0DD64AFB 7036043B 3CE80317A6C2
# Round 6 7036043B F1470BC2 23251E3C8545
# Round 7 F1470BC2 394C8F45 6C04950AE4C6
# Round 8 394C8F45 348DC746 5788386CE581
# Round 9 348DC746 F37100C6 C0C9E926B839
# Round 10 F37100C6 3C22A9CB 91E307631D72
# Round 11 3C22A9CB 0A37C369 211F830D893A
# Round 12 0A37C369 5C725FFB 7130E5455C54
# Round 13 5C725FFB F4748AD6 91C4D04980FC
# Round 14 F4748AD6 CC6C340E 5443B681DC8D
# Round 15 CC6C340E BA88F699 B691050A16B5
# Round 16 FB21FB9C BA88F699 CA3D03B87032

# Cipher Text: 56CC09E7CFDC4CEF

# After initial permutation: FB21FB9CBA88F699
# Round 1 BA88F699 CC6C340E CA3D03B87032
# Round 2 CC6C340E F4748AD6 B691050A16B5
# Round 3 F4748AD6 5C725FFB 5443B681DC8D
# Round 4 5C725FFB 0A37C369 91C4D04980FC
# Round 5 0A37C369 3C22A9CB 7130E5455C54
# Round 6 3C22A9CB F37100C6 211F830D893A
# Round 7 F37100C6 348DC746 91E307631D72
# Round 8 348DC746 394C8F45 C0C9E926B839
# Round 9 394C8F45 F1470BC2 5788386CE581
# Round 10 F1470BC2 7036043B 6C04950AE4C6
# Round 11 7036043B 0DD64AFB 23251E3C8545
# Round 12 0DD64AFB 499542F9 3CE80317A6C2
# Round 13 499542F9 82E13C49 7289D2A58257
# Round 14 82E13C49 5E1CEC63 45D48AB428D2
# Round 15 5E1CEC63 F0AAF0AA 69A659256A26
# Round 16 CC00CCFF F0AAF0AA 0B02679B49A5
# Plain Text: 0123456789ABCDEF




# CODE-
print("--------------------------------------------------")
print("DES - DATA ENCRYPTION STANDARD ALGORITHM")

pt = input("Enter the 64 bit plain Text (16 Characters): ")
key = input("Enter the 64 bit key (16 Characters): ")

# HEX TO BIN
def hex2bin(s):
    mp = {'0':"0000",'1':"0001",'2':"0010",'3':"0011",
          '4':"0100",'5':"0101",'6':"0110",'7':"0111",
          '8':"1000",'9':"1001",'A':"1010",'B':"1011",
          'C':"1100",'D':"1101",'E':"1110",'F':"1111"}
    return "".join(mp[i] for i in s)

# BIN TO HEX
def bin2hex(s):
    mp = {"0000":'0',"0001":'1',"0010":'2',"0011":'3',
          "0100":'4',"0101":'5',"0110":'6',"0111":'7',
          "1000":'8',"1001":'9',"1010":'A',"1011":'B',
          "1100":'C',"1101":'D',"1110":'E',"1111":'F'}
    return "".join(mp[s[i:i+4]] for i in range(0,len(s),4))

# BIN TO DEC
def bin2dec(binary):
    return int(str(binary),2)

# DEC TO BIN
def dec2bin(num):
    res = bin(num).replace("0b","")
    return res.zfill(4)

# PERMUTATION
def permute(k, arr, n):
    return "".join(k[i-1] for i in arr[:n])

# LEFT SHIFT
def shift_left(k, shifts):
    return k[shifts:] + k[:shifts]

# XOR
def xor(a,b):
    return "".join('0' if i==j else '1' for i,j in zip(a,b))


# INITIAL PERMUTATION
initial_perm = [58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7]

# EXPANSION
exp_d = [32,1,2,3,4,5,4,5,
6,7,8,9,8,9,10,11,
12,13,12,13,14,15,16,17,
16,17,18,19,20,21,20,21,
22,23,24,25,24,25,26,27,
28,29,28,29,30,31,32,1]

# P-BOX
per = [16,7,20,21,29,12,28,17,
1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,
19,13,30,6,22,11,4,25]

# FINAL PERM
final_perm = [40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25]

# S-BOX (ALL 8)
sbox = [
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
 [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
 [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
 [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],

[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
 [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
 [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],

[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
 [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
 [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
 [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],

[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
 [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
 [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
 [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],

[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
 [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
 [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
 [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],

[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
 [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
 [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
 [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],

[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
 [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
 [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
 [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],

[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
 [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
 [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
 [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]


def encrypt(pt, rkb):
    pt = hex2bin(pt)

    # Initial Permutation
    pt = permute(pt, initial_perm, 64)
    print("\nAfter initial permutation:", bin2hex(pt))

    left = pt[:32]
    right = pt[32:]

    for i in range(16):
        # Expansion
        right_expanded = permute(right, exp_d, 48)

        # XOR with key
        xor_x = xor(right_expanded, rkb[i])

        # S-box substitution
        sbox_str = ""
        for j in range(8):
            block = xor_x[j*6:(j+1)*6]
            row = int(block[0] + block[5], 2)
            col = int(block[1:5], 2)
            val = sbox[j][row][col]
            sbox_str += dec2bin(val)

        # Straight permutation
        sbox_str = permute(sbox_str, per, 32)

        # XOR with left
        result = xor(left, sbox_str)
        left = result

        # Swap (except last round)
        if i != 15:
            left, right = right, left

        # 🔥 PRINT EACH ROUND
        print("Round", i+1, 
              bin2hex(left), 
              bin2hex(right), 
              bin2hex(rkb[i]))

    # Combine
    combine = left + right

    # Final permutation
    cipher_text = permute(combine, final_perm, 64)

    return cipher_text


# KEY GENERATION
key = hex2bin(key)

keyp = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,
10,2,59,51,43,35,27,19,11,3,60,52,44,36,
63,55,47,39,31,23,15,7,62,54,46,38,
30,22,14,6,61,53,45,37,29,21,13,5,
28,20,12,4]

key = permute(key, keyp, 56)

shift_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

key_comp = [14,17,11,24,1,5,3,28,15,6,21,10,
23,19,12,4,26,8,16,7,27,20,13,2,
41,52,31,37,47,55,30,40,51,45,33,48,
44,49,39,56,34,53,46,42,50,36,29,32]

left, right = key[:28], key[28:]
rkb = []

for i in range(16):
    left = shift_left(left, shift_table[i])
    right = shift_left(right, shift_table[i])
    combine = left + right
    rkb.append(permute(combine, key_comp, 48))


# ENCRYPTION
cipher = bin2hex(encrypt(pt, rkb))
print("\nCipher Text:", cipher)

# DECRYPTION
rkb_rev = rkb[::-1]
text = bin2hex(encrypt(cipher, rkb_rev))
print("Plain Text:", text)