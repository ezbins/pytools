#!/usr/bin/env python3

from Crypto.PublicKey import RSA


new_key = RSA.generate(2048, e=65537)
public_key = new_key.publickey().exportKey("OpenSSH")
private_key = new_key.exportKey("PEM")

#public key 寫入檔案 .pub
with open('root.pub','wb') as f:
    f.write(public_key)

#private key 寫入檔案
with open('root','wb') as f:
    f.write(private_key)
