class Comment:
    def __init__(self, text, author) -> None:
        self._text = text
        self._author = author
        self._replies = []
        self._soft_deleted = False

    def add_reply(self, comment) -> None:
        self._replies.append(comment)

    def text(self) -> str:
        if self._soft_deleted:
            return "Цей коментар було видалено."

        return f"{self._author}: {self._text}"

    def remove_reply(self) -> None:
        self._soft_deleted = True

    def restore_reply(self) -> None:
        self._soft_deleted = False

    def display(self, padding=0) -> str:
        print(" "*padding + self.text())

        for reply in self._replies:
            reply.display(padding+4)
