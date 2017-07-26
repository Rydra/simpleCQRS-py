from bus import Bus
from domain import InventoryItem
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


def test_inventory_item():
    item = InventoryItem(10, "potato")
    assert item.id == 10
    assert item.name == "potato"
    assert item.activated


def test_deactivate_inventory_item():
    item = InventoryItem(10, "potato")
    item.deactivate()
    assert not item.activated


def test_load_entity_from_history():
    events = [InventoryItemCreated(10, "businessman"), InventoryItemDeactivated(10)]
    item = InventoryItem()
    item.load_from_history(events)

    assert item.id == 10
    assert item.name == "businessman"
    assert not item.activated
