fwoutput = """
Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Copyright (c) 2002-2015, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under
license. Certain components of this software are licensed under
the GNU General Public License (GPL) version 2.0 or the GNU
Lesser General Public License (LGPL) Version 2.1. A copy of each
such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://www.opensource.org/licenses/lgpl-2.1.php
^Mfnts-fntc03-10gacc-d-sw01# terminal length 0^M
sh int desc | i fiac
^Mfnts-fntc03-10gacc-d-sw01# sh int desc | i fiac^M
Eth1/5        eth    10G     Uplink to fnts-fntc03-fiacc-sw06-A e1/21
Eth1/13       eth    10G     Uplink to fnts-fntc03-fiacc-sw06-B e1/21
Po4                      Uplink to fnts-fntc03-fiacc-sw07-A
Po5                      Uplink to fnts-fntc03-fiacc-sw07-B
Po6                      Uplink to fnts-fntc03-fiacc-sw08-A
Po7                      Uplink to fnts-fntc03-fiacc-sw08-B
Po8                      Uplink to fnts-fntc03-fiacc-sw09-A
Po9                      Uplink to fnts-fntc03-fiacc-sw09-B
Po25                     Uplink to fnts-fntc03-fiacc-sw06-A
Po26                     Uplink to fnts-fntc03-fiacc-sw06-B
^Mfnts-fntc03-10gacc-d-sw01# exit^M#
"""
#placeholder var for 'cmd' var in ssh_host
cmd = 'sh int desc | i fiac'

#filter based on 'cmd' var (delete above 'cmd' and puts string into list)
fwlist = (fwoutput.rpartition(cmd)[-1]).splitlines()

#strip hostname of random characters
hostname = str(fwlist[-1]).replace('^M', '').replace('#', '').replace('exit', '')

print(fwlist)
print(hostname)


