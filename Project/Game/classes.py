class Items:
    def __init__(self, name):
        self.name = name


class Rooms:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.routes = []

    def connect(self, other):
        if other not in self.routes:
            self.routes.append(other)
            other.routes.append(self)


class Player:
    def __init__(self, name, age, location, days_left=30):
        self.name = name
        self.age = age
        self.location = location
        self.days_left = days_left
        self.items = []
        self.collected = []

    def has_item(self, item_name):
        return item_name in [item.name for item in self.items]

    def collect(self, item):
        self.items.append(item)
        self.collected.append(item.name)
        self.location.items.remove(item)
        return True

    def move(self, destination):
        self.location = destination
        self.days_left -= 1