from numbers import Number
from typing import Tuple
from mpmath import mp


def encode(encode_input: Number) -> Tuple:
    """
    Encodes input into Pi
    :param encode_input: Numeric input
    :return: Tuple containing the start and ending pointers within pi
    """
    substring = str(encode_input)
    pi_str = ''
    incrementing_number = 1000
    while substring not in pi_str:
        mp.dps = incrementing_number  # set number of digits
        pi_str = str(mp.pi)  # print pi to a thousand places
        pi_str = pi_str.replace(".", "")
        incrementing_number = incrementing_number * incrementing_number
    else:
        loc = pi_str.find(substring)
        return loc, loc + len(substring)


def decode(decode_input: Tuple) -> Number:
    """
    Decodes tuple into Numeric
    :param decode_input: Tuple input
    :return: The original encoded data
    """
    mp.dps = decode_input[1] + 1  # set number of digits
    pi_str = str(mp.pi)  # print pi to a thousand places
    pi_str = pi_str.replace(".", "")
    return int(pi_str[decode_input[0]: decode_input[1]])


test = encode(123)
print(test)
print(decode(test))
