# Zeek Network Traffic Analysis

## Overview
This document details the process of generating and analyzing network traffic using Zeek. The analysis covers different types of traffic, log analysis, and identification of suspicious activities.

## 1. Traffic Generation
We simulated various types of network traffic between the host and the VM to observe how Zeek logs them.

### Browsing Websites (HTTP/HTTPS Traffic)
- Accessed multiple websites using Mozilla Firefox.
- Observed HTTP and HTTPS requests.

**Screenshot:**
![image](https://github.com/user-attachments/assets/5832dde0-2781-4494-a844-332b4d66a3f9)


### Performing DNS Queries
- Used `nslookup` and `dig` to resolve domain names.

```bash
nslookup example.com
```

**Screenshot:**

![image](https://github.com/user-attachments/assets/0b92bacc-b502-4521-8cef-e2f570628d8d)


### Using SSH for Remote Connections
- Connected from the host to the VM using SSH.

```bash
ssh user@vm-ip
```
## 2. Simulating Malicious Activities
To test Zeek’s ability to detect anomalies, we introduced the following activities:

### Running a Port Scan
- Used `nmap` to scan open ports on the VM.

```bash
nmap -sS -p- vm-ip
```

**Screenshot:**

![image](https://github.com/user-attachments/assets/7ceafac5-ee53-450f-8bca-bf3defbcd723)


### Sending Suspicious HTTP Requests
- Accessed an HTTP-only URL to check for insecure communication.

```bash
curl -v http://example.com
```

**Screenshot:**

![image](https://github.com/user-attachments/assets/8d6fe930-23b7-4d8b-9cf8-f6cee2e3c94c)


## 3. Log Analysis
Zeek generated logs for all network activities. Below are key logs analyzed:

### Connection Log (`conn.log`)
- Summarizes all network connections.

```bash
cat /usr/local/zeek/logs/current/conn.log
```

**Screenshot:**

![image](https://github.com/user-attachments/assets/63e9449d-580e-44e1-9d3b-cd8531b562b1)


### HTTP Log (`http.log`)
- Records details of HTTP requests.

```bash
cat /usr/local/zeek/logs/current/http.log
```

**Screenshot:**

![image](https://github.com/user-attachments/assets/2a8198c2-fb6b-4ef6-ac44-2583438a2452)


### DNS Log (`dns.log`)
- Captures all DNS queries.

```bash
cat /usr/local/zeek/logs/current/dns.log
```

**Screenshot:**

![image](https://github.com/user-attachments/assets/5dc73e81-8ac5-4f51-a6d2-79966b772d5d)


### SSL Log (`ssl.log`)
- Lists all SSL/TLS sessions.

```bash
cat /usr/local/zeek/logs/current/ssl.log
```

**Screenshot:**

![image](https://github.com/user-attachments/assets/47337c2a-5a11-4ff3-8b23-3589940159ae)

### Weird Log (`weird.log`)
- Detects anomalies in network traffic.

```bash
cat /usr/local/zeek/logs/current/weird.log
```
**Screenshot:**

![image](https://github.com/user-attachments/assets/b4eea6e1-647d-4e8f-809e-fc110ad2d3d4)


## 4. Summary and Findings
- Different types of traffic were successfully logged by Zeek.
- Suspicious activities such as port scanning and HTTP requests were detected in `weird.log` and `conn.log`.
- DNS queries and SSL connections were logged as expected.

## 5. Conclusion
Zeek effectively monitors network traffic and detects anomalies. By analyzing its logs, we can identify potential security threats and ensure better network visibility.

