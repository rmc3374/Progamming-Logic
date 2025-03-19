cars = ["Chevy Monte Carlo", "Mazda Miata", "Chevy Corvette", "Pontiac Thunderbird", "Dodge Hellcat SRT"]

for car in cars: 
    if (car == 'Chevy Monte Carlo'):
        continue
    print(cars)

# can also program like this:
# range has 3 parameters: how many in loop, define where range ends (manditory), skipping data points

for i in range(len(cars)): 
    if (cars(i) == 'Chevy Monte Carlo'):
        continue
    print(cars(i))