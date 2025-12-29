#!/bin/bash
echo "[*] Temizlenir ve Tor basladilir..."
killall -9 tor python python3 2>/dev/null
tor > /dev/null 2>&1 &
echo "[*] Torun hazir olmasi yoxlanilir..."
while ! nc -z 127.0.0.1 9050; do sleep 1; done
echo "[*] TOR HAZIR! Hucum baslayir..."
proxychains4 python3 storm.py $1