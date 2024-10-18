import json
import proxy

proxies = []
failed = []
sender = []

with open('data.json', 'r') as f:
    file = json.load(f)

for line in file:
    proxies.append(proxy.proxy(line['id'], line['name'], line['online'], line['deviceMetrics']['batteryLevel']))
iter = 0
for p in proxies:
    print(f"Proxy: {iter}")
    p.printInfos()
    iter += 1

# If a online proxy finds itself on a failed list, remove it from the failed list
# Get its ip, if the filter fails, that specifc proxy is saved as failed
# If the failed proxy is in the failed list, ignores
# Else stores it on the senders list
# Goes one by one on the senders list
# Get its name (It will determinate the group and the proxy itself) 
# Send a message like "Proxy sma 01 está offline"
# Resets the proxies list (keeps stored the failed list)
# Resets the senders list
# Waits 5 minutes
