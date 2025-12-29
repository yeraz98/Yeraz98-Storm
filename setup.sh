#!/bin/bash
pkg update && pkg upgrade -y
pkg install python tor proxychains-ng git -y
echo "StrictChain
proxy_dns
remote_dns_res
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
socks5 127.0.0.1 9050" > /data/data/com.termux/files/usr/etc/proxychains.conf
chmod +x turbo.sh
echo "Qurasdirma tamamlandi!"