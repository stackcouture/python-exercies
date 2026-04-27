### AWS Setup & Boto3 Basics

## Overview
This document covers the basic setup required to start using Python with AWS using Boto3.

---
## What is Boto3?
Boto3 is the official Python SDK for AWS.  
It allows developers to interact with AWS services like EC2, S3, IAM, etc., programmatically.

### Why Boto3?
- Automate AWS resource management
- Integrate AWS services into applications
- Replace manual CLI operations with code

---
## Install Boto3
To install Boto3, use pip:
```bash 
pip install boto3
```
---

## What is AWS CLI
AWS CLI (Command Line Interface) is a tool that allows you to interact with AWS services using terminal commands.

## Install AWS CLI
Linux / macOS:
```bash 
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

On Windows
- Download the AWS CLI MSI installer from the official AWS CLI page.
- Run the installer and follow the on-screen instructions.

---
## AWS Configure

```bash 
aws configure
```

You'll be asked for:

- AWS Access Key ID
- AWS Secret Access Key
- Default region
- Output format