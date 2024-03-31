import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('countries.csv')

# Veri çerçevesinin JSON formatına dönüştürülmesi
json_data = df.to_json('countries.json', orient='records')

# İşlem başarılıysa mesaj bastır
print("Veri başarıyla JSON formatına dönüştürüldü.")
