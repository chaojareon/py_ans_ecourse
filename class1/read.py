import yaml
import json
from pprint import pprint

with open("ymltst.yml") as y:
    yaml_list = yaml.load(y)

with open("jsntst.json") as j:
    json_list = json.load(j)

y.close()
j.close()

print "YAML pretty print:"
pprint(yaml_list)
print "\nJSON pretty print:"
pprint(json_list)

