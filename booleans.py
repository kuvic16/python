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
# 4 12 0 0
# 8 14 0 0
# 8 20 0 0
# 8 12 0 0
# 10 13 0 0
# 9 16 0 0
# 3 11 0 0
# 11 13 0 0
# 2 19 0 0
# 7 14 0 0
# 7 18 0 0
# 9 20 0 0
# 3 11 0 0
# 1. The player is dealt two face-up cards. The dealer is dealt one face-up card.
# 2. The player may ask to be dealt another card("hit") as many times as they wish.
# if the sum of their cards exceeds 21, they lost the round immediately.


def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    if player_total <= 11 and dealer_total > 0 and player_low_aces > 0:
        return True
    elif player_total <= 0 and dealer_total > 0 and player_high_aces == 1:
        return True
    elif player_total <= 14 and (dealer_total < 3 or dealer_total > 7):
        return True
    else:
        return False


print(should_hit(4, 12, 0, 0))
