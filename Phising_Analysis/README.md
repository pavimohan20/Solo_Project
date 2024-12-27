# Phishing Analysis Assignment

## **Overview**
This document outlines the analysis performed on 5 emails provided in `.eml` format. The goal is to identify phishing emails and document the findings using appropriate tools and methodologies. 

## **Mission**
As a SOC analyst, the task is to:
- Analyze 5 `.eml` emails.
- Identify potential phishing emails.
- Write a detailed report with observations and tool usage.

## **Phishing Fundamentals**
Before starting, complete the following TryHackMe rooms:
1. [Phishing Emails 1](https://tryhackme.com/room/phishingemails1tryoe)
2. [Phishing Emails 2](https://tryhackme.com/room/phishingemails2rytmuv)

## **Analysis Workflow**
### **General Steps for Scanning `.eml` Files**
1. **Open the `.eml` file**:
   - Use an email client (Thunderbird, Outlook) or a text editor for source code.
2. **Inspect Email Headers**:
   - Identify sender, recipient, date, and subject.
   - Look for unusual mail servers or relay paths.
3. **Check Email Content**:
   - Look for suspicious links, attachments, or requests for sensitive data.
4. **Analyze Attachments and Links**:
   - Use tools like VirusTotal to scan attachments and decode shortened URLs.
5. **Use Specialized Tools**:
   - Employ PhishTools, MX Lookup, Spamhaus, etc., to gather threat intelligence.

---

## **Questions to Answer**
For each email, document:
1. **Timestamp**: When was the email sent?
2. **Sender**: Who sent the email?
3. **Sender's Email Address**: Verify the email address of the sender.
4. **Reply-To Address**: Does it differ from the sender's address?
5. **Brand Impersonation**: Which brand is being mimicked?
6. **Originating IP**: Extract and defang it.
7. **Domain of Interest**: Identify and defang the domain.
8. **Shortened URL**: Decode and defang the URL.
9. **Phishing Verdict**: Is it phishing or legitimate? Explain your reasoning.

---

## **Tools Used**
### **1. VirusTotal**
- Scans files and URLs for malicious content.
- [VirusTotal Website](https://www.virustotal.com)

### **2. PhishTools**
- Combines threat intelligence and OSINT for email analysis.
- [PhishTools Website](https://phish.tools)

### **3. MX Lookup**
- Verifies mail server records for the domain.
- [MX Lookup Website](https://mxtoolbox.com)

### **4. PhishTank**
- Collaborative platform for phishing data and analysis.
- [PhishTank Website](https://www.phishtank.com)

### **5. Spamhaus**
- Provides threat intelligence for network security.
- [Spamhaus Website](https://www.spamhaus.org)

---

## **Phishing Incident Response Playbook**
### **1. Prepare**
- Train employees on phishing awareness.
- Deploy and maintain email security solutions.

### **2. Detect**
- Identify phishing emails via automated tools or user reports.

### **3. Analyze**
- Inspect headers, content, links, and attachments.
- Use analysis tools to identify malicious indicators.

### **4. Contain**
- Block domains, URLs, or attachments in email systems.
- Notify users not to interact with the email.

### **5. Eradicate**
- Remove phishing emails from mailboxes.
- Reset credentials for compromised accounts.

### **6. Recover**
- Restore affected systems.
- Monitor for further phishing activity.

### **7. Post-Incident Handling**
- Conduct a review and update security measures.
- Document lessons learned and share findings.

---

## **Example Report Format**
| **Email** | **Question**                     | **Details**                                                                 |
|-----------|-----------------------------------|-----------------------------------------------------------------------------|
| Email 1   | Timestamp                        | 2024-12-25 12:34:56 UTC                                                   |
|           | Sender                           | John Doe                                                                   |
|           | Sender's Email Address           | john.doe@example.com                                                      |
|           | Reply-To Address                 | phishing.scam@example.com                                                 |
|           | Brand Impersonated               | Amazon                                                                    |
|           | Originating IP (Defanged)        | 192.168.0[.]1                                                             |
|           | Domain of Interest (Defanged)    | phishing-site[.]com                                                       |
|           | Shortened URL (Defanged)         | bit[.]ly/phish123                                                         |
|           | Phishing Verdict                 | Yes (contains malicious links impersonating Amazon login)                 |

---

## **Submission Requirements**
- **Report**: Include screenshots of tools used for each email.
- **Documentation**: Save the findings in the provided Excel sheet.
- **Summary**: Add an overview of key findings and recommendations.

---

## **References**
- [TryHackMe Rooms](https://tryhackme.com)
- [VirusTotal](https://www.virustotal.com)
- [PhishTank](https://www.phishtank.com)

---
