with open("rural_fires.csv", "r", encoding="utf-8") as file:
    with open("table_rural_fires.csv", "w", encoding="utf-8") as filewrite:
        for line in file:
            if line.startswith("1"):
                filewrite.write(line)
