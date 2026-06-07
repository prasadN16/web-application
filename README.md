# Vulnerability Scanner

## Overview

This project is a simple Python-based Vulnerability Scanner designed to identify common security issues in web applications and network services. It scans for open ports, detects weak configurations, checks SSL/TLS certificates, and generates a vulnerability assessment report.

## Features

* Scan for open TCP ports
* Detect running services on discovered ports
* Check SSL/TLS certificate validity and expiration
* Identify potentially exposed sensitive files and directories
* Generate vulnerability reports in JSON format
* Calculate overall risk score

## Technologies Used

* Python 3
* Socket Programming
* SSL Module
* Requests Library
* JSON

## Project Structure

vulnerability-scanner/
├── scanner.py
├── report.json
├── requirements.txt
└── README.md

## How It Works

1. The scanner checks common ports on the target host.
2. Service information is collected from open ports.
3. SSL certificates are inspected for validity and expiration.
4. Common sensitive paths are tested:

   * /.env
   * /.git/config
   * /wp-config.php.bak
   * /phpinfo.php
   * /actuator
   * /console
5. Findings are categorized by severity.
6. A vulnerability report is generated.

## Installation

Clone the repository:

git clone https://github.com/your-username/vulnerability-scanner.git

Navigate to the project directory:

cd vulnerability-scanner

Install dependencies:

pip install -r requirements.txt

## Usage

Run the scanner:

python scanner.py

Or specify a target:

python scanner.py https://example.com

## Sample Output

Open Ports:

* 80 (HTTP)
* 443 (HTTPS)

Vulnerabilities Found:

* SSL Certificate Expiring Soon
* Environment File Exposed
* Git Repository Exposed
* PHPInfo Page Exposed

Risk Score: 16

## Sample Findings

### High Severity

* SSL Certificate Expiring Soon

### Low Severity

* Exposed .env file
* Exposed .git directory
* WordPress configuration backup
* PHPInfo page exposure
* Spring Boot actuator endpoint
* Management console exposure

## Security Recommendations

* Renew SSL certificates before expiration.
* Remove unnecessary public files.
* Restrict access to administrative endpoints.
* Disable phpinfo() on production servers.
* Regularly patch and update software.
* Perform periodic security assessments.

## Learning Outcomes

Through this project, students can learn:

* Basic penetration testing concepts
* Vulnerability assessment techniques
* Network service enumeration
* SSL/TLS security analysis
* Secure configuration practices
* Report generation and risk assessment

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not scan systems without explicit permission from the owner.

## Author

Prasad N

## License

This project is released under the MIT License.
