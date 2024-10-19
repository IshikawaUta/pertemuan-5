# # membuat list
# buah = ["apel", "pisang", "mangga"]

# # mengakses element
# print(buah[0]) #output: apel

# #mengubah element
# buah[3] = "pir"
# buah[4] = "alpukat"
# print(buah) # output: ['apel', 'pisang', 'mangga', 'pir', 'alpukat']

# membuat list
buah = ["apel", "pisang", "mangga"]

# mengakses elemen
# print(buah[0])  # output: apel

# menambahkan elemen baru
# buah.append("pir")
# buah.append("alpukat")
buah.insert(0, "anggur")
buah.extend(["pir", "alpukat"])
buah.remove("mangga")
print(buah)  # output: ['apel', 'pisang', 'mangga', 'pir', 'alpukat']
