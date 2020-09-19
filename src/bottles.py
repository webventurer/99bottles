FIXME = None


class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        text = [self.verse(number) for number in range(upper, lower - 1, -1)]
        return "\n".join(text)

    def verse(self, number):
        bottle_number = BottleNumber.from_number(number)
        return (
            f"{bottle_number} of beer on the wall, ".capitalize()
            + f"{bottle_number} of beer.\n"
            f"{bottle_number.action()} {bottle_number.successor()} "
            f"of beer on the wall.\n"
        )


class BottleNumber:
    def __init__(self, number):
        self.number = number

    @classmethod
    def from_number(cls, number):
        return {0: BottleNumber0(number),
                1: BottleNumber1(number),
                6: BottleNumber6(number)}.get(
            number, BottleNumber(number)
        )

    def quantity(self):
        return str(self.number)

    def container(self):
        return "bottles"

    def action(self):
        return f"Take {self.pronoun()} down and pass it around,"

    def pronoun(self):
        return "one"

    def successor(self):
        return BottleNumber.from_number(self.number - 1)

    def __str__(self):
        return f"{self.quantity()} {self.container()}"


class BottleNumber0(BottleNumber):
    def quantity(self):
        return "no more"

    def action(self):
        return "Go to the store and buy some more,"

    def successor(self):
        return BottleNumber.from_number(99)


class BottleNumber1(BottleNumber):
    def container(self):
        return "bottle"

    def pronoun(self):
        return "it"


class BottleNumber6(BottleNumber):
    def quantity(self):
        return "1"

    def container(self):
        return "six-pack"

