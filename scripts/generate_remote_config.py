import json

config = {
    "app_name": "CHM Cambodia DNS",
    "version": "2.0",
    "notice": "Welcome to CHM Cambodia DNS VIP",
    "servers": [
        {"name": "Cambodia VIP 01", "ip": "103.216.x.x", "ssl_port": 443},
        {"name": "Cambodia VIP 02 (Gaming)", "ip": "103.216.x.y", "ssl_port": 443}
    ]
}

with open('remote_config_output.json', 'w') as f:
    json.dump(config, f, indent=2)
print("Config generated successfully.")
