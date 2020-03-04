import meraki

dashboard = meraki.DashboardAPI(output_log=False)

# To do
# Move AP corp network after RWS usage is finished
# Move AP to room network when RWS usage starts

ssid_definition = {
    'authMode': 'psk',
    'bandSelection': 'Dual band operation',
    'enabled': False,
    'encryptionMode': 'wpa',
    'ipAssignmentMode': 'Bridge mode',
    'lanIsolationEnabled': False,
    'minBitrate': 11,
    'name': '',
    'perClientBandwidthLimitDown': 0,
    'perClientBandwidthLimitUp': 0,
    'psk': '',
    'splashPage': 'None',
    'ssidAdminAccessible': False,
    'useVlanTagging': False,
    'wpaEncryptionMode': 'WPA2 only'
    }

def get_org_names(hotelid):
    orgs = dashboard.organizations.getOrganizations()
    return [org['id'] for org in orgs]

def get_org_network_names(hotelid):
    orgs = dashboard.organizations.getOrganizations()
    org_id = [org['id'] for org in orgs if org['name'] == hotelid]

    nets = dashboard.networks.getOrganizationNetworks(org_id[0])
    return [net['name'] for net in nets]

def provision(hotelid, roomid, name, psk, ssid_definition=ssid_definition):
    orgs = dashboard.organizations.getOrganizations()
    org_id = [org['id'] for org in orgs if org['name'] == hotelid]

    nets = dashboard.networks.getOrganizationNetworks(org_id[0])
    net = [net['id'] for net in nets if net['name'] == roomid]

    ssid_definition['name'] = name
    ssid_definition['psk'] = psk
    ssid_definition['enabled'] = True

    try:
        return dashboard.ssids.updateNetworkSsid(net[0], "0", **ssid_definition)
    except meraki.exceptions.APIError as e:
        return e

def deprovision(hotelid, roomid, ssid_definition=ssid_definition):
    orgs = dashboard.organizations.getOrganizations()
    org_id = [org['id'] for org in orgs if org['name'] == hotelid]

    nets = dashboard.networks.getOrganizationNetworks(org_id[0])
    net = [net['id'] for net in nets if net['name'] == roomid]

    ssid_definition['name'] = 'Unconfigured SSID 1'
    ssid_definition['psk'] = 'unused psk'
    ssid_definition['enabled'] = False

    try:
        return dashboard.ssids.updateNetworkSsid(net[0], "0", **ssid_definition)
    except meraki.exceptions.APIError as e:
        return e

if __name__ == '__main__':
    pass