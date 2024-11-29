
# Windows Server 2022 Active Directory Setup and Monitoring Challenge

## Overview
This challenge guides you through deploying a secure **Windows Server 2022** environment with **Active Directory**, essential server roles (IIS, DNS, DHCP), user management, **Sysmon monitoring**, and demonstration of its functionality to a client. It provides experience with Active Directory configuration, user management, and security practices while using users like **Alice** (Administrator) and **Bob** (Standard User) for realistic role-based access.

---

## Table of Contents
- [System Preparation](#system-preparation)
- [Active Directory Setup](#active-directory-setup)
- [User Management with Alice and Bob](#user-management-with-alice-and-bob)
- [Server Roles](#server-roles)
  - [IIS for Alice](#iis-for-alice)
  - [DNS Configuration](#dns-configuration)
  - [DHCP Configuration](#dhcp-configuration)
- [Sysmon Monitoring](#sysmon-monitoring)
- [Client-Side Access and Reporting](#client-side-access-and-reporting)
- [Evaluation](#evaluation)
- [Conclusion](#conclusion)

---

## System Preparation

Set up your virtualization environment with the following Virtual Machines (VMs):
- **Server VM**: Windows Server 2022 installation.
- **Domain Controller VM**: Active Directory installation.
- **Client VMs**: For user access and monitoring.

If you're short on resources, you can use a **single server** as both your Domain Controller and Server VM, along with one Client VM.

### Steps:
1. Install **Windows Server 2022** evaluation on the Server and Domain Controller VMs.
2. Configure the VMs to be networked within the same environment.

![image](https://github.com/user-attachments/assets/cdcfbcbc-1d75-4125-9185-e2a4dafd8eb5)
![image](https://github.com/user-attachments/assets/7fa8045d-c306-4718-ba87-84f547cc1487)


## Active Directory Setup

1. Promote the **Domain Controller VM** to a Domain Controller.
2. Create a new **Active Directory forest** and **domain structure**.
3. Configure **DNS** service on the Domain Controller.
4. Create **Organizational Units (OUs)** for user and group management.

### Domain Controller Configuration:
1. Open **Server Manager**, then select **Manage** → **Add Roles and Features**.
2. Select **Active Directory Domain Services** and follow the wizard to install.
3. After installation, promote the server to a Domain Controller.

![image](https://github.com/user-attachments/assets/78b5ff92-524f-4d69-b1d2-945910b005a8)


---

## User Management with Alice and Bob

1. **Create user accounts** for Alice and Bob in Active Directory:
   - **Alice**: Administrator role, placed in a dedicated OU.
   - **Bob**: Standard User, placed in a separate OU with permissions limited to `/Users/Bob`.

2. Use **Group Policy Objects (GPOs)** to manage user settings based on OUs. 
   - Alice will have full permissions, while Bob's access will be restricted.

### Example GPO Setup for Alice and Bob:
1. Open **Group Policy Management Console (GPMC)**.
2. Create and configure **GPOs** for different OUs.

## Server Roles

### IIS for Alice
1. **Install IIS** (Internet Information Services) on the Server VM.
2. Configure IIS for Alice’s web application/service, ensuring robust security (permissions, Web Application Firewall, etc.).

### Testing IIS:
1. Ensure the web application is accessible only to authorized users within the domain.
2. Verify permissions for Alice as an Administrator.

![image](https://github.com/user-attachments/assets/91f55cae-3c94-4985-acdb-1e6330fc89ed)


### DNS Configuration
1. Verify DNS functionality within the Active Directory domain.
2. Configure **conditional forwarders** or integrate with external DNS if needed.

![image](https://github.com/user-attachments/assets/4ea8e246-9c83-47e9-a7d9-3bb0be234c42)


### DHCP Configuration
1. Install and configure **DHCP** on the Server VM.
2. Set up **IP address allocation** within the domain and ensure automatic IP assignment.

![image](https://github.com/user-attachments/assets/b7a78fb9-c4a4-4c41-97c4-42d206d806ff)


---

## Sysmon Monitoring

1. **Install Sysmon** on the Server VM.
2. Configure Sysmon to capture events specific to Alice and Bob, including:
   - **Process creation** (e.g., Alice’s admin actions, Bob’s file access).
   - **Network connections** (e.g., suspicious external IP connections).

### Sysmon Configuration:
1. Download Sysmon from Sysinternals.
2. Create configuration files to filter out unnecessary noise and focus on relevant events.

### Demonstrating Sysmon Functionality
1. Simulate suspicious activities (e.g., Alice running an unauthorized process, Bob accessing restricted files).
2. Show how Sysmon captures and logs these events.

![image](https://github.com/user-attachments/assets/47aff601-b121-48fb-8203-e5aa1456ebd5)



## Client-Side Access and Reporting

1. **Access the Server VM** from the Client VMs using domain credentials (Alice and Bob).
2. Verify access permissions for each user, demonstrating the differences between Alice’s administrative rights and Bob’s restricted access.

### Verifying Access:
- Alice should have full access to server resources.
- Bob should be restricted from accessing sensitive folders.

![image](https://github.com/user-attachments/assets/368e1b70-ec67-4948-bcdc-48413c6286bb)
![image](https://github.com/user-attachments/assets/4c7a0feb-1d7f-42aa-beb2-ba4e9eb5a86f)



### Analyzing Sysmon Logs
1. Access and review Sysmon logs on the Server VM to identify relevant events related to Alice and Bob.
2. Prepare a **client-facing report** summarizing the findings, potential security concerns, and Sysmon's value in monitoring system activity.

![image](https://github.com/user-attachments/assets/77a57e77-bdb9-45d2-9a36-f0fcf86e3d9e)


## Conclusion

This challenge provides hands-on experience with **Windows Server 2022**, **Active Directory**, and essential server roles. By configuring Sysmon and demonstrating its capabilities, you will enhance your understanding of monitoring system activities and applying security best practices in a real-world environment.

