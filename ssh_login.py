#!/usr/bin/env python3

from pexpect import pxssh
import getpass

try:
    ssh = pxssh.pxssh()
    #passwd = getpass.getpass()
    ssh.login('52.74.188.31','root',ssh_key="/home/shao/.ssh/cobain-singapore.pem")
    ssh.sendline('date')
    ssh.prompt()
    print(ssh.before.decode('utf-8'))
    ssh.logout()
    ssh.close()
except pxssh.ExceptionPxssh:
    print("check ip,username or password")



