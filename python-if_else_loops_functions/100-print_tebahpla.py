#!/usr/bin/python3
print("".join(["{}".format(chr(122 - i) if i % 2 == 0 else "{}".format(chr(90 - i + 1)) for i in range(26)]), end="")
