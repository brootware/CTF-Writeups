encoded_string = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"

# decodedString = ''.join(
#     [chr((ord(encoded_string[i]) << 8) + ord(encoded_string[i + 1])) for i in range(0, len(encoded_string), 2)])

for i in range(len(encoded_string)):
    decodedString = ''
    first = chr(ord(encoded_string[i]) >> 8)
    print(first)
    second = chr((ord(encoded_string[i]))-((ord(encoded_string[i]) >> 8) << 8))
    print(second)

# picoCTF{16_bits_inst34d_of_8_e141a0f7}
