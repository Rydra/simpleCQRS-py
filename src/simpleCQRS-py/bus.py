class Bus:
    def __init__(self):
        self.routes = {}

    def register_handler(self, handler):
        command_type = type(handler)
        if not self.routes.has_key(command_type):
            self.routes[command_type] = []

        self.routes[command_type].append(lambda message: handler(message))


    def send(self, command):
        command_type = type(command)
        if not self.routes.has_key(command_type):
            raise Exception("no handler registered")

        self.routes[command_type][0](command)

    def publish(self, event):
        event_type = type(event)
        if not self.routes.has_key(event_type):
            return

        for handler in self.routes[event_type]:
            handler(event)
