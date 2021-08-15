def sign(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1


print(sign(1))
print(sign(-1))


def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    candy_text = "candies"
    if total_candies == 1:
        candy_text = "candy"

    print("Splitting", total_candies, candy_text)
    return total_candies % 3


to_smash(91)
to_smash(1)


def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or (rain_level < 5 and have_hood) or not(rain_level > 0 and is_workday)


# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)


def new():
    print("")
    print("======================")


print("====================")
print(True ^ True)

print("====================")
print(bool(1))
print(bool(0))

print("====================")
print(int(True))
print(int(False))

new()
a = True
b = False
c = True

print(a + b + c)

# The player is dealt two face-up cards. The dealer is dealth one face-up card.
