import xmlrpc.client as xc
import xmlrpc.server as xs
class TestLink:
    def get_testlink_integration(self):
        #enter code hereenter code here
        client = xc.Server('http://' + host + ':' + port + '/RPC2')
        client.supervisor.getState()
        client.supervisor.getProcessInfo('process name')
