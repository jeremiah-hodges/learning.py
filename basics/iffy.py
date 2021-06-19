
is_tall = True
is_human = True

# comparisons
if is_human or is_tall :
    print("Hello you are human and tall")
else:
    print("You are either not human or not tall or both")

# using else if
if is_human and is_tall:
    print("You are human and tall")
elif is_human and not(is_tall):
    print("You are a short human")
elif not(is_human) and is_tall:
    print("You are not human and tall")
else:
    print("You are neither human nor tall")