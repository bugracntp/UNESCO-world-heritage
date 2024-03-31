import pandas as pd

def xls_to_csv(input_file, output_file):
    # Excel dosyasını oku
    xls_data = pd.read_excel(input_file)
    
    # CSV dosyasına yaz
    xls_data.to_csv(output_file, index=False)
    
    print("Dönüşüm tamamlandı. CSV dosyası oluşturuldu:", output_file)

# Kullanım örneği
input_file = "input_file.xls"  # XLS dosyasının adı ve yolunu buraya girin
output_file = "output_file.csv"  # Çıktı CSV dosyasının adı ve yolunu buraya girin
xls_to_csv(input_file, output_file)
