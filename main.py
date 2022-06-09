with open('utca.txt', 'r') as f:
    with open ('utca_copy.txt', 'w') as f2:
        for line in f:
            f2.write(line.replace(' ', ','))




# 3. Generate a CSV with taxId, owned properties and gross tax