countries=[]
populations=[]
country_file= open("HigherOrLowerGame/Country.txt","r")
while True:
    country=country_file.readline()
    if not country:
        break
    else:
        print(country)
        length=len(country)
 
        countries.append(country[0:length-1])
print(countries)
population_file= open("HigherOrLowerGame/Population.txt","r")
while True:
    population=population_file.readline()
    if not population:
        break
    else:
        print(population)
        length=len(population)
        populations.append(population[0:length-1])
print(populations)    
country1=
