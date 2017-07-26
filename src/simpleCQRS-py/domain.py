from events import InventoryItemDeactivated, InventoryItemCreated


class AggregateRoot:
    def __init__(self, event_map):
        self._changes = []
        self._event_map = event_map
        self._version = 0

    @property
    def id(self):
        raise NotImplementedError()

    @property
    def version(self):
        return self._version

    def get_uncommited_changes(self):
        return self._changes

    def mark_changed_as_commited(self):
        self._changes.clear()

    def load_from_history(self, history):
        for event in history:
            self._apply_change(event, False)

    def _apply_change(self, event, is_new=True):
        event_type = type(event)
        if event_type in self._event_map:
            self._event_map[event_type](event)

        if is_new:
            self._changes.append(event)

class InventoryItem(AggregateRoot):

    def __init__(self, id=None, name=None):
        event_map = {
            InventoryItemDeactivated: self._apply_inventory_deactivated_item_event,
            InventoryItemCreated: self._apply_inventory_created_item_event
        }

        super().__init__(event_map)

        if id is not None:
            self._apply_change(InventoryItemCreated(id, name))

    @property
    def id(self):
        return self._id

    def _apply_inventory_created_item_event(self, event):
        self._id = event.id
        self.name = event.name
        self.activated = True

    def _apply_inventory_deactivated_item_event(self, event):
        self.activated = False

    def deactivate(self):
        if not self.activated:
            raise Exception("Already activated")

        self._apply_change(InventoryItemDeactivated(self._id))
