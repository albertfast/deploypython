def string_to_xor_mask(string, encoded_values):
    # String'i binary'e çevir
    binary_string = ''.join(format(ord(char), '08b') for char in string).ljust(len(encoded_values) * 32, '0')
    
    # Her bir encoded değeri için XOR maskesini hesapla
    xor_masks = []
    for i, encoded_value in enumerate(encoded_values):
        segment = binary_string[i*32:(i+1)*32]  # Her 32 bitlik segmenti al
        xor_mask = int(segment, 2) ^ encoded_value  # XOR maskesi hesapla
        xor_masks.append(xor_mask)
    
    return xor_masks

# Örnek veriler
examples = {
    "tacocat": [2073094817, 1679126547],
    "never odd or even": [267657050, 233917524, 234374596, 250875466, 17830160],
    "lager, sir, is regal": [267394382, 167322264, 66212897, 200937635, 267422503],
    "go hang a salami, I'm a lasagna hog": [200319795, 133178981, 234094669, 267441422, 78666124, 99619077, 267653454, 133178165, 124794470],
    "egad, a base tone denotes a bad age": [267389735, 82841860, 267651166, 250793668, 233835785, 267665210, 99680277, 133170194, 124782119]
}

# XOR maskelerini hesapla ve sonuçları yazdır
for string, encoded_values in examples.items():
    xor_masks = string_to_xor_mask(string, encoded_values)
    print(f"String: {string}")
    print(f"XOR Masks: {xor_masks}\n")

# Kullanıcıdan giriş al ve işlem yap
user_string = input("Bir string girin: ")
user_encoded_values = list(map(int, input("Encoded değerleri virgülle ayrılmış şekilde girin: ").split(',')))

# Kullanıcı girdisi için XOR maskelerini hesapla ve yazdır
user_xor_masks = string_to_xor_mask(user_string, user_encoded_values)
print(f"String: {user_string}")
print(f"XOR Masks: {user_xor_masks}")
