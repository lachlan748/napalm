#assumes the following commands are enabled on the destination devie:
#aaa authorization exec default local
#aaa new-model
#aaa authentication login default local
#ip scp server enable

import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.0.0.1', 'cisco', 'cisco', optional_args={'secret':'cisco'})
iosvl2.open()

print ('Accessing 10.0.0.1')
iosvl2.load_merge_candidate(filename='005_acl.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No changes required.')
    iosvl2.discard_config()

iosvl2.close()
