import pandas as pd

# İşlem verilerini tabloya dökelim
data = {
    'Side': ['Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell', 'Sell'],
    'Quantity': [3, 7, 5, 10, 20, 2, 5, 10, 20, 5, 10, 20, 3, 10, 5, 20, 5, 10, 50, 5, 10, 1, 5, 5, 10, 10, 4, 5, 3, 3, 4, 10, 8, 2, 10, 1, 50, 5, 20, 35, 30, 20, 15, 5, 5, 10, 20, 9, 1, 10, 90, 10, 5, 20, 30, 20, 15, 10],
    'Avg Price': [32.00, 5.16, 5.80, 9.10, 4.10, 2.85, 5.80, 3.00, 15.50, 1.79, 10.00, 25.00, 1.25, 3.20, 4.40, 2.37, 5.50, 3.00, 14.80, 5.10, 7.50, 5.50, 8.00, 3.00, 27.90, 25.00, 5.90, 6.40, 7.30, 6.20, 5.50, 6.60, 5.80, 5.71, 14.20, 2.00, 3.90, 30.70, 15.90, 6.80, 4.20, 1.50, 1.00, 9.90, 25.00, 6.40, 6.50, 11.10, 10.10, 6.40, 7.80, 10.50, 10.60, 2.90, 25.00, 22.90],
    'Filled Time': ['07/16/2024 15:59:28 EDT', '07/16/2024 15:58:59 EDT', '07/16/2024 15:58:34 EDT', '07/16/2024 15:57:56 EDT', '07/16/2024 15:56:57 EDT', '07/16/2024 15:56:43 EDT', '07/16/2024 15:56:33 EDT', '07/16/2024 15:56:09 EDT', '07/16/2024 15:55:59 EDT', '07/16/2024 15:54:19 EDT', '07/16/2024 15:54:19 EDT', '07/16/2024 15:54:09 EDT', '07/16/2024 15:53:45 EDT', '07/16/2024 15:53:05 EDT', '07/16/2024 15:52:37 EDT', '07/16/2024 15:52:19 EDT', '07/16/2024 15:51:37 EDT', '07/16/2024 15:51:11 EDT', '07...
}

df = pd.DataFrame(data)

# DataFrame'i Excel dosyasına kaydedelim
file_path = '/mnt/data/trading_records_fixed.xlsx'
df.to_excel(file_path, index=False)

file_path
