# **El Doctor - A Monitoring Tool to Rule Them All!**

## **Module:** Scripting  
## **Competence:** Able to write a custom script to monitor machines  
## **Type of Challenge:** Consolidation  

---

## **Mission Overview**

In this challenge, I was tasked with creating a custom monitoring tool, **El Doctor**, from scratch. Unlike traditional pre-made monitoring tools with graphical dashboards, this tool is designed to be lightweight, script-based, and customizable to suit different monitoring needs. The main aim was to monitor system metrics, display them interactively, collect data at regular intervals, and send notifications when certain system thresholds are met.

---

## **Key Features**

### 1. **Interactive Curses Interface (dialog_monitor.sh)**
   - An interactive command-line interface (CLI) was implemented using **`dialog`** (or a curses-based library), which provides a user-friendly and real-time display of system metrics.
   - The interface includes:
     - **CPU usage**
     - **Memory usage**
     - **Disk space**
     - **Network usage**
   - The interface is continuously updated, giving the user an overview of the system's health in real time.

### 2. **System Metrics Collection (show_metrics.sh)**
   - This script runs on a scheduled cron job to collect key system metrics such as:
     - **CPU Usage**
     - **RAM Usage**
     - **Disk Space Usage**
     - **Network Statistics**
   - The collected data is stored in a **CSV file** for historical analysis. The file is appended every hour with the latest metrics.
   - Example output of the CSV file format:
     ```
     Date, Time, CPU Usage, RAM Usage, Disk Space Usage
     2024-11-15, 14:00, 25%, 60%, 50%
     2024-11-15, 15:00, 30%, 55%, 49%
     ```

### 3. **Alert System (send_weekly_report.sh)**
   - The **`send_weekly_report.sh`** script sends an automatic email every week with a summary of the system's health.
   - If a critical condition is detected (such as high CPU usage, low RAM, etc.), the system will send an immediate notification to the configured email address.
   - The script checks system parameters and sends an email using `sendmail` or other available mail programs (e.g., `msmtp`).
   - The weekly report is sent every Sunday at 5:00 PM, and it includes:
     - **CPU Usage**
     - **Memory Usage**
     - **Disk Space**
     - **Network Stats**
     - **Alerts for Critical Conditions** (e.g., CPU usage > 90%, RAM < 20%)

---

## **Cron Jobs**

To ensure the tool is running efficiently, cron jobs have been set up to:

1. **Collect Metrics Every Hour:**
   The following cron job is configured to run **show_metrics.sh** every hour to capture system data.
   ```bash
   0 * * * * /bin/bash /home/pavithra/show_metrics.sh
