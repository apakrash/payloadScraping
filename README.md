# payloadScraping

This script is used for scraping out the payload from the packet capture. This is very useful in situations where InfoSec rules prevent from sharing packet data for confidentiality preservation


## Usage

There are 2 files that can be run for this:
payloadScraping_1.2.exe or payloadScraping_1.2.py 

## For running payloadScraping_1.2.py

Python 3.x is needed to run this script.

The following library installation is required(pip installation is a pre-requisite): https://pypi.org/project/scapy/ via pip3 install scapy

Place the pcap files and the script in a new folder

The syntax to run the script is: python3 payloadScraping_1.2.py test.pcap test2.pcap

i.e. after python3 payloadScraping.py mention the names of all files separated by a space.

The script will save files with stripped payload with naming convention: strippedPayload_FILENAME



## For running payloadScraping_1.2.exe

Place the exe file and the script in a folder

The syntax to run the script is: python3 payloadScraping_1.2.exe test.pcap

The executable file will save files with stripped payload with naming convention: strippedPayload_FILENAME


For any questions, please reach out to apakrash@cisco.com
