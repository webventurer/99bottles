FIXME = None


class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, first, last):
        text = [self.verse(number) for number in range(first, last - 1, -1)]
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

    def verse(self, number):
        if number == 0:
            return (
                f"{self.quantity(number).capitalize()} "
                f"{self.container(number)} of beer on the wall, "
                f"{self.quantity(number)} {self.container(number)} of beer.\n"
                f"Go to the store and buy some more, "
                f"99 bottles of beer on the wall.\n"
            )
        else:
            return (
                f"{self.quantity(number).capitalize()} "
                f"{self.container(number)} of beer on the wall, "
                f"{self.quantity(number)} {self.container(number)} of beer.\n"
                f"Take {self.pronoun(number)} down and pass it around, "
                f"{self.quantity(number-1)} {self.container(number-1)} "
                f"of beer on the wall.\n"
            )
