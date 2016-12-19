#!/usr/bin/env python3

import string
import random

specChar = string.ascii_letters + string.digits + "!@#$%^&*"

words = []
for x in range(14):
    words.append(random.choice(specChar))
pw=''
for word in words:
    pw += word
print(pw)
