# Kiruvchi ma'lumotlar
data = [
    {'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}
]

# Natija (Chiquvchi ma'lumot)
def chiquvchi_malumotlar(data):
    for d in data:
        # Ma'lumotlar bo'linishi
        print("Output (Chiquvchi ma'lumot)")
        for value in set(d.values()):
            print(value)
            # ismlar chiqarish
            names = [key for key, val in d.items() if val == value]
            print(' '.join(names))

# Fonksiyonni chaqirish
chiquvchi_malumotlar(data)
