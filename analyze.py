import pyshark
import matplotlib.pyplot as plt
from collections import Counter

# Load the pcap file
print("Loading traffic file...")
cap = pyshark.FileCapture('traffic.pcap')
# Collect data
protocols = []
src_ips = []

print("Analyzing packets...")
for packet in cap:
    try:
        protocols.append(packet.highest_layer)
        src_ips.append(packet.ip.src)
    except:
        pass

print(f"Total packets analyzed: {len(protocols)}")

# Count protocols
protocol_counts = Counter(protocols)
ip_counts = Counter(src_ips)

# Print results
print("\nTop Protocols:")
for proto, count in protocol_counts.most_common(5):
    print(f"  {proto}: {count} packets")

print("\nTop Source IPs:")
for ip, count in ip_counts.most_common(5):
    print(f"  {ip}: {count} packets")

# Plot protocol chart
plt.figure(figsize=(10,5))
plt.bar(list(protocol_counts.keys())[:10], list(protocol_counts.values())[:10], color='blue')
plt.title('Network Protocols Distribution')
plt.xlabel('Protocol')
plt.ylabel('Number of Packets')
plt.tight_layout()
plt.savefig('protocols_chart.png')
plt.show()
print("Chart saved!")