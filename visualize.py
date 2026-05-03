import pyshark
import matplotlib.pyplot as plt
from collections import Counter

# Load the pcap file
print("Loading traffic file...")
cap = pyshark.FileCapture('traffic.pcap')

# Collect data
protocols = []
src_ips = []
lengths = []

print("Analyzing packets...")
for packet in cap:
    try:
        protocols.append(packet.highest_layer)
        src_ips.append(packet.ip.src)
        lengths.append(int(packet.length))
    except:
        pass

# Chart 1 - Top 5 Source IPs
ip_counts = Counter(src_ips)
top_ips = dict(ip_counts.most_common(5))

plt.figure(figsize=(10,5))
plt.bar(top_ips.keys(), top_ips.values(), color='green')
plt.title('Top 5 Source IP Addresses')
plt.xlabel('IP Address')
plt.ylabel('Number of Packets')
plt.tight_layout()
plt.savefig('ip_chart.png')
plt.show()
print("IP chart saved!")

# Chart 2 - Packet size distribution
plt.figure(figsize=(10,5))
plt.hist(lengths, bins=50, color='red')
plt.title('Packet Size Distribution')
plt.xlabel('Packet Size (bytes)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('size_chart.png')
plt.show()
print("Size chart saved!")