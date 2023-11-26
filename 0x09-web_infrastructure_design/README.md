# Web infrastructure design

*You can see the project diagrams from [here](./projectDiagrams/)*
## Overview

This project outlines the design and implementation of a secure and scalable web infrastructure for hosting the website `www.foobar.com`. The infrastructure is designed to ensure high availability, secure data transmission, and effective monitoring.

## Components

1. **Load-Balancer (Nginx):**
    - Serves as a load balancer, distributing incoming traffic among multiple web servers.
    - Terminates SSL to ensure encrypted communication.

1. **Web Servers (Nginx):**
    - Two web servers to handle incoming HTTP and HTTPS requests.
    - Serve static content and forward dynamic content requests to the application server.

1. **Application Server:**
    - Processes dynamic content requests from web servers.
    - Communicates with the database and executes application code.

1. **Application Files (Code Base):**
    - Contains the website's codebase, including HTML, CSS, JavaScript, and server-side code.
    - Stored on both web servers for redundancy.

1. **Database (MySQL):**
    - Stores and manages data used by the application.

1. **Firewalls:**
    - Three firewalls control incoming and outgoing traffic, enhancing security.

1. **SSL Certificate:**
    - Enables HTTPS for www.foobar.com, ensuring secure data transmission.

1. **Monitoring Clients:**
    - Data collectors for monitoring services (e.g., Sumo Logic) gather insights into infrastructure health and performance.

## Specifics of the Infrastructure
- **Firewalls:** Ensure security by controlling traffic, preventing unauthorized access, and protecting against potential threats.

- **HTTPS:** Encrypts data in transit, ensuring the confidentiality and integrity of transmitted information.

- **Monitoring:** Provides insights into infrastructure health and performance for proactive management.

- **SSL Termination at Load Balancer:** Simplifies certificate management; consider implications for internal network encryption.

- **MySQL Cluster:** Consider implementing a MySQL cluster for high availability and fault tolerance.

- **Diverse Components:** Introduce diversity or redundancy in critical areas to mitigate risks of simultaneous failures.

## Issues and Considerations

1. **SSL Termination at Load Balancer:**
    - Consider the implications for internal network encryption and adjust the setup accordingly.

1. **Single MySQL Server Accepting Writes:**
    - Consider implementing a MySQL cluster with replicas for high availability.

1. **Identical Components Across Servers:**
    - Assess the risk and, if necessary, introduce diversity or redundancy in critical areas.
