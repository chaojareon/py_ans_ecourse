from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

print "All the crypto entries and thier children:\n"

for i in range(0,len(crypto)):
    print crypto[i]
    for child in crypto[i].all_children:
        print " " + child.text

pfsgroup2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO",childspec=r"set pfs group2")

print "\nEntries with pfs group2:\n"

for i in range(0,len(pfsgroup2)):
    print pfsgroup2[i]
    for child in pfsgroup2[i].all_children:
        print " " + child.text

notaes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO",childspec=r"set transform-set AES-SHA")

print "\nEntries not using AES:\n"

for i in range(0,len(notaes)):
    print notaes[i]
    for child in notaes[i].all_children:
        print " " + child.text
