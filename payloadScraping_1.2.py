__author__ = "Abhishek Pakrashi(apakrash)"
__email__ = "apakrash@cisco.com"
__status__ = "alpha"

from scapy.all import *
import sys

for INFILE in sys.argv[1:]:
    print('processing ' + INFILE)
    OUTFILE = 'strippedPayload_' + INFILE
    paks = rdpcap(INFILE)
    for pak in paks:
        if TCP in pak:
                pak[TCP].remove_payload()
        elif UDP in pak:
                pak[UDP].remove_payload()
    wrpcap(OUTFILE, paks)
    print(OUTFILE+' written')