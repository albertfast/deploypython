# Understand:
# The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files.
# For each file there is a known set of operations which may be applied to it:
# -write W,
# -read R,
# -execute X.
# The first line contains the number N — the number of files contained in the filesystem.
# The following N lines contain the file names and allowed operations with them, separated by spaces.
# The next line contains an integer M — the number of operations to the files.
# In the last M lines specify the operations that are requested for files. One file can be requested many times.
# You need to recover the control over the access rights to the files.
# For each request your program should return OK if the requested operation is valid or Access denied if the operation is invalid.

# Example:    Input:                  Output:
#             4
#             helloworld.exe R X
#             pinglog W R
#             nya R
#             goodluck X W R
#             5
#             read nya                OK
#             write helloworld.exe    Access denied
#             execute nya             Access denied
#             read pinglog            OK
#             write pinglog           OK

# Plan:
# Step 1: Define operation mapping
# Create a dictionary to map operations (read, write, execute) to their shorthand (R, W, X).

# Step 2: Input number of files
# Read the total number of files (n) from the user.

# Step 3: Initialize dictionary for access rights
# Create an empty dictionary to store file names as keys and their associated rights as values.

# Step 4: Populate file access rights
# Loop n times:
#     - Read input for each file, containing the file name and its rights.
#     - Split the input to separate the file name and the list of rights.
#     - Add the file name as a key in the dictionary and its rights as a set of values.

# Step 5: Input number of operations
# Read the total number of operations (m) from the user.

# Step 6: Validate operations
# Loop m times:
#     - Read input for each operation, containing the operation type and file name.
#     - Check:
#         1. If the file exists in the dictionary.
#         2. If the shorthand for the operation (from the mapping) is in the file's rights.
#     - If both conditions are true:
#         - Print "OK".
#     - Otherwise:
#         - Print "Access denied".

# Step 7: End
# Finish processing after validating all operations.

'''
# Implementation:
def check_access():
    # Step 1: Map operation names to their short codes (read -> R, write -> W, execute -> X)
    # This dictionary is used to easily convert operation names into their corresponding access rights.
    operations_map = {"read": "R", "write": "W", "execute": "X"}

    # Step 2: Get the number of files and initialize a dictionary to store their access rights.
    n = int(input("Enter the number of files: "))  # Number of files with defined access rights.
    access_rights = {}  # Dictionary to store file names and their corresponding access rights.

    # Step 3: Loop to input file names and their access rights.
    for _ in range(n):
        # Input format: file_name followed by its access rights (e.g., "file_name R W X").
        data = input("Enter file name and its rights (e.g., file R W X): ").split()
        file = data[0]  # The first part is the file name.
        rights = set(data[1:])  # Remaining parts are the access rights, stored as a set.
        # Example: "helloworld.exe R X" => file = "helloworld.exe", rights = {"R", "X"}
        access_rights[file] = rights  # Store the file and its rights in the dictionary.

    # Step 4: Get the number of operations to process.
    m = int(input("Enter the number of operations: "))

    # Step 5: Process each operation request.
    for _ in range(m):
        # Input format: operation type and file name (e.g., "read file_name").
        operation, file = input("Enter operation and file name (e.g., read file): ").split()

        # Step 6: Check if the operation is valid.
        # First, check if the file exists in the dictionary.
        # Then, check if the operation's corresponding access right exists in the file's rights.
        if file in access_rights and operations_map.get(operation) in access_rights[file]:
            print("OK")  # If valid, print OK.
        else:
            print("Access denied")  # If invalid, print Access denied.

# Call the function to execute the program.
check_access()

# Detailed Explanation of Each Step:
# Step 1: The operations_map dictionary maps long-form operations ("read", "write", "execute") to short codes ("R", "W", "X")
#         so that we can easily compare them with the access rights stored for each file.
#
# Step 2: The number of files is input as an integer. We initialize an empty dictionary (access_rights) to store the
#         access rights of each file.
#
# Step 3: For each file, the input is split into a list. The first element is the file name, and the remaining
#         elements are the access rights (e.g., "R", "W", "X"). These access rights are stored as a set
#         for efficient lookup.
#         Example: Input: "helloworld.exe R X" => access_rights = {"helloworld.exe": {"R", "X"}}
#
# Step 4: The number of operations to be checked is input as an integer.
#
# Step 5: For each operation, the input is split into the operation type ("read", "write", "execute") and the file name.
#
# Step 6: The operation is validated in two steps:
#         - First, check if the file exists in the access_rights dictionary.
#         - Then, use operations_map to convert the operation into its short code and check if this short code exists
#           in the access rights of the file.
#         If both checks pass, print "OK". Otherwise, print "Access denied".


# Time Complexity Analysis:
# - Adding n files to the dictionary: O(n).
# - Processing m operations:
#   - Dictionary lookup: O(1).
#   - Set lookup: O(1).
#   Total: O(m).
# - Overall: O(n + m).
# This is efficient and scales well for large inputs.
'''


def check_access():
    # İşlem isimlerini kısa kodlara eşlemek için bir sözlük oluşturuyoruz.
    operations_map = {"read": "R", "write": "W", "execute": "X"}

    # Kullanıcıdan toplam dosya sayısını alıyoruz.
    while True:
        try:
            n = int(input("Dosya sayısını girin: ").strip())
            if n < 1:
                print("Dosya sayısı 1 veya daha büyük olmalıdır.")
                continue
            break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    # Dosya isimlerini ve izinlerini saklamak için bir sözlük oluşturuyoruz.
    access_rights = {}

    # Kullanıcıdan dosya isimleri ve izinlerini alıyoruz.
    for _ in range(n):
        while True:
            try:
                data = input("Dosya ismi ve izinleri girin (örneğin: file R W X): ").strip().split()
                if len(data) < 2:
                    print("Lütfen bir dosya ismi ve en az bir izin girin.")
                    continue

                file = data[0]  # İlk eleman dosya adıdır.
                # İzinleri büyük harfe çevirip bir kümeye ekliyoruz (map kullanmadan).
                rights = set()
                for right in data[1:]:
                    rights.add(right.upper())  # Her izin büyük harfe çevrilir ve kümeye eklenir.

                # Geçerli izinleri kontrol ediyoruz.
                if not rights.issubset({"R", "W", "X"}):
                    print("Geçersiz izin tespit edildi. Yalnızca 'R', 'W' veya 'X' izinlerini girin.")
                    continue

                access_rights[file] = rights  # Dosya ve izinlerini sözlüğe ekliyoruz.
                break
            except Exception as e:
                print(f"Bir hata oluştu: {e}")

    # Kullanıcıdan işlem sayısını alıyoruz.
    while True:
        try:
            m = int(input("İşlem sayısını girin: ").strip())
            if m < 1:
                print("İşlem sayısı 1 veya daha büyük olmalıdır.")
                continue
            break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    # İşlemleri kontrol ediyoruz.
    for _ in range(m):
        while True:
            try:
                operation, file = input("İşlem ve dosya ismini girin (örneğin: read file): ").strip().split()

                # İşlem türünü küçük harfe çevirip sözlükten kısa kodu alıyoruz.
                operation_code = operations_map.get(operation.lower())

                if operation_code is None:
                    print("Geçersiz işlem. Yalnızca 'read', 'write' veya 'execute' işlemleri kabul edilir.")
                    continue

                # Dosya ve işlem izni kontrolü yapıyoruz.
                if file in access_rights and operation_code in access_rights[file]:
                    print("OK")
                else:
                    print("Access denied")
                break
            except ValueError:
                print("Lütfen işlem ve dosya ismini doğru formatta girin.")
            except Exception as e:
                print(f"Bir hata oluştu: {e}")


# Fonksiyonu çalıştırıyoruz.
check_access()

'''
def check_access():
    # Map operation names to short codes (read -> R, write -> W, execute -> X)
    operations_map = {"read": "R", "write": "W", "execute": "X"}

    # Get the number of files
    while True:
        try:
            n = int(input().strip())
            if n < 1:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Dictionary to store file names and their access rights
    access_rights = {}

    # Input file names and their permissions
    for _ in range(n):
        while True:
            try:
                data = input().strip().split()
                if len(data) < 2:
                    print("Please provide a file name and at least one permission.")
                    continue
                
                file = data[0]  # The first element is the file name.
                # Convert permissions to uppercase and store them in a set
                rights = set()
                for right in data[1:]:
                    rights.add(right.upper())

                # Check for invalid permissions
                if not rights.issubset({"R", "W", "X"}):
                    print("Invalid permissions detected. Only 'R', 'W', or 'X' are allowed.")
                    continue

                # Add file and its permissions to the dictionary
                access_rights[file] = rights
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    # Get the number of operations
    while True:
        try:
            m = int(input().strip())
            if m < 1:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Check operations
    for _ in range(m):
        while True:
            try:
                operation, file = input().strip().split()

                # Convert operation name to short code
                operation_code = operations_map.get(operation.lower())

                if operation_code is None:
                    print("Invalid operation. Only 'read', 'write', or 'execute' are allowed.")
                    continue

                # Check if the file exists and if the operation is permitted
                if file in access_rights and operation_code in access_rights[file]:
                    print("OK")
                else:
                    print("Access denied")
                break
            except ValueError:
                print("Please provide a valid operation and file name.")
            except Exception as e:
                print(f"An error occurred: {e}")

# Run the function
check_access()


# Detaylı Açıklamalar:
# Adım 1: operations_map sözlüğü uzun işlem adlarını (örneğin "read") kısa koda (örneğin "R") dönüştürür.
# Bu sayede işlem türlerini dosya izinleriyle kolayca karşılaştırabiliriz.

# Adım 2: Kullanıcıdan toplam dosya sayısını alırız. Daha sonra, her dosyanın adını ve izinlerini saklamak için
# bir access_rights sözlüğü başlatırız.

# Adım 3: Kullanıcıdan her dosya için veri alırız. Bu veri, dosya adını ve izinleri içerir.
# Örneğin: Girdi: "helloworld.exe R X" -> Sözlüğe: {"helloworld.exe": {"R", "X"}} olarak eklenir.

# Adım 4: Kaç işlem sorgusu yapılacağını alırız.

# Adım 5: Her işlem için kullanıcıdan "işlem türü" ve "dosya adı" alırız.
# Örneğin: "read helloworld.exe".

# Adım 6: İşlemi kontrol ederiz:
# - İlk olarak, dosya adının sözlükte olup olmadığını kontrol ederiz.
# - Daha sonra, operations_map kullanarak işlem türünü kısa koda çeviririz ve bu kodun izinlerde olup olmadığını kontrol ederiz.
# Eğer işlem geçerliyse "OK", geçerli değilse "Access denied" yazdırırız.

# Kodda Kullanılan Fonksiyonların Detayları:

# strip():
# Kullanıcının girişindeki baştaki ve sondaki gereksiz boşlukları temizler.
# Örneğin, "  read  " -> "read".

# split():
# Girdiyi boşluklara göre ayırarak bir liste oluşturur.
# Örneğin, "file R W X" -> ["file", "R", "W", "X"].

# upper():
# Küçük harfleri büyük harfe çevirir.
# Örneğin, "r" -> "R".

# set():
# Tekrarlanan elemanları otomatik olarak temizler ve hızlı erişim sağlar.
# Örneğin, ["R", "R", "X"] -> {"R", "X"}.

# issubset():
# Bir kümenin diğer bir kümenin alt kümesi olup olmadığını kontrol eder.
# Örneğin, {"R", "X"}.issubset({"R", "W", "X"}) -> True.

# get():
# Sözlükte bir anahtara karşılık gelen değeri döndürür. Eğer anahtar bulunamazsa `None` döner.
# Örneğin, operations_map.get("read") -> "R".
# Eğer "read" anahtarı yoksa `None` döner.

# int():
# Kullanıcıdan alınan string girdiyi tam sayıya çevirir.
# Örneğin, "42" -> 42.

# continue:
# Döngünün mevcut iterasyonunu atlayarak bir sonraki iterasyona geçer.

# break:
# Döngüyü tamamen sonlandırır ve döngünün dışına çıkar.

# in:
# Bir elemanın bir veri yapısında bulunup bulunmadığını kontrol eder.
# Örneğin, "R" in {"R", "W", "X"} -> True.

# Zaman Karmaşıklığı Analizi:
# - n dosyasını sözlüğe eklemek: O(n).
# - m işlemini kontrol etmek:
#   - Sözlükte dosya arama: O(1).
#   - Set içinde izin kontrolü: O(1).
#   Toplam: O(m).
# - Genel toplam: O(n + m).
# Bu çözüm, büyük girişler için verimli ve ölçeklenebilir.

'''

























