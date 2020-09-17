FIXME = None


class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        text = [self.verse(number) for number in range(upper, lower - 1, -1)]
        return "\n".join(text)

    def verse(self, number):
        return (
            f"{self.quantity(number).capitalize()} "
            f"{self.container(number)} of beer on the wall, "
            f"{self.quantity(number)} {self.container(number)} of beer.\n"
            f"{self.action(number)}"
            f"{self.quantity(self.successor(number))} "
            f"{self.container(self.successor(number))} "
            f"of beer on the wall.\n"
        )

    def quantity(self, number):
        return BottleNumber(number).quantity()

    def container(self, number):
        return BottleNumber(number).container()

    def action(self, number):
        return BottleNumber(number).action()

    def pronoun(self, number):
        return BottleNumber(number).pronoun()

    def successor(self, number):
        return BottleNumber(number).successor()


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
            return "Go to the store and buy some more, "
        else:
            return f"Take {self.pronoun()} down and pass it around, "

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
