# Sysmon for Linux Installation and Configuration Guide

This guide provides a step-by-step walkthrough for installing and configuring Sysmon on a Kali Linux virtual machine. Sysmon is a powerful tool for monitoring and logging system activity, aiding in security analysis and system monitoring.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation Steps](#installation-steps)
4. [Configuration](#configuration)
5. [Testing the Setup](#testing-the-setup)
6. [Troubleshooting](#troubleshooting)
7. [Conclusion](#conclusion)

## Introduction

System Monitor (Sysmon) is a system service that logs system activity to assist in detecting malicious or anomalous behavior. Originally developed for Windows, Sysmon is now available for Linux systems, providing detailed information about process creations, network connections, and file modifications.

## Prerequisites

Before proceeding, ensure you have:

- A Kali Linux virtual machine set up.
- Sudo privileges to install and configure system services.
- An active internet connection for downloading packages.

## Installation Steps

1. **Update System Packages**

   Begin by updating your package lists to ensure you have the latest information on available packages:

   ```bash
   sudo apt-get update
   ```
![image](https://github.com/user-attachments/assets/8ec5f425-42c5-4a27-8890-61574e7dadaf)

   

2. **Install Required Dependencies**

   Sysmon for Linux may require certain dependencies. Install them using:

   ```bash
   sudo apt-get install -y apt-transport-https
   ```

  ![image](https://github.com/user-attachments/assets/f4b2032f-af4b-4b61-b47f-d52ea5132aa8)


3. **Add Microsoft's Package Repository**

   Download and install the Microsoft package repository to access Sysmon:

   ```bash
   wget -q https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
   sudo dpkg -i packages-microsoft-prod.deb
   ```

  ![image](https://github.com/user-attachments/assets/2ba9cfb6-ace5-4c5b-8328-92065f19718e)


4. **Install Sysmon for Linux**

   With the repository added, install Sysmon:

   ```bash
   sudo apt-get update
   sudo apt-get install -y sysmonforlinux
   ```

   ![image](https://github.com/user-attachments/assets/f206db3e-d033-4226-91fc-40d47504244f)


## Configuration

1. **Create a Configuration Directory**

   Create a directory to store Sysmon's configuration file:

   ```bash
   sudo mkdir -p /etc/sysmon
   ```

2. **Download a Sample Configuration File**

   Download a sample configuration file to customize:

   ```bash
   sudo curl -o /etc/sysmon/sysmonconfig.xml https://raw.githubusercontent.com/SwiftOnSecurity/sysmon-config/master/sysmonconfig-export.xml
   ```

3. **Edit the Configuration File**

   Open the configuration file with a text editor:

   ```bash
   sudo nano /etc/sysmon/sysmonconfig.xml
   ```

   Customize the `<EventFiltering>` section as needed. For example, to exclude process creation events by the root user, add:

   ```xml
   <EventFiltering>
     <ProcessCreate onmatch="exclude">
       <User condition="is">root</User>
     </ProcessCreate>
   </EventFiltering>
   ```

4. **Apply the Configuration**

   Install or update Sysmon with the new configuration:

   ```bash
   sudo sysmon -i /etc/sysmon/sysmonconfig.xml
   ```

## Testing the Setup

1. **Verify Sysmon is Running**

   Check the status of the Sysmon service:

   ```bash
   sudo systemctl status sysmon
   ```
![image](https://github.com/user-attachments/assets/fbfa5e0e-fc4a-4423-ab94-8e1e33c0b7d1)


2. **Generate Test Events**

   Perform actions such as creating or deleting files, and starting or stopping processes to generate logs.

3. **Review Logs**

   Sysmon logs can be found in the system's syslog. View them using:

   ```bash
   sudo grep 'Sysmon' /var/log/syslog
   ```
   ![image](https://github.com/user-attachments/assets/15a4d02f-4691-479f-9464-70eccf5522be)

## **Simulating Common System Activities**

To generate events for monitoring:

### Create a File

```bash
touch /tmp/testfile.txt
```

### Modify the File

```bash
echo "Sample content" > /tmp/testfile.txt
```

### Delete the File

```bash
rm /tmp/testfile.txt
```

### Start a Process

```bash
sleep 60 &
```
![image](https://github.com/user-attachments/assets/98a212fb-4934-4365-af88-05a176c7419f)


### Establish a Network Connection

```bash
nc -l 8080 &
```
![image](https://github.com/user-attachments/assets/83d60ce9-f559-462f-a0b8-ac3398378fe0)


## 2. Analyzing Sysmon Logs

Sysmon logs are typically stored in `/var/log/syslog`. To filter and view Sysmon-related logs:

```bash
sudo grep 'ProcessCreate' /var/log/syslog
```

To view logs in a human-readable format:

```bash
sudo /opt/sysmon/sysmonLogView /var/log/syslog
```


## 3. Stopping Sysmon

To stop the Sysmon service:

```bash
sudo systemctl stop sysmon
```

To disable Sysmon from starting on boot:

```bash
sudo systemctl disable sysmon
```

## Troubleshooting

- **Issue:** `sysmon: command not found`

  **Solution:** Ensure that Sysmon is installed correctly. Verify the installation path and that it's included in your system's `PATH` variable.

- **Issue:** `curl: (23) Failure writing output to destination`

  **Solution:** Ensure the destination directory exists and that you have write permissions. For example, create the directory `/etc/sysmon` if it doesn't exist.

## Conclusion

By following this guide, you've successfully installed and configured Sysmon for Linux on your Kali Linux virtual machine. Sysmon is now actively monitoring your system, providing detailed logs to assist in security analysis and system monitoring.


