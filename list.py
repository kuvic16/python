primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],  # (Comma after the last element is optional)
]

hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# A list can contain a mix of different types of variables
my_favourite_things = [32, 'raindrops on roses', help]


# Elements at the end of the list can be accessed with negative numbers, starting from -1:
print(planets[-1])
print(planets[-2])
print(planets[0:3])
