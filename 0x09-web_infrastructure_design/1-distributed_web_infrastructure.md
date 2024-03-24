## Whiteboard Breakdown: Three-Server Web Infrastructure for foobar.com [invalid URL removed]

This design improves scalability, redundancy, and fault tolerance compared to the single-server setup.

**Components:**

1. **Load Balancer (HAproxy):** This new element sits in front of the web servers, acting as a traffic director. It receives user requests, distributes them among the web servers based on a chosen algorithm (explained below), and sends the response back to the user.

2. **Web Servers (Nginx - Server 1 & 2):** We now have two web servers running Nginx software. The load balancer distributes traffic between them for better performance and redundancy.

3. **Application Server:**  The application server (e.g., PHP-FPM) remains on the same server as before, processing dynamic website content.

4. **Application Files:** The website's codebase resides on a server, accessible by both web servers.

5. **Database Cluster (MySQL):** We introduce a MySQL database cluster with two servers:

    * **Primary Node:** This server holds the main copy of the database and handles all write requests (adding, updating, deleting data).
    * **Replica Node:** This server replicates the data from the primary node in real-time or with a slight delay. It handles read requests (retrieving data) from the application server, reducing load on the primary.

**Explanation:**

* **Load Balancer & Algorithm:** HAproxy can use various algorithms to distribute traffic, such as:
    * **Round Robin:** Requests are distributed sequentially to each web server, ensuring a fair workload.
    * **Least Connections:** HAproxy directs requests to the server with the fewest active connections, optimizing utilization.

* **Active-Passive vs. Active-Active:**
    * **Active-Passive:** Only one web server actively serves traffic (Active), while the other acts as a hot spare (Passive). If the active server fails, the passive one takes over, minimizing downtime.
    * **Active-Active:** Both web servers actively handle traffic, distributing the load and improving performance. However, additional configuration is needed to ensure data consistency across servers.  (We'll use Active-Active in this example)

* **Database Cluster:**
    * The application server primarily interacts with the **Primary Node** to write data.
    * It can read data from either the **Primary Node** or the **Replica Node**, depending on the configuration and workload.

**Improved Scalability:**

Adding web servers allows the infrastructure to handle increased traffic. The load balancer distributes the workload, preventing a single server from becoming overloaded.

**Reduced SPOF:**

While the application server and database cluster still represent potential SPOFs, having two web servers mitigates the risk. If one web server fails, the load balancer directs traffic to the remaining server, minimizing downtime.

**Security Concerns:**

* **Firewall:** This infrastructure lacks a firewall to filter incoming traffic and prevent unauthorized access.
* **HTTPS:** The website doesn't use HTTPS encryption, making data transmission vulnerable to interception.

**Monitoring:**

The setup doesn't include monitoring tools to track server health, application performance, or database activity. This makes it difficult to proactively identify and troubleshoot issues.

**Next Steps:**

* Implement a firewall to secure incoming traffic.
* Configure HTTPS for encrypted communication between users and the website.
* Integrate monitoring tools to track server performance and proactively address potential problems.
