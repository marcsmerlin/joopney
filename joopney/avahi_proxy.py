from jeepney import DBusAddress, new_method_call
from jeepney.io.blocking import DBusConnection

from typing import Final

BUS_NAME: Final[str] = 'org.freedesktop.Avahi'
DEFAULT_OBJECT_PATH: Final[str] = '/'
SERVER_INTERFACE: Final[str] = 'org.freedesktop.Avahi.Server2'

PROTO_IPV4: Final = 0
PROTO_IPV6: Final = 1
PROTO_UNSPEC: Final = -1
IF_UNSPEC: Final = -1

class AvahiProxy:
    def __init__(self, object_path: str=None, interface: str=None):
        self.address = DBusAddress(
            object_path=object_path,
            bus_name=BUS_NAME,
            interface=interface)

class AvahiServerProxy(AvahiProxy):
    def __init__(self):
        super().__init__(
            object_path=DEFAULT_OBJECT_PATH,
            interface=SERVER_INTERFACE)

    def get_host_name(self, connection: DBusConnection) -> str:
        message = new_method_call(self.address, 'GetHostName')
        response = connection.send_and_get_reply(message)
        return response.body[0]

    def get_domain_name(self, connection: DBusConnection) -> str:
        message = new_method_call(self.address, 'GetDomainName')
        response = connection.send_and_get_reply(message)
        return response.body[0]

    def entry_group_new(self, connection: DBusConnection) -> str:
        message = new_method_call(self.address, 'EntryGroupNew')
        response = connection.send_and_get_reply(message)
        return response.body[0]

if __name__ == '__main__':

    from connection import ConnectionContext

    with ConnectionContext() as connection:

        print(AvahiServerProxy().get_host_name(connection))
