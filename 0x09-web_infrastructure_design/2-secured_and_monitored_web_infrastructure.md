## Whiteboard Breakdown: Secured and Monitored Three-Server Web Infrastructure for foobar.com [invalid URL removed]

This design prioritizes security, scalability, and proactive monitoring compared to the previous setups.

**Components:**

1. **Load Balancer (HAproxy):** Similar to the previous design, the load balancer distributes traffic among the web servers.

2. **Firewalls (Internal, Web Server, Database):** Three firewalls provide additional security:

    * **Internal Firewall:** Filters traffic between servers within the infrastructure.
    * **Web Server Firewall:** Located in front of each web server, it filters incoming traffic before it reaches the web server. 
    * **Database Firewall:** Controls access to the database server.

3. **Web Servers (Nginx - Server 1 & 2):** These servers run Nginx and terminate SSL/TLS encryption for HTTPS traffic.

4. **Application Server:** The application server processes dynamic website content.

5. **Application Files:** The website's codebase resides on a separate server for better security.

6. **Database Cluster (MySQL):** Similar to before, we have a MySQL cluster with:

    * **Primary Node:** Handles write requests.
    * **Replica Node:** Replicates data from the primary for read requests.

7. **Monitoring Clients:**  Each server runs a monitoring client that collects data on server performance, application health, and database activity.

8. **Monitoring Service (e.g., Sumologic):** This external service receives data from the monitoring clients and provides a central platform for analyzing and visualizing server health.

**Explanation:**

**Security Enhancements:**

* **Firewalls:** These filter incoming and outgoing traffic, blocking malicious attempts and improving overall security.
* **HTTPS:**  An SSL certificate encrypts communication between the user's browser and the web server, protecting sensitive data like login credentials.  Terminating SSL at the load balancer is explained in the limitations section.

**Monitoring:**

* **Monitoring Clients:** These lightweight software agents collect performance metrics from the servers and applications.
* **Monitoring Service:**  An external service like Sumologic centralizes data collection, allowing for real-time monitoring, historical analysis, and alerting for potential issues. 
* **Monitoring QPS:** To monitor web server QPS (Queries Per Second), the monitoring client can track the number of requests processed by the web server within a specific timeframe. This helps identify potential bottlenecks or resource limitations.


**Improved Scalability:**

The infrastructure can handle increased traffic by adding more web servers behind the load balancer.

**Limitations:**

* **SSL Termination at Load Balancer:** While terminating SSL at the load balancer can improve performance, it requires additional configuration to ensure secure communication between the load balancer and web servers. It's generally recommended to terminate SSL at the web server level for better security.
* **Single Write Server:** The MySQL cluster still has a single point of failure for write operations. Implementing a multi-master or Galera cluster configuration can improve write availability.
* **Homogeneous Servers:**  Having all components on each server can be inefficient. Consider separating the database server from the web servers for better resource management and security.

**Next Steps:**

* Consider a multi-master or Galera cluster for the MySQL database to improve write availability.
* Separate database servers from web servers for better resource allocation and security.
* Explore containerization technologies like Docker for easier deployment and scaling.

By implementing these security measures and monitoring tools, you can proactively identify and address issues before they impact website functionality. 
