import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl1 = driver(hostname='10.0.0.1', username='cisco', password='cisco', optional_args={'secret':'cisco'})
iosvl1.open()

ios_output = iosvl1.get_facts()
print(json.dumps(ios_output, indent=4))

ios_output = iosvl1.get_interfaces()
print(json.dumps(ios_output, indent=4))
