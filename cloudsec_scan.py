import json
import argparse

parser = argparse.ArgumentParser(description="CloudSec-Scan - AWS Misconfiguration Scanner")
parser.add_argument("--config", type=str, default="cloud_config.json", help="Path to cloud config file")
args = parser.parse_args()

print("\nCloudSec-Scan v2.0 Starting...\n")

with open(args.config, "r") as file:
    config = json.load(file)

incidents = []
incident_id = 1
risk_score = 0

# ---- Check S3 Buckets ----
for bucket in config["s3_buckets"]:
    if bucket["public_access"]:
        risk_score += 30
        incidents.append({
            "id": f"CLOUD-2026-{incident_id:03}",
            "type": "Public S3 Bucket",
            "resource": bucket["name"],
            "severity": "HIGH",
            "recommendation": "Disable public access immediately"
        })
        incident_id += 1

    if not bucket["encryption_enabled"]:
        risk_score += 15
        incidents.append({
            "id": f"CLOUD-2026-{incident_id:03}",
            "type": "S3 Bucket Without Encryption",
            "resource": bucket["name"],
            "severity": "MEDIUM",
            "recommendation": "Enable server-side encryption"
        })
        incident_id += 1


# ---- Check IAM Users ----
for user in config["iam_users"]:
    if not user["mfa_enabled"]:
        risk_score += 25
        incidents.append({
            "id": f"CLOUD-2026-{incident_id:03}",
            "type": "IAM User Without MFA",
            "resource": user["username"],
            "severity": "HIGH",
            "recommendation": "Enable Multi-Factor Authentication"
        })
        incident_id += 1

    if user["policy"] == "AdministratorAccess":
        risk_score += 20
        incidents.append({
            "id": f"CLOUD-2026-{incident_id:03}",
            "type": "Overprivileged IAM User",
            "resource": user["username"],
            "severity": "MEDIUM",
            "recommendation": "Apply least privilege principle"
        })
        incident_id += 1


# ---- Print Report ----
print("----- Cloud Security Posture Report -----\n")

for incident in incidents:
    print(f"{incident['id']} | {incident['type']} | {incident['severity']} | {incident['resource']}")

print("\nOverall Risk Score:", risk_score, "/ 100")

if risk_score >= 60:
    print("Security Posture: CRITICAL")
elif risk_score >= 30:
    print("Security Posture: MODERATE")
else:
    print("Security Posture: LOW")

# ---- Export Report ----
with open("cloudsec_report.txt", "w") as report:
    for incident in incidents:
        report.write(f"{incident}\n")
    report.write(f"\nOverall Risk Score: {risk_score}/100\n")

print("\nReport exported to cloudsec_report.txt")