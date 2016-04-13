"""
Solution for Problem 1 in CE4024 Lab Project
Author: Jiang Huan
Date: 12 Apr 2016
"""

def XOR(A, B):
    """
    Exclusive OR operation on two multi-bytes.
    """
    return bytes(a^b for a, b in zip(A, B))

def get_name(client_msg, server_msg):
    i = 6
    magic = b'E '
    name = b''
    while True:
        temp = XOR(XOR(server_msg[i:i+2], magic), client_msg[i:i+2])
        if b' ' in temp:
            name += temp[:temp.find(b' ')]
            return name
        else:
            name += temp
        i += 2
        magic = temp

if __name__ == '__main__':
    client_file = open('ClientLogEnc.dat', 'rb')
    server_file = open('ServerLogEnc.dat', 'rb')
    output_file = open('Problem1.txt', 'w')
    while True:
        client_msg = client_file.read(128)
        server_msg = server_file.read(128)
        if len(client_msg) != 128 or len(server_msg) != 128:
            break
        if XOR(client_msg, b'LOGIN') == XOR(server_msg, b'WELCO'):
            output_file.write(str(get_name(client_msg, server_msg), 'ascii'))
            output_file.write('\n')
    output_file.close()
