Tool Name: Breaking IP

Description: Breaking IP is a tool developed in Python that allows you to make customizable requests to HTTP and HTTPS services. You can specify the number of requests to be sent, the destination URL and other options to test the performance and availability of a web server. This tool can be useful for evaluating the responsiveness of a server under load or for checking the availability of an online service.

Main features:

Customizable sending of HTTP/HTTPS requests.
Flexible configuration of request quantities.
Measurement of average request latency.
Server availability assessment.
Simple and interactive command line interface.
Recommended Use: Breaking IP can be used for testing, monitoring and evaluating web services. It is important to note that the responsible and ethical use of this tool is fundamental, and it should only be used on systems and services for which you have permission and authorization.

Always remember to follow the applicable policies and regulations when carrying out tests on servers and web services. Make sure that your use of the tool is ethical and legal.


NEW UPDATE:

User Interruption Handling (Ctrl + C): A try and except KeyboardInterrupt block has been added to capture the user's interruption (Ctrl + C) and display a message thanking the user for using the tool before exiting.

Display Improvements: Minor formatting and display improvements have been made to make the interface more visually pleasing.

Request Timeout: A timeout of 10 seconds has been added to each HTTP request to prevent the program from getting stuck in cases of lengthy connections.

Response Code Check: The HTTP request response code is now checked, and if the code is 200 (OK), the latency time is recorded. This improves accuracy in detecting target connectivity.

Entry of Number of Requests per Packet: An option has been added for the user to specify how many requests should be included in each sending packet. This allows greater flexibility in configuring requests.

![Capturar](https://github.com/lixz07/breakingip/assets/138683122/42c2f34b-463d-4676-980f-d9898f0dc4f0)



Last update: 21/09/2023

