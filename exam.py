'''
# Loop from 0 to 100
for loop_variable in range(101):  # range(101) goes from 0 to 100
    # Check if the variable is between 0 and 50 inclusive, or between 62 and 100 inclusive
    if (0 <= loop_variable <= 50) or (62 <= loop_variable <= 100):
        # Print the loop variable if the condition is satisfied
        print(loop_variable)


#Loop from 0 to 100
for cool_var in range(101):
    if (0 <= cool_var <= 50) or (62 <= cool_var <= 100):
        print(cool_var)
#We're looping from 0 to 100. For each number, if it's between 0 and 50 or between 62 and 100, we print it.            
'''

# Kullanıcıdan iki büyük harfli girdi al
ui = input("İki büyük harf girin (örneğin 'AA'): ")

# İlk ve ikinci harfi ayır
first_letter = ui[0]
second_letter = ui[1]

# İlk harfin pozisyonunu bul ve 26 ile çarp
first_letter_position = (ord(first_letter) - ord('A') + 1) * 26

# İkinci harfin pozisyonunu bul
second_letter_position = ord(second_letter) - ord('A') + 1

# Toplam pozisyonu hesapla
total_position = first_letter_position + second_letter_position

# Sonucu yazdır
print(f"{ui} konumu: {total_position}")
