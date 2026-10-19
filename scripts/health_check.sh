#!/bin/bash
services=("nginx" "badvpn-udpgw" "dropbear")
for s in "${services[@]}"; do
    if ! systemctl is-active --quiet "$s"; then
        systemctl restart "$s"
    fi
done
