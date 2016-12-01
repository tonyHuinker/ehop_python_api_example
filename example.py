
import csv
import json
import ConfigParser
from Ehop import Ehop


###############################################################
######## Variables                                     ########
###############################################################

vars_file = "vars.cfg"

# Load Vars
config = ConfigParser.ConfigParser()
config.read(vars_file)
eh_host = config.get("DEFAULT","eh_host")          # Extrahop Host
api_key = config.get("DEFAULT", "api_key")

###############################################################
######## Program Start                                 ########
###############################################################

eh = Ehop(host=eh_host,apikey=api_key)

#example of querying a device group and getting slowest users by loadtime
body = '{ "cycle": "auto", "from": -604800000, "metric_category": "ica_user_detail", "metric_specs": [ { "name": "load_time" } ], "object_ids": [ 0 ], "object_type": "application", "until": 0 }'
metrics = json.loads(eh.api_request("POST", "metrics/total", body=body).read())

for stat in metrics['stats']:
    values = stat['values']
    for value in values:
        for obj in value:
            val = obj['value']
            key = obj['key']
            load = val['sum']
            name = key['str']
            print "user name " + str(name) + " had a load time of " + str(load)
