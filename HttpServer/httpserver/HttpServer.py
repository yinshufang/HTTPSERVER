#coding=utf-8
'''
name:yin
time:20180930
'''
from socket import * 
import  sys
import re
from threading import Thread
from setting import *
import time

class HTTPServer(object):
    def __init__(self,addr=('0.0.0.0',80)):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.addr=addr
        self.bind(addr)




    def bind(self,addr):
        self.ip=addr[0]
        self.port=addr[1]
        self.sockfd.bind(addr)
    #http服务器启动
    def serve_forever(self):
        self.sockfd.listen(5)
        print('listen the port %d...'%self.port)
        while True:
            connfd,addr=self.sockfd.accept()
            print('connect from ',addr)
            handle_client=Thread(target=self.handle_request,args=(connfd,))
            handle_client.start()

    def handle_request(self,connfd):
        #接收请求
        request=connfd.recv(4096)
        request_lines=request.splitlines()
        #获取请求行
        request_line=request_lines[0].decode()

        #正则表达式提取请求方法和请求内容
        pattern=r'(?P<METHOD>[A-Z]+)\s+(?P<PATH>/\S*)'
        try:
            env=re.match(pattern,request_line).groupdict()
        except:
            response_headlers="HTTP/1.1 500 Server Error"
            response_headlers+='\r\n'
            response_body='Server Error'
            response=response_headlers+response_body
            connfd.send(response.encode())
            return
        #将请求发送给frame得到返回结果
        status,reponse_body=self.send_request(env['METHOD'],env['PATH'])
        #根据响应马组织响应头内容
        reponse_headlers=self.get_headlers(status)
        reponse=reponse_headlers+reponse_body
        connfd.send(reponse.encode())
        connfd.close()
    #和frame交互　发送request 获取request
    def send_request(self,method,path):
        s=socket()
        s.connect(frame_addr)
        #向webframe发送method  path
        s.send(method.encode())
        time.sleep(0.1)
        s.send(path.encode())

        status=s.recv(128).decode()

        
        reponse_body=s.recv(40960).decode()


        return status,reponse_body

    def get_headlers(self,status):
        if status=='200':
            reponse_headlers="HTTP/1.1 200 OK\r\n"
            reponse_headlers+='\r\n'
        elif status=='404':
            reponse_headlers="HTTP/1.1 404 Not Found\r\n"
            reponse_headlers+='\r\n'            
        return reponse_headlers

if __name__=='__main__':
    httpd=HTTPServer(ADDR)
    httpd.serve_forever()