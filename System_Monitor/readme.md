Here’s a detailed **Markdown document** for your **El Doctor - A monitoring tool to rule them all!** project:

```markdown
# El Doctor - A Monitoring Tool to Rule Them All!

## Overview

**El Doctor** is a custom-built system monitoring tool created to provide a comprehensive and interactive way of monitoring system health. Unlike many pre-existing tools with complex dashboards, **El Doctor** leverages simple yet effective scripts to monitor system metrics, alert for critical issues, and provide weekly reports via email. This tool is built with flexibility and creativity in mind, focusing on ease of use and automation through cron jobs.

---

## Mission

The goal of this project is to create a custom monitoring script that allows you to:
- **Collect useful system data** such as CPU usage, RAM usage, disk space, and network activity.
- **Present an interactive interface** to visualize system health using `curses` or a similar tool.
- **Automate the collection of system metrics** every hour and store them in a CSV file.
- **Notify yourself when the system is in a critical state** (e.g., low RAM, high CPU usage) by sending email alerts.
- **Send a weekly system health report** with key metrics.
  
The mission encourages creativity, allowing you to customize the features as per your needs. By using this challenge, you'll gain practical experience with system monitoring, shell scripting, and automation.

---

## Key Features

- **Interactive Curses Interface:**
  - A real-time monitoring dashboard that displays system metrics interactively.
  
- **Hourly Metrics Collection:**
  - Collects important system metrics (CPU usage, RAM usage, disk space, etc.) every hour.
  - Saves the collected data in a CSV format for historical analysis.

- **Critical Alert Notifications:**
  - Alerts you via email when the system crosses critical thresholds (e.g., high CPU usage, low available RAM).

- **Weekly System Health Report:**
  - Sends a detailed report of the system’s health every week.

---

## Modules and Scripts

The project consists of the following core modules and scripts:

### 1. `show_metrics.sh`
- **Function:** Collects and logs system metrics every hour (e.g., CPU usage, RAM usage, disk space).
- **Output:** Metrics are stored in a CSV file for future reference.

### 2. `dialog_monitor.sh`
- **Function:** Provides an interactive monitoring interface using the `dialog` tool to display system metrics in real-time.

### 3. `send_weekly_report.sh`
- **Function:** Sends a weekly summary of system health (e.g., CPU usage, RAM usage, disk space) via email.
- **Schedule:** Runs once a week, typically on Sundays.

### 4. `cron_jobs.sh`
- **Function:** Configures cron jobs to automate the execution of `show_metrics.sh` and `send_weekly_report.sh` at specified intervals (hourly for metrics collection and weekly for report sending).

---

## Prerequisites

To run the scripts in this project, you need the following tools:

- **Dialog:** For the interactive curses-based interface.
  ```bash
  sudo apt-get install dialog
  ```

- **Mail Utility:** For sending email alerts. You can use `msmtp`, `sendmail`, or similar tools.
  ```bash
  sudo apt-get install msmtp
  ```

---

## Installation

### Step 1: Clone the Repository

Clone the repository to your machine:

```bash
git clone https://github.com/your-username/el-doctor.git
cd el-doctor
```

### Step 2: Configure Cron Jobs

To automate the script execution, configure cron jobs.

- **Hourly Metrics Collection:**
  This cron job runs `show_metrics.sh` every hour.
  
  Open your crontab:

  ```bash
  crontab -e
  ```

  Add the following line:

  ```bash
  0 * * * * /bin/bash /home/your-username/el-doctor/show_metrics.sh
  ```

- **Weekly Report:**
  This cron job runs `send_weekly_report.sh` every Sunday at 5:00 PM.

  Add this line to your crontab:

  ```bash
  0 17 * * 0 /bin/bash -c '/home/your-username/el-doctor/send_weekly_report.sh'
  ```

### Step 3: Set Up Email Notifications

To enable email notifications, configure an email utility like `msmtp` or `sendmail`.

#### For `msmtp`:

1. Create a configuration file `~/.msmtprc` with the following content:

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

2. Replace `your-email@gmail.com` and `your-app-password` with your actual email address and app-specific password (for Gmail).

---

## Usage

### Running the Scripts

You can manually run any of the scripts for testing or on-demand execution:

- **Run the Metrics Collection Script:**
  ```bash
  /bin/bash /home/your-username/el-doctor/show_metrics.sh
  ```

- **Run the Interactive Monitoring Interface:**
  ```bash
  /bin/bash /home/your-username/el-doctor/dialog_monitor.sh
  ```

### Email Alerts

The scripts monitor critical system metrics (e.g., high CPU usage, low available RAM) and will send email notifications if the thresholds are crossed. Here's an example of how an alert is triggered for high CPU usage:

```bash
if [ $(echo "$cpu_usage > 90" | bc) -eq 1 ]; then
  echo "CPU Usage is Critical!" | mail -s "Critical Alert: CPU Usage High" user@example.com
fi
```

---

## Example Output

### 1. CSV File Format (Hourly Metrics)

The **show_metrics.sh** script logs system metrics every hour in a CSV format:
```
Date, Time, CPU Usage, RAM Usage, Disk Space Usage
2024-11-15, 14:00, 30%, 60%, 50%
2024-11-15, 15:00, 35%, 58%, 52%
```

### 2. Weekly Report Email

The **send_weekly_report.sh** script sends a summary email every Sunday:

**Subject:** Weekly System Health Report  
**Body:**
```
CPU Usage: 85%
Memory Usage: 70%
Disk Space Usage: 50%
Alerts: None
```

---

## Troubleshooting

- **Issue: Email notifications are not working**
  - Ensure your email utility (e.g., `msmtp` or `sendmail`) is correctly configured.
  - Make sure your email provider allows third-party applications to send emails (e.g., use app passwords for Gmail).

- **Issue: Metrics not being logged**
  - Check if the cron jobs are set up properly by running `crontab -l`.
  - Inspect the CSV files to ensure the metrics are being logged every hour.

- **Issue: No output in interactive interface**
  - Ensure `dialog` is installed on your machine:

    ```bash
    sudo apt-get install dialog
    ```

---

## Folder Structure

The folder structure of the repository is as follows:

```
el-doctor/
├── show_metrics.sh              # Collects system metrics every hour
├── dialog_monitor.sh            # Interactive curses-based monitoring interface
├── send_weekly_report.sh        # Sends weekly system health report via email
├── cron_jobs.sh                 # Configures cron jobs for automation
```

---

## Final Thoughts

**El Doctor** is designed to provide you with full control over system monitoring while practicing shell scripting and automation. This project not only enhances your understanding of system health checks but also helps you build a flexible, custom solution for your own needs.

By using **El Doctor**, you gain the skills to monitor a machine's health effectively and react to system anomalies in real time.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Instructions:

1. **Copy** the above content.
2. **Paste** it into a new file called `README.md` in the root directory of your GitHub repository.

This **Markdown document** provides an extensive overview of the **El Doctor** project, detailing the features, setup, and usage instructions for the tool.
