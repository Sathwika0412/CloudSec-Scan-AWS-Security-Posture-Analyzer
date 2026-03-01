# CloudSec-Scan-AWS-Security-Posture-Analyzer
# CloudSec-Scan – AWS Security Posture Analyzer

CloudSec-Scan is a Python-based cloud security auditing tool that simulates AWS environment misconfiguration detection.  

This project analyzes cloud configuration data and identifies high-risk security issues such as public S3 buckets, missing encryption, IAM users without MFA, and overprivileged access policies.

---

## 🚀 Features

- Detects publicly accessible S3 buckets
- Identifies S3 buckets without encryption
- Flags IAM users without Multi-Factor Authentication (MFA)
- Detects overprivileged IAM users with AdministratorAccess
- Implements risk scoring system
- Classifies overall cloud security posture
- Exports structured security audit report

---

## 🛠 Technologies Used

- Python
- JSON Configuration Parsing
- Risk Scoring Logic
- Security Misconfiguration Detection

---

## 📊 Sample Output
CLOUD-2026-001 | Public S3 Bucket | HIGH | finance-data-backup
CLOUD-2026-002 | S3 Bucket Without Encryption | MEDIUM | finance-data-backup
CLOUD-2026-003 | IAM User Without MFA | HIGH | admin_user
CLOUD-2026-004 | Overprivileged IAM User | MEDIUM | admin_user

Overall Risk Score: 90 / 100
Security Posture: CRITICAL

---

## 📂 Project Structure
CloudSec-Scan/
│
├── cloud_config.json # Simulated AWS configuration
├── cloudsec_scan.py # Main scanning engine
├── cloudsec_report.txt # Generated security report
└── README.md # Project documentation

---

## ▶ How to Run

```bash
python cloudsec_scan.py --config cloud_config.json
Project Objective

To simulate real-world cloud security posture assessment and demonstrate understanding of:

AWS S3 security risks

IAM misconfiguration risks

Least privilege principle

Cloud shared responsibility model

Risk classification and reporting

🔐 Future Improvements

Add real AWS SDK (boto3) integration

Integrate with security dashboards

Add compliance scoring (CIS Benchmark simulation)

Add automated remediation suggestions

 Author

Sathwika
Cybersecurity Enthusiast | SOC & Cloud Security Focused


---

