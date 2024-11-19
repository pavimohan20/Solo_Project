# **Windows Installation and Configuration Project**

## **Project Overview**
This project involves installing Windows 10 for a client and configuring the system according to the following requirements:
- Create and manage user accounts with specific permissions.
- Install and configure antivirus software.
- Enable and verify the firewall for system security.

---

## **System Requirements**
- **Operating System**: Windows 10
- **Tools Used**: VirtualBox (for virtual machine setup), Microsoft Defender Antivirus, Windows Firewall

---

## **Project Objectives**
1. Install Windows 10.
2. Create two users:
   - **Alice**: Administrator with full system access.
   - **Bob**: Restricted user with read, write, and execute permissions limited to their own folder (`C:\Users\Bob`).
3. Install and configure antivirus software.
4. Enable and verify the Windows Firewall.

---

## **Steps Completed**

### **1. Windows Installation**
- Installed Windows 10 using an evaluation copy.
- Set up a virtual machine in VirtualBox for testing purposes.

### **2. User Account Creation**
- Created **Alice** (Administrator) with full system privileges.
- Created **Bob** (Standard User) with restricted access.

#### **Folder Permissions for Bob**
- Verified the creation of `C:\Users\Bob` folder after logging in as Bob.
- Configured folder permissions to:
  - Allow Bob: **Read**, **Write**, and **Execute** access in `C:\Users\Bob`.
  - Restrict access to other users (e.g., Pavithra, Public).

### **3. Antivirus Installation and Configuration**
- Used **Microsoft Defender Antivirus** (pre-installed in Windows 10).
- Performed the following:
  - Enabled **Real-time protection**.
  - Ran a **Quick Scan** to ensure no current threats were detected.
  - Verified the antivirus updates and definitions were up-to-date.

### **4. Windows Firewall Configuration**
- Verified Windows Firewall is enabled for:
  - Domain Network
  - Private Network
  - Public Network
- Reviewed and adjusted app permissions to ensure unnecessary apps were blocked.

---

## **Testing and Validation**
- Logged in as **Alice** to verify administrative privileges.
- Logged in as **Bob** to confirm restricted access to the system.
- Ran antivirus scans to validate system protection.
- Checked firewall logs to confirm network security.

---

## **Results**
All requirements were successfully implemented:
- Windows 10 installed and configured.
- User accounts created with appropriate privileges.
- System protected by antivirus and firewall.
- Validation tests passed.

---

## **Future Improvements**
- Automate user account creation and permission configuration using PowerShell.
- Evaluate third-party antivirus software for enhanced protection.
- Configure scheduled scans and periodic backups for additional system reliability.

---

## **Author**
- **Pavithra Mohan**  
