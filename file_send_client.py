# coding=utf-8
import socket
import cv2
import base64

#サーバ側に送信する物をバイト型に変換
def conver(name,extens):
    f = open(name+'.'+extens, 'rb').read()
    f_conver=base64.b64encode(f)
    #f.close()
    return f_conver

#文字列を指定の数ずつに区切る
def split_str(s, n):
    "split string by its length"
    #sorce by http://yak-shaver.blogspot.jp/2013/08/blog-post.html
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

host = "127.0.0.1"
port = 1270

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

filename=input("サーバに送信したいファイル名(拡張子を含む)->").split(".")
name=filename[0]
extens=filename[1]
conver_byte = conver(name,extens)
conver_byte_split = split_str(conver_byte,150)

client.send(extens.encode())
response = client.recv(1024)

while True:
    if response.decode() == "start":
        for i in conver_byte_split:
            client.send(i)
        break
    else:
        print(response.decode())
        split_len = len(conver_byte_split)
        client.send(str(split_len).encode())
        response = client.recv(1024)

client.close()