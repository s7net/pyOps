# pyOps

## HTTP Client Creator with Limited Access

### Installation
Download the server script:
```bash
wget https://s7net.github.io/pyOps/server.py
```

### Usage
Start the server with restricted access:
```bash
python server.py --bind <SERVER_IP> --allow <ALLOWED_IPS>
```
- `<SERVER_IP>`: The IP address to bind the server.
- `<ALLOWED_IPS>`: Comma-separated list of IPs allowed to connect.

---
