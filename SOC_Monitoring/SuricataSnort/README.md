# Suricata and Snort

## Competence: **Implementation**
## Duration: **3 days**
## Challenge Type: **Solo**

---

### Follow the courses to aid you:

- [Suricata](https://app.pluralsight.com/ilx/video-courses/clips/50753b79-5e9e-435b-a76d-285797d67e68)
- [Snort](https://youtu.be/ZhFZyE26jys?si=MJ-8O7gtg-aPDS7t)

### Follow the TryHackMe:

- [Snort TryHackMe Room](https://tryhackme.com/r/room/snort)
- [IDSEvasion TryHackMe Room](https://tryhackme.com/r/room/idsevasion)

---

## Tasks

### 1. Setup and Basic Configuration

#### Install Snort on a Separate Virtual Machine

Run the following command to install Snort:

```bash
sudo apt update
sudo apt install snort
```

![image](https://github.com/user-attachments/assets/1d74412f-3f87-483d-9ef5-e6282f895e83)
<!-- Screenshot after installation -->

#### Configure Snort Configuration File (`snort.conf`)

Edit the Snort configuration file:

```bash
sudo nano /etc/snort/snort.conf
```

This will open the `snort.conf` file. In this file, set the `HOME_NET` and `EXTERNAL_NET` variables.

```bash
# Set home and external networks
var HOME_NET your ip
var EXTERNAL_NET !$HOME_NET
```

![image](https://github.com/user-attachments/assets/28ff8a09-7746-4ac5-ae5e-f81c654f87ba)
 <!-- Screenshot of the `snort.conf` file -->

#### Define Rule Path

Next, define the rule path:

```bash
var RULE_PATH /etc/snort/rules
include $RULE_PATH/local.rules
```

![image](https://github.com/user-attachments/assets/c4464679-816c-4da0-958e-2205f49a0c14)
 <!-- Screenshot of rule path in config -->

#### Set Up Logging

Define the logging configuration to capture alerts and logs:

```bash
output log_tcpdump: /var/log/snort/snort.log
output alert_fast: /var/log/snort/alert
```

#### Set Network Interface

Make sure your network interface is correctly defined for traffic capture:

```bash
config interface: enp0s3
```
### 2. Testing and Verification

#### Start Snort in Live Mode

Start Snort to begin capturing live traffic. The following command will display Snort alerts in the terminal:

```bash
sudo snort -A console -c /etc/snort/snort.conf -i enp0s3
```

(./screenshots/snort_live_mode.png) <!-- Screenshot of Snort running in live mode -->

#### Generate Test Traffic

Generate test traffic using `ping` and `nmap`:

1. **Ping Command**:
```bash
ping 8.8.8.8
```
![image](https://github.com/user-attachments/assets/1b699dce-6086-4cb5-b151-3cee60e99362)
 <!-- Screenshot of ping test result -->

2. **Nmap Command**:
```bash
nmap -p 80 --open --script=icmp-ping your ip
```
![image](https://github.com/user-attachments/assets/6086a57c-3afc-47dd-8e5f-13c760e0d234)
 <!-- Screenshot of nmap result -->

#### Verify Traffic Capture

Once test traffic is generated, verify that Snort captures it by checking the logs:

```bash
cat /var/log/snort/alert
```

![image](https://github.com/user-attachments/assets/d6ccd5ff-3310-4a94-8821-a409b8ce97a8)
<!-- Screenshot of Snort alert log -->

---

### 3. Rule Creation and Customization

#### Custom Rules in `local.rules`

Add the following custom rules to **`local.rules`** for detecting ICMP packets and ICMP Echo Requests:

```bash
# Rule to detect any ICMP packet
alert icmp any any -> any any (msg:"ICMP Packet Detected"; sid:1000001;)

# Rule to detect ICMP Echo Requests from the Home Network
alert icmp $HOME_NET any -> $EXTERNAL_NET any (msg:"ICMP Echo Request from Home Network"; itype:8; sid:1000002;)
```

#### Verify Custom Rules

To ensure the custom rules are working, generate the same traffic as earlier (ping or nmap) and check the alerts:

```bash
cat /var/log/snort/alert
---

### 4. Rule Optimization (Optional)

To reduce false positives and optimize detection accuracy, analyze captured traffic and refine the rules. For example, you could adjust the `$HOME_NET` variable or add additional qualifiers to your rules.

---

### 5. Deliverables

- **Screenshots** showing the configuration of Snort, including the **`snort.conf`** file and **`local.rules`**.
- **Logs** demonstrating Snort capturing and logging test traffic.
- **Comparison report** on Snort's configuration and effectiveness of custom rules.
- **Optional report** on the optimization process.

---

### Additional Resources

- [Snort Official Documentation](https://snort.org/)
- [Suricata Official Documentation](https://suricata.io/)
```

