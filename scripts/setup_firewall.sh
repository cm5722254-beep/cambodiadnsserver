#!/bin/bash
iptables -t nat -A PREROUTING -i eth0 -p udp --dport 5300 -j REDIRECT --to-ports 7300
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p udp --dport 7300 -j ACCEPT
