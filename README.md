# Network Traffic Analysis with Wireshark

## What is this project?
This project analyzes real network traffic captured using Wireshark and visualizes it using Python.

## Tools Used
- Wireshark 4.6.5
- Python 3
- PyShark library
- Matplotlib library

## What it does
- Captures live network traffic using Wireshark
- Analyzes 36,000+ real network packets
- Identifies protocols like TCP, TLS, DNS, QUIC, NTP
- Generates a bar chart showing protocol distribution

## How to run
1. Install Wireshark
2. Install Python libraries: pip install pyshark matplotlib
3. Place your traffic.pcap file in the project folder
4. Run analyze.py


## Project Files
- analyze.py - Main analysis script
- visualize.py - Additional visualizations
- requirements.txt - Required libraries
- summary_report.txt - Analysis results report
- protocols_chart.png - Protocol distribution chart
- ip_chart.png - Top source IPs chart
- size_chart.png - Packet size distribution chart

## Team Members
- Chhavi Bhagat (Technical Implementation)
- [Partner Name] (Presentation)
 ## Results
The analysis showed that QUIC and TCP were the most common protocols in the captured traffic.
