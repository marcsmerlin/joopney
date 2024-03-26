from pprint import pprint

from connection import ConnectionContext
from dbus_proxy import DefaultDBusProxy

with ConnectionContext() as connection:

    pprint(DefaultDBusProxy().list_activatable_names(connection))
