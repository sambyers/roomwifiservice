import meraki
from config import meraki_org

dashboard = meraki.DashboardAPI(output_log=False)

orgs = dashboard.organizations.getOrganizations()
org_id = [org['id'] for org in orgs if org['name'] == meraki_org]

# This script is if you want to generate some meraki wireless networks to fill out drop down in the sample web app.

for n in range(202, 210):
    name = str(n)
    c = dashboard.networks.createOrganizationNetwork(org_id[0], name, 'wireless')
    print(f'Created {c["name"]}')