class Messenger:
    def __init__(self) -> None:
        self.observers: list= list()
    

    def add_observer(self, observer) -> None:
        self.observers.append(observer)
    

    def remove_observer(self, observer) -> None:
        self.observers.remove(observer)
    

    def notify_observers(self, sender, message: str) -> None:
        for observer in self.observers:
            observer.receive_notification(sender, message)


class User:
    def __init__(self, name: str) -> None:
        self.name = name

    
    def receive_notification(self, sender, message: str) -> None:
        print(f"[{self.name}] New message from '{sender}': {message}")


class Group:
    def __init__(self, name: str) -> None:
        self.name = name
        self.members: list = list()

    
    def add_member(self, member) -> None:
        self.members.append(member)
    

    def receive_notification(self, sender, message) -> None:
        print(f"[Group '{self.name}'] New message from '{sender}': {message}")