x = "There are  %d types of people" % 10
binary = "binary"
do_not = "don't"

y = "thos who know %s, and those who %s" % (binary, do_not)

print(x)
print(y)

print("I said: %r " % (x))
print(" I also said: '%s'" % (y))

hilarious = "true"
joke_evaluation = "Isn't that joke funny? %r"

print(joke_evaluation % hilarious)

e = "left half"
y = "right half"

u = e + y
print(u)