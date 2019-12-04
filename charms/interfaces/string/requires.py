from charmhelpers.core import hookenv
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint, scopes, when


class StringRequires(Endpoint):
    scope = scopes.GLOBAL

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        set_flag(self.expand_name('{endpoint_name}.joined'))

    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        if self.data():
            set_flag(self.expand_name('{endpoint_name}.ready'))
        else:
            clear_flag(self.expand_name('{endpoint_name}.ready'))

    @when('endpoint.{endpoint_name}.departed')
    def departed(self):
        clear_flag(self.expand_name('{endpoint_name}.joined'))
        clear_flag(self.expand_name('{endpoint_name}.ready'))

    def receive_strings(self):
        """Receive the published string """
        strings = []

        for relation in self.relations:
            for unit in relation.units:
                strings.append(unit.received['string'])

        return strings
