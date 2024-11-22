# Century Game - PowerShell CLI Exercise

This repository contains the encrypted passwords for the **Century** game, a series of exercises designed to test and improve your PowerShell CLI skills. Each level of the game provides a password that you need to encrypt with GPG and keep track of.

## Overview

The game involves connecting to different servers, completing challenges, and retrieving passwords. Each password is then encrypted using GPG and stored in this repository for safekeeping.

## Instructions

1. **Complete each level** in the Century game, starting from `Century1`.
2. **Retrieve the password** for each level.
3. **Encrypt the collected passwords** using GPG.
4. **Upload the encrypted passwords** to this repository.
5. Share your **public GPG key** for verification.

## Files in this Repository

- `passwords.txt.gpg`: Encrypted file containing the passwords for each level.
- `my_public_key.asc`: Exported public GPG key.

## Public GPG Key

Use the following command to export your public key:

```bash
gpg --armor --export <your-key-id> > my_public_key.asc