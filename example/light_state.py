from typing import Protocol

# State Interface
class LightState(Protocol):
    def switch(self, bulb) -> None:
        ...

# Object
class Bulb:
    def __init__(self):
        self.state = OnState()

    def switch(self) -> None:
        self.state.switch(self)
        

# Concrete State
class OnState:
    def switch(self, bulb) -> None:
        bulb.state = OffState()
        print("Light is Off.")
        

# Concrete State
class OffState:
    def switch(self, bulb: Bulb) -> None:
        bulb.state = OnState()
        print("Light is on.")


def main() -> None:
    b = Bulb()
    b.switch()
    b.switch()


if __name__ == '__main__':
    main()
