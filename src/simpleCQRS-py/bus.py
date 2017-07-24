class Bus:
    def __init__(self):
        self.routes = {}

    def register_handler(self, message_type, handler):
        if not (message_type in self.routes):
            self.routes[message_type] = []

        self.routes[message_type].append(lambda message: handler(message))

    def send(self, command):
        command_type = type(command)
        if not (command_type in self.routes):
            raise Exception("no handler registered")

        self.routes[command_type][0](command)

    def publish(self, event):
        event_type = type(event)
        if not (event_type in self.routes):
            return

        for handler in self.routes[event_type]:
            handler(event)
