print("Haii, selamat datang di Kamus bahasa-bahasa asing")
r = input("Siapa namamu?")
print("Baiklah", r,",", "akan saya tunjukkan bahasa-bahasa nya")

meme_dict = {
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "ROFL": "Tanggapan terhadap lelucon",
    "SHEESH": "Sedikit ketidaksetujuan",
    "CREEPY": "Menakutkan, tidak menyenangkan",
    "AGGRO": "Untuk menjadi agresif/marah"
}

print(meme_dict.keys())
print("-----------------------------------------------------------------------------------------------")
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (bebas kapitalisasi, spasi akan diabaikan): ")
    word = word.replace(" ", "").upper()  
    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("Tidak ada bung -_-")
    print(" ")
