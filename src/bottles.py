FIXME = None


class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        text = [self.verse(number) for number in range(upper, lower - 1, -1)]
        return "\n".join(text)

    def container(self, number):
        if number == 1:
            return "bottle"
        else:
            return "bottles"

    def pronoun(self, number):
        if number == 1:
            return "it"
        else:
            return "one"

    def quantity(self, number):
        if number == 0:
            return "no more"
        else:
            return str(number)

    def action(self, number):
        if number == 0:
            return "Go to the store and buy some more, "
        else:
            return f"Take {self.pronoun(number)} down and pass it around, "

    def successor(self, number):
        if number == 0:
            return 99
        else:
            return number - 1

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
