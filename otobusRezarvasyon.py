import datetime
import random

print("Otobüs Koltuk Rezarvasyon Sistemi By DevSeu")

# Koltuk bilgilerini içeren koltuk sözlüğü
# Koltuk numaraları ve bu koltuklara ait bilgilerin saklandığı bir sözlük yapısı kullanılmış.
koltuk = {
    1: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    2: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    3: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    4: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    5: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    6: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    7: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    8: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    9: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    10: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    11: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    12: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    13: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    14: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    15: {"Koltuk Türü": "Normal Koltuk", "durum": "Boş"},
    16: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    17: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    18: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    19: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    20: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    21: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    22: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    23: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    24: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    25: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    26: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    27: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    28: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    29: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    30: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    31: {"Koltuk Türü": "PS5 Koltuk", "durum": "Boş"},
    32: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    33: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    34: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    35: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    36: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    37: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    38: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    39: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    40: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    41: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    42: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    43: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    44: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    45: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    46: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
    47: {"Koltuk Türü": "PS5 Yataklı Koltuk", "durum": "Boş"},
}

yemekSistemi = [
    {"isim": "Kıymalı Pide", "fiyat": 25.99},
    {"isim": "Mercimek Çorbası", "fiyat": 10.50},
    {"isim": "Fırında Tavuk", "fiyat": 35.75},
    {"isim": "Baklava", "fiyat": 12.25},
    {"isim": "İskender Kebap", "fiyat": 40.00},
    {"isim": "Pilav Üstü Tavuk", "fiyat": 28.00},
    {"isim": "Köfte", "fiyat": 22.00},
    {"isim": "Mantı", "fiyat": 19.99},
    {"isim": "Etli Pide", "fiyat": 29.99},
    {"isim": "Yoğurtlu Kebap", "fiyat": 38.50},
    {"isim": "Adana Kebap", "fiyat": 34.00},
    {"isim": "Kuzu Tandır", "fiyat": 45.00},
    {"isim": "Pirinç Pilavı", "fiyat": 8.50},
    {"isim": "Izgara Levrek", "fiyat": 42.00},
    {"isim": "Beyti Kebap", "fiyat": 32.50},
    {"isim": "Su Böreği", "fiyat": 17.99},
    {"isim": "Lahmacun", "fiyat": 4.50},
    {"isim": "Cacık", "fiyat": 6.00},
    {"isim": "Kabak Tatlısı", "fiyat": 9.99},
    {"isim": "Şiş Kebap", "fiyat": 37.50},
    {"isim": "Kuzu Şiş", "fiyat": 42.00},
    {"isim": "Kahvaltı Tabağı", "fiyat": 20.00},
    {"isim": "Köz Patlıcanlı Ezme", "fiyat": 11.50},
    {"isim": "Karnabahar Kızartması", "fiyat": 13.50},
    {"isim": "Köri Soslu Tavuk", "fiyat": 36.00},
    {"isim": "Kıymalı Pide", "fiyat": 25.99},
    {"isim": "Mercimek Çorbası", "fiyat": 10.50},
    {"isim": "Fırında Tavuk", "fiyat": 35.75},
    {"isim": "Baklava", "fiyat": 12.25},
    {"isim": "Karnıyarık", "fiyat": 27.50},
    {"isim": "İskender Kebap", "fiyat": 40.00},
    {"isim": "Pilav Üstü Tavuk", "fiyat": 28.00},
    {"isim": "Kadayıf", "fiyat": 14.50},
    {"isim": "Köfte", "fiyat": 22.00},
    {"isim": "Mantı", "fiyat": 19.99},
    {"isim": "Etli Pide", "fiyat": 29.99},
    {"isim": "Yoğurtlu Kebap", "fiyat": 38.50},
    {"isim": "Adana Kebap", "fiyat": 34.00},
    {"isim": "Kuzu Tandır", "fiyat": 45.00},
    {"isim": "Pirinç Pilavı", "fiyat": 8.50},
    {"isim": "Kuru Fasulye", "fiyat": 12.50},
    {"isim": "Izgara Levrek", "fiyat": 42.00},
    {"isim": "Beyti Kebap", "fiyat": 32.50},
    {"isim": "Su Böreği", "fiyat": 17.99},
    {"isim": "Lahmacun", "fiyat": 4.50},
    {"isim": "Cacık", "fiyat": 6.00},
    {"isim": "Kabak Tatlısı", "fiyat": 9.99},
    {"isim": "Şiş Kebap", "fiyat": 37.50},
    {"isim": "Kuzu Şiş", "fiyat": 42.00},
    {"isim": "Somon Izgara", "fiyat": 39.99},
    {"isim": "Tavuklu Salata", "fiyat": 16.50},
    {"isim": "Kahvaltı Tabağı", "fiyat": 20.00},
    {"isim": "Köz Patlıcanlı Ezme", "fiyat": 11.50},
    {"isim": "Karnabahar Kızartması", "fiyat": 13.50},
    {"isim": "Köri Soslu Tavuk", "fiyat": 36.00},
    {"isim": "Köri Soslu Sebzeler", "fiyat": 18.50},
    {"isim": "Sebzeli Noodle", "fiyat": 21.50},
    {"isim": "Kremalı Mantar Çorbası", "fiyat": 12.75},
    {"isim": "Somon Izgara", "fiyat": 45.00},
    {"isim": "Kıymalı Börek", "fiyat": 16.50},
    {"isim": "Tavuklu Salata", "fiyat": 19.25},
    {"isim": "Kırmızı Et Güveç", "fiyat": 38.50},
    {"isim": "Tavuklu Pilav", "fiyat": 24.99},
    {"isim": "Elmalı Kurabiye", "fiyat": 10.50},
    {"isim": "Kuru Fasulye", "fiyat": 18.00},
    {"isim": "Sütlaç", "fiyat": 14.99},
    {"isim": "Sebzeli Pizza", "fiyat": 26.75},
    {"isim": "Acılı Kebap", "fiyat": 32.00},
    {"isim": "Közlenmiş Patlıcan Salatası", "fiyat": 15.50},
    {"isim": "Meksika Çorbası", "fiyat": 13.99},
    {"isim": "Ispanaklı Börek", "fiyat": 16.50},
    {"isim": "Fırında Levrek", "fiyat": 42.00},
    {"isim": "Tavuk Şinitzel", "fiyat": 29.50},
    {"isim": "Muzlu Kek", "fiyat": 11.50},
    {"isim": "Bulgur Pilavı", "fiyat": 17.00},
    {"isim": "Pancar Salatası", "fiyat": 12.99},
    {"isim": "Kıymalı Ispanak", "fiyat": 21.50},
    {"isim": "Fırında Kaşarlı Tavuk", "fiyat": 34.00},
    {"isim": "Elma Kompostosu", "fiyat": 9.50},
    {"isim": "Zeytinyağlı Dolma", "fiyat": 18.50},
    {"isim": "Peynirli Börek", "fiyat": 16.50},
    {"isim": "Tavuklu Mantar Sote", "fiyat": 26.99},
    {"isim": "Brokoli Çorbası", "fiyat": 12.50},
    {"isim": "Fırında Tavuklu Makarna", "fiyat": 29.75},
    {"isim": "Muzlu Milkshake", "fiyat": 13.50},
    {"isim": "Köfteli Yoğurtlu Patates", "fiyat": 23.50},
    {"isim": "Çikolatalı Kek", "fiyat": 11.50},
    {"isim": "Fettuccine Alfredo", "fiyat": 28.50},
    {"isim": "Köfte Izgara", "fiyat": 22.75},
    {"isim": "Bakla Yemeği", "fiyat": 16.99},
    {"isim": "Tavuk Kebap", "fiyat": 27.00},
    {"isim": "Makarna Salatası", "fiyat": 18.50},
    {"isim": "Türlü", "fiyat": 21.99},
    {"isim": "Tavuklu Nohut Salatası", "fiyat": 19.50},
    {"isim": "Mantarlı Omlet", "fiyat": 14.75},
    {"isim": "Kıymalı Ekmek Kadayıfı", "fiyat": 16.50},
    {"isim": "Tavuklu Tost", "fiyat": 22.00},
    {"isim": "Kereviz Kökü Salatası", "fiyat": 15.99},
    {"isim": "Fırında Somon", "fiyat": 42.50},
    {"isim": "Sebzeli Güveç", "fiyat": 25.00},
    {"isim": "Tavuklu Biber Dolması", "fiyat": 22.99},
    {"isim": "Pırasa Yemeği", "fiyat": 19.50},
    {"isim": "Hünkar Beğendi", "fiyat": 32.50},
    {"isim": "Köfteli Pilav", "fiyat": 24.50},
    {"isim": "Meksika Usulü Tavuklu Quesadilla", "fiyat": 29.99},
    {"isim": "Kıymalı Karnabahar Yemeği", "fiyat": 21.50},
    {"isim": "Kavurma", "fiyat": 28.50},
    {"isim": "Közlenmiş Patlıcanlı Kebap", "fiyat": 34.50},
    {"isim": "Peynirli Tost", "fiyat": 18.50},
    {"isim": "Kıymalı Enginar Yemeği", "fiyat": 22.99},
    {"isim": "Sebzeli Omlet", "fiyat": 14.75},
    {"isim": "Tavuklu Makarna", "fiyat": 23.50},
    {"isim": "Fırında Tavuklu Patates", "fiyat": 29.50},
    {"isim": "Karnıyarık", "fiyat": 21.99},
    {"isim": "Tavuklu Börek", "fiyat": 19.50},
    {"isim": "Fırında Patatesli Kıymalı Yemek", "fiyat": 26.50},
    {"isim": "Kahvaltılık Omlet", "fiyat": 15.75},
    {"isim": "Kremalı Brokoli Çorbası", "fiyat": 15.99},
    {"isim": "Közlenmiş Patlıcan Mezesi", "fiyat": 14.50},
    {"isim": "Deniz Mahsüllü Risotto", "fiyat": 32.00},
    {"isim": "Sebzeli Pizza", "fiyat": 26.50},
    {"isim": "Köfteli Bulgur Pilavı", "fiyat": 19.99},
    {"isim": "Karidesli Noodle", "fiyat": 29.50},
    {"isim": "Sarma", "fiyat": 21.00},
    {"isim": "Tavuklu Mantar Sote", "fiyat": 23.99},
    {"isim": "Patates Kızartması", "fiyat": 8.50},
    {"isim": "Izgara Köfte Salatası", "fiyat": 18.50},
    {"isim": "Fırında Patlıcanlı Tavuk", "fiyat": 29.50},
    {"isim": "Kıymalı Biber Dolması", "fiyat": 22.99},
    {"isim": "Nohutlu Yaprak Sarma", "fiyat": 20.50},
    {"isim": "Peynirli Pide", "fiyat": 17.50},
    {"isim": "Fırında Levrek", "fiyat": 38.50},
    {"isim": "Sebzeli Dürüm", "fiyat": 21.50},
    {"isim": "Kıymalı Kuru Fasulye", "fiyat": 19.99},
    {"isim": "Közlenmiş Kırmızı Biberli Patates Salatası", "fiyat": 13.50},
    {"isim": "Kremalı Tavuklu Mantar Soslu Penne", "fiyat": 27.50},
    {"isim": "Kıymalı Ispanak Yemeği", "fiyat": 21.99},
    {"isim": "Közlenmiş Patlıcanlı Izgara Tavuk", "fiyat": 32.50},
    {"isim": "Sebzeli Börek", "fiyat": 18.99},
    {"isim": "Fırında Tavuklu Kabak Yemeği", "fiyat": 28.50},
    {"isim": "Fırında Peynirli Makarna", "fiyat": 24.50},
    {"isim": "Tavuklu Cacık", "fiyat": 16.50},
    {"isim": "Tereyağlı Ekmek", "fiyat": 7.50},
    {"isim": "Izgara Köfte", "fiyat": 22.50},
    {"isim": "Kıymalı Lahana Sarması", "fiyat": 21.50},
    {"isim": "Fırında Kıymalı Sebzeli Yemek", "fiyat": 26.50},
    {"isim": "Tavuklu Makarna", "fiyat": 24.99},
    {"isim": "Beyaz Peynirli Salata", "fiyat": 12.50},
    {"isim": "Köfte Izgara", "fiyat": 28.50},
    {"isim": "Kremalı Mantar Çorbası", "fiyat": 14.99},
    {"isim": "Fırında Tavuklu Patates", "fiyat": 27.50},
    {"isim": "Kıymalı Mantı", "fiyat": 23.50},
    {"isim": "Izgara Tavuk Şiş", "fiyat": 32.00},
    {"isim": "Sebzeli Noodle", "fiyat": 19.50},
    {"isim": "Zeytinyağlı Kuru Fasulye", "fiyat": 17.99},
    {"isim": "Çıtır Tavuk", "fiyat": 21.50},
    {"isim": "Közlenmiş Patlıcanlı Tavuk Şiş", "fiyat": 29.50},
    {"isim": "Lahmacun", "fiyat": 15.99},
    {"isim": "Izgara Karides", "fiyat": 34.50},
    {"isim": "Peynirli Omlet", "fiyat": 13.50},
    {"isim": "Fırında Kaşarlı Patates", "fiyat": 11.99},
    {"isim": "Zeytinyağlı Enginar", "fiyat": 25.50},
    {"isim": "Kıymalı Bezelye Yemeği", "fiyat": 18.99},
    {"isim": "Fırında Tavuklu Mantar Sote", "fiyat": 26.50},
    {"isim": "Közlenmiş Kırmızı Biberli Patates", "fiyat": 13.50},
    {"isim": "Tavuklu Pilav", "fiyat": 21.99},
    {"isim": "Kıymalı Enginar Dolması", "fiyat": 27.50},
    {"isim": "Tavuklu Pizza", "fiyat": 26.50},
    {"isim": "Izgara Dana Bonfile", "fiyat": 42.50},
    {"isim": "Kıymalı Yaprak Sarma", "fiyat": 20.50},
    {"isim": "Fırında Sebzeli Tavuk", "fiyat": 28.50},
    {"isim": "Közlenmiş Patlıcanlı Et Sote", "fiyat": 36.50},
    {"isim": "Domatesli Bulgur Pilavı", "fiyat": 15.99},
    {"isim": "Kıymalı Taze Fasulye", "fiyat": 19.50},
    {"isim": "Fırında Karides", "fiyat": 36.50},
    {"isim": "Tavuklu Çorba", "fiyat": 12.99},
    {"isim": "Muhallebi", "fiyat": 4.99},
    {"isim": "Sütlaç", "fiyat": 4.99},
    {"isim": "Tulumba", "fiyat": 4.99},
    {"isim": "Revani", "fiyat": 5.99},
    {"isim": "Baklava", "fiyat": 7.99},
    {"isim": "Kadayıf", "fiyat": 7.99},
    {"isim": "Künefe", "fiyat": 8.99},
    {"isim": "Lokum", "fiyat": 4.99},
    {"isim": "Akide Şekeri", "fiyat": 2.99},
    {"isim": "Pestil", "fiyat": 4.99},
    {"isim": "Sucuk", "fiyat": 6.99},
    {"isim": "Pastırma", "fiyat": 10.99},
    {"isim": "Kavurma", "fiyat": 12.99},
]

icecekSistemi = [
    {"isim": "Kola", "fiyat": 5.99},
    {"isim": "Ayran", "fiyat": 2.99},
    {"isim": "Limonata", "fiyat": 4.99},
    {"isim": "Meyve Suyu", "fiyat": 6.99},
    {"isim": "Su", "fiyat": 1.99},
    {"isim": "Gazoz", "fiyat": 5.99},
    {"isim": "Çay", "fiyat": 2.99},
    {"isim": "Kahve", "fiyat": 7.99},
    {"isim": "Mocha", "fiyat": 8.99},
    {"isim": "Latte", "fiyat": 9.99},
    {"isim": "Sıcak Çikolata", "fiyat": 6.99},
    {"isim": "Soda", "fiyat": 3.99},
    {"isim": "Cappy Portakal Suyu", "fiyat": 7.99},
    {"isim": "Sprite", "fiyat": 5.99},
    {"isim": "Fanta", "fiyat": 5.99},
    {"isim": "Iced Tea", "fiyat": 6.99},
    {"isim": "Mango Lassi", "fiyat": 8.99},
    {"isim": "Ginger Ale", "fiyat": 4.99},
    {"isim": "Vitaminli Su", "fiyat": 7.99},
    {"isim": "Enerji İçeceği", "fiyat": 9.99},
    {"isim": "Maden Suyu", "fiyat": 2.99},
    {"isim": "Kahve Likörü", "fiyat": 12.99},
    {"isim": "Çilekli Smoothie", "fiyat": 8.99},
    {"isim": "Mango Smoothie", "fiyat": 8.99},
    {"isim": "Karpuzlu Iced Tea", "fiyat": 7.99},
    {"isim": "Cappuccino", "fiyat": 9.99},
    {"isim": "Turkish Coffee", "fiyat": 6.99},
    {"isim": "Milkshake", "fiyat": 10.99},
    {"isim": "Hot Chocolate", "fiyat": 6.99},
    {"isim": "Irish Coffee", "fiyat": 12.99},
    {"isim": "Americano", "fiyat": 7.99},
    {"isim": "Mojito", "fiyat": 11.99},
    {"isim": "Bloody Mary", "fiyat": 12.99},
    {"isim": "Sangria", "fiyat": 14.99},
    {"isim": "Cosmopolitan", "fiyat": 11.99},
    {"isim": "Margarita", "fiyat": 12.99},
    {"isim": "Gin Fizz", "fiyat": 10.99},
    {"isim": "Coca-Cola", "fiyat": 3.50},
    {"isim": "Pepsi", "fiyat": 3.25},
    {"isim": "Sprite", "fiyat": 3.00},
    {"isim": "Fanta", "fiyat": 3.00},
    {"isim": "Ayran", "fiyat": 2.50},
    {"isim": "Limonata", "fiyat": 3.50},
    {"isim": "Soğuk Çay", "fiyat": 4.00},
    {"isim": "Sıcak Çikolata", "fiyat": 5.25},
    {"isim": "Kahve", "fiyat": 4.50},
    {"isim": "Latte", "fiyat": 6.00},
    {"isim": "Mocha", "fiyat": 6.50},
    {"isim": "Americano", "fiyat": 5.50},
    {"isim": "Espresso", "fiyat": 3.50},
    {"isim": "Turk Kahvesi", "fiyat": 4.00},
    {"isim": "Sıcak Su", "fiyat": 1.50},
    {"isim": "Buzlu Çay", "fiyat": 4.00},
    {"isim": "Meyveli Soda", "fiyat": 3.75},
    {"isim": "Limonlu Soda", "fiyat": 3.00},
    {"isim": "Portakallı Soda", "fiyat": 3.25},
    {"isim": "Greyfurtlu Soda", "fiyat": 3.25},
    {"isim": "Kış Çayı", "fiyat": 4.25},
    {"isim": "Ihlamur Çayı", "fiyat": 3.50},
    {"isim": "Ada Çayı", "fiyat": 3.75},
    {"isim": "Yeşil Çay", "fiyat": 4.00},
    {"isim": "Sıcak Elma Çayı", "fiyat": 4.50},
    {"isim": "Salep", "fiyat": 5.50},
    {"isim": "Boza", "fiyat": 4.00},
    {"isim": "Mango Smoothie", "fiyat": 6.75},
    {"isim": "Çilek Smoothie", "fiyat": 6.50},
    {"isim": "Karışık Meyve Smoothie", "fiyat": 7.00},
    {"isim": "Milkshake", "fiyat": 6.25},
    {"isim": "Vanilyalı Milkshake", "fiyat": 6.50},
    {"isim": "Çikolatalı Milkshake", "fiyat": 6.50},
    {"isim": "Karamel Milkshake", "fiyat": 6.75},
    {"isim": "Muzlu Milkshake", "fiyat": 6.50},
    {"isim": "Portakallı Milkshake", "fiyat": 6.75},
    {"isim": "Mojito", "fiyat": 13.99},
    {"isim": "Cosmopolitan", "fiyat": 11.99},
    {"isim": "Long Island Iced Tea", "fiyat": 12.99},
    {"isim": "Tequila Sunrise", "fiyat": 9.99},
    {"isim": "Pina Colada", "fiyat": 10.99},
    {"isim": "Black Russian", "fiyat": 9.99},
    {"isim": "White Russian", "fiyat": 10.99},
    {"isim": "Bellini", "fiyat": 12.99},
    {"isim": "Screwdriver", "fiyat": 8.99},
    {"isim": "Dark 'N' Stormy", "fiyat": 11.99},
    {"isim": "Bloody Mary", "fiyat": 10.99},
    {"isim": "Mai Tai", "fiyat": 14.99},
    {"isim": "Mimosa", "fiyat": 10.99},
    {"isim": "Negroni", "fiyat": 12.99},
    {"isim": "Aperol Spritz", "fiyat": 11.99},
    {"isim": "Gimlet", "fiyat": 10.99},
    {"isim": "Whiskey Sour", "fiyat": 11.99},
    {"isim": "French 75", "fiyat": 13.99},
    {"isim": "Singapore Sling", "fiyat": 12.99},
    {"isim": "Sangria", "fiyat": 11.99},
    {"isim": "Martini", "fiyat": 12.99},
    {"isim": "Manhattan", "fiyat": 11.99},
    {"isim": "Sidecar", "fiyat": 13.99},
    {"isim": "Margarita", "fiyat": 12.99},
    {"isim": "Gin Fizz", "fiyat": 10.99},
    {"isim": "Rum and Coke", "fiyat": 9.99},
    {"isim": "Daiquiri", "fiyat": 10.99},
    {"isim": "Tom Collins", "fiyat": 9.99},
    {"isim": "Mudslide", "fiyat": 12.99},
    {"isim": "Alabama Slammer", "fiyat": 11.99},
    {"isim": "Zombie", "fiyat": 14.99},
    {"isim": "Sazerac", "fiyat": 12.99},
    {"isim": "Corpse Reviver", "fiyat": 13.99},
    {"isim": "Aviation", "fiyat": 11.99},
    {"isim": "Bourbon Sour", "fiyat": 11.99},
    {"isim": "Cuba Libre", "fiyat": 8.99},
    {"isim": "Mango Lassi", "fiyat": 7.99},
    {"isim": "Kir Royale", "fiyat": 14.99},
    {"isim": "Lemon Drop", "fiyat": 11.99},
    {"isim": "Peach Bellini", "fiyat": 12.99},
    {"isim": "Ayran", "fiyat": 2.99},
    {"isim": "Şalgam Suyu", "fiyat": 3.99},
    {"isim": "Boza", "fiyat": 4.99},
    {"isim": "Salep", "fiyat": 5.99},
    {"isim": "Limonata", "fiyat": 6.99},
    {"isim": "Sahlep", "fiyat": 7.99},
    {"isim": "Demli Çay", "fiyat": 1.99},
    {"isim": "Ayva Şarabı", "fiyat": 9.99},
    {"isim": "Meyankökü Şerbeti", "fiyat": 4.99},
    {"isim": "Boğma Rakı", "fiyat": 24.99},
    {"isim": "Köpüklü İçecek", "fiyat": 2.99},
    {"isim": "Uludağ Gazozu", "fiyat": 3.99},
    {"isim": "Şıra", "fiyat": 4.99},
    {"isim": "Kahve Türk", "fiyat": 5.99},
    {"isim": "Kahve Filtre", "fiyat": 6.99},
    {"isim": "Cezve İçi Türk Kahvesi", "fiyat": 7.99},
    {"isim": "Elma Şerbeti", "fiyat": 2.99},
    {"isim": "Naneli Limonata", "fiyat": 4.99},
    {"isim": "Kış Çayı", "fiyat": 3.99},
    {"isim": "Sade Soda", "fiyat": 1.99},
    {"isim": "Tuzlu Ayran", "fiyat": 3.99},
    {"isim": "Türk Meyve Suyu", "fiyat": 5.99},
    {"isim": "Limonlu Çay", "fiyat": 2.99},
    {"isim": "Tarçınlı Türk Kahvesi", "fiyat": 6.99},
    {"isim": "Kara Dut Şerbeti", "fiyat": 4.99},
    {"isim": "Cevizli Boza", "fiyat": 7.99},
    {"isim": "Sütlü Kahve", "fiyat": 5.99},
    {"isim": "Vişne Şurubu", "fiyat": 3.99},
    {"isim": "Sumaklı Şalgam Suyu", "fiyat": 6.99},
    {"isim": "Melisa Çayı", "fiyat": 4.99},
    {"isim": "Karadut Suyu", "fiyat": 5.99},
    {"isim": "Biberli Ayran", "fiyat": 2.99},
    {"isim": "Beyaz Gazoz", "fiyat": 3.99},
    {"isim": "Nar Ekşili Şerbet", "fiyat": 4.99},
    {"isim": "Kırmızı Erik Şerbeti", "fiyat": 5.99},
    {"isim": "Boza", "fiyat": 5.99},
    {"isim": "Salep", "fiyat": 7.99},
    {"isim": "Ayran", "fiyat": 2.99},
    {"isim": "Türk Kahvesi", "fiyat": 4.99},
    {"isim": "Turşu Suyu", "fiyat": 3.99},
    {"isim": "Serbet", "fiyat": 6.99},
    {"isim": "Şalgam Suyu", "fiyat": 4.99},
    {"isim": "Sahlep", "fiyat": 8.99},
    {"isim": "Limonata", "fiyat": 4.99},
    {"isim": "Naneli Limonata", "fiyat": 5.99},
    {"isim": "Demleme Çay", "fiyat": 3.99},
    {"isim": "Ada Çayı", "fiyat": 3.99},
    {"isim": "Elma Çayı", "fiyat": 3.99},
    {"isim": "Karaçay", "fiyat": 3.99},
    {"isim": "Menengiç Kahvesi", "fiyat": 6.99},
    {"isim": "Kakuleli Çay", "fiyat": 4.99},
    {"isim": "Sade Türk Kahvesi", "fiyat": 4.99},
    {"isim": "Salepli Çay", "fiyat": 5.99},
    {"isim": "Tarçınlı Türk Kahvesi", "fiyat": 5.99},
    {"isim": "Kestane Şekeri Suyu", "fiyat": 4.99},
    {"isim": "Hünkar Beğendi", "fiyat": 9.99},
    {"isim": "Bozbaş", "fiyat": 12.99},
    {"isim": "İçli Köfte Suyu", "fiyat": 6.99},
    {"isim": "Kelle Paça", "fiyat": 8.99},
    {"isim": "Şıllık", "fiyat": 6.99},
    {"isim": "Kabak Tatlısı Şerbeti", "fiyat": 5.99},
    {"isim": "Türk Kahvesi", "fiyat": 5.99},
    {"isim": "Çay", "fiyat": 3.99},
    {"isim": "Boza", "fiyat": 4.99},
    {"isim": "Salep", "fiyat": 7.99},
    {"isim": "Menengiç Kahvesi", "fiyat": 8.99},
    {"isim": "Sahlep", "fiyat": 6.99},
    {"isim": "Demlik Çay", "fiyat": 3.99},
    {"isim": "Limonata", "fiyat": 4.99},
    {"isim": "Şerbet", "fiyat": 3.99},
    {"isim": "Karakız", "fiyat": 9.99},
    {"isim": "Üzüm Pekmezi", "fiyat": 6.99},
    {"isim": "Tarçın Çayı", "fiyat": 4.99},
    {"isim": "Adaçayı", "fiyat": 4.99},
    {"isim": "Güllaç Şerbeti", "fiyat": 5.99},
    {"isim": "Dibek Kahvesi", "fiyat": 8.99},
    {"isim": "Salep Çiçeği Çayı", "fiyat": 6.99},
    {"isim": "Kızılcık Şerbeti", "fiyat": 5.99},
    {"isim": "Havuç Şerbeti", "fiyat": 4.99},
    {"isim": "Elma Şerbeti", "fiyat": 4.99},
    {"isim": "Turşu Suyu", "fiyat": 3.99},
    {"isim": "Kestane Şerbeti", "fiyat": 5.99},
    {"isim": "Sütlü Çay", "fiyat": 4.99},
    {"isim": "Hibiskus Çayı", "fiyat": 4.99},
    {"isim": "Ihlamur Çayı", "fiyat": 4.99},
    {"isim": "Karabaş Çayı", "fiyat": 4.99},
    {"isim": "Tarhana Çorbası", "fiyat": 6.99},
    {"isim": "Sumaklı Şerbet", "fiyat": 5.99},
    {"isim": "Kuşburnu Şerbeti", "fiyat": 5.99},
    {"isim": "Gül Şurubu", "fiyat": 6.99},
    {"isim": "Mürdüm Eriği Şerbeti", "fiyat": 5.99},
    {"isim": "Çörekotu Çayı", "fiyat": 4.99},
    {"isim": "Kuzu İçliği", "fiyat": 9.99},
    {"isim": "Mahlepli Salep", "fiyat": 7.99},
    {"isim": "Beyaz Boza", "fiyat": 4.99},
    {"isim": "Kefir", "fiyat": 5.99},
]

# !İndirim % Olarak Eklenecek
indirimSistem = {
    "Karsı Cinsin Yanına Rezerve": 0.20,
    "Ogrenci": 0.10,
    "Aktarma": 0.5,
    "Aktarma Bileti Aynı Firma": 0.5,  # ! Firma adı belirlenecek!
}

anaFiyatlar = {
    "Koltuk Değiştirme": 30,
    "Normal Koltuk" : 350,
    "PS5 Koltuk" : 500,
    "PS5 Yataklı Koltuk" : 900,  # !15 Adet Yatak Var.
    "Ücretli Tuvalet" : 50,
    "Ekstra Valiz" : 45,  # !Kişi Başı Max 2 Valiz Ücretsiz
}

# Rezervasyon bilgilerini içeren kisiler listesi
# Rezervasyon yapılan kişilere ait bilgilerin saklandığı bir liste yapısı kullanılmış.
kisiler = []

# Rezervasyon işlemlerini gerçekleştiren fonksiyon
def rezerve(koltukNo):
    global kisiler
    global gecerlilikTarihi

    # Koltuk numarasının geçerliliğini kontrol et
    if koltukNo not in koltuk.keys():
        print("Geçersiz koltuk numarası!")
        return

    # Seçilen koltuğun dolu olup olmadığını kontrol et
    if koltuk[koltukNo]["durum"] == "Dolu":
        print("Seçtiğiniz koltuk dolu!")
        return

    # Rezervasyon yapacak kişiye ait bilgileri al
    koltukTuru = koltuk[koltukNo]["Koltuk Türü"]
    print(f"Seçilen koltuk türü: {koltukTuru}")

    ad = input("Adınız Giriniz: ")
    soyad = input("Soyadınız Giriniz: ")
    cinsiyet = input("Cinsiyeti girin (Erkek, Kadın): ").title()

    # Cinsiyet girişinin doğruluğunu kontrol et
    if cinsiyet not in ["Erkek", "Kadın"]:
        print("Geçersiz cinsiyet!")
        return

    # Koltuğu rezerve et ve gerekli bilgileri güncelle
    koltuk[koltukNo]["durum"] = "Dolu"
    koltuk[koltukNo]["Cinsiyet"] = cinsiyet

    # Bilet alış tarihi ve geçerlilik tarihini hesapla
    alisTarihi = datetime.datetime.now()
    gecerlilikTarihi = alisTarihi + datetime.timedelta(days=2)

    print("Bilet alış tarihi:", alisTarihi.strftime("%d.%m.%Y %H:%M:%S"))
    print("Geçerlilik tarihi:", gecerlilikTarihi.strftime("%d.%m.%Y %H:%M:%S"))

    # Geçerlilik tarihinin alış tarihinden önce olup olmadığını kontrol et
    if gecerlilikTarihi < alisTarihi:
        print("Bilet Geçersiz! Geçerlilik Tarihi Geçmiş.")
        return

    # Rezervasyon bilgilerini kisiler listesine ekle
    kisiler.append({
        "koltuk_no": koltukNo,
        "ad": ad,
        "soyad": soyad,
        "cinsiyet": cinsiyet,
        "gecerlilik_tarihi": gecerlilikTarihi,
        "fiyat": 0  # Fiyat, bilet kesildiğinde hesaplanacak
    })

    # Fatura tutarını hesapla
    fatura = anaFiyatlar[koltukTuru]

    # Yemek seçimi
    yemekSecimi = input("Yemek ister misiniz? (Evet/Hayır): ").lower()
    if "evet" in yemekSecimi:
        secilenYemekler = secim_yap(yemekSistemi, "yemek")
        fatura += sum(yemek["fiyat"] for yemek in secilenYemekler)

    # İçecek seçimi
    icecekSecimi = input("İçecek ister misiniz? (Evet/Hayır): ").lower()
    if "evet" in icecekSecimi:
        secilenIcecekler = secim_yap(icecekSistemi, "içecek")
        fatura += sum(icecek["fiyat"] for icecek in secilenIcecekler)

    # Tuvalet seçimi
    wcIstegi = input("Yolculuk süresince WC gitmek ister misiniz? (Evet/Hayır): ").lower()
    if "evet" in wcIstegi:
        fatura += anaFiyatlar["Ücretli Tuvalet"]
        print(f"WC ücreti ({anaFiyatlar['Ücretli Tuvalet']} TL) faturaya eklenmiştir.")

    # Valiz sayısı
    valizSayisi = int(input("Kaç adet ekstra valiziniz var? (Max 2 valiz ücretsiz): "))
    if valizSayisi > 2:
        ekstraValizUcreti = (valizSayisi - 2) * anaFiyatlar["Ekstra Valiz"]
        fatura += ekstraValizUcreti
        print(f"Ekstra valiz ücreti ({ekstraValizUcreti} TL) faturaya eklenmiştir.")

    indirimYuzde = 0
    for indirim, yuzde in indirimSistem.items():
        if indirim in cinsiyet:
            indirimYuzde = max(indirimYuzde, yuzde)

    indirimMiktari = fatura * indirimYuzde
    fatura -= indirimMiktari

    # Faturayı kisiler listesine ekle
    kisiler[-1]["fiyat"] = fatura
    print(f"Toplam fatura tutarı: {fatura} TL")

    return fatura

def secim_yap(secim_listesi, secim_tipi):
    secilen_secimler = []
    print(f"{secim_tipi.capitalize()} Seçenekleri:")
    for index, secim in enumerate(secim_listesi, start=1):
        print(f"{index} - {secim['isim']} - {secim['fiyat']} TL")

    secim_no_str = input(f"{secim_tipi.capitalize()} numarası seçin (Çıkış için 'q'): ")
    if secim_no_str.lower() == "q":
        return secilen_secimler

    secim_nolar = secim_no_str.strip().split(" ")
    for secim_no in secim_nolar:
        if secim_no.isdigit():
            secim_index = int(secim_no)
            if 1 <= secim_index <= len(secim_listesi):
                secilen_secimler.append(secim_listesi[secim_index - 1])
                print(f"{secim_listesi[secim_index - 1]['isim']} seçildi.")
            else:
                print(f"Geçersiz {secim_tipi.lower()} numarası: {secim_no}")
        else:
            print(f"Geçersiz giriş: {secim_no}")

    return secilen_secimler


def benzersizId():
    mevcutIdler = set()
    while True:
        uid = random.randint(1000, 9999)

        if uid not in mevcutIdler:
            mevcutIdler.add(uid)
            break

    return uid

def bilet_kes(kisiler):
    toplamGelir = 0
    for kisi in kisiler:
        # Kişinin bilet fiyatını "kisi" sözlüğünden alın
        fatura = kisi.get("fiyat", 0)
        toplamGelir += fatura  # Toplam geliri hesaplıyoruz
        print(f"""
        Müşteri adı: {kisi['ad']}
        Müşteri soyadı: {kisi['soyad']}
        Müşteri Cinsiyeti: {kisi['cinsiyet']}
        Benzersiz ID: {benzersizId()}
        Bilet Geçerlilik Tarihi: {kisi['gecerlilik_tarihi']}
        Müşteriye Ait Toplam Fiyat: {fatura} TL
        """)
    print(f"Toplam Gelir: {toplamGelir} TL")

# Ana döngü
while True:
    print("""
    Yapabileceğiniz İşlemler:
    1 - Koltukları Göster
    2 - Koltuk Rezerve Et
    3 - Koltuk Değiştirme
    4 - Rezervasyon İptal
    5 - Bilet Kes
    6 - Admin Menüsü
    7 - Çıkış
    """)

    # Kullanıcının seçim yapmasını sağla
    sec = input("Yapmak İstediğiniz İşlemi Seçiniz: ")

    # koltukları gösterme işlemi
    if sec == "1":
        if len(koltuk) > 0:
            for koltukNo, koltukBilgisi in koltuk.items():
                print(
                    f"Koltuk No: {koltukNo} | Koltuk Türü: {koltukBilgisi['Koltuk Türü']} | Durum: {koltukBilgisi['durum']}")
        else:
            print("Hiç koltuk bulunmamaktadır.")

    #koltuk rezerve etme işlemi
    elif sec == "2":
        biletSayisi = int(input("Kaç Adet Bilet Almak İstersiniz: "))
        for i in range(biletSayisi):
            koltukNo = int(input("Rezerve etmek istediğiniz koltuk numarasını girin: "))
            rezerve(koltukNo)

    #koltuk değiştirme işlemi
    elif sec == "3":
        koltukNo = int(input("Değiştirmek istediğiniz koltuk numarasını girin: "))
        yeniKoltukNo = int(input("Yeni koltuk numarasını girin: "))
        if koltukNo in koltuk.keys() and yeniKoltukNo in koltuk.keys():
            if koltuk[koltukNo]["durum"] == "Dolu" and koltuk[yeniKoltukNo]["durum"] == "Boş":
                koltukTuru = koltuk[koltukNo]["Koltuk Türü"]
                cinsiyet = koltuk[koltukNo]["Cinsiyet"]
                koltuk[koltukNo]["durum"] = "Boş"
                koltuk[koltukNo]["Cinsiyet"] = None
                koltuk[yeniKoltukNo]["durum"] = "Dolu"
                koltuk[yeniKoltukNo]["Cinsiyet"] = cinsiyet
                print("Koltuk değiştirme işlemi başarıyla tamamlandı!")
            elif koltuk[koltukNo]["durum"] == "Onaylandı":
                print("""Değiştirmek istediğiniz koltuk durumu onaylandı!
Koltuk Değiştirmek için Müşteri Hizmetleri ile iletişime geçin.
Müşteri Hizmetleri Numarası: ........""")
        else:
            print("Geçersiz koltuk numarası!")

    #rezervasyon iptal işlemi
    elif sec == "4":
        koltukNo = int(input("İptal etmek istediğiniz rezervasyonun koltuk numarasını girin: "))
        if koltukNo in koltuk.keys():
            if koltuk[koltukNo]["durum"] == "Dolu":
                koltuk[koltukNo]["durum"] = "Boş"
                print("Rezervasyon iptal edildi.")
            elif koltuk[koltukNo]["durum"] == "Onaylandı":
                print("""İptal etmek istediğiniz rezervasyon onaylandı!
Rezervasyon iptali için Müşteri Hizmetleri ile iletişime geçin.
Müşteri Hizmetleri Numarası: ........""")
            else:
                print("Seçtiğiniz koltuk zaten boş!")
        else:
            print("Geçersiz koltuk numarası!")

    #bilet kesme işlemi
    elif sec == "5":
        bilet_kes(kisiler)

    # admin menüsü işlemi
    elif sec == "6":
        adminPanelAdi = "admin"
        password = "12345"

        kullaniciAdi = input("Kullanıcı Adı Giriniz: ").lower()
        şifre = input("Şifre Giriniz: ")

        if kullaniciAdi == adminPanelAdi and şifre == password:
            print("Başarıyla Giriş Yaptınız!")
            while True:
                print("""
    ADMİN Menüsü:
    1 - Koltukları Göster
    2 - Koltuk Rezerve Onayla
    3 - Koltuk Değiştirme
    4 - Rezervasyon İptal
    5 - Tüm Rezerveleri Onayla
    6 - Kullanıcı Menüsü
    7 - Çıkış
""")

                secim = input("Bir işlem seçin: ")

                if secim == "1":
                    if len(koltuk) > 0:
                        for koltukNo, koltukBilgisi in koltuk.items():
                            print(f"Koltuk No: {koltukNo} | Koltuk Türü: {koltukBilgisi['Koltuk Türü']} | Durum: {koltukBilgisi['durum']}")
                    else:
                        print("Hiç koltuk bulunmamaktadır.")

                elif secim == "2":
                    koltukNo = int(input("Onaylamak istediğiniz rezervasyonun koltuk numarasını girin: "))
                    if koltukNo in koltuk.keys():
                        if koltuk[koltukNo]["durum"] == "Onaylandı":
                            print("Bu koltuk zaten onaylanmış!")
                        elif koltuk[koltukNo]["durum"] == "Dolu":
                            koltuk[koltukNo]["durum"] = "Onaylandı"
                            print("Rezervasyon onaylandı.")
                        else:
                            print("Seçtiğiniz koltuk dolu değil!")
                    else:
                        print("Geçersiz koltuk numarası!")

                elif secim == "3":
                    koltukNo = int(input("Değiştirmek istediğiniz koltuk numarasını girin: "))
                    yeniKoltukNo = int(input("Yeni koltuk numarasını girin: "))
                    if koltukNo in koltuk and yeniKoltukNo in koltuk:
                        if koltuk[koltukNo]["durum"] == "Onaylandı" and koltuk[yeniKoltukNo]["durum"] == "Boş":
                            koltukTuru = koltuk[koltukNo]["Koltuk Türü"]
                            cinsiyet = koltuk[koltukNo]["Cinsiyet"]
                            koltuk[koltukNo]["durum"] = "Boş"
                            koltuk[koltukNo]["Cinsiyet"] = None
                            koltuk[yeniKoltukNo]["durum"] = "Dolu"
                            koltuk[yeniKoltukNo]["Cinsiyet"] = cinsiyet
                            print("Koltuk değiştirme işlemi başarıyla tamamlandı!")
                        else:
                            print("Koltuk değiştirme işlemi geçersiz.")
                    else:
                        print("Geçersiz koltuk numarası!")

                elif secim == "4":
                    koltukNo = int(input("İptal etmek istediğiniz rezervasyonun koltuk numarasını girin: "))
                    if koltukNo in koltuk.keys():
                        if koltuk[koltukNo]["durum"] == "Onaylandı":
                            koltuk[koltukNo]["durum"] = "Boş"
                            print("Rezervasyon iptal edildi.")

                        else:
                            print("Seçtiğiniz koltuk zaten boş!")
                    else:
                        print("Geçersiz koltuk numarası!")

                elif secim == "5":
                    for koltukNo, koltukBilgisi in koltuk.items():
                        if koltukBilgisi["durum"] == "Dolu":
                            koltuk[koltukNo]["durum"] = "Onaylandı"
                            print(f"{koltukNo}. Koltuk Başarıyla Onaylandı!")
                    print("Tüm rezarvasyonlar onaylandı!")

                elif secim == "6":
                    break

                elif secim == "7":
                    exit()

                else:
                    print("Geçersiz seçim!")

        else:
            print("Hatalı Kullanıcı Adı veya Şifre!")

    # çıkış işlemi
    elif sec == "7":
        print("Çıkış yapılıyor...")
        break

    # Geçersiz seçim durumu
    else:
        print("Geçersiz seçim!")