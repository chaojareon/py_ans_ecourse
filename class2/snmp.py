from snmp_helper import snmp_get_oid,snmp_extract

OID1 = '1.3.6.1.2.1.1.5.0'
OID2 = '1.3.6.1.2.1.1.1.0'

PORT1 = 8061
PORT2 = 7961

device1 = ('50.76.53.27','galileo',PORT1)
device2 = ('50.76.53.27','galileo',PORT2)

snmp_data = snmp_get_oid(device1, oid=OID2)
output = snmp_extract(snmp_data)
print output
snmp_data = snmp_get_oid(device1, oid=OID1)
output = snmp_extract(snmp_data)
print output
snmp_data = snmp_get_oid(device2, oid=OID2)
output = snmp_extract(snmp_data)
print output
snmp_data = snmp_get_oid(device2, oid=OID1)
output = snmp_extract(snmp_data)
print output
