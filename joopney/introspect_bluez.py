from connection import ConnectionContext
from bluez_proxy import introspect

with ConnectionContext() as connection:

   print(introspect(connection))