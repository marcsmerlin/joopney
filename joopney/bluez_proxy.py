from typing import Any, Final

from jeepney import DBusAddress, new_method_call, Properties
from jeepney.io.blocking import DBusConnection

from joopney.introspectable_proxy import IntrospectableProxy

BUS_NAME: Final[str] = 'org.bluez'
DEFAULT_PATH: Final[str] = '/org/bluez'
HCI0_OBJECT_PATH: Final[str] = '/org/bluez/hci0'
ADAPTER_INTERFACE: Final[str] = 'org.bluez.Adapter1'

def introspect(connection: DBusConnection) -> str:
    return IntrospectableProxy(
        object_path=DEFAULT_PATH,
        bus_name=BUS_NAME
    ).introspect(connection=connection)

class BluezProxy:
    def __init__(self, object_path: str=None, interface: str=None):
        self.address = DBusAddress(
            object_path=object_path,
            bus_name='org.bluez',
            interface=interface)

class BluezHCI0Proxy(BluezProxy):
    def __init__(self):
        super().__init__(object_path=HCI0_OBJECT_PATH, interface=ADAPTER_INTERFACE)

    def start_discovery(self, connection: DBusConnection) -> None:
        message = new_method_call(self.address, 'StartDiscovery')
        connection.send_and_get_reply(message)

    def stop_discovery(self, connection) -> None:
        message = new_method_call(self.address, 'StopDiscovery')
        connection.send_and_get_reply(message)

    def get_all(self, connection: DBusConnection) -> dict[str, Any]:
        reply = connection.send_and_get_reply(Properties(self.address).get_all())
        return reply.body[0]

    def get(self, connection: DBusConnection, field: str) -> Any:
        reply = connection.send_and_get_reply(Properties(self.address).get(field))
        return reply.body[0][1]

if __name__ == '__main__':

    from connection import ConnectionContext

    with ConnectionContext() as connection:
        proxy = BluezHCI0Proxy()

        print(proxy.get_all(connection).keys())
