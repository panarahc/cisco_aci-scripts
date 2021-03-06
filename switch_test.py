#!/usr/bin/env python
'''
Autogenerated code using webarya.py
Original Object Document Input: 
{"totalCount":"1","imdata":[{"infraNodeP":{"attributes":{"descr":"","dn":"uni/infra/nprof-Leafs","name":"Leafs","ownerKey":"","ownerTag":""},"children":[{"infraLeafS":{"attributes":{"descr":"","name":"Leafs","ownerKey":"","ownerTag":"","type":"range"},"children":[{"infraNodeBlk":{"attributes":{"descr":"","from_":"201","name":"3a608b521b4633b7","to_":"202"}}}]}},{"infraRsAccPortP":{"attributes":{"tDn":"uni/infra/accportprof-RPIs"}}},{"infraRsAccPortP":{"attributes":{"tDn":"uni/infra/accportprof-Routers"}}}]}}]}
'''


# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.infra
from cobra.internal.codec.xmlcodec import toXMLStr

# ACI Toolkit packages
import acitoolkit.acitoolkit as ACI

# All the other stuff we need.
import sys, random, string

def hello_message():
    print "\nPlease be cautious with this application.  The author did very little error checking and can't ensure it will work as expected.\n"
    print description
    junk = raw_input('Press Enter/Return to continue.')
    return

def load_utils():
    try:
        global GO
        import go_utils as GO
    except:
        print 'Can not find go_utils.py.  This file is required.'
        exit()

def load_config():
    try:
        global GO_CONFIG
        import go_lab_config as GO_CONFIG

    except ImportError:
        print 'No config file found (go_lab_config.py).  Use "--makeconfig" to create a base file.'
        exit()
    except:
        print 'There is syntax error with your config file.  Please use the python interactive interpreture to diagnose. (python; import go_lab_config)'
        exit()

load_utils()
load_config()

admin_info = GO.collect_admin(GO_CONFIG)
cobra_md = GO.cobra_login(admin_info)




# the top level object on which operations will be made
# Confirm the dn below is for your top dn
topDn = cobra.mit.naming.Dn.fromString('uni/infra/nprof-Leafs')
topParentDn = topDn.getParent()
topMo = cobra_md.lookupByDn(topParentDn)

# build the request using cobra syntax
infraNodeP = cobra.model.infra.NodeP(topMo, ownerKey=u'', name=u'Leafs', descr=u'', ownerTag=u'')
infraLeafS = cobra.model.infra.LeafS(infraNodeP, ownerKey=u'', type=u'range', name=u'Leafs', descr=u'', ownerTag=u'')
infraNodeBlk = cobra.model.infra.NodeBlk(infraLeafS, from_=u'201', name=u'3a608b521b4633b7', descr=u'', to_=u'202')
infraRsAccPortP = cobra.model.infra.RsAccPortP(infraNodeP, tDn=u'uni/infra/accportprof-RPIs')
infraRsAccPortP2 = cobra.model.infra.RsAccPortP(infraNodeP, tDn=u'uni/infra/accportprof-Routers')


# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
cobra_md.commit(c)