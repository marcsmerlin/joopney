from joopney.connection import ConnectionContext
from joopney.bluez_proxy import introspect

from common import print_xml

with ConnectionContext() as connection:

   print_xml(introspect(connection))
