from transport import Transport


class Airplane(Transport):
    def fly(self):
        print(f"{self.name} is flying")

    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def show_wingspan(self):
        print(f"Wingspan of {self.name}: {self.wingspan} meters")
