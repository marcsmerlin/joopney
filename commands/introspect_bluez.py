from joopney.connection import ConnectionContext
from joopney.bluez_proxy import introspect

with ConnectionContext() as connection:

   print(introspect(connection))
   