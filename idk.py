with open("Booksnew.csv", "r") as file:
    with open("Books1.csv", "w") as fileNew:
    
        for line in file:
            fileNew.write(line.replace('http', 'https'))