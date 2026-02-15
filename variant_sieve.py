
"""
Title: Bio-Variant Sieve (v1.0)
Author: [Pınar Öztürk]
Date: February 2026
Description: Automated pipeline for prioritizing rare pathogenic variants 
             using population frequency and functional effect filters.
"""






import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt

def varyant_filtreleme(dosya_yolu, frekans_esigi, homozigot_only):
    try:
        df = pd.read_csv(dosya_yolu)

        toplam_varyant = len(df)

        #Tablonun gnomAD_Freq sütunundaki değerler belirlenen değerden küçük mü?

        nadir = df[df['gnomAD_Freq'] <= frekans_esigi]
        if homozigot_only:
            nadir = nadir[nadir['Zygosity'] == 'Hom']
            #Eğer hem heterozigot hem de homozigot görmek istersen nadir = nadir[(nadir['Zygosity'] == 'Hom') | (nadir['Zygosity'] == 'Het')]

        patojenik = ["missense_variant", "frameshift_variant", "missense_variant"]

        adaylar = nadir[nadir['Effect'].isin(patojenik)]

         #Filtreleme sonrası kalan varyantlar için:
        elenecek_varyant_sayisi = toplam_varyant - len(adaylar)

        return adaylar, toplam_varyant, elenecek_varyant_sayisi
    except FileNotFoundError:
        print(f"Hata: '{dosya_yolu}' dosyası bulunamadı!")
        sys.exit(1)
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")
        sys.exit(1)



def main():
    parser = argparse.ArgumentParser(description="Nadir hastalık varyant önceliklendirme")
    parser.add_argument("--input", help="Analiz edilecek CSV dosyası", required=True)
    parser.add_argument("--freq", type=float, help="Maksimum gnomAD frekansı (örn: 0.001)", default=0.01)
    parser.add_argument("--homozigot", action="store_true", help="Sadece homozigot olanları getir")
    args = parser.parse_args()

    adaylar, toplam_varyant, elenecek_varyant_sayisi = varyant_filtreleme(args.input, args.freq, args.homozigot)
    print(f"Bulunan varyant sayisi: {adaylar}")
    print("\n--- Filtrelenmis Sonuclar ---")
    print(adaylar[['Gene', 'gnomAD_Freq', 'Effect']].head())

    labels = ['Filtrelenenler', 'Aday Varyantlar']
    sizes = [elenecek_varyant_sayisi, len(adaylar)]
    colors = ['#2D4F1E', '#4B3621']  # favori renklerim
    explode = (0, 0.1)
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title(f'Varyant Önceliklendirme: {toplam_varyant} Varyant İçinden')
    plt.savefig('variant_prioritization_summary.png')  # Grafiği PNG olarak kaydetmek için
    print("\nÖzet grafik 'variant_prioritization_summary.png' olarak kaydedildi.")
    plt.show()


if __name__ == "__main__":
    main()











