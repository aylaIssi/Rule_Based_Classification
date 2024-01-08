# Görev 1: Aşağıdaki Soruları Yanıtlayınız
# Soru 1: persona.csv dosyasını okutunuz
# ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
df = pd.read_csv("/Users/kerem/Desktop/persona.csv")
df.info()

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?
unique_price = df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

price_counts = df['PRICE'].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df.columns
df['COUNTRY'].value_counts()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df["PRICE"].value_counts()
df.groupby("COUNTRY")["PRICE"].sum()

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

df["SOURCE"].value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].mean()

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].mean()

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY","SOURCE"])["PRICE"].mean()

# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
asd = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean()

# Görev 3: Çıktıyı PRICE’a göre sıralayınız
# • Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# • Çıktıyı agg_df olarak kaydediniz

#agg_df = df.sort_values(by='PRICE', ascending=False)
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values(by="PRICE", ascending=False)
agg_df.head()

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.

agg_df.reset_index(inplace=True)
agg_df.head()

# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'

# Age değişkenini kategorik değişkene çevirme
bins = [0, 18, 23, 30, 40, 70]  # Aralık sınırlarını belirleyin
labels = ['0_18', '19_23', '24_30', '31_40', '41_70']  # Kategori etiketlerini belirleyin

agg_df["AGE_2"] = pd.cut(agg_df["AGE"], bins=bins, labels=labels, right=False)

# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.


agg_df['customers_level_based'] = agg_df['COUNTRY'] + '_' + agg_df['SOURCE'] + '_' + agg_df['SEX'] + '_' + agg_df['AGE_2']
agg_df["CUSTOMERS_LEVEL_BASED"] = [str(agg_df.loc[i, "COUNTRY"]).upper() + "_" +
                                   str(agg_df.loc[i, "SOURCE"]).upper() + "_" +
                                   str(agg_df.loc[i, "SEX"]).upper() + "_" +
                                   str(agg_df.loc[i, "AGE_2"]).upper() for i in range(len(agg_df))]
agg_df = agg_df.groupby("CUSTOMERS_LEVEL_BASED").agg({"PRICE": "mean"}).sort_values(by="PRICE", ascending=False)
agg_df.reset_index(inplace=True)
agg_df.head()
