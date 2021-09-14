
import paramiko
import os
import getpass

def movethemfiles(conn, remote_dir):
    for x in 

def main():
    while True:
        try:
            ip= input('Ip Address:\n>')
            user= input('Username:\n>')
            remote_dir= input("Remote host target directory:\n>")
            password =getpass.getpass()

            t = paramiko.Transport(ip, 22)
            t.connect(username=user, password=getpass.getpass())
            sftp = paramiko.SFTPClient.from_transport(t)


            sftp.stat(remote_dir)

            movethemfiles(sftp, remote_dir)
            sftp.close()
        except ValueError:
            print("This is a error")

