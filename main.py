import socket

def check_server(host, port=80):
    """Check if a server is reachable via TCP."""
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"✅ Server {host}:{port} is reachable.")
    except Exception as e:
        print(f"❌ Server {host}:{port} is unreachable. {e}")

def main():
    servers = ["103.248.228.188"]
    for server in servers:
        print(f"\n🔄 Checking {server}...")
        check_server(server, 65431)  # 443 端口是 HTTPS
        print("-" * 50)

if __name__ == "__main__":
    main()
