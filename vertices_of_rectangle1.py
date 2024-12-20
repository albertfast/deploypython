import matplotlib.pyplot as plt

# x ve y koordinatlarını saklamak için boş listeler oluşturuyoruz
x_coords = []
y_coords = []

# Üç noktayı kullanıcıdan alıyoruz
for i in range(3):
    x = int(input(f"Enter x{i + 1}: "))  # x koordinatını al
    y = int(input(f"Enter y{i + 1}: "))  # y koordinatını al
    x_coords.append(x)  # x koordinatını listeye ekle
    y_coords.append(y)  # y koordinatını listeye ekle

# Her listede bir kere bulunan (eşsiz) x ve y koordinatını buluyoruz
fourth_x = [x for x in x_coords if x_coords.count(x) == 1][0]
fourth_y = [y for y in y_coords if y_coords.count(y) == 1][0]

# Dördüncü köşenin koordinatlarını listelere ekliyoruz
x_coords.append(fourth_x)
y_coords.append(fourth_y)
print("x4:",fourth_x)
print("y4:",fourth_y)

# Dikdörtgenin köşelerini sırayla birleştirmek için köşeleri yeniden sıralıyoruz
# İlk köşeyi, dördüncü köşeyi bulduktan sonra doğru sırayla yerleştiriyoruz.
x_ordered = [x_coords[0], x_coords[1], fourth_x, x_coords[2], x_coords[0]]
y_ordered = [y_coords[0], y_coords[1], fourth_y, y_coords[2], y_coords[0]]

# Grafik çizimi
plt.figure(figsize=(6, 6))
plt.plot(x_ordered, y_ordered, 'bo--')  # Kesikli çizgiler ve renk

# Her bir köşe için etiketler
plt.text(x_coords[0], y_coords[0], 'P1', ha='right', color='red')
plt.text(x_coords[1], y_coords[1], 'P2', ha='right', color='green')
plt.text(x_coords[2], y_coords[2], 'P3', ha='right', color='blue')
plt.text(fourth_x, fourth_y, 'P4 (Final Point)', ha='right', color='purple')  # Dördüncü köşeyi etiketle

# Eksen ayarları
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Dikdörtgenin Köşeleri ve Dördüncü Nokta (Kesikli Çizgiler)")
plt.grid(True)
plt.show()
