# upper, lower, title, strip, lstrip, rstrip, center, join
string = "      GAbRiEl diAS            "
print(string.upper())
print(string.lower())
print(string.title())
print(string.strip())
print(string.lstrip())
print(string.rstrip())
string = string.title().strip()
print(string.center(50, "#"))
print(string.center(50))
print(".".join(string))