from bus import Bus
from events import InventoryItemCreated, InventoryItemDeactivated
from readmodel import InventoryListHandler, BullshitDB


def test_register_handler():
    bus = Bus()

    inventory_list_handler = InventoryListHandler()
    bus.register_handler(InventoryItemCreated, inventory_list_handler.handle)
    bus.register_handler(InventoryItemDeactivated, inventory_list_handler.handle)

    message = InventoryItemCreated(10, 'potato')
    bus.publish(message)
    assert len(BullshitDB.list) == 1

    message = InventoryItemDeactivated(10)
    bus.publish(message)
    assert len(BullshitDB.list) == 0
