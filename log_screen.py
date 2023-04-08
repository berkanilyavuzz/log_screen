import tkinter as tk

kullanıcı_Adı = ["BERK","ESRA","SENA","ŞEVVAL","TUANA","FURKAN","YASİN","NAGEHAN","BURAK","MELİHA","ALPER"]
kullanıcı_Sifre = ["Extremis3.0"]

pencere = tk.Tk()
pencere.title("Giriş Ekranı")

tk.Label(pencere, text="Kullanıcı Adı Giriniz:").grid(row=0, column=0)
tk.Label(pencere, text="Şifre Giriniz:").grid(row=1, column=0)

ad_giriş = tk.Entry(pencere)
şifre_giriş = tk.Entry(pencere, show="*")

def basarisiz_giris():
    hata_mesajı = "Kullanıcı adı veya Şifre hatalı"
    uyarı = tk.Toplevel()
    uyarı.title("Hata")
    tk.Label(uyarı, text=hata_mesajı).pack()
    tk.Button(uyarı, text="Tamam", command=uyarı.destroy).pack()

def basarili_giris():
    isim = ad_giriş.get()
    sifre = şifre_giriş.get()
    if isim in kullanıcı_Adı and sifre in kullanıcı_Sifre:
        basarili_mesaj = "Giriş Başarılı"
        tk.Label(pencere, text=basarili_mesaj).grid(row=3, column=0, columnspan=2)
    else:
        basarisiz_giris()

tk.Button(pencere, text="Giriş", command=basarili_giris).grid(row=2, column=0, columnspan=2)
ad_giriş.grid(row=0, column=1)
şifre_giriş.grid(row=1, column=1)

pencere.mainloop()
