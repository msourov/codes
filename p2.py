# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#
# pprint.pprint(count)


class Person:
    def __init__(self, name):
        self.name = name

    def __format__(self, format_spec):
        if format_spec == "scream":
            return self.name.upper() + "!"
        elif format_spec == "repeat":
            return self.name * 3
        return self.name


p = Person("Pat")
print(f"{p}")
print(f"{p:scream}")
print(f"{p:repeat}")