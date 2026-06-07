{
  "target": "https://example.com",
  "timestamp": "2026-06-07T05:46:51.323482Z",
  "scan_duration_seconds": 6.29,
  "open_ports": [
    80,
    443
  ],
  "services": {
    "80": {
      "service": "HTTP",
      "banner": ""
    },
    "443": {
      "service": "HTTPS",
      "banner": ""
    },
    "http_meta": {}
  },
  "vulnerabilities": [
    {
      "id": "SSL-002",
      "severity": "HIGH",
      "category": "SSL/TLS",
      "title": "SSL Certificate Expiring Soon",
      "description": "Certificate expires in 27 days.",
      "evidence": "Expiry: Jul  4 17:41:00 2026 GMT",
      "recommendation": "Renew the SSL certificate before it expires."
    },
    {
      "id": "PATH-331",
      "severity": "LOW",
      "category": "Exposed Paths",
      "title": "Environment File Exposed (Access Restricted)",
      "description": ".env file may contain DB passwords, API keys, and secrets.",
      "evidence": "HTTP 403 at https://example.com/.env \u2014 resource exists but access is denied.",
      "recommendation": "Verify /.env is not accidentally exposed."
    },
    {
      "id": "PATH-555",
      "severity": "LOW",
      "category": "Exposed Paths",
      "title": "Git Repository Exposed (Access Restricted)",
      "description": "Exposed .git directory allows source code extraction.",
      "evidence": "HTTP 403 at https://example.com/.git/config \u2014 resource exists but access is denied.",
      "recommendation": "Verify /.git/config is not accidentally exposed."
    },
    {
      "id": "PATH-668",
      "severity": "LOW",
      "category": "Exposed Paths",
      "title": "WordPress Config Backup Exposed (Access Restricted)",
      "description": "Backup of wp-config.php may contain database credentials.",
      "evidence": "HTTP 403 at https://example.com/wp-config.php.bak \u2014 resource exists but access is denied.",
      "recommendation": "Verify /wp-config.php.bak is not accidentally exposed."
    },
    {
      "id": "PATH-971",
      "severity": "LOW",
      "category": "Exposed Paths",
      "title": "PHPInfo Page Exposed (Access Restricted)",
      "description": "phpinfo() reveals server configuration, PHP version, and loaded modules.",
      "evidence": "HTTP 403 at https://example.com/phpinfo.php \u2014 resource exists but access is denied.",
      "recommendation": "Verify /phpinfo.php is not accidentally exposed."
    },
    {
      "id": "PATH-925",
      "severity": "LOW",
      "category": "Exposed Paths",
      "title": "Spring Boot Actuator Exposed (Access Restricted)",
      "description": "Actuator endpoints may leak configuration, health data, or allow RCE.",
      "evidence": "HTTP 403 at https://example.com/actuator \u2014 resource exists but access is denied.",
      "recommendation": "Verify /actuator is not accidentally exposed."
    },
    {
      "id": "PATH-580",
      "severity": "LOW",
      "category": "Exposed Paths",
      "title": "Management Console Exposed (Access Restricted)",
      "description": "Management console is publicly accessible.",
      "evidence": "HTTP 403 at https://example.com/console \u2014 resource exists but access is denied.",
      "recommendation": "Verify /console is not accidentally exposed."
    }
  ],
  "summary": {
    "total_vulnerabilities": 7,
    "severity_counts": {
      "CRITICAL": 0,
      "HIGH": 1,
      "MEDIUM": 0,
      "LOW": 6,
      "INFO": 0
    },
    "open_port_count": 2,
    "risk_score": 16
  }
}