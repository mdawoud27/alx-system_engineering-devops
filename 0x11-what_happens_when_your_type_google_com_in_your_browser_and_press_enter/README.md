# What happens when you type `google.com` in your browser and press Enter: From URL to Web Page

Blog Link: [Medium](https://medium.com/@dawoud27/understanding-the-journey-of-a-web-request-from-url-to-web-page-fba784c9e4bf) || [LinkedIn](https://www.linkedin.com/pulse/what-happens-when-you-type-googlecom-your-browser-press-dawoud-ks19f)

When we use the internet daily, we enter URLs into our browsers and patiently wait for the page we want to see to load. But have you ever thought about what happens behind the scenes when you do that?

In this article, we will understand the journey of a web request from the *URL address* to the *web page* and explore how this complex process works.

*But first let's understand the URL structure take a look of the following picture:*

![URL Pic](./images/URL.png) 

## DNS Request: Gateway to the Internet
*The journey of a web request begins when you enter a URL into your browser.*

- Initially, the browser sends a request to the **Domain Name System (DNS)** to convert the entered *URL address* into an *IP address*. This process helps enable communication with the hosting server of the website you are trying to access.

- It sends a DNS query to a DNS resolver, which then recursively queries various DNS servers until it obtains the IP address associated with the domain name.

![IP Address image](./images/ip.png)

## TCP/IP: Establishing Connections
*The Transmission **Control Protocol/Internet Protocol (TCP/IP)** is a suite of communication protocols used to connect devices on a network. It is the basis for the Internet and most other modern networks.*

- Once the browser obtains the *IP address*, it establishes a connection using the **Transmission Control Protocol (TCP)** via the **Internet Protocol (IP)**.

- This connection allows for reliable data transmission by segmenting information into **packets** ready for transmission across the network.


- **TCP/IP** forms the backbone of internet communication, facilitating seamless connectivity between clients and servers.

## Firewall: Safeguarding the Gateway

*Before data packets reach their destination, they may encounter firewalls.* 

Firewalls act as vigilant guards, filtering incoming and outgoing traffic to protect networks from unauthorized access and potential threats.

Through predefined rules and policies, firewalls regulate traffic flow, ensuring secure and controlled communication channels.

![Firewall picture](./images/firewall.png)
<!-- Reference https://us.norton.com/blog/privacy/firewall -->

## HTTPS/SSL: Ensuring Secure Communication

**Security** and **privacy** *are essential when browsing the internet, In our quest for secure browsing, HTTPS steps onto the stage.*

Therefore, the **Secure Hypertext Transfer Protocol (HTTPS)** with *SSL/TLS* encryption is used to secure data transmission between the *browser* and the *server*.

HTTPS prevents eavesdropping and unauthorized access to sensitive information exchanged during browsing sessions.

![HTTPS/SSL Picture](./images/HTTPS.jpg)

<!-- Reference https://medium.com/@kasunpdh/ssl-handshake-explained-4dabb87cdce -->

## Load Balancer: Distributing the Load

*A load balancer is a device that distributes incoming network traffic across multiple servers.*

Large-scale and expanding websites use **load balancers** to distribute incoming traffic across multiple servers. 

Load balancers optimize resource *utilization*, *enhance scalability*, and *improve fault tolerance* by evenly distributing the workload among various servers.

![Load balencer](./images/load-balencer.png)

## Web Server: Serving up the Content

*Once our request reaches its destination, it encounters the web server hosting the requested web page.*

- The **web server** processes your request, retrieves the relevant resources such as HTML, CSS, and JavaScript files, and constructs a response to send back to your browser.

- Through *HTTP* or *HTTPS* protocols, web servers *fulfill* user requests, *retrieving* and *transmitting relevant data* for rendering in the browser.

![Web server](./images/Types-of-Web-Servers.webp)

## Application Server: Executing Dynamic Content

*In some cases, the **web server** may require assistance from an **application server** to fulfill your request.*

- **Application servers** execute server-side scripts and handle dynamic content generation, interfacing with databases and external services to process user requests.

- By executing server-side logic, application servers facilitate dynamic web experiences, enabling personalized content delivery and interactive functionalities.

## Database: Where Data Resides

*Behind many web applications lies a database where crucial data is **stored** and **retrieved**.*

- **Databases** store structured data used by web *applications*, *providing persistent storage for user information*, *content*, and *system configurations*.

- **Application servers** interact with **databases** to *retrieve*, *manipulate*, and *update data*, ensuring seamless integration between frontend interfaces and backend data sources.

![databases](./images/database.png)

## Conclusion: Navigating the Digital Landscape

Understanding the journey of a web request reveals a sophisticated system of interconnected technologies. 

From the *URL address* to delivering the *final page*, each component plays a vital role in organizing the flow of information across the internet. 

By understanding these details, we not only enhance our appreciation for the digital landscape but also empower ourselves to navigate it with confidence and understanding.

*So, the next time you enter a URL into your browser, contemplate the intricate journey it embarks on to bring the web to your fingertips.*

![The whole pic](./images/alx-task.png)
