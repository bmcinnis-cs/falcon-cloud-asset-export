# NIST SP 800-171r2 → CrowdStrike CSPM Policy Mapping

**Source:** NIST SP 800-171Ar3 (May 2024) assessment procedures  
**Policies:** 3,017 total across AWS (1,274), Azure (699), GCP (493), General/Kubernetes (393), and unnamed cross-cloud (71+10+77)  
**Generated:** 2026-05-14

---

## 03.01 Access Control

**Controls:** Account Management (03.01.01), Access Enforcement (03.01.02), Least Privilege (03.01.05–07), Remote Access (03.01.12), Publicly Accessible Content (03.01.22)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 3 | Medium | AWS | IAM user has global access ("*") from user inline policies |
| 4 | Low | AWS | IAM high privileged user with group inline policy |
| 5 | Low | AWS | IAM high privileged user with group managed policy |
| 6 | Low | AWS | IAM high privileged user with user inline policy |
| 7 | Low | AWS | IAM high privileged user with user managed policy |
| 8 | Info | AWS | IAM root user has an active access key |
| 19 | Medium | AWS | EC2 high privileged instance profile with IAM managed policy |
| 20 | Medium | AWS | EC2 high privileged instance profile with IAM inline policy |
| 21 | Medium | AWS | EC2 instance publicly configured allows global public IP in ingress rule(s) on non-web ports |
| 22 | Low | AWS | EC2 instance publicly configured allows global public IP in ingress rule(s) on high-risk port(s) |
| 25 | Info | AWS | Access to sensitive information - AWS::IAM::Role |
| 26 | Info | AWS | Access to sensitive information - AWS::IAM::User |
| 27 | Info | AWS | Access to sensitive information - AWS::EC2::Instance |
| 28 | Info | AWS | Access to sensitive information - AWS::Lambda::Function |
| 33 | Info | AWS | Excessive infra permissions - AWS::IAM::Role |
| 34 | Info | AWS | Excessive infra permissions - AWS::IAM::User |
| 35 | Info | AWS | Excessive infra permissions - AWS::IAM::Policy/UserPolicy/RolePolicy/GroupPolicy |
| 36 | Info | AWS | Excessive infra permissions - AWS::EC2::Instance |
| 37 | Info | AWS | Excessive infra permissions - AWS::Lambda::Function |
| 39 | Info | AWS | Assumable By External Accounts - AWS::IAM::Role |
| 46 | Info | AWS | Assumable By IAM - AWS::IAM::Role |
| 47 | Info | AWS | Administrative permissions - AWS::IAM::User |
| 48 | Info | AWS | Administrative permissions - AWS::IAM::Role |
| 49 | Info | AWS | Administrative permissions - AWS::IAM::Policy |
| 50 | Info | AWS | Administrative permissions - AWS::IAM::UserPolicy/RolePolicy/GroupPolicy |
| 51 | Info | AWS | Administrative permissions - AWS::IAM::InstanceProfile |
| 52 | Info | AWS | Administrative permissions - AWS::EC2::Instance |
| 51 | Medium | AWS | S3 bucket configured for public access |
| 52 | Low | AWS | S3 bucket configured for any authenticated user access |
| 164 | Low | AWS | Lambda function is configured to allow cross account access |
| 165 | Medium | AWS | Lambda function is configured to be publicly exposed |
| 166 | Medium | AWS | Lambda function contains overly permissive role |
| 265 | Medium | AWS | EC2 instance publicly configured allows global public IP in ingress rule(s) |
| 266 | Medium | AWS | EC2 Default security group does not block all traffic |
| 281 | Low | AWS | S3 bucket policy with global write, read, or delete permissions |
| 390 | Low | AWS | SQS Queue accessible to any identity |
| 515 | Medium | AWS | S3 bucket with Block Public Access setting disabled |
| 546 | Low | AWS | API Gateway request authorization not required |
| 563 | High | AWS | S3 bucket ACL allows global Read or Write access |
| 591 | High | AWS | IAM support role has not been created to manage incidents with AWS Support |
| 593 | High | AWS | IAM user has granted permissions outside of groups |
| 601 | High | AWS | S3 Bucket is not set to deny HTTP requests |
| 610 | Info | AWS | IAM policies that allow full (*:*) administrative privileges attached to user |
| 611 | Low | AWS | IAM policies that allow full (*:*) administrative privileges attached to group without members |
| 612 | Medium | AWS | IAM policies that allow full (*:*) administrative privileges attached to role |
| 648 | High | AWS | IAM user has both Console access and Access Keys |
| 1003 | Medium | AWS | AMI Shared With Multiple Accounts |
| 1006 | Medium | AWS | API Gateway Without Configured Authorizer |
| 1034 | Low | AWS | Cross-Account IAM Assume Role Policy Without ExternalId or MFA |
| 1042 | Medium | AWS | EC2 Instance Using Default Security Group |
| 1046 | Info | AWS | ECR Repository Is Publicly Accessible |
| 1047 | Low | AWS | ECS Service Admin Role Is Present |
| 1061 | Medium | AWS | IAM Access Key Is Exposed |
| 1063 | Medium | AWS | IAM Group Without Users |
| 1065 | Medium | AWS | IAM Policies Attached To User |
| 1066 | Medium | AWS | IAM Policies With Full Privileges |
| 1067 | Medium | AWS | IAM Policy Grants 'AssumeRole' Permission Across All Services |
| 1068 | Low | AWS | IAM Policy Grants Full Permissions |
| 1069 | Medium | AWS | IAM Role Allows All Principals To Assume |
| 1076 | Medium | AWS | Lambda Permission Principal Is Wildcard |
| 1081 | Medium | AWS | Public Lambda via API Gateway |
| 1094 | Info | AWS | S3 Bucket Access to Any Principal |
| 1095 | Low | AWS | S3 Bucket ACL Allows Read to All Users |
| 1096 | Low | AWS | S3 Bucket ACL Allows Read to Any Authenticated User |
| 1097 | Info | AWS | S3 Bucket Allows Delete Action From All Principals |
| 1098 | Low | AWS | S3 Bucket Allows Get Action From All Principals |
| 1099 | Low | AWS | S3 Bucket Allows List Action From All Principals |
| 1100 | Info | AWS | S3 Bucket Allows Put Action From All Principals |
| 1102 | Info | AWS | S3 Bucket With All Permissions |
| 1103 | Info | AWS | S3 Bucket With Public Access |
| 1165 | Medium | AWS | EC2 Instance Has No IAM Role |
| 1169 | Medium | AWS | EC2 Network ACL Ineffective Denied Traffic |
| 1187 | Medium | AWS | Elasticsearch Without IAM Authentication |
| 1195 | Medium | AWS | Empty Roles For ECS Cluster Task Definitions |
| 1205 | High | AWS | IAM Access Analyzer Not Enabled |
| 1206 | Medium | AWS | IAM Group Inline Policies |
| 1208 | High | AWS | IAM Policies Without Groups |
| 1209 | Medium | AWS | IAM Policy On User |
| 1212 | High | AWS | IAM User With No Group |
| 1214 | Medium | AWS | IoT Policy Allows Action as Wildcard |
| 1215 | Medium | AWS | IoT Policy Allows Wildcard Resource |
| 1217 | Medium | AWS | KMS Allows Wildcard Principal |
| 1220 | Low | AWS | Lambda Functions With Full Privileges |
| 1228 | Low | AWS | Neptune Cluster With IAM Database Authentication Disabled |
| 1276 | High | AWS | Support Has No Role Associated |
| 1306 | High | AWS | CloudWatch Logs Destination With Vulnerable Policy |
| 1325 | High | AWS | EC2 Instance Using API Keys |
| 1329 | Medium | AWS | EFS With Vulnerable Policy |
| 1338 | Medium | AWS | Elasticsearch Domain With Vulnerable Policy |
| 1345 | Medium | AWS | Glue With Vulnerable Policy |
| 1346–1406 | Medium | AWS | Group/Role/User With Privilege Escalation By Actions (iam:*, cloudformation:*, ec2:*, lambda:*, glue:*) |
| 1365 | Medium | AWS | IAM Role Policy passRole Allows All |
| 1366 | Low | AWS | IAM Role With Full Privileges |
| 1368 | Medium | AWS | IAM User With Access To Console |
| 1374 | Low | AWS | Neptune Cluster Instance is Publicly Accessible |
| 1380 | Medium | AWS | Public and Private EC2 Share Role |
| 1387 | Medium | AWS | REST API With Vulnerable Policy |
| 1415 | Low | AWS | Secrets Manager With Vulnerable Policy |
| 1420 | High | AWS | Security Group Not Used |
| 1429 | High | AWS | SSO Permission With Inadequate User Session Duration |
| 1430 | Medium | AWS | SSO Policy with full privileges |
| 1431 | Medium | AWS | SSO Identity User Unsafe Creation |
| 1579 | Low | AWS | Lambda function URL configured with NO authentication |
| 1621 | Low | AWS | IAM Role can be assumed by all principals |
| 64790 | Medium | Cross-Cloud | Identity is externally accessible and has excessive permissions |
| 64791 | Medium | Cross-Cloud | Identity is externally accessible and has access to sensitive data |
| 64792 | Medium | Cross-Cloud | Unused identity with excessive permissions |
| 64805 | Medium | Cross-Cloud | Publicly exposed compute resource is connected to identity with excessive permissions |
| 68241 | High | Cross-Cloud | Externally assumable identity |
| 68533 | Low | Cross-Cloud | Privileged identity has MFA disabled |
| 68536 | Low | Cross-Cloud | Compute with RCE has excessive permissions |
| 70293 | Medium | Cross-Cloud | Identity has unused excessive infrastructure permissions |
| 70301 | Low | Cross-Cloud | Identity is externally accessible and has unused excessive infrastructure permissions |
| 199 | Low | Azure | AKS not enabled with RBAC |
| 84 | Medium | Azure | Key Vault RBAC access control is not enabled |
| 190 | Medium | Azure | Azure subscription has more than 3 owners |
| 192 | Medium | Azure | Azure deprecated accounts present in subscription |
| 1847–1850 | Medium | Azure | Custom Role allows admin/role-assignment/custom-owner permissions |
| 5011 | Medium | General/K8s | Authorization Mode RBAC Not Set |
| 5017 | High | General/K8s | Cluster Admin Rolebinding With Superuser Permissions |
| 5035 | High | General/K8s | Ensure Administrative Boundaries Between Resources |
| 5073 | Medium | General/K8s | Node Restriction Admission Control Plugin Not Set |
| 5079 | Medium | General/K8s | Permissive Access to Create Pods |
| 5094 | Medium | General/K8s | RBAC Roles Allow Privilege Escalation |
| 5095–5100 | Medium | General/K8s | RBAC Roles with Attach/Exec/Impersonate/Port-Forwarding/Read Secrets Permissions |
| 401 | Medium | GCP | IAM primitive 'owner' or 'editor' roles are in use |
| 414 | Medium | GCP | Compute Engine VM has service account assigned with Editor role |
| 461 | Low | GCP | IAM service account has admin privileges |
| 462 | Medium | GCP | IAM user with service account privileges |
| 3069 | High | GCP | User with IAM Role |
| 3072 | Medium | GCP | VM With Full Cloud Access |

---

## 03.03 Audit and Accountability

**Controls:** Event Logging (03.03.01), Audit Record Content (03.03.02), Audit Record Generation (03.03.03), Response to Failures (03.03.04), Review/Analysis/Reporting (03.03.05), Time Stamps (03.03.07), Protection of Audit Information (03.03.08)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 55 | Low | AWS | CloudTrail is not enabled on account |
| 56 | Medium | AWS | Ensure CloudTrail is enabled in all regions |
| 57 | Info | AWS | Logging Enabled - AWS::OpenSearch::Domain |
| 59 | Low | AWS | Redshift cluster not configured with audit logging enabled |
| 172 | Medium | AWS | EMR cluster logging is not configured |
| 184 | Medium | AWS | Config service failed to deliver log files |
| 208 | Medium | AWS | CloudTrail trails are not integrated with CloudWatch Logs |
| 507 | High | AWS | CloudWatch log metric filter and alarm missing for S3 bucket policy changes |
| 512 | High | AWS | VPC with no active Flow Logs configured |
| 544 | High | AWS | CloudWatch log metric filter and alarm missing for AWS Config changes |
| 561 | Low | AWS | S3 CloudTrail bucket with access logging disabled |
| 572 | Medium | AWS | S3 bucket policy allows public access to CloudTrail logs |
| 574 | High | AWS | CloudWatch log metric filter and alarm missing for security group changes |
| 578 | High | AWS | CloudWatch log metric filter and alarm missing for unauthorized API calls |
| 579 | High | AWS | CloudWatch log metric filter and alarm missing for changes to Network Access Control Lists |
| 585 | Low | AWS | S3 CloudTrail bucket allows deletion of logs without MFA |
| 587 | High | AWS | CloudWatch log metric filter and alarm missing for changes to network gateways |
| 588 | High | AWS | CloudWatch log metric filter and alarm missing for changes to route tables |
| 589 | High | AWS | CloudWatch log metric filter and alarm missing for VPC changes |
| 592 | Low | AWS | CloudTrail log validation is not enabled |
| 594 | High | AWS | CloudWatch log metric filter and alarm missing for AWS Organization changes |
| 595 | High | AWS | CloudWatch log metric filter and alarm missing for Management Console sign-ins without MFA |
| 596 | High | AWS | CloudWatch log metric filter and alarm missing for root account usage |
| 597 | High | AWS | CloudWatch log metric filter and alarm missing for IAM policy changes |
| 598 | High | AWS | CloudWatch log metric filter and alarm missing for CloudTrail configuration changes |
| 599 | High | AWS | CloudWatch log metric filter and alarm missing for Management Console authentication failures |
| 600 | High | AWS | CloudWatch log metric filter and alarm missing for deletion or scheduled deletion of customer created CMKs |
| 603 | Medium | AWS | CloudTrail logs are not encrypted using a Customer Master Key |
| 606 | High | AWS | CloudTrail is not configured to log S3 object-level write events |
| 607 | High | AWS | CloudTrail is not configured to log S3 object-level read events |
| 143 | Medium | AWS | EKS control plane cluster logging is disabled |
| 1022 | High | AWS | CloudTrail Log File Validation Disabled |
| 1023 | High | AWS | CloudTrail Log Files Not Encrypted With KMS |
| 1024 | Medium | AWS | CloudTrail Logging Disabled |
| 1025 | High | AWS | CloudTrail Multi Region Disabled |
| 1026 | High | AWS | CloudTrail Not Integrated With CloudWatch |
| 1027 | High | AWS | CloudTrail SNS Topic Name Undefined |
| 1028 | High | AWS | CloudWatch Without Retention Period Specified |
| 1032 | High | AWS | Configuration Aggregator to All Regions Disabled |
| 1101 | Medium | AWS | S3 Bucket Logging Disabled |
| 1117 | High | AWS | Stack Notifications Disabled |
| 1134 | Medium | AWS | API Gateway V2 Stage Access Logging Settings Not Defined |
| 1137 | Medium | AWS | API Gateway Deployment Without Access Log Setting |
| 1146 | Medium | AWS | CloudWatch Logging Disabled |
| 1147 | Medium | AWS | CloudWatch Metrics Disabled |
| 1158 | Medium | AWS | DocDB Logging Is Disabled |
| 1166 | Medium | AWS | EC2 Instance Monitoring Disabled |
| 1171 | Low | AWS | CloudTrail trail logging is disabled |
| 1173 | Medium | AWS | API Gateway is not logging execution requests |
| 1174 | High | AWS | ECS Cluster with Container Insights Disabled |
| 1185 | Medium | AWS | Elasticsearch Logs Disabled |
| 1188 | High | AWS | ElasticSearch Without Slow Logs |
| 1189 | Medium | AWS | ELB Access Log Disabled |
| 1191 | Medium | AWS | ELBv2 ALB Access Log Disabled |
| 1220 | Medium | AWS | CodeBuild project has logging disabled |
| 1227 | Medium | AWS | MSK Cluster Logging Disabled |
| 1234 | Medium | AWS | Redshift Cluster Logging Disabled |
| 1246 | Medium | AWS | S3 Bucket CloudTrail Logging Disabled |
| 1281 | Medium | AWS | VPC FlowLogs Disabled |
| 1297 | Low | AWS | CloudTrail Log Files S3 Bucket is Publicly Accessible |
| 1298 | Medium | AWS | CloudTrail Log Files S3 Bucket with Logging Disabled |
| 1299 | Medium | AWS | CloudWatch AWS Config Configuration Changes Alarm Missing |
| 1300 | High | AWS | CloudWatch AWS Organizations Changes Missing Alarm |
| 1301 | Medium | AWS | CloudWatch Changes To NACL Alarm Missing |
| 1302 | Medium | AWS | Cloudwatch Cloudtrail Configuration Changes Alarm Missing |
| 1303 | Medium | AWS | CloudWatch Disabling Or Scheduled Deletion Of Customer Created CMK Alarm Missing |
| 1304 | High | AWS | CloudWatch IAM Policy Changes Alarm Missing |
| 1307 | Medium | AWS | CloudWatch Management Console Auth Failed Alarm Missing |
| 1308 | High | AWS | CloudWatch Console Sign-in Without MFA Alarm Missing |
| 1309 | High | AWS | CloudWatch Network Gateways Changes Alarm Missing |
| 1310 | Medium | AWS | CloudWatch Root Account Use Missing |
| 1311 | High | AWS | CloudWatch Route Table Changes Alarm Missing |
| 1312 | Medium | AWS | CloudWatch S3 policy Change Alarm Missing |
| 1313 | Medium | AWS | Cloudwatch Security Group Changes Alarm Missing |
| 1314 | Info | AWS | CloudWatch Unauthorized Access Alarm Missing |
| 1315 | Medium | AWS | CloudWatch VPC Changes Alarm Missing |
| 1333 | Medium | AWS | EKS cluster logging is not enabled |
| 1340 | High | AWS | CloudWatch metric alarm actions disabled |
| 1383 | Medium | AWS | RDS Without Logging |
| 1390 | Medium | AWS | AppSync API logging not enabled |
| 1406 | Medium | AWS | Route 53 Public hosted Zone CloudWatch query logging is disabled |
| 1408 | Medium | AWS | Step Function State Machine All logging is disabled |
| 1440 | Medium | AWS | API Gateway Stage access logging is not enabled |
| 1451 | Medium | AWS | CloudTrail trail is not configured as an organizational trail |
| 1452 | High | AWS | Cloudtrail is not configured to log Lambda Function events |
| 1454 | High | AWS | CloudTrail log not using SNS Notifications |
| 1455 | High | AWS | CloudTrail does not have DynamoDB data events enabled |
| 1565 | Medium | AWS | SNS Topic delivery status logging is not enabled |
| 37 | Medium | AWS | ELB configured with access logging disabled |
| 38 | Medium | AWS | NLB/ALB configured with access logging disabled |
| 674 | Medium | AWS | CloudFront distribution with access logging disabled |
| 948 | High | AWS | CloudWatch Log Group policy for organization trail doesn't allow member account writes |
| 97 | High | Azure | Activity log alerts does not alert for create or update network security group events |
| 98 | High | Azure | SQL server configured with auditing disabled |
| 102 | High | Azure | Activity log alerts does not alert for delete network security group events |
| 103 | High | Azure | Activity log alerts does not alert for create policy assignment events |
| 104 | High | Azure | Activity log alerts does not alert for update security policy events |
| 105 | High | Azure | Activity log alerts does not alert for create or update security solution events |
| 106 | High | Azure | Activity log alerts does not alert for delete security solution events |
| 107 | High | Azure | Activity log alerts does not alert for create or update SQL server firewall rule events |
| 108 | High | Azure | Activity log alerts does not alert for delete SQL server firewall rule events |
| 136 | High | Azure | Load Balancer diagnostic logging disabled |
| 137 | High | Azure | Network Security Group diagnostic logging disabled |
| 138 | High | Azure | App Service web application diagnostic logging disabled |
| 139 | High | Azure | Virtual Network diagnostic logging disabled |
| 140 | High | Azure | SQL database diagnostic and audit logging disabled |
| 553 | High | Azure | Activity log alerts does not alert for delete policy assignment events |
| 651 | High | Azure | Activity log alerts does not alert for delete public IP address events |
| 653 | High | Azure | Activity log alerts does not alert for create or update public IP address events |
| 658 | Medium | Azure | Network Security Group flow log retention period is less than 90 days |
| 888–890 | Medium | Azure | Storage Account logging for Blob/Queue/Table Service is disabled |
| 1413 | High | Azure | Diagnostic settings not integrated with Azure Monitor |
| 1555 | Medium | Azure | Azure Log Profile should send activity logs for all regions |
| 1556 | Medium | Azure | Log Profile should send logs for all activities |
| 1558 | Medium | Azure | Azure Log Profiles retention activity should be set for 365 days |
| 892 | High | GCP | Log metric filter and alert does not exist for VPC Network Firewall Rule changes |
| 893 | High | GCP | Log metric filter and alert does not exist for VPC Network Route changes |
| 894 | High | GCP | Log metric filter and alert does not exist for VPC Network changes |
| 895 | High | GCP | Log metric filter and alert does not exist for Project Ownership Assignments and Changes |
| 896 | High | GCP | Log metric filter and alert does not exist for Audit Configuration Changes |
| 897 | High | GCP | Log metric filter and alert does not exist for Custom Role changes |
| 898 | High | GCP | Log metric filter and alert does not exist for Cloud Storage IAM Permission changes |
| 899 | High | GCP | Log metric filter and alert does not exist for SQL Instance Configuration changes |
| 900 | Medium | GCP | Cloud Logging retention policy not enabled |
| 901 | High | GCP | VPC flow logs not enabled for a subnet in a VPC Network |
| 902 | High | GCP | Cloud Logging for SQL instance configuration changes not enabled |
| 951 | High | GCP | Cloud Logging does not audit Cloud Storage Bucket permission changes |
| 1705 | Medium | GCP | Cloud Storage bucket logging is disabled |
| 2049–2093 | High | GCP | Admin read/data read/data write logs not enabled (BigQuery, Cloud Functions, GKE, Spanner, SQL, Storage, etc.) |
| 3036 | High | GCP | IAM Audit Not Properly Configured |
| 3067 | Medium | GCP | Stackdriver Logging Disabled |
| 5004–5009 | High | General/K8s | Audit Log Maxage/Maxbackup/Maxsize/Path not set, Audit Policy not defined/not covering key concerns |

---

## 03.04 Configuration Management

**Controls:** Baseline Configuration (03.04.01), Configuration Settings (03.04.02), Configuration Change Control (03.04.03), Least Functionality (03.04.06), Authorized Software (03.04.08), System Component Inventory (03.04.10)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 141 | Low | AWS | Config service is not enabled |
| 145 | Medium | AWS | EKS is not configured to use current version |
| 148 | Medium | AWS | ECR repository setting (tag immutability) is not enabled |
| 184 | Medium | AWS | Config service failed to deliver log files |
| 266 | Medium | AWS | EC2 Default security group does not block all traffic |
| 276 | Medium | AWS | EC2 instance with IMDS v1 enabled |
| 495 | High | AWS | DMS with Auto Minor Version Upgrade disabled |
| 590 | High | AWS | RDS Minor Upgrades Not Enabled |
| 886 | Medium | AWS | ECS Fargate task definition not using the latest platform version |
| 1012 | High | AWS | Automatic Minor Upgrades Disabled |
| 1032 | High | AWS | Configuration Aggregator to All Regions Disabled |
| 1040 | High | AWS | CloudFormation Stack resources are in a Drifted State |
| 1041 | High | AWS | CloudFormation Stack is not using Termination Protection |
| 1045 | Medium | AWS | ECR Image Tag Not Immutable |
| 1233 | High | AWS | LightSail instance using outdated blueprint |
| 1261 | Medium | AWS | RDS cluster automatic minor version upgrade is disabled |
| 1295 | Medium | AWS | Lambda function using deprecated runtime |
| 1461 | Medium | AWS | EKS Cluster Kubernetes version is on extended support |
| 1462 | Low | AWS | EKS Cluster should not use a deprecated authentication method |
| 1487 | Medium | AWS | EC2 instance launched with key pair |
| 1492 | High | AWS | EC2 Instance NOT utilizing detailed monitoring capabilities |
| 1588 | Medium | AWS | Database cluster automatic minor version upgrade is disabled |
| 145 | Medium | Azure | EKS is not configured to use current version |
| 200 | Medium | Azure | AKS version is outdated |
| 910 | Medium | GCP | GKE Node has Auto-Upgrade disabled |
| 909 | Medium | GCP | GKE Node has Auto-Repair disabled |
| 3049 | High | GCP | Outdated GKE Version |
| 5046 | High | General/K8s | Image Pull Policy Of The Container Is Not Set To Always |
| 5047 | High | General/K8s | Image Without Digest |
| 5077 | High | General/K8s | Object Is Using A Deprecated API Version |

---

## 03.05 Identification and Authentication

**Controls:** User Identification, Authentication, Re-Authentication (03.05.01), MFA (03.05.03), Identifier Management (03.05.05), Password Management (03.05.07), Authenticator Management (03.05.12)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 1 | High | AWS | IAM user access key active longer than 90 days |
| 8 | Info | AWS | IAM root user has an active access key |
| 9 | Info | AWS | IAM root user has MFA not configured |
| 10 | Low | AWS | IAM user MFA not configured |
| 11 | Medium | AWS | IAM password policy allows reuse |
| 12 | Medium | AWS | IAM password policy does not expire in 90 days |
| 13 | Medium | AWS | IAM password policy does not require lower case |
| 14 | Medium | AWS | IAM password policy allow minimum length less than 14 |
| 15 | Medium | AWS | IAM password policy does not require a number |
| 16 | Medium | AWS | IAM password policy does not require a symbol |
| 17 | Medium | AWS | IAM password policy does not require upper case letter |
| 18 | Medium | AWS | IAM password policy set to not expire |
| 82 | Info | AWS | Unrotated Credentials - AWS::IAM::User |
| 83 | Info | AWS | Unrotated Password - AWS::IAM::User |
| 88 | Info | AWS | Unused Access Keys - AWS::IAM::User |
| 450 | High | AWS | IAM user access key active longer than 90 days but never used |
| 451 | High | AWS | IAM user access key inactive and older than 90 days |
| 559 | High | AWS | RDS Instance Not Configured with IAM Authentication |
| 576 | High | AWS | IAM credentials unused for 45 days or greater are enabled |
| 577 | High | AWS | IAM User with more than one active access key |
| 602 | Low | AWS | IAM Root account configured with Virtual MFA |
| 642 | Medium | AWS | ElastiCache for Redis cluster with AUTH default user access disabled |
| 647 | High | AWS | IAM user inactive for more than 30 days |
| 648 | High | AWS | IAM user has both Console access and Access Keys |
| 796 | High | AWS | RDS cluster not configured with IAM authentication |
| 1006 | Medium | AWS | IAM user access key active longer than 365 days |
| 1010 | High | AWS | Authentication Without MFA |
| 1013 | High | AWS | AWS Password Policy With Unchangeable Passwords |
| 1062 | Medium | AWS | IAM Database Auth Not Enabled |
| 1064 | High | AWS | IAM Password Without Minimum Length |
| 1075 | Medium | AWS | AWS Secrets Manager secret has automatic rotation disabled |
| 1078 | High | AWS | Misconfigured Password Policy Expiration |
| 1080 | High | AWS | Password Without Reuse Prevention |
| 1092 | Low | AWS | Root Account Has Active Access Keys |
| 1125 | Medium | AWS | High Access Key Rotation Period |
| 1149 | High | AWS | Cognito UserPool Without MFA |
| 1203 | Medium | AWS | Secrets Manager secret configured with automatic rotation not rotated as scheduled |
| 1204 | Medium | AWS | Secrets Manager secret not configured to rotate within 90 days |
| 1211 | Medium | AWS | IAM User Has Too Many Access Keys |
| 1279 | Medium | AWS | IAM User Without Password Reset |
| 1367 | High | AWS | IAM User Policy Without MFA |
| 1378 | Medium | AWS | No Password Policy Enabled |
| 1582 | Low | AWS | IAM root user has been recently used |
| 1586 | Medium | AWS | IAM password policy does not allow users to change their passwords |
| 68531 | Low | Cross-Cloud | High privileged identity with excessive permissions has unrotated credentials and MFA disabled |
| 68540 | Medium | Cross-Cloud | Privileged identity has unused access keys |
| 68541 | Medium | Cross-Cloud | Identity with access to sensitive data has MFA disabled |
| 68542 | Medium | Cross-Cloud | Identity with access to sensitive data has unrotated credentials |
| 68552 | High | Cross-Cloud | Privileged identity has multiple access keys |
| 68240 | High | Cross-Cloud | Unused identity |
| 68242 | Medium | Cross-Cloud | Identity with unrotated credentials has excessive permissions |
| 151 | Info | Azure | Unrotated Credentials - microsoft.graph.application |
| 189 | Info | Azure | Unrotated Password - microsoft.graph.user |
| 539 | Low | Azure | Azure Entra ID Security Defaults are disabled |
| 1062 | Medium | Azure | AWS Cognito UserPool configured without Multi-Factor Authentication (MFA) |
| 72772 | Low | Azure | Azure Tenant not using Conditional Access Policies |
| 79095 | Low | Azure | Conditional access does not block legacy authentication |
| 79096 | Medium | Azure | Conditional access does not require compliant or hybrid-joined device |
| 532 | Medium | GCP | Firebase MFA not Enabled |
| 904 | Medium | GCP | Ensure API Keys Are Rotated Every 90 Days |
| 1715 | Medium | GCP | IAM service account key needs to be rotated within 15 days |
| 1716 | High | GCP | IAM service account key not rotated more than 90 days |
| 5036–5039 | Medium | General/K8s | Etcd Client/Peer Certificate Authentication issues |
| 5113 | Medium | General/K8s | ServiceAccount Allows Access Secrets |

---

## 03.06 Incident Response

**Controls:** Incident Handling (03.06.01), Incident Monitoring, Reporting, and Response (03.06.02)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 169 | High | AWS | GuardDuty is not enabled |
| 604 | High | AWS | Ensure AWS Security Hub is enabled |
| 1093 | High | AWS | AWS Detective is not enabled |
| 1203 | Medium | AWS | GuardDuty Detector Disabled |
| 1717 | Medium | AWS | GuardDuty ECS Fargate Agent Management is not enabled |
| 1718 | Medium | AWS | GuardDuty S3 protection is Not Enabled |
| 1719 | Medium | AWS | GuardDuty EKS Protection is Not Enabled |
| 1720 | Medium | AWS | GuardDuty RDS Protection is Not Enabled |
| 1721 | Medium | AWS | GuardDuty DNS Logs are Not Enabled |
| 1722 | Medium | AWS | GuardDuty EKS add on management is not enabled |
| 1723 | Medium | AWS | GuardDuty Cloudtrail is Not Enabled |
| 1724 | Medium | AWS | GuardDuty Malware Protection NOT enabled |
| 1725 | Medium | AWS | GuardDuty Lambda Protection is Not Enabled |
| 591 | High | AWS | IAM support role has not been created to manage incidents with AWS Support |
| 1806 | High | AWS | CloudWatch metric alarm actions disabled |
| 623 | High | Azure | Azure Security Contacts not enabled for Subscription Owners |
| 624 | High | Azure | Azure Security Contacts additional email addresses not configured |
| 625 | High | Azure | Azure Security Contact notifications not set to 'High' |
| 1933 | High | Azure | Defender for Kubernetes is not enabled |
| 751–760, 813–820 | High | Azure | Microsoft Defender for Cloud is set to Off (App Service, SQL, Key Vault, Servers, Storage, Containers, DNS, Resource Manager, Databases, CosmosDB) |
| 1897 | High | AWS | Macie Session is not enabled |

---

## 03.08 Media Protection

**Controls:** Media Storage (03.08.01), Media Sanitization (03.08.03), System Backup – Cryptographic Protection (03.08.09)

Covers encryption at rest and backup integrity for cloud storage, databases, and volumes.

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 1 | Info | AWS | Encrypted At Rest - AWS::EC2::Instance |
| 15 | Info | AWS | Encrypted At Rest - AWS::RDS::DBCluster |
| 16 | Info | AWS | Encrypted At Rest - AWS::RDS::DBSnapshot |
| 17 | Info | AWS | Encrypted At Rest - AWS::RDS::DBInstance |
| 18 | Info | AWS | Encrypted At Rest - AWS::RDS::DBClusterSnapshot |
| 29 | Info | AWS | Backup enablement status - AWS::RDS::DBInstance |
| 41 | Medium | AWS | EBS volume configured without encryption |
| 42 | Medium | AWS | EBS snapshot configured without encryption |
| 46 | Medium | AWS | KMS key configured with key rotation disabled |
| 50 | Medium | AWS | RDS instances not configured with encryption at rest enabled |
| 57 | Low | AWS | Redshift cluster not configured for encryption |
| 61 | Low | AWS | Redshift snapshot configured without encryption |
| 167 | Low | AWS | DynamoDB tables are not being encrypted with customer owned keys |
| 178 | Info | AWS | Backup enablement status - AWS::DynamoDB::Table |
| 245 | High | AWS | S3 bucket with versioning not enabled |
| 247 | High | AWS | Athena workgroup not configured to encrypt all data at rest |
| 261 | High | AWS | DMS not configured for encryption with a CMK |
| 284 | High | AWS | EFS File System is encrypted without CMK |
| 288 | Low | AWS | EKS cluster not utilizing encryption of secrets |
| 290 | Low | AWS | EFS File System not configured with encryption at rest |
| 311 | Low | AWS | Kinesis delivery stream with encryption disabled |
| 397 | Medium | AWS | ECS Fargate task definition not encrypting ephemeral storage with KMS |
| 513 | Low | AWS | ElastiCache for Redis is not configured with encryption at-rest |
| 514 | Low | AWS | Redshift cluster not configured for encryption with a CMK |
| 525 | Medium | AWS | KMS key scheduled for deletion |
| 526 | Medium | AWS | KMS CMK expiring within 30 days |
| 535 | Medium | AWS | Kinesis delivery stream not configured for encryption with a CMK |
| 551 | High | AWS | SQS Queue Encryption Configured with a default KMS key |
| 565 | High | AWS | S3 bucket is not configured with MFA Delete |
| 603 | Medium | AWS | CloudTrail logs are not encrypted using a Customer Master Key |
| 616 | High | AWS | RDS retention policy less than 7 days |
| 637 | Medium | AWS | ElastiCache for Redis cluster not configured for encryption with a Customer Managed Key |
| 706 | High | AWS | RDS instance with automatic backup setting disabled |
| 791 | High | AWS | RDS cluster with copy tags to snapshots disabled |
| 792 | Medium | AWS | RDS instance not encrypted with customer managed key |
| 794 | Medium | AWS | RDS Cluster not encrypted with customer managed key |
| 878 | Medium | AWS | ECS cluster instance volume with encryption disabled |
| 925 | High | AWS | EBS volume encryption is not enabled by default in all regions |
| 1039 | Low | AWS | EBS Volume Encryption Disabled |
| 1050 | Low | AWS | EFS Not Encrypted |
| 1051 | High | AWS | EFS Without KMS |
| 1086 | Medium | AWS | RDS With Backup Disabled |
| 1106 | Medium | AWS | S3 Bucket Without Versioning |
| 1116 | Medium | AWS | SQS With SSE Disabled |
| 1159 | Low | AWS | DynamoDB Table Not Encrypted |
| 1175 | Low | AWS | ECS Cluster Not Encrypted At Rest |
| 1182 | Low | AWS | ElastiCache With Disabled at Rest Encryption |
| 1184 | Low | AWS | ElasticSearch Encryption With KMS Disabled |
| 1186 | Low | AWS | ElasticSearch Not Encrypted At Rest |
| 1222 | High | AWS | Low RDS Backup Retention Period |
| 1229 | Low | AWS | Neptune Database Cluster Encryption Disabled |
| 1232 | Low | AWS | RDS Storage Encryption Disabled |
| 1233 | Low | AWS | RDS Storage Not Encrypted |
| 1235 | Medium | AWS | Redshift Cluster Without KMS CMK |
| 1251 | Low | AWS | S3 Bucket Without Server-side-encryption |
| 1254 | Low | AWS | SageMaker Data Encryption Disabled |
| 1259 | High | AWS | Secrets Manager Should Specify KmsKeyId |
| 1286 | Low | AWS | Workspace Without Encryption |
| 1305 | Medium | AWS | CloudWatch Log Group Without KMS |
| 1317 | Low | AWS | DAX Cluster Not Encrypted |
| 1319 | High | AWS | DOCDB Cluster Encrypted With AWS Managed Key |
| 1320 | Low | AWS | DOCDB Cluster Not Encrypted |
| 1323 | Low | AWS | EBS Default Encryption Disabled |
| 1324 | Low | AWS | EBS Volume Snapshot Not Encrypted |
| 1326 | High | AWS | ECR Repository Not Encrypted With CMK |
| 1328 | Low | AWS | ECS Task Definition Volume Not Encrypted |
| 1330 | Low | AWS | EKS Cluster Encryption Disabled |
| 1335 | Low | AWS | ElastiCache Replication Group Not Encrypted At Rest |
| 1343 | Low | AWS | Glue Data Catalog Encryption Disabled |
| 1344 | Low | AWS | Glue Security Configuration Encryption Disabled |
| 1381 | Medium | AWS | RDS Cluster With Backup Disabled |
| 1416 | Medium | AWS | Secretsmanager Secret Encrypted With AWS Managed Key |
| 1417 | Medium | AWS | Secretsmanager Secret Without KMS |
| 1628 | Medium | AWS | S3 Bucket not encrypted with Customer Managed Key (CMK) |
| 1637 | High | AWS | S3 Bucket key is disabled |
| 1665 | Medium | AWS | Workspace root volume is not encrypted |
| 1668 | Medium | AWS | Workspace user volume is not encrypted |
| 1730 | Medium | AWS | EFS access point NOT enforcing a root directory |
| 1732 | Medium | AWS | EFS File System backups are not enabled |
| 1741 | High | AWS | Disabled KMS key remains undeleted |
| 1742 | High | AWS | KMS key policy ALLOWS all KMS actions |
| 1853–1865 | High | AWS | Backup plan does not include [EFS/EBS/RDS/DynamoDB/EC2/S3/FSx/Redshift/etc.] resources |
| 70963 | Medium | Cross-Cloud | Database contains sensitive data and not encrypted at rest |
| 64801 | Low | Cross-Cloud | Database contains sensitive data and has no backups enabled |
| 70 | High | Azure | Azure Disk Encryption (ADE) not enabled on OS disk |
| 71 | High | Azure | Azure Disk Encryption (ADE) not enabled on data disk |
| 72 | High | Azure | Azure Disk Encryption (ADE) not enabled on unattached disk |
| 124 | High | Azure | SQL database has transparent data encryption disabled |
| 126 | High | Azure | Storage Account configured with blob service encryption disabled |
| 127 | High | Azure | Storage Account configured with file service encryption disabled |
| 327 | High | Azure | Cosmos DB account is not encrypted with Customer Supplied Encryption Key (CSEK) |
| 570 | Medium | Azure | Virtual Machine OS and Data disks are not encrypted with a Customer Managed Key (CMK) |
| 628 | High | Azure | Storage Account with soft delete disabled for blobs and containers |
| 676 | Medium | Azure | Storage Account is not encrypted with a Customer Managed Key (CMK) |
| 460 | High | GCP | Cloud Storage not configured to used CSEK |
| 3016 | Medium | GCP | Disk Encryption Disabled |

---

## 03.11 Risk Assessment

**Controls:** Risk Assessment (03.11.01), Vulnerability Monitoring and Scanning (03.11.02), Risk Response (03.11.04)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 43 | Info | AWS | Sensor installed - AWS::EC2::Instance |
| 53 | Info | AWS | IMDSv1 Enabled - AWS::EC2::Instance |
| 77 | Info | AWS | Remote Code Execution Risk - AWS::EC2::Instance |
| 80 | Info | AWS | Network-Reachable Vulnerabilities - AWS::Lambda::Function,AWS::ECS::Task |
| 147 | Low | AWS | ECR repository not set to Scan on Push |
| 180 | Info | AWS | Has code-reachable critical severity vulnerabilities - AWS::EC2::Instance,AWS::Lambda::Function |
| 181 | Info | AWS | Has code-reachable high severity vulnerabilities - AWS::EC2::Instance,AWS::Lambda::Function |
| 182 | Info | AWS | Has code-reachable RCE vulnerabilities - AWS::EC2::Instance,AWS::Lambda::Function |
| 183 | Low | AWS | Compute resource with reachable critical-severity vulnerabilities is publicly exposed |
| 184 | Low | AWS | Compute resource with reachable critical-severity vulnerabilities is publicly exposed to the internet |
| 185 | Info | Cross-Cloud | Compute resource with reachable high-severity vulnerabilities is publicly exposed and accesses sensitive data |
| 186 | Low | Cross-Cloud | Compute resource with reachable high-severity vulnerabilities is publicly exposed |
| 187 | Info | Cross-Cloud | Compute resource with reachable RCE vulnerabilities is publicly exposed and accesses sensitive data |
| 188 | Low | Cross-Cloud | Compute resource with reachable RCE vulnerabilities is publicly exposed |
| 276 | Medium | AWS | EC2 instance with IMDS v1 enabled |
| 790 | Medium | AWS | RDS PostgreSQL vulnerable to local file read |
| 1278 | High | AWS | Unscanned ECR Image |
| 64807 | Medium | Cross-Cloud | Compute is publicly exposed to the internet with IMDSv1 enabled |
| 68532 | Info | Cross-Cloud | Publicly exposed compute with RCE has excessive permissions |
| 68534 | Low | Cross-Cloud | Publicly exposed compute with RCE has no sensor |
| 68535 | Low | Cross-Cloud | Publicly exposed compute has access to sensitive data |
| 68536 | Low | Cross-Cloud | Compute with RCE has excessive permissions |
| 68537 | Low | Cross-Cloud | Compute with RCE has access to sensitive data |
| 68538 | Medium | Cross-Cloud | Compute instance with RCE contains cleartext credentials in user-data |
| 68546 | Medium | Cross-Cloud | Compute with no sensor has excessive permissions |
| 68548 | Medium | Cross-Cloud | Compute with RCE has no sensor |
| 44 | Info | Azure | Sensor installed - Microsoft.Compute/virtualMachines |
| 45 | Info | GCP | Sensor installed - compute.googleapis.com/Instance |
| 103 | Info | ASPM | Has code-reachable critical severity vulnerabilities - ASPM::Application |
| 107 | Info | ASPM | Has code-reachable high severity vulnerabilities - ASPM::Application |
| 119 | Info | ASPM | Has code-reachable RCE vulnerabilities - ASPM::Application |
| 991 | High | GCP | Artifact Registry Container Analysis API is Not Enabled |
| 1967 | Medium | GCP | Artifact Registry Image Vulnerability is Disabled |

---

## 03.12 Security Assessment and Monitoring

**Controls:** Security Assessment (03.12.01), Plan of Action and Milestones (03.12.02), Continuous Monitoring (03.12.03), Information Exchange (03.12.05)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 141 | Low | AWS | Config service is not enabled |
| 169 | High | AWS | GuardDuty is not enabled |
| 604 | High | AWS | Ensure AWS Security Hub is enabled |
| 953 | High | GCP | Access Approval API is Disabled |
| 906 | High | GCP | Cloud Asset Inventory API is Disabled |
| 1093 | High | AWS | AWS Detective is not enabled |
| 1147 | Medium | AWS | CloudWatch Metrics Disabled |
| 1166 | Medium | AWS | EC2 Instance Monitoring Disabled |
| 1174 | High | AWS | ECS Cluster with Container Insights Disabled |
| 1203 | Medium | AWS | GuardDuty Detector Disabled |
| 1492 | High | AWS | EC2 Instance NOT utilizing detailed monitoring capabilities |
| 1806 | High | AWS | CloudWatch metric alarm actions disabled |
| 1897 | High | AWS | Macie Session is not enabled |
| 1933 | High | Azure | Defender for Kubernetes is not enabled |
| 751–760, 813–820 | High | Azure | Microsoft Defender for Cloud is set to Off (various services) |
| 1205 | High | AWS | IAM Access Analyzer Not Enabled |
| 399 | High | AWS | ECS cluster with Container Insights disabled |

---

## 03.13 System and Communications Protection

**Controls:** Boundary Protection (03.13.01), Network Communications – Deny by Default (03.13.06), Transmission and Storage Confidentiality (03.13.08), Network Disconnect (03.13.09), Cryptographic Key Management (03.13.10), Cryptographic Protection (03.13.11), Session Authenticity (03.13.15)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 27 | Medium | AWS | ELB configured as publicly accessible on non-web ports |
| 28 | Medium | AWS | NLB/ALB configured as publicly accessible on non-web ports |
| 29 | Medium | AWS | ELB global access configured to one or more administrative ports |
| 30 | Medium | AWS | NLB/ALB global access configured to one or more administrative ports |
| 31 | Medium | AWS | ELB SSL negotiation configured with insecure ciphers |
| 32 | Medium | AWS | NLB/ALB SSL negotiation configured with insecure ciphers on externally facing load balancer |
| 33 | Medium | AWS | ELB configured with a vulnerable SSL protocol |
| 34 | Medium | AWS | NLB/ALB configured with a vulnerable SSL protocol |
| 35 | Info | AWS | ELB configured publicly with TLS/SSL disabled |
| 36 | Info | AWS | ALB configured publicly with TLS/SSL disabled |
| 46 | Medium | AWS | KMS key configured with key rotation disabled |
| 60 | Medium | AWS | Redshift parameter group not configured with SSL |
| 133 | High | AWS | NLB/ALB SSL negotiation configured with insecure ciphers for internally facing load balancer |
| 149 | Medium | AWS | SNS subscription communicating with topic over HTTP |
| 170 | Low | AWS | ElastiCache for Redis is not configured with in-transit encryption |
| 171 | Medium | AWS | EMR block public access setting is disabled |
| 173 | Medium | AWS | API Gateway is accessible through public API endpoints |
| 174 | Low | AWS | API Gateway is not using SSL certificates to verify HTTP requests made to backend |
| 175 | Low | AWS | API Gateway is not configured to use a WAF |
| 176 | Low | AWS | CloudFront is not configured to use an AWS WAF |
| 177 | Low | AWS | CloudFront is using insecure TLS/SSL protocols |
| 265 | Medium | AWS | EC2 instance publicly configured allows global public IP in ingress rule(s) |
| 266 | Medium | AWS | EC2 Default security group does not block all traffic |
| 279 | Medium | AWS | CloudFront allows viewers to access files with HTTP |
| 286 | Medium | AWS | EC2 Security Group allows ingress from 0.0.0.0/0 to remote server administration ports |
| 288 | Low | AWS | EKS cluster not utilizing encryption of secrets |
| 289 | Medium | AWS | EKS cluster with open VPC CIDR range for public access |
| 292 | Medium | AWS | EC2 Security Group allows ingress from ::/0 to remote server administration ports |
| 293 | Low | AWS | EC2 Network ACLs allow ingress from 0.0.0.0/0 to remote server administration ports |
| 512 | High | AWS | VPC with no active Flow Logs configured |
| 521 | Medium | AWS | DMS endpoint does not have SSL configured |
| 545 | Low | AWS | API Gateway is not configured to use a WAFv2 |
| 547 | Medium | AWS | VPC subnets should not allow automatic public IP assignment |
| 550 | Low | AWS | VPC route table with VPC peering overly permissive to all traffic |
| 580–585 | Medium | AWS | EC2 instance allows global public internet/internal SSH/RDP access |
| 601 | High | AWS | S3 Bucket is not set to deny HTTP requests |
| 672 | Medium | AWS | CloudFront origin protocol policy does not enforce HTTPS only |
| 734 | Medium | AWS | CloudFront distribution using insecure TLS version |
| 770 | Medium | AWS | NLB/ALB listener allowing connection requests over HTTP |
| 771 | Medium | AWS | ELB Classic listener allowing connection requests over HTTP |
| 788 | High | AWS | ALB is not using the latest predefined security policy |
| 1001 | Medium | AWS | ALB Listening on HTTP |
| 1004 | Medium | AWS | API Gateway Endpoint Config is Not Private |
| 1007 | Medium | AWS | API Gateway Without SSL Certificate |
| 1008 | Medium | AWS | API Gateway without WAF |
| 1020 | Medium | AWS | CloudFront Without Minimum Protocol TLS 1.2 |
| 1021 | Medium | AWS | CloudFront Without WAF |
| 1036 | Low | AWS | DB Security Group Open To Large Scope |
| 1037 | Info | AWS | DB Security Group With Public Scope |
| 1038 | Low | AWS | Default Security Groups With Unrestricted Traffic |
| 1041 | Medium | AWS | EC2 Instance Has Public IP |
| 1043 | High | AWS | EC2 Instance Using Default VPC |
| 1053 | High | AWS | ElastiCache Using Default Port |
| 1054 | High | AWS | ElastiCache Without VPC |
| 1055 | Medium | AWS | Elasticsearch with HTTPS disabled |
| 1056 | Medium | AWS | ELB Using Insecure Protocols |
| 1057 | Low | AWS | ELB Using Weak Ciphers |
| 1082 | Low | AWS | Public Port Wide |
| 1085 | High | AWS | RDS Using Default Port |
| 1087 | Low | AWS | Redis Not Compliant |
| 1090 | High | AWS | Redshift Using Default Port |
| 1107 | Medium | AWS | Secure Ciphers Disabled |
| 1108 | Low | AWS | Security Group Ingress Not Restricted |
| 1109 | Medium | AWS | Security Group With Unrestricted Access To SSH |
| 1113 | High | AWS | AWS Network Firewall without stateful rule group |
| 1116 | Medium | AWS | AWS Network Firewall without stateless rule group |
| 1120 | Low | AWS | Unknown Port Exposed To Internet |
| 1121 | Low | AWS | Unrestricted Security Group Ingress |
| 1126 | Medium | AWS | ALB Is Not Integrated With WAF |
| 1145 | Medium | AWS | Cloudfront Viewer Protocol Policy Allows HTTP |
| 1167 | Medium | AWS | EC2 Instance Subnet Has Public IP Mapping On Launch |
| 1168 | High | AWS | EC2 Network ACL Duplicate Rule |
| 1170 | Medium | AWS | EC2 Network ACL Overlapping Ports |
| 1171 | Medium | AWS | EC2 Permissive Network ACL Protocols |
| 1172 | Medium | AWS | EC2 Public Instance Exposed Through Subnet |
| 1173 | Low | AWS | EC2 Sensitive Port Is Publicly Exposed |
| 1179 | Medium | AWS | EFS Volume With Disabled Transit Encryption |
| 1183 | Medium | AWS | ElastiCache With Disabled Transit Encryption |
| 1190 | Low | AWS | ELB Sensitive Port Is Exposed To Entire Network |
| 1194 | Medium | AWS | ELB Without Secure Protocol |
| 1196 | Medium | AWS | EMR Cluster Without Security Configuration |
| 1198 | High | AWS | EMR Without VPC |
| 1199 | Low | AWS | Fully Open Ingress |
| 1218 | Medium | AWS | KMS Key Rotation Disabled |
| 1238 | Medium | AWS | MSK Cluster in-transit encryption disabled |
| 1243 | Low | AWS | OpenSearch domain not configured with HTTPS |
| 1245 | Medium | AWS | OpenSearch domain not configured with latest TLS security policy |
| 1252 | Medium | AWS | S3 Bucket Without SSL In Write Actions |
| 1260 | Medium | AWS | Security Group Egress CIDR Open To World |
| 1261 | Medium | AWS | Security Group Egress With All Protocols |
| 1263 | Medium | AWS | Security Group Egress With Port Range |
| 1264 | Medium | AWS | Security Group Ingress With All Protocols |
| 1265 | Medium | AWS | Security Group Ingress With Port Range |
| 1267 | Medium | AWS | Security Groups Allows Unrestricted Outbound Traffic |
| 1268 | Low | AWS | Security Group Unrestricted Access To RDP |
| 1269 | Low | AWS | Security Groups With Exposed Admin Ports |
| 1272 | High | AWS | Security Groups Without VPC Attached |
| 1273 | High | AWS | Shield Advanced Not In Use |
| 1277 | Medium | AWS | TCP UDP Protocol Network ACL Entry Allows All Ports |
| 1283 | Medium | AWS | VPC Without Network Firewall |
| 1332 | Medium | AWS | EKS Cluster Has Public Access |
| 1334 | Medium | AWS | EKS node group remote access disabled |
| 1336 | Medium | AWS | ElastiCache Replication Group Not Encrypted At Transit |
| 1337 | Medium | AWS | Elasticsearch Domain Not Encrypted Node To Node |
| 1377 | Medium | AWS | Network ACL With Unrestricted Access To SSH |
| 1376 | Low | AWS | Network ACL With Unrestricted Access To RDP |
| 1385 | High | AWS | Redshift Cluster Without VPC |
| 1410 | Medium | AWS | S3 Bucket Policy Accepts HTTP Requests |
| 1423 | Medium | AWS | Redshift cluster does not have fips compliant ssl connection enabled |
| 1428 | Medium | AWS | SSM Session Transit Encryption Disabled |
| 1453 | Medium | AWS | VPC Subnet Assigns Public IP |
| 1506–1551 | Medium | AWS | EC2 Security Group is overly permissive to [SSH/RDP/HTTP/MySQL/SMTP/etc.] Port(s) |
| 1570 | Medium | AWS | EC2 Network ACLs allows all TCP or UDP ports |
| 1577 | High | AWS | VPC Peering lacks DNS resolution from accepter and requester VPC |
| 1623 | Medium | AWS | AWS Glue connection not configured to use SSL |
| 1740 | Medium | AWS | EC2 Security Group is overly permissive to entire private networks |
| 63–68 | Medium | Azure | Network Security Group rules allow ingress/egress from any source |
| 73 | Medium | Azure | PostgreSQL database does not enforce SSL |
| 86 | Medium | Azure | Key Vault firewall is not enabled |
| 109 | Medium | Azure | Default Network Access Rule for Storage Accounts is not Set to Deny |
| 110 | Medium | Azure | Storage Account has secure transfer disabled |
| 654–657 | Medium | Azure | Network Security Group rule allows RDP/SSH/UDP/HTTP(S) access from any source |
| 1311 | Medium | Azure | Azure SQL Server not using TLS version 1.2 or higher |
| 411 | Medium | GCP | VPC allows access to SSH from all networks |
| 412 | Medium | GCP | VPC allows access to RDP from all networks |
| 413 | Medium | GCP | Cloud Load Balancing SSL proxy custom SSL policy allows weak cipher suites |
| 457 | Medium | GCP | Cloud Load Balancing SSL proxy custom SSL policy configured with a vulnerable SSL protocol |
| 467–478 | Medium | GCP | VPC allows access to [DNS/FTP/HTTP/SMB/MongoDB/MySQL/etc.] from all networks |
| 479 | Medium | GCP | VPC firewall rule allows inbound access from all networks to all internal networks |
| 901 | High | GCP | VPC flow logs not enabled for a subnet in a VPC Network |
| 1690 | Medium | GCP | Firewall logging is not enabled |
| 5013 | Medium | General/K8s | Auto TLS Set To True |
| 5019 | Medium | General/K8s | CNI Plugin Does Not Support Network Policies |
| 5040–5041 | Medium | General/K8s | Etcd TLS Certificate Files Not Properly Set/Configured |
| 5071 | High | General/K8s | Network Policy Is Not Targeting Any Pod |
| 5080 | Medium | General/K8s | Pod Misconfigured Network Policy |
| 5120 | High | General/K8s | Service Type is NodePort |
| 5121 | Medium | General/K8s | Service With External Load Balancer |
| 5134 | Medium | General/K8s | TSL Connection Certificate Not Setup |
| 5140 | Medium | General/K8s | Weak TLS Cipher Suites |

---

## 03.14 System and Information Integrity

**Controls:** Flaw Remediation (03.14.01), Malicious Code Protection (03.14.02), System Monitoring (03.14.06)

| ID | Sev | Provider | Policy Name |
|----|-----|----------|-------------|
| 43 | Info | AWS | Sensor installed - AWS::EC2::Instance |
| 53 | Info | AWS | IMDSv1 Enabled - AWS::EC2::Instance (SSRF/metadata attack surface) |
| 145 | Medium | AWS | EKS is not configured to use current version |
| 147 | Low | AWS | ECR repository not set to Scan on Push |
| 219 | Medium | AWS | Auto Scaling group launch configuration template utilizing IMDSv1 |
| 276 | Medium | AWS | EC2 instance with IMDS v1 enabled |
| 495 | High | AWS | DMS with Auto Minor Version Upgrade disabled |
| 590 | High | AWS | RDS Minor Upgrades Not Enabled |
| 724 | Medium | AWS | API Gateway Rest API WAFv2 WebACL not configured with AMR for Log4j Vulnerability |
| 790 | Medium | AWS | RDS PostgreSQL vulnerable to local file read |
| 886 | Medium | AWS | ECS Fargate task definition not using the latest platform version |
| 907 | Medium | GCP | Ensure Cloud Armor policies are enabled to detect Apache Log4j2 Vulnerabilities |
| 1012 | High | AWS | Automatic Minor Upgrades Disabled |
| 1166 | Medium | AWS | EC2 Instance Monitoring Disabled |
| 1278 | High | AWS | Unscanned ECR Image |
| 1295 | Medium | AWS | Lambda function using deprecated runtime |
| 1461 | Medium | AWS | EKS Cluster Kubernetes version is on extended support |
| 1492 | High | AWS | EC2 Instance NOT utilizing detailed monitoring capabilities |
| 1493 | Medium | AWS | EC2 instance with non-compliant patch status |
| 1588 | Medium | AWS | Database cluster automatic minor version upgrade is disabled |
| 1724 | Medium | AWS | GuardDuty Malware Protection NOT enabled |
| 1926 | Medium | AWS | EC2 Amazon Machine Image IMDSv1 configured |
| 44 | Info | Azure | Sensor installed - Microsoft.Compute/virtualMachines |
| 45 | Info | GCP | Sensor installed - compute.googleapis.com/Instance |
| 68534 | Low | Cross-Cloud | Publicly exposed compute with RCE has no sensor |
| 68546 | Medium | Cross-Cloud | Compute with no sensor has excessive permissions |
| 68547 | Medium | Cross-Cloud | Compute with no logging has excessive permissions |
| 68548 | Medium | Cross-Cloud | Compute with RCE has no sensor |
| 271–274 | Medium | Azure | App Service/Function may be insecure to Log4Shell vulnerabilities |
| 909 | Medium | GCP | GKE Node has Auto-Repair disabled |
| 910 | Medium | GCP | GKE Node has Auto-Upgrade disabled |
| 106557 | Info | K8s/Container | Privileged container(s) |
| 106560 | Info | K8s/Container | Container(s) run as root |
| 106561 | Medium | K8s/Container | Container(s) without runAsNonRoot |
| 106562 | Medium | K8s/Container | Privilege escalation allowed |
| 106568 | Medium | K8s/Container | Container(s) with sysadmin capability |
| 106577 | Medium | K8s/Container | Workload without SELinux or AppArmor |
| 106579 | Medium | K8s/Container | Workload without recommended seccomp profile |
| 5046 | High | General/K8s | Image Pull Policy Of The Container Is Not Set To Always |
| 5047 | High | General/K8s | Image Without Digest |
| 5067 | High | General/K8s | Missing AppArmor Profile |
| 5108 | Medium | General/K8s | Seccomp Profile Is Not Configured |

---

## Summary Table

| NIST Control Family | Description | Mapped Policy Count (approx.) |
|---------------------|-------------|-------------------------------|
| 03.01 Access Control | IAM, least privilege, public access | ~120 |
| 03.02 Awareness and Training | Security training programs | 0 (not automatable via CSPM) |
| 03.03 Audit and Accountability | Logging, CloudTrail, CloudWatch alarms | ~115 |
| 03.04 Configuration Management | Baselines, versioning, patch levels | ~28 |
| 03.05 Identification and Authentication | MFA, passwords, credential rotation | ~52 |
| 03.06 Incident Response | GuardDuty, Security Hub, Defender, alerts | ~25 |
| 03.07 Maintenance | Remote maintenance controls | 0 (primarily procedural) |
| 03.08 Media Protection | Encryption at rest, backups, KMS | ~95 |
| 03.09 Personnel Security | Screening, termination | 0 (HR processes, not technical) |
| 03.10 Physical Protection | Physical access | 0 (cloud-managed) |
| 03.11 Risk Assessment | Vulnerability scanning, CVE exposure, sensor coverage | ~20 |
| 03.12 Security Assessment and Monitoring | Continuous monitoring, Config, Security Hub | ~15 |
| 03.13 System and Communications Protection | TLS/SSL, firewalls, VPC, WAF, encryption in transit | ~180 |
| 03.14 System and Information Integrity | Patching, malware, sensor, IMDSv2, container hardening | ~40 |
| 03.15 Planning | SSP, rules of behavior | 0 (documentation controls) |
| 03.16 System and Services Acquisition | Third-party services security | 0 (contractual/process) |
| 03.17 Supply Chain Risk Management | Supply chain controls | ~8 (container image provenance) |
| **Total** | | **~698 directly mapped** |

---

## Notes

- **Not automatable via CSPM:** 03.02 (Awareness/Training), 03.07 (Maintenance procedures), 03.09 (Personnel Security), 03.10 (Physical Protection), 03.15 (Planning/SSP), 03.16 (Acquisition), and most of 03.17 are procedural/organizational controls that cannot be measured by CSPM tooling.
- **Cross-cloud policies** (the unnamed provider group) map primarily to 03.01, 03.11, and 03.14 — they represent graph-based combined-risk scenarios (e.g., publicly exposed + vulnerable + excessive permissions).
- **General/Kubernetes** policies map heavily to 03.01, 03.03, 03.13, and 03.14 — container and cluster hardening domains.
- **ASPM policies** (application-layer) complement 03.11 and 03.14 for code-reachable vulnerability coverage.
- Policy counts reflect distinct policy entries; many policies have duplicate short_codes across categories in the AWS dataset.
