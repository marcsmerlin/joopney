from typing import Final, Any

from jeepney import DBusAddress, new_method_call, Properties, Message
from jeepney.io.blocking import DBusConnection

from connection import ConnectionContext
from introspectable_proxy import IntrospectableProxy

BUS_NAME: Final[str] = 'org.freedesktop.DBus'
DEFAULT_PATH: Final[str] = '/org/freedesktop/DBus'
DEFAULT_INTERFACE: Final[str] = 'org.freedesktop.DBus'


def introspect(connection: DBusConnection) -> str:
    return IntrospectableProxy(
        object_path=DEFAULT_PATH,
        bus_name=BUS_NAME
    ).introspect(connection=connection)


class DBusProxy:
    def __init__(self, object_path: str=None, interface: str=None):
        self.address = DBusAddress(
            object_path=object_path,
            bus_name=BUS_NAME,
            interface=interface)


class DefaultDBusProxy(DBusProxy):
    def __init__(self):
        super().__init__(object_path=DEFAULT_PATH, interface=DEFAULT_INTERFACE)

    def list_names(self, connection: DBusConnection) -> [str]:
        message = new_method_call(self.address, 'ListNames')
        response = connection.send_and_get_reply(message)
        return response.body[0]

    def list_activatable_names(self, connection: DBusConnection) -> [str]:
        message = new_method_call(self.address, 'ListActivatableNames')
        response = connection.send_and_get_reply(message)
        return response.body[0]

    def get_all(self, connection: DBusConnection) -> dict[str, Any]:
        reply = connection.send_and_get_reply(Properties(self.address).get_all())
        return reply.body[0]

    def get(self, connection: DBusConnection, field: str) -> dict[str, Any]:
        reply = connection.send_and_get_reply(Properties(self.address).get(field))
        return reply.body[0][1]

    def hello(self, connection: DBusConnection, greeting:str='') -> None:
        message: Message = new_method_call(
            remote_obj=self.address,
            method='Hello',
            signature='s',
            body=(greeting,))

        connection.send(message=message)


if __name__ == '__main__':

    with ConnectionContext() as connection:

        import pprint

        pprint.pprint(DefaultDBusProxy().list_activatable_names(connection))
