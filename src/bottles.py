FIXME = None


class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        text = [self.verse(number) for number in range(upper, lower - 1, -1)]
        return "\n".join(text)

    def verse(self, number):
        bottle_number = BottleNumber(number)
        next_bottle_number = BottleNumber(bottle_number.successor())
        return (
            f"{bottle_number} of beer on the wall, ".capitalize() +
            f"{bottle_number} of beer.\n"
            f"{bottle_number.action()} {next_bottle_number} "
            f"of beer on the wall.\n"
        )


class BottleNumber:
    def __init__(self, number):
        self.number = number

    def quantity(self):
        if self.number == 0:
            return "no more"
        else:
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