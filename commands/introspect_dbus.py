from joopney.connection import ConnectionContext
from joopney.dbus_proxy import introspect

with ConnectionContext() as connection:

   print(introspect(connection))
