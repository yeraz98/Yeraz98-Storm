# ⚡ Yeraz98 Storm ⚡

Bu araç **yeraz98** tərəfindən hazırlanmış, Python əsaslı güclü bir şəbəkə analiz və test alətidir.

---

## 📥 Quraşdırılma Qaydası (Installation)

Aracı ilk dəfə istifadə edirsinizsə, Termux terminalına bu əmri kopyalayıb yapışdırın:

```bash
pkg update && pkg upgrade -y && pkg install git python -y && git clone https://github.com/yeraz98/Yeraz98-Storm && cd Yeraz98-Storm && bash setup.sh
```

---

## 🚀 İşə Salma Qaydası (Usage)

Aracı işə salmaq üçün mütləq bir **HƏDƏF** (IP və ya Sayt) qeyd etməlisiniz. Əks halda "IndexError" xətası alacaqsınız.

### 1. Əgər qovluğun içindəsinizsə:
```bash
python storm.py <HƏDƏF_ADI>
```

### 2. Termux-u yeni açmısınızsa (Qısa yol):
```bash
cd ~/Yeraz98-Storm && python storm.py <HƏDƏF_ADI>
```

> **Nümunə istifadə:**
> `python storm.py google.com`  yaxud  `python storm.py 1.1.1.1`

---

## 📂 Fayllar və Funksiyalar
* **storm.py** - Əsas icraedici proqram.
* **setup.sh** - Lazımi kitabxanaların avtomatik quraşdırılması.
* **turbo.sh** - Sürətləndirmə modulu.

---
👤 **Developer:** [yeraz98](https://github.com/yeraz98)
