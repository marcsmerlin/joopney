from pprint import pprint
from typing import List

from connection import ConnectionContext
from dbus_proxy import DefaultDBusProxy

with ConnectionContext() as connection:

    names: List[str] = DefaultDBusProxy().list_activatable_names(connection)
    names.sort()
    pprint(names)
