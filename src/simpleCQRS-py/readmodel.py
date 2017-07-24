from events import InventoryItemCreated, InventoryItemDeactivated


class InventoryItemListDto:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class InventoryListHandler:

    def __init__(self):
        self.handlers = {
            InventoryItemCreated: self.handle_inventory_item_created,
            InventoryItemDeactivated: self.handle_inventory_item_deactivated
        }

    def handle_inventory_item_created(self, inventory_item_created_message):
        BullshitDB.list.append(InventoryItemListDto(inventory_item_created_message.id, inventory_item_created_message.name))

    def handle_inventory_item_deactivated(self, inventory_item_deactivated):
        BullshitDB.list = [item for item in BullshitDB.list if item.id != inventory_item_deactivated.id]

    def handle(self, message):
        self.handlers[type(message)](message)



class BullshitDB:
    details = {}
    list = []


class ReadModelFacade:
    def get_inventory_items(self):
        return BullshitDB.list

    def get_inventory_item_details(self, id):
        return BullshitDB.details[id]
