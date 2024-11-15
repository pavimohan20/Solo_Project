# El Doctor - A Monitoring Tool to Rule Them All

## Overview

**El Doctor** is a custom-built system monitoring tool designed to provide real-time insights into the health of your machine. Unlike many pre-built solutions, **El Doctor** offers a simple, script-based approach with interactive features and email notifications, allowing you to monitor critical system metrics such as CPU usage, RAM, disk space, and network activity. The tool also sends weekly reports and alerts when the system enters a critical state.

---

## Key Features

- **Interactive Curses Interface:**
  - A user-friendly command-line interface (CLI) using `dialog` to display real-time system metrics.
  - Monitors CPU usage, memory usage, disk space, and network statistics.
  
- **System Metrics Collection:**
  - Periodically collects key system metrics every hour.
  - Stores the data in a CSV file for historical analysis and performance tracking.
  
- **Critical Alert System:**
  - Sends notifications if the system reaches critical thresholds (e.g., high CPU usage, low available RAM).
  
- **Weekly System Report:**
  - Sends a detailed system health report via email every week.
  - Contains CPU usage, RAM usage, disk space usage, network stats, and alerts for critical conditions.

---

## Prerequisites

Before running **El Doctor**, make sure your machine has the following installed:

- **Dialog** (for the curses interface):
  ```bash
  sudo apt-get install dialog
Mail Utility (such as msmtp or sendmail for email notifications):
bash
Copy code
sudo apt-get install msmtp
Files Included
show_metrics.sh: Script for collecting system metrics (CPU, RAM, disk space, etc.) every hour.
dialog_monitor.sh: Interactive curses-based interface for real-time system monitoring.
send_weekly_report.sh: Script that sends a weekly report via email with system health details.
cron_jobs.sh: Configuration file for setting up the cron jobs to execute the scripts at scheduled intervals.
Installation & Setup
1. Clone the Repository
Start by cloning this repository to your machine:

bash
Copy code
git clone https://github.com/your-username/el-doctor.git
cd el-doctor
2. Configure Cron Jobs
To automate the scripts, you need to configure cron jobs for periodic execution.

Hourly Metrics Collection: This cron job runs the show_metrics.sh script every hour. Open your crontab with:

bash
Copy code
crontab -e
Then add the following line:

bash
Copy code
0 * * * * /bin/bash /home/your-username/el-doctor/show_metrics.sh
Weekly Report: This cron job runs send_weekly_report.sh every Sunday at 5:00 PM. Add the following line to your crontab:

bash
Copy code
0 17 * * 0 /bin/bash -c '/home/your-username/el-doctor/send_weekly_report.sh'
3. Set Up Email Notifications
Make sure you have configured an email utility like msmtp or sendmail to send email alerts.

For msmtp, update your configuration in ~/.msmtprc:

ini
Copy code
account default
host smtp.gmail.com
port 587
from your-email@gmail.com
auth on
user your-email@gmail.com
password your-app-password
tls on
For sendmail, configure your SMTP server as required.

Make sure to replace your-email@gmail.com and your-app-password with your actual email address and app-specific password (for Gmail).

Usage
Running Scripts Manually
You can manually run any of the scripts if you need immediate results.

Run the Metrics Collection Script:

bash
Copy code
/bin/bash /home/your-username/el-doctor/show_metrics.sh
Run the Interactive Monitoring Interface:

bash
Copy code
/bin/bash /home/your-username/el-doctor/dialog_monitor.sh
Email Alerts
The critical alert system checks for system thresholds (e.g., high CPU usage or low available RAM). If any of the conditions are met, the system will send an email to the configured address.

Example email alert for high CPU usage:

bash
Copy code
if [ $(echo "$cpu_usage > 90" | bc) -eq 1 ]; then
  echo "CPU Usage is Critical!" | mail -s "Critical Alert: CPU Usage High" user@example.com
fi
Folder Structure
bash
Copy code
el-doctor/
├── show_metrics.sh              # Collect system metrics every hour
├── dialog_monitor.sh            # Interactive monitoring interface (curses)
├── send_weekly_report.sh        # Send weekly system health report
├── cron_jobs.sh                 # Cron job configuration for automation
Example Output
CSV File Format (Metrics are logged every hour):

mathematica
Copy code
Date, Time, CPU Usage, RAM Usage, Disk Space Usage
2024-11-15, 14:00, 25%, 60%, 50%
2024-11-15, 15:00, 30%, 55%, 49%
Weekly Report Email (Sent every Sunday):

yaml
Copy code
Subject: Weekly System Health Report
Body:
- CPU Usage: 80%
- Memory Usage: 75%
- Disk Space: 60%
- Alerts: None
Final Thoughts
El Doctor is a lightweight, customizable monitoring tool that allows you to keep track of your system's health through simple scripts. While powerful, it is also easy to set up and modify to suit your specific needs. This tool is perfect for those who prefer a hands-on approach to system monitoring and want more control over their system's metrics.

