#!/usr/bin/env python3

from pexpect import pxssh
import datetime as dt

def ssh_login(ip,user,pw):
    try:
        ssh = pxssh.pxssh()
        ssh.login(ip, user, pw)
        ssh.sendline('pidof java')
        ssh.prompt()

        with open('pidjava.log', 'a') as f:
            f.write(str(dt.datetime.now()))
            f.write("\n")
            f.write(ip)
            f.write("\n")
            f.write(ssh.before.decode('utf-8'))

        ssh.logout()
        ssh.close()

        return True
    except pxssh.ExceptionPxssh:                
        return False
    

with open('sshid','r') as fin:
    for line in fin:
        (ip,user,pw) = line.split(" ")
        if ssh_login(ip,user,pw):
            print("Success!")
        else:
            print("check ip,username or password")