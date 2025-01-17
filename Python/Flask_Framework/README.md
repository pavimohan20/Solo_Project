# Project: Form in Python with Flask

---

## Skills Developed
- **Backend Development**: Python programming (introduction to logical structures).
- **Form Sanitization and Validation**: Ensuring safe and valid data handling.
- **HTTP Methods**: Implementation of POST and GET requests.
- **Template Engine**: Use of Jinja for dynamic templates.

---

## Problem Statement
The company Hackers Poulette™ sells DIY kits and accessories for Raspberry Pi. They need a contact form for users to reach their technical support team. Your mission is to develop a Python application to:

1. Display a contact form.
2. Process responses with sanitization and validation.
3. Provide feedback to users, either correcting errors or confirming submission.

---

## Performance Criteria
- **Error Handling**:
  - Return the form with preserved valid responses when users make errors.
  - Display error messages near their respective fields.
- **Sanitization and Validation**:
  - Perform server-side sanitization to neutralize harmful content like `<script>` tags.
  - Validate mandatory fields and ensure email validity.
- **Feedback**:
  - Show a "Thank you for contacting us" page summarizing the encoded information upon successful submission.
- **Spam Prevention**:
  - Implement a honeypot anti-spam technique.

---

## Form Fields
1. **First Name and Last Name**: Text input (mandatory).
2. **Email**: Text input (mandatory, valid email required).
3. **Country**: Dropdown list (mandatory).
4. **Message**: Text input (mandatory).
5. **Gender**: Radio buttons for M/F (mandatory).
6. **Subjects**: Checkboxes for "Repair", "Order", and "Others" (optional, defaults to "Others" if none selected).

---

## Project Features
### Contact Form Functionalities
- **Server/Client Architecture**: Displays a contact form and processes data using Flask.
- **Sanitization**: Neutralizes harmful inputs to prevent vulnerabilities like XSS.
- **Validation**:
  - Ensures all mandatory fields are completed.
  - Validates email format.
- **Feedback**:
  - Displays error messages or a confirmation page.

### Security Features
- Protects against XSS (Cross-Site Scripting) vulnerabilities.
- Implements SSTI (Server-Side Template Injection) protection.
- Utilizes a honeypot field to reduce spam submissions.

### Deployment
- Flask application can be deployed on a local server or cloud platform.

---

## Learning Outcomes
By the end of the project, you will:
1. Understand the difference between POST and GET requests.
2. Implement XSS and SSTI protection measures.
3. Use Flask, a Python micro-framework, effectively.
4. Perform application deployment.

---

## Resources
- [FreeCodeCamp Flask Tutorial](https://www.youtube.com/watch?v=Qr4QMBUPxWo)
- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

