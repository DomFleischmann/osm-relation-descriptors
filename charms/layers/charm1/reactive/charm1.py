from charmhelpers.core.hookenv import status_set, log
from charms.reactive import clear_flag, set_flag, when, when_not, endpoint_form_flag
import charms.sshproxy


@when('sshproxy.configured')
@when_not('charm1.installed')
def install_charm1_proxy_charm():
    """Set the status to active when ssh configured."""
    set_flag('charm1.installed')
    status_set('active', 'Ready!')

@when('string.joined')
def send_hostname:
    """ Sends hostname of the machine """
    err = ''
    try:
        cmd = ['hostname']
        result, err = charms.sshproxy._run(cmd)
    except:
        log('command failed: {}'.format(err))
    else:
        string_interface = endpoint_from_flag('string.joined')
        string_interface.publish_string(result)
        clear_flag('osm-vca.joined')
