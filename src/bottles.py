FIXME = None


class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        text = [self.verse(number) for number in range(upper, lower - 1, -1)]
        return "\n".join(text)

    def verse(self, number):
        bottle_number = self.for_bottle_number(number)
        next_bottle_number = self.for_bottle_number(bottle_number.successor())
        return (
            f"{bottle_number} of beer on the wall, ".capitalize()
            + f"{bottle_number} of beer.\n"
            f"{bottle_number.action()} {next_bottle_number} "
            f"of beer on the wall.\n"
        )

    def for_bottle_number(self, number):
        return {0: BottleNumber0(number), 1: BottleNumber1(number)}.get(
            number, BottleNumber(number)
        )


class BottleNumber:
    def __init__(self, number):
        self.number = number

    def quantity(self):
        return str(self.number)

    def container(self):
        if self.number == 1:
            return "bottle"
        else:
            return "bottles"

    def action(self):
        if self.number == 0:
            return "Go to the store and buy some more,"
        else:
            return f"Take {self.pronoun()} down and pass it around,"

    def pronoun(self):
        if self.number == 1:
            return "it"
        else:
            return "one"

    def successor(self):
        if self.number == 0:
            return 99
        else:
            return self.number - 1

    def __str__(self):
        return f"{self.quantity()} {self.container()}"


class BottleNumber0(BottleNumber):
    def quantity(self):
        return "no more"
