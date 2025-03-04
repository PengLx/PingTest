import subprocess

def ping_server(host):
    """Ping a server and return its status."""
    try:
        output = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
        if output.returncode == 0:
            print(f"✅ Server {host} is reachable.")
        else:
            print(f"❌ Server {host} is unreachable.")
        print(output.stdout)
    except Exception as e:
        print(f"⚠️ Error pinging {host}: {e}")

def main():
    """Main function to ping multiple servers."""
    servers = [
        "google.com",  # Google DNS
        "103.248.228.188"
    ]
    
    for server in servers:
        print(f"\n🔄 Pinging {server}...")
        ping_server(server)
        print("-" * 50)

if __name__ == "__main__":
    main()
