current_pop = 10000
decrease_rate = 0.10  

for year in range(10, 0, -1):
    print(f"{year}th year - {int(current_pop)}")
    current_pop = current_pop / (1 + decrease_rate) 