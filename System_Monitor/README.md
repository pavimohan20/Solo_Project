I apologize for the confusion. The content I provided earlier is meant to be in **Markdown format** as per your request. I'll correct the approach and provide you the **entire README in Markdown format** below:

```markdown
# El Doctor - A Monitoring Tool to Rule Them All

## Overview

**El Doctor** is a custom-built system monitoring tool that provides real-time insights into the health of your machine. Unlike many pre-built solutions, **El Doctor** offers a simple, script-based approach with interactive features and email notifications. It allows you to monitor critical system metrics such as CPU usage, RAM, disk space, and network activity. Additionally, it sends weekly reports and alerts when the system enters a critical state, ensuring that you are always informed of your system's health.

---

## Features

- **Interactive Curses Interface:**
  - User-friendly command-line interface (CLI) using `dialog` for displaying real-time system metrics.
  - Monitors key metrics: CPU usage, RAM usage, disk space, and network activity.

- **System Metrics Collection:**
  - Collects system metrics every hour and stores them in a CSV file for historical analysis.
  
- **Critical Alert System:**
  - Sends email notifications when the system exceeds critical thresholds (e.g., high CPU usage, low available RAM).

- **Weekly System Report:**
  - Sends an email with a weekly system health report, including CPU usage, RAM usage, disk space usage, and network stats.

---

## Prerequisites

Before running **El Doctor**, make sure your machine has the following installed:

- **Dialog** (for the curses interface):
  ```bash
  sudo apt-get install dialog
  ```

- **Mail Utility** (such as `msmtp` or `sendmail` for email notifications):
  ```bash
  sudo apt-get install msmtp
  ```

---

## Files Included

The following scripts are part of the **El Doctor** project:

- **`show_metrics.sh`:** Collects system metrics (CPU, RAM, disk space, etc.) every hour and stores them in a CSV file.
- **`dialog_monitor.sh`:** Provides an interactive monitoring interface using `dialog`.
- **`send_weekly_report.sh`:** Sends a weekly system health report via email.
- **`cron_jobs.sh`:** Configures cron jobs to automate the execution of scripts.

---

## Installation & Setup

### 1. Clone the Repository

Clone this repository to your machine:
```bash
git clone https://github.com/your-username/el-doctor.git
cd el-doctor
```

### 2. Configure Cron Jobs

To automate the execution of the scripts, configure cron jobs.

- **Hourly Metrics Collection:**
  This cron job runs the **`show_metrics.sh`** script every hour.
  Open your crontab:
  ```bash
  crontab -e
  ```
  Add the following line:
  ```bash
  0 * * * * /bin/bash /home/your-username/el-doctor/show_metrics.sh
  ```

- **Weekly Report:**
  This cron job runs **`send_weekly_report.sh`** every Sunday at 5:00 PM.
  Add this line to your crontab:
  ```bash
  0 17 * * 0 /bin/bash -c '/home/your-username/el-doctor/send_weekly_report.sh'
  ```

### 3. Set Up Email Notifications

Ensure you have configured an email utility like `msmtp` or `sendmail` for sending email alerts.

- **For `msmtp`,** configure your email settings in `~/.msmtprc`:
  ```ini
  account default
  host smtp.gmail.com
  port 587
  from your-email@gmail.com
  auth on
  user your-email@gmail.com
  password your-app-password
  tls on
  ```

- **For `sendmail`,** configure your SMTP server as required.

Make sure to replace `your-email@gmail.com` and `your-app-password` with your actual email address and app-specific password (for Gmail).

---

## Usage

### Running Scripts Manually

You can manually run any of the scripts if you want to test or execute them on demand.

- **Run the Metrics Collection Script:**
  ```bash
  /bin/bash /home/your-username/el-doctor/show_metrics.sh
  ```

- **Run the Interactive Monitoring Interface:**
  ```bash
  /bin/bash /home/your-username/el-doctor/dialog_monitor.sh
  ```

### Email Alerts

The **critical alert system** monitors system thresholds (e.g., high CPU usage or low available RAM). If any threshold is crossed, an email notification is sent.

Example of how an alert is triggered:
```bash
if [ $(echo "$cpu_usage > 90" | bc) -eq 1 ]; then
  echo "CPU Usage is Critical!" | mail -s "Critical Alert: CPU Usage High" user@example.com
fi
```

---

## Folder Structure

The project directory structure is as follows:

```
el-doctor/
├── show_metrics.sh              # Collect system metrics every hour
├── dialog_monitor.sh            # Interactive monitoring interface (curses)
├── send_weekly_report.sh        # Send weekly system health report
├── cron_jobs.sh                 # Cron job configuration for automation
```

---

## Example Output

- **CSV File Format** (Metrics are logged every hour):
  ```
  Date, Time, CPU Usage, RAM Usage, Disk Space Usage
  2024-11-15, 14:00, 25%, 60%, 50%
  2024-11-15, 15:00, 30%, 55%, 49%
  ```

- **Weekly Report Email** (Sent every Sunday):
  ```
  Subject: Weekly System Health Report
  Body:
  - CPU Usage: 80%
  - Memory Usage: 75%
  - Disk Space: 60%
  - Alerts: None
  ```

---

## Troubleshooting

- **Issue: Email notifications not working**
  - Ensure that your email utility (e.g., `msmtp` or `sendmail`) is properly configured.
  - Check that your email provider allows sending emails from third-party applications (e.g., use App passwords for Gmail).
  
- **Issue: Metrics not being collected**
  - Verify that cron jobs are correctly set up by running `crontab -l`.
  - Check the logs generated by **`show_metrics.sh`** to ensure metrics are being written to the CSV file.

- **Issue: No output in interactive interface**
  - Ensure `dialog` is installed:
    ```bash
    sudo apt-get install dialog
    ```

---

## Final Thoughts

**El Doctor** is a lightweight, customizable monitoring tool that allows you to track your system's health through simple scripts. While powerful, it is also easy to set up and modify to fit your specific needs. This tool offers a practical understanding of system monitoring and gives you full control over the metrics you wish to track.

By using **El Doctor**, you gain insight into how system monitoring works under the hood while also being able to customize it according to your preferences.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This is a **complete README.md file** in **Markdown format** that includes:

- **Overview** of the project
- **Features** of the tool
- **Installation and Setup** instructions
- **File descriptions**
- **Cron job setup**
- **Usage instructions**
- **Troubleshooting tips**
- **Folder structure and output format**
- **Final thoughts**
- **License information**

This file should serve as a comprehensive guide for anyone using your **El Doctor** project. Let me know if you need any additional modifications or additions!
