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

    def verse(self, number):
        if number == 0:
            return (
                "No more bottles of beer on the wall, "
                "no more bottles of beer.\n"
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall.\n"
            )
        elif number == 1:
            return (
                f"{number} {self.container(number)} of beer on the wall, "
                f"{number} {self.container(number)} of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n"
            )
        else:
            return (
                f"{number} {self.container(number)} of beer on the wall, "
                f"{number} {self.container(number)} of beer.\n"
                f"Take one down and pass it around, "
                f"{number-1} {self.container(number-1)} of beer on the wall.\n"
            )
