# 🧬 Bio-Variant Sieve: Automated NGS Prioritization Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Bioinformatics](https://img.shields.io/badge/field-Bioinformatics-green)](https://en.wikipedia.org/wiki/Bioinformatics)

**Bio-Variant Sieve**, büyük ölçekli NGS (Next-Generation Sequencing) verilerinden nadir ve potansiyel patojenik varyantları hızlıca ayıklamak için geliştirilmiş bir komut satırı aracıdır. Özellikle nadir hastalık araştırmalarında "aday gen" belirleme sürecini otomatize eder.

## 🛠️ Temel Özellikler
* **Frekans Filtrelemesi:** gnomAD veritabanı üzerinden populasyon frekansı (AF) bazlı süzme.
* **Zygosity Analizi:** Otozomal resesif modeller için homozigot varyant izolasyonu.
* **Fonksiyonel Etki Önceliklendirme:** `stop_gained`, `frameshift` ve `missense` varyantlarını otomatik yakalama.
* **Görsel Raporlama:** Analiz sonuçlarını anlık olarak profesyonel grafiklere (Matplotlib) dönüştürme.

## 📊 Örnek Analiz Çıktısı
Aşağıdaki grafik, 10.000+ varyant içeren bir ham verinin bu araçla süzülmüş halini göstermektedir:

![Varyant Analiz Özeti](variant_prioritization_summary.png)

## 🚀 Kurulum ve Kullanım

### Kurulum
```bash
git clone [https://github.com/](https://github.com/)[Kullanıcı-Adın]/Variant-Sieve.git
cd Variant-Sieve
pip install -r requirements.txt
###Kullanım
python variant_sieve.py --input test_data.csv --freq 0.001 --homozigot
