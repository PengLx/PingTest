import platform
import subprocess

def ping_server(host):
    """Ping a server to check connectivity."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]
    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Server {host} is reachable.\n")
        print(output.stdout)
    except subprocess.CalledProcessError:
        print(f"Server {host} is unreachable.\n")

def main():
    """Main function to ping multiple servers."""
    servers = [
        "103.248.228.188"
    ]
    
    for server in servers:
        print(f"Pinging {server}...")
        ping_server(server)
        print("-" * 50)

if __name__ == "__main__":
    main()
