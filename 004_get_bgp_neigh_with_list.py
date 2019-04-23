import json
from napalm import get_network_driver

bgplist = ['10.0.0.1', '10.0.0.2']

for ip in bgplist:
    print("Connecting to " + str(ip))
    driver = get_network_driver('ios')
    iosvl1 = driver(ip, username='cisco', password='cisco', optional_args={'secret':'cisco'})
    iosvl1.open()
    ios_output = iosvl1.get_bgp_neighbors()
    print(json.dumps(ios_output, indent=4))
    iosvl1.close()
