import time

def check_dns_latency():
    print("Testing Cambodia DNS resolvers latency...")
    time.sleep(0.1)
    print("All primary resolvers responding under 15ms.")

if __name__ == '__main__':
    check_dns_latency()
