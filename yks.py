from fpdf import FPDF
import os

class Ogrenci:
    def __init__(self, isim, soyisim, mekan, tyt_net, ayt_net, hedefler, zayif_dersler, iyi_dersler, temel_bilgiler, ihtiyaçlar):
        self.isim = isim
        self.soyisim = soyisim
        self.mekan = mekan
        self.tyt_net = tyt_net
        self.ayt_net = ayt_net
        self.hedefler = hedefler
        self.zayif_dersler = zayif_dersler
        self.iyi_dersler = iyi_dersler
        self.temel_bilgiler = temel_bilgiler
        self.ihtiyaçlar = ihtiyaçlar

    def create_study_plan(self):
        günler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

        plan = f"{self.isim} {self.soyisim} için haftalık çalışma planı:\n\n"
        plan += f"Bölüm: {self.mekan}\n"
        plan += f"Hedef: {self.hedefler}\n\n"

        plan += "Güçlü Olduğun Konular:\n"
        for i in self.iyi_dersler:
            plan += f"- {i}\n"
        
        plan += "\nZayıf Olduğun Konular:\n"
        for i in self.zayif_dersler:
            plan += f"- {i}\n"

        plan += "\nTemel Bilgilerinin Olduğu Konular:\n"
        for i in self.temel_bilgiler:
            plan += f"- {i}\n"

        plan += "\nYapman Gerekenler:\n"
        for ihtiyaç in self.ihtiyaçlar:
            plan += f"- {ihtiyaç}\n"

        plan += "\n\nÖnerilen Haftalık Çalışma Programı:\n"

        for i, gün in enumerate(günler):
            plan += f"\n{gün}:\n"
            if i % 2 == 0:  # Çift günlerde zayıf olunan konulara ağırlık verelim
                plan += "  Sabah:\n"
                plan += "    - 08:00 - 10:00: Zayıf olduğun konularda konu çalış (2 saat)\n"
                plan += "    - 10:00 - 10:15: Ara\n"
                plan += "    - 10:15 - 11:15: Güçlü olduğun konularda test çöz (1 saat)\n"
                plan += "    - 11:15 - 11:30: Ara\n"
                plan += "    - 11:30 - 12:30: Matematikten 40 soru çöz (1 saat)\n"
                plan += "    - 12:30 - 13:30: Öğle Yemeği\n"
                plan += "  Öğleden Sonra:\n"
                plan += "    - 13:30 - 15:30: Fizik çalış (2 saat)\n"
                plan += "    - 15:30 - 15:45: Ara\n"
                plan += "    - 15:45 - 17:15: Kimya tekrar et (1.5 saat)\n"
                plan += "    - 17:15 - 17:30: Ara\n"
                plan += "    - 17:30 - 18:30: Biyolojiden 40 soru çöz (1 saat)\n"
                plan += "    - 18:30 - 18:45: Ara\n"
                plan += "    - 18:45 - 19:45: Yeni konular öğren (1 saat)\n"
            else:  # Tek günlerde güçlü olunan konulara pekiştirme yapalım
                plan += "  Sabah:\n"
                plan += "    - 08:00 - 10:00: Güçlü olduğun konularda test çöz (2 saat)\n"
                plan += "    - 10:00 - 10:15: Ara\n"
                plan += "    - 10:15 - 11:15: Eksik olduğun konularda pratik yap (1 saat)\n"
                plan += "    - 11:15 - 11:30: Ara\n"
                plan += "    - 11:30 - 12:30: Güçlü konularda 30 soru çöz (1 saat)\n"
                plan += "    - 12:30 - 13:30: Öğle Yemeği\n"
                plan += "  Öğleden Sonra:\n"
                plan += "    - 13:30 - 15:30: Yeni konular öğren (2 saat)\n"
                plan += "    - 15:30 - 15:45: Ara\n"
                plan += "    - 15:45 - 17:15: Zayıf konulara çalış (1.5 saat)\n"
                plan += "    - 17:15 - 17:30: Ara\n"
                plan += "    - 17:30 - 18:30: 50 soru çöz (1 saat)\n"
                plan += "    - 18:30 - 18:45: Ara\n"
                plan += "    - 18:45 - 19:45: Genel tekrar yap (1 saat)\n"

        return plan

    def save_as_pdf(self, dosya_yolu):
        pdf = FPDF()
        pdf.add_page()

        # Arial fontunu kullanarak ayarlama
        pdf.set_font("Arial", size=12)

        lines = self.create_study_plan().split("\n")
        for line in lines:
            pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True, align='L')

        pdf.output(dosya_yolu)
        if os.name == 'nt':  # Windows
            os.system(f"start {dosya_yolu}")
        else:  # macOS veya Linux
            os.system(f"xdg-open {dosya_yolu}")

def clas():
    print("YKS Çalışma Programı Oluşturucu\n")

    isim = input("Öğrencinin ismini girin: ")
    soyisim = input("Öğrencinin soyismini girin: ")
    mekan = input("Öğrencinin bölümü (Sayısal, Eşit Ağırlık, Sözel, Dil) girin: ")

    tyt_net = {
        "Matematik": int(input("TYT Matematik net sayısını girin: ")),
        "Fizik": int(input("TYT Fizik net sayısını girin: ")),
        "Kimya": int(input("TYT Kimya net sayısını girin: ")),
        "Biyoloji": int(input("TYT Biyoloji net sayısını girin: "))
    }
    
    ayt_net = {
        "Matematik": int(input("AYT Matematik net sayısını girin: ")),
        "Fizik": int(input("AYT Fizik net sayısını girin: ")),
        "Kimya": int(input("AYT Kimya net sayısını girin: ")),
        "Biyoloji": int(input("AYT Biyoloji net sayısını girin: "))
    }

    hedefler = input("Öğrencinin hedeflerini girin: ")
    zayif_dersler = input("Zayıf olduğu dersleri (virgül ile ayırarak) girin: ").split(',')
    iyi_dersler = input("Güçlü olduğu dersleri (virgül ile ayırarak) girin: ").split(',')
    temel_bilgiler = input("Temel bilgileri olan konuları (virgül ile ayırarak) girin: ").split(',')
    ihtiyaçlar = input("Yapması gerekenler (virgül ile ayırarak) girin: ").split(',')

    ogrenci = Ogrenci(isim, soyisim, mekan, tyt_net, ayt_net, hedefler, zayif_dersler, iyi_dersler, temel_bilgiler, ihtiyaçlar)
    
    # PDF'yi masaüstüne kaydet
    dosya_yolu = os.path.join(os.path.expanduser("~/Desktop"), f"{isim}_{soyisim}_calisma_plani.pdf")
    ogrenci.save_as_pdf(dosya_yolu)
    print(f"Çalışma planı '{dosya_yolu}' olarak kaydedildi.")

if __name__ == "__main__":
    clas()
