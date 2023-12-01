from dataclasses import dataclass
from typing import Protocol

# State Interface
class DocumentState(Protocol):
    def edit(self):
        ...

    def review(self):
        ...

    def finalise(self):
        ...

# State Context
class DocumentContext(Protocol):
    content: list[str]

    def set_state(self, state: DocumentState):
        ...

    def edit(self):
        ...

    def review(self):
        ...

    def finalise(self):
        ...

    def show_content(self):
        ...

# Concrete State
@dataclass
class Draft:
    document: DocumentContext

    def edit(self):
        print("Editing the document....")
        self.document.content.append("Edited content.")

    def review(self):
        print("Document under review")
        self.document.set_state(Review(self.document))

    def finalise(self):
        print("You need to review the document before finalising.")


# Concrete State
@dataclass
class Review:
    document: DocumentContext

    def edit(self):
        print("The document is under review, cannot edit now.")

    def review(self):
        print("The document is already reviewed.")

    def finalise(self):
        print("Finalising the document....")
        self.document.set_state(Publish(self.document))


# Concrete State
@dataclass
class Publish:
    document: DocumentContext

    def edit(self):
        print("The document is finalised. Editing is not allowed.")

    def review(self):
        print("The document is finalised. Review is not possible.")

    def finalise(self):
        print("The document is already finalised.")


# Object
class Document:
    def __init__(self):
        self.state: DocumentState = Draft(self)
        self.content: list[str] = []

    def set_state(self, state):
        self.state = state

    def edit(self):
        self.state.edit()

    def review(self):
        self.state.review()

    def finalise(self):
        self.state.finalise()

    def show_content(self):
        print("Document content:", " ".join(self.content))


def main():
    document = Document()
    document.edit()
    document.review()
    document.edit()
    document.finalise()
    document.review()
    document.edit()
    document.show_content()


if __name__ == "__main__":
    main()
