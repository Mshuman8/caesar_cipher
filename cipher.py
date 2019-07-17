# Code out your function definitions here

# The encode function needs to take a word, split it into characters, then take the cipher_number and shift them each that many times.
alpha_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encode(word, cipher_num):
    word = word.lower()
    coded_answer = ""
    word_array = list(word)
    non_let = [" ", ".", ",", "!", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for char in word_array: 
        if char in non_let:
            coded_answer += char
        else:
            original_num = alpha_array.index(char)
            new_value = original_num + int(cipher_num)
            # No need for if/else because you can use mod because eitherway it, need to subtract one. will work.
            new_value = new_value%26
            new_let = alpha_array[new_value]
            coded_answer = coded_answer + new_let
    return coded_answer
    

def decode(word, cipher_num):
    word = word.lower()
    coded_answer = ""
    word_array = list(word)
    non_let = [" ", ".", ",", "!", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for char in word_array: 
        if char in non_let:
            coded_answer += char
        else:
            decoded_num = alpha_array.index(char)
            new_value = decoded_num - int(cipher_num)
            new_value = new_value%26
            new_let = alpha_array[new_value]
            coded_answer = coded_answer + new_let
    return coded_answer
    

def user_encode(): 
    word = input("What word or sentence would you like to encode? \n")
    number = input("What number would you like your Caesar Cipher to offset by?\n")
    print(encode(word, number))
    
def user_decode(): 
    word = input("What word or sentence would you like to decode? \n")
    number = input("What number would you like your Caesar Cipher to offset by?\n")
    print(decode(word, number))
    

def caesar_cipher_user():
    print("Welcome to my Caesar Cipher Encoder and Decoder")
    en_or_de = input("What would you like to do, encode or decode?")
    loop = True
    while loop == True:
        if en_or_de.lower() == "encode" or en_or_de == "code":
            user_encode()
            loop = False
        elif en_or_de.lower() == "decode":
            user_decode()
            loop = False
        else:
            print("Invalid response. Please enter 'encode' or 'decode'")
            loop = True

# ALL OF THE FOLLOWING CODE WAS WHEN I WAS TRYING TO DO IT WITH A DICTIONARY AND SEARCHING FOR A KEY IF YOU KNOW THE VALUE.
# coded_answer = ""

# alph_dict_let = [{"a":0}, {"b":1}, {"c":2}, {"d":3}, {"e":4}, {"f":5}, {"g":6}, {"h":7}, {"i":8}, {"j":9}, {"k":10}, {"l":11}, {"m":12}, {"n":13}, {"o":14}, {"p":15}, {"q":16}, {"r":17}, {"s":18}, {"t":19}, {"u":20}, {"v":21}, {"w":22}, {"x":23}, {"y":24}, {"z":25}]

# alpha_dict_num = [{0:"a"}, {1:"b"}, {2:"c"}, {3:"d"}, {4:"e"}, {5:"f"}, {6:"g"}, {7:"h"}, {8:"i"}, {9:"j"}, {10:"k"}, {11:"l"}, {12:"m"}, {13:"n"}, {14:"o"}, {15:"p"}, {16:"q"}, {17:"r"}, {18:"s"}, {19:"t"}, {20:"u"}, {21:"v"}, {22:"w"}, {23:"x"}, {24:"y"}, {25:"z"}]


# def encode(word, cipher_num):
#     word_array = list(word)
#     for char in word_array:
#         original_num = alpha_dict_let[][char]
#         new_value = original_num + cipher_num
#         if new_value <= 25:
#             new_let = alpha_array[new_value]
#         else: 
#             new_value = new_value - 26
#             new_let = alpha_array[new_value]
#         coded_answer = coded_answer + new_let
#     print(coded_answer)
    
# encode("hello", 4)
# # should be "lipps" ("hello is 7 4 11 11 14 so it becomes 11 8 15 15 18 which is "lipps" ")

# def decode(word, cipher_num):
#     word_array = list(word)
#     for char in word_array: 
#         decoded_num = alpha_dict_let[]["char"]
#         new_value = decoded_num - cipher_num
#         if new_value >= 0:
#             new_let = alpha_array[new_value]
#         else: 
#             new_value = new_value + 26
#             new_let = alpha_array[new_value]
#         coded_answer = coded_answer + new_let
#     print(coded_answer)



    