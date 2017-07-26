class Repository:
    def __init__(self, storage, type):
        self._storage = storage
        self.type = type

    def save(self, entity):
        self._storage.save_event(entity.id, entity.get_uncommited_changes())

    def get(self, id):
        obj = self.type()
        events = self._storage.get_events(id)
        obj.load_from_history(events)
        return obj