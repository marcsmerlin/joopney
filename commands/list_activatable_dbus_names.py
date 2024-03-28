from pprint import pprint
from typing import List

from joopney.connection import ConnectionContext
from joopney.dbus_proxy import DefaultDBusProxy

with ConnectionContext() as connection:

    names: List[str] = DefaultDBusProxy().list_activatable_names(connection)
    names.sort()
    pprint(names)