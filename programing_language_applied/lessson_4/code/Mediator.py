class ControlTower:
    def __init__(self):
        self.planes: list = list()

    
    def add_plane(self, plane) -> None:
        self.planes.append(plane)
        plane.register_current_tower(self)


    def send_message(self, plane, message: str) -> None:
        print(f"Control Tower to '{plane.name}': {message}")
        for other_plane in self.planes:
            if other_plane != plane:
                other_plane.receive_message(plane, message)


class Plane:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tower = None

    
    def register_current_tower(self, tower: ControlTower) -> None:
        self.tower = tower


    def send_message(self, message: str):
        self.tower.send_message(self, message)


    def receive_message(self, plane, message: str) -> None:
        print(f"{self.name} received a message from {plane.name}: {message}")