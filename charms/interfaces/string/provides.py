from charmhelpers.core import hookenv
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint, scopes, when


class StringProvides(Endpoint):
    scope = scopes.GLOBAL

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        set_flag(self.expand_name('{endpoint_name}.joined'))

    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        set_flag(self.expand_name('{endpoint_name}.ready'))

    @when('endpoint.{endpoint_name}.departed')
    def departed(self):
        clear_flag(self.expand_name('{endpoint_name}.joined'))
        clear_flag(self.expand_name('{endpoint_name}.ready'))

    def publish_string(self, string):
        """Publish the string"""

        for relation in self.relations:
            relation.to_publish['string'] = string
