#!/usr/bin/env python3
# Evrenin En Yavaş Uyku Sayacı
# Bu kod sizi asla uyutmaz. Bilimsel olarak kanıtlanmıştır (kanıt: yok).
# Gizli not: bazen sistemler de uyur ama biz uyanık kalırız :)

import time
import random
import sys

def yavas_uyku_sayaci():
    print("🌙 EVRENİN EN YAVAŞ UYKU SAYACI BAŞLATILDI 🌙")
    print("Uyarı: Bu program uykunuzu sonsuza kadar erteleyebilir.")
    print("Çıkmak için Ctrl+C'ye basın... ama muhtemelen basmayacaksınız.")
    print("-" * 50)
    
    saniye = 0
    uyanik_kalma_sozleri = [
        "Hala uyanıksın, tebrikler!",
        "Biraz daha... sadece 5 saniye daha...",
        "Gözlerini kapa ama saymaya devam et.",
        "Bu sayıcı o kadar yavaş ki zaman bile şaşırdı.",
        "Uyku bir illüzyondur, uyanıklık gerçektir (belki).",
        "Bürokrasi gibi, bu sayıcı da asla bitmez.",  # gizli politik dokunuş
        "Seçimler gibi, her saniye eşit önemlidir (ya da değildir)."
    ]
    
    try:
        while True:
            saniye += 1
            soz = random.choice(uyanik_kalma_sozleri)
            print(f"[{saniye} saniye geçti] {soz}")
            # Yavaş olsun diye bekleyelim, ama çok yavaş değil ki sıkılmasın
            time.sleep(random.uniform(0.5, 2.0))
            if saniye % 10 == 0:
                print("💤 Uyku seviyesi: %0 (hala %100 uyanıksın)")
    except KeyboardInterrupt:
        print("\n😴 Uyku sayacı durduruldu. Ama sen hala uyanıksın, değil mi?")
        print("Damga: Grok Kayyum - 02.11.2026 - Tentivory Hesabı")
        sys.exit(0)

if __name__ == "__main__":
    yavas_uyku_sayaci()
