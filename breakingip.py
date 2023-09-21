import asyncio
import httpx
import os
import socket
import time
from tabulate import tabulate

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    banner = """
██████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██║██╔══██╗
██████╔╝██████╔╝█████╗  ███████║█████╔╝ ██║██╔██╗ ██║██║  ███╗    ██║██████╔╝
██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗ ██║██║╚██╗██║██║   ██║    ██║██╔═══╝ 
██████╔╝██║  ██║███████╗██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    ██║██║     
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝     
                                                                            

Use with moderation, knowledge is not a crime, the crime is the acts used in it.
"""
    print(banner)

def check_target_status(target):
    try:
        # Use o socket para verificar a conexão
        socket.create_connection((target, 80), timeout=10)
        return "Online"
    except (socket.error, socket.timeout):
        return "Offline"

async def send_request(target):
    async with httpx.AsyncClient() as client:
        try:
            start_time = time.time()
            response = await client.get(target, timeout=10)  # Use um timeout razoável
            end_time = time.time()

            # Verifique o código de resposta para detecção mais precisa
            if response.status_code == 200:
                return end_time - start_time
            else:
                return 0
        except Exception as e:
            print(f"Error sending request: {e}")
            return 0

async def send_request_package(target, package_size, num_requests_per_package):
    tasks = []

    for _ in range(package_size):
        task = send_request(target)
        tasks.append(task)

    latencies = await asyncio.gather(*tasks)
    average_latency = sum(latencies) / package_size

    return average_latency

async def perform_requests(target, num_requests, requests_per_package, num_requests_per_package):
    total_latency = 0

    num_packages = num_requests // requests_per_package
    remaining_requests = num_requests % requests_per_package

    print(f"Sending {num_requests} requests to {target} in packages of {requests_per_package} with {num_requests_per_package} requests per package...")
    
    try:
        for _ in range(num_packages):
            average_latency = await send_request_package(target, requests_per_package, num_requests_per_package)
            total_latency += average_latency

        if remaining_requests > 0:
            average_latency = await send_request_package(target, remaining_requests, num_requests_per_package)
            total_latency += average_latency

    except KeyboardInterrupt:
        print("\nUser interrupted the operation. Exiting...")

    return total_latency / num_requests

if __name__ == "__main__":
    clear_terminal()
    show_banner()
    print("Welcome to the HTTP Request Latency Checker!")
    print("Please enter the URL or IP address of the target.")
    target = input("Target (or 'quit' to exit): ")

    if target.lower() == 'quit':
        print("Thanks for using the tool!")
        exit()

    try:
        num_requests = int(input("Total number of requests to send: "))
        requests_per_package = int(input("Requests per package: "))
        num_requests_per_package = int(input("Requests per package (per request): "))
    except ValueError:
        print("Please enter valid numbers.")
        exit(1)

    loop = asyncio.get_event_loop()
    average_latency = loop.run_until_complete(perform_requests(target, num_requests, requests_per_package, num_requests_per_package))
    loop.close()

    status = check_target_status(target)
    
    print("\nResults:")
    table = [["Target", "Status", "Average Latency (s)"],
             [target, status, f"{average_latency:.2f}"]]
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
