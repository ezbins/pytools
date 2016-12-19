#!/usr/bin/env python3

import string
import random

complexString = string.ascii_letters + string.digits + string.punctuation

randomStr = ""
for i in range(40):
    randomStr += "".join(random.choice(complexString))


print(randomStr)
