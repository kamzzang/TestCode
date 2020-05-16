import string

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

from string import ascii_uppercase
from string import ascii_lowercase

alpha_list = list(ascii_uppercase) # 대문자 리스트 ['A','B', 'C', 'D', ...,  'X', 'Y', 'Z']
alpha_list = list(ascii_lowercase) # 소문자 리스트 ['a','b', 'c', 'd', ...,  'x', 'y', 'z']