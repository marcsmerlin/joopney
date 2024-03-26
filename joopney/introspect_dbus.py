from connection import ConnectionContext
from dbus_proxy import introspect

with ConnectionContext() as connection:

   print(introspect(connection))
