import os
import subprocess

def ping_server(host):
    """Ping a server and return its status."""
    try:
        output = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True, check=True)
        print(f"Server {host} is reachable.\n")
        print(output.stdout)
    except subprocess.CalledProcessError:
        print(f"Server {host} is unreachable.\n")

def main():
    """Main function to ping multiple servers."""
    servers = [
        "google.com",
        "103.248.228.188",
    ]
    
    for server in servers:
        print(f"Pinging {server}...")
        ping_server(server)
        print("-" * 50)

if __name__ == "__main__":
    main()
