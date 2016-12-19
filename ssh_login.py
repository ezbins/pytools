#!/usr/bin/env python3

from pexpect import pxssh
import getpass

ssh = pxssh.pxssh()

#passwd = getpass.getpass()
ssh.login('192.168.1.125','root','999ibm')
ssh.sendline('pidof java')
ssh.prompt()
print(ssh.before.decode('utf-8'))
ssh.logout()




