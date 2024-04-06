from cloudflareddns.cloudflareddns import get_public_ip, update
from dotenv import load_dotenv
import os
from datetime import datetime
import time

CF_API_EMAIL = "CF_API_EMAIL"
CF_API_KEY = "CF_API_KEY"
CF_HOSTS = "CF_HOSTS"
REFRESH_PERIOD = "REFRESH_PERIOD"

def validate_env():
    required_env = [CF_API_EMAIL, CF_API_KEY, CF_HOSTS]
    for env_var in required_env:
        if env_var not in os.environ:
            raise Exception(f"{env_var} env not set")
    
    if REFRESH_PERIOD not in os.environ:
        os.environ[REFRESH_PERIOD] = 300


def main():
    print(f"DDNS update started at {str(datetime.now())}")
    
    hosts_str = os.environ[CF_HOSTS]
    public_ip = get_public_ip()

    hosts = hosts_str.split(";")
    for host in hosts:
        print(f"Updating host {host} -> {public_ip}...", end="", flush=True)
        res = update(host, public_ip)
        print(res)


if __name__ == "__main__":
    load_dotenv()
    validate_env()
    
    refresh_sleep = int(os.environ[REFRESH_PERIOD])
    while True:
        main()
        print(f"Sleeping for {refresh_sleep}s")
        time.sleep(refresh_sleep)
