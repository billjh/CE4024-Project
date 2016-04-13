"""
Solution for Problem 2 in CE4024 Lab Project
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

def case_welcome(client_msg, server_msg):
    name = get_name(client_msg, server_msg)
    server_log = b'WELCOME ' + name + b' ' * (120 - len(name))
    client_log = XOR(XOR(server_msg, server_log), client_msg)
    return '[CORRECT] ' + str(client_log.replace(b'LOGIN', b'').strip(), 'ascii')

def case_password(client_msg, server_msg):
    server_log = b'PASSWORD MISMATCH' + b' ' * 111
    client_log = XOR(XOR(server_msg, server_log), client_msg)
    return '[WRONG]   ' + str(client_log.replace(b'LOGIN', b'').strip(), 'ascii')

def case_username(client_msg, server_msg):
    server_log = b'INCORRECT USERNAME' + b' ' * 110
    client_log = XOR(XOR(server_msg, server_log), client_msg)
    return '[WRONG]   ' + str(client_log.replace(b'LOGIN', b'').strip(), 'ascii')

if __name__ == '__main__':
    client_file = open('ClientLogEnc.dat', 'rb')
    server_file = open('ServerLogEnc.dat', 'rb')
    output_file = open('Problem2.txt', 'w')
    while True:
        client_msg = client_file.read(128)
        server_msg = server_file.read(128)
        if len(client_msg) != 128 or len(server_msg) != 128:
            break
        if XOR(client_msg, b'LOGIN') == XOR(server_msg, b'WELCO'):
            output_file.write(case_welcome(client_msg, server_msg))
            output_file.write('\n')
        elif XOR(client_msg, b'LOGIN') == XOR(server_msg, b'PASSW'):
            output_file.write(case_password(client_msg, server_msg))
            output_file.write('\n')
        elif XOR(client_msg, b'LOGIN') == XOR(server_msg, b'INCOR'):
            output_file.write(case_username(client_msg, server_msg))
            output_file.write('\n')
    output_file.close()
