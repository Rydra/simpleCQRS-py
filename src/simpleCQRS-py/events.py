class Message:
    pass


class Event(Message):
    def __init__(self, version=0):
        self.version = version


class InventoryItemDeactivated(Event):
    def __init__(self, id):
        Event.__init__(self)
        self.id = id


class InventoryItemCreated(Event):
    def __init__(self, id, name):
        Event.__init__(self)
        self.id = id
        self.name = name