"""
This script generates a list of all possible passwords of a given length using only lowercase alphabet letters.
The main function prints the list to the screen in a formatted way.

AUTHOR: Raymond Holsapple
LAST UPDATE: 10/25/2016
"""

import string

def password(n):
    """
    This function generates a list of passwords of length n.
    :param n: (integer) Number of characters in each password.
    :return passwords: (list of strings) List of all passwords generated.
    """
    alphabet = string.ascii_lowercase[:]
    len_alphabet = len(alphabet)
    done_flag = 0
    passwords = []

    for k in range(len_alphabet):
        passwords.append(alphabet[k])

    if n > 1:
        while done_flag == 0:
            temp_pswd_list = []
            for k in range(len(passwords)):
                for j in range(len_alphabet):
                    temp_string = passwords[k]
                    temp_string += alphabet[j]
                    temp_pswd_list.append(temp_string)

            passwords = temp_pswd_list

            if len(passwords[0]) == n:
                done_flag = 1

    return passwords


if __name__ == '__main__':
    password_list = password(3)
    num_passwords = len(password_list)
    num_lines = int(num_passwords/100)

    for k in range(num_lines):
        line_string = '  '.join(password_list[100*k:100*k+100])
        print(line_string)

    final_line = '  '.join(password_list[num_lines*100:num_passwords])
    print(final_line)
