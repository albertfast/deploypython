from tqdm import tqdm

import time

people_names = ["Albert", "John", "Mary", "Kimberly"]

[print(name) for name in tqdm(people_names, desc="People Names")]

for i in tqdm(range(100), desc= "Basic Loop"):
    time.sleep(0.1)




