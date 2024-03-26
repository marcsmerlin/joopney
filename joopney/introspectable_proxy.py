from jeepney import DBusAddress, new_method_call, Message
from jeepney.io.blocking import DBusConnection

class IntrospectableProxy:

    def __init__(
            self,
            object_path: str,
            bus_name:str
        ):

        self.address = DBusAddress(
            object_path=object_path,
            bus_name=bus_name,
            interface='org.freedesktop.DBus.Introspectable'
        )

    def introspect(self, connection: DBusConnection) -> str:
        message: Message = new_method_call(self.address, 'Introspect')
        response = connection.send_and_get_reply(message)
        return response.body[0]
