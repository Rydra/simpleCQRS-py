class Message:
    pass

class Event(Message):
    def __init__(self, version):
        self.version = version

class InventoryItemDeactivated(Event):
    def __init__(self, id, version):
        Event.__init__(self, version)
        self.id = id

class InventoryItemCreated(Event):
    def __init__(self, id, name, version):
        Event.__init__(self, version)
        self.id = id
        self.name = name