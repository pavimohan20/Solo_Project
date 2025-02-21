# Suricata Forensics Challenge

## Overview

**Type of Challenge:** Forensics  
**Duration:** 1 day  
**Challenge Type:** Solo  

The objective of this challenge was to configure and deploy Suricata in a test environment, analyze network traffic, create custom rules, and generate detailed reports based on the findings.

---

## 1. Environment Setup

### Installation of Suricata

- Suricata was installed on a virtual machine.
- Dependencies such as `libpcap`, `libnet`, and others were installed to ensure proper functionality.

### Commands to install Suricata:

```bash
sudo apt update
sudo apt install suricata
```

**Screenshot:**  
![image](https://github.com/user-attachments/assets/d4a1445f-d5cb-4ab0-acdb-05a29de4aeb7)


---

## 2. Initial Configuration

### Suricata YAML Configuration

The Suricata configuration file (`/etc/suricata/suricata.yaml`) was updated to set up network interfaces for live traffic capture and enable logging in both JSON and EVE format. Below are the changes made to the configuration file:

#### Network Interface Configuration

The `interface` section was updated to specify the network interface to capture live traffic. The following changes were made:

```yaml
# interface: enp0s3
# Set the interface to capture live traffic
interface: enp0s3``

#### Logging Configuration

The logging settings were modified to log output in both `eve.json` and `suricata.log` files for later analysis. The following configuration changes were made:

```yaml
outputs:
  - eve-log:
      enabled: yes
      filetype: regular
      filename: /var/log/suricata/eve.json
      types:
        - alert
        - dns
        - http
        - tls
  - syslog:
      enabled: yes
      facility: local0
      level: info
      enable-file-cache: yes
```

These changes enable logging to both JSON format for detailed alerts (`eve.json`) and the standard `suricata.log` file.

#### AF-Packet Configuration

The AF-Packet interface was configured for optimized packet capture and analysis. The following configuration was added:

```yaml
af-packet:
  - interface: enp0s3
    threads: auto
    cluster-id: 102
    cluster-type: cluster_flow
    defrag: yes
    use-nmap: yes
    ring-size: 2048
```

This configuration sets up packet capture on the `enp0s3` interface, with features like automatic threading (`threads: auto`), flow clustering (`cluster-type: cluster_flow`), fragmentation reassembly (`defrag: yes`), Nmap support (`use-nmap: yes`), and a ring size of `2048`.

---

## 3. Basic Testing

### Starting Suricata in Live Mode

Suricata was started in live mode to capture and log network traffic.

### Commands used to start Suricata:

```bash
sudo suricata -c /etc/suricata/suricata.yaml -i enp0s3
```

### Verifying Traffic Capture

Various network traffic was generated using tools like `curl`, `ping`, and `nmap` to test Suricata's ability to log traffic.

**Screenshot:**  

![image](https://github.com/user-attachments/assets/9f6f42bc-c063-4e01-95da-7cff718bbd0d)

---

## 4. Understanding Suricata Rules

The existing Suricata rules were studied to understand their structure. Documentation on writing custom rules was consulted to create new rules tailored to detect specific types of network behavior.

---

## 5. Creating Custom Rules

Five custom Suricata rules were created to detect specific network behaviors:
  sudo nano /var/lib/suricata/rules/local.rules

1. **SSH Login Attempts**  
   Detects login attempts on SSH.
   
2. **HTTP Requests to /admin URI**  
   Detects HTTP GET requests to the `/admin` URI.

3. **Suspicious DNS Queries**  
   Detects suspicious DNS queries for known malicious domains.

4. **Large HTTP Responses**  
   Detects large HTTP responses that might indicate data exfiltration.

5. **SSH Brute Force Attempts**  
   Detects brute force attempts on SSH.

**Custom Rules:**

```plaintext
alert tcp any any -> any 22 (msg:"SSH login attempt"; content:"Password"; pcre:"/Password\s+/"; sid:1000001;)
alert http any any -> any any (msg:"HTTP request to /admin URI"; content:"GET /admin"; http_method; sid:1000002;)
alert dns any any -> any any (msg:"Suspicious DNS query for malicious domain"; dns.query; content:"malicious-domain.com"; sid:1000003;)
alert http any any -> any any (msg:"Large HTTP response (potential data exfiltration)"; content:"HTTP/1.1 200 OK"; http_response; sid:1000004;)
alert tcp any any -> any 22 (msg:"SSH brute force attempt detected"; flow:to_server,established; content:"Failed password"; pcre:"/Failed password/"; sid:1000005;)
```

---

## 6. Deliverables

### A. Screenshot of the Suricata Configuration File

- Included in the configuration section above.

### B. Zip File with Logs Showing Suricata Successfully Capturing and Logging Traffic

- The logs have been successfully captured and are available in the following zip file:
  ![image](https://github.com/user-attachments/assets/463b7263-0b11-46d2-8b7a-5aaa538342e8)


### C. Report

- A detailed report (3 pages) on the setup, initial findings, and issues encountered has been provided separately.

---

## Conclusion

This project successfully demonstrated the installation, configuration, and rule creation capabilities of Suricata for detecting various network behaviors. By generating specific traffic and triggering the rules, the system captured valuable information to be used for forensic analysis.
```
