from typing import TypeAlias

from jeepney.io.blocking import DBusConnection, open_dbus_connection

Connection: TypeAlias = DBusConnection

class ConnectionContext:

    def __init__(self, bus: str='SYSTEM'):

        self.bus: str = bus

    def __enter__(self):
        self.connection: DBusConnection = open_dbus_connection(bus=self.bus)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

