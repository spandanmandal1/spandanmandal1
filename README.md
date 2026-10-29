## Hi, I'm Spandan

DevOps Engineer in Kolkata, India, with 2+ years running production workloads on AWS EKS.

Open to DevOps, Platform and SRE roles · available to join immediately.

**At Questalious (2024–2026)** I built the Terraform modules behind our dev, staging and prod environments,
cut deployment time from 30 to 10 minutes by parallelising GitHub Actions, ran the DevSecOps checks on every
service, and set up Prometheus and Grafana monitoring for 8 microservices that I was on call for.

**Now** I'm building observability and self-hosted LLM tooling on Kubernetes.

### Projects

**[alert-triage-bot](https://gitlab.com/spandanmandal/alert-triage-bot)** · Python, FastAPI, Prometheus, Alertmanager, Loki, Ollama, Helm

When an alert fires, the bot pulls the matching error logs from Loki, asks a self-hosted LLM for a likely
cause, and posts both to Slack, 7–9 s after the alert arrives. Handles retries, flapping alerts and a dead LLM
without losing the alert. Developed on GitLab, mirrored [here](https://github.com/spandanmandal1/alert-triage-bot).

**[ecommerce-eks-gitops](https://github.com/spandanmandal1/ecommerce-eks-gitops)** · AWS EKS, Terraform, Argo CD, GitHub Actions, Trivy

A 19-service e-commerce app on EKS behind an ALB. Terraform for the VPC and cluster, Argo CD for GitOps
deploys, Prometheus, Grafana and Loki for observability, and a Trivy gate in CI that caught and blocked
2 critical CVEs.

### Stack

- **Cloud & IaC:** AWS (EKS, EC2, VPC, IAM, S3, RDS, Route 53, CloudWatch), Terraform, Ansible
- **Containers & CI/CD:** Docker, Kubernetes, Helm, Argo CD, GitHub Actions, Jenkins
- **Security in CI:** Trivy, SonarQube, Gitleaks, OWASP Dependency-Check, OWASP ZAP
- **Observability:** Prometheus, Grafana, Loki, Alertmanager, ELK Stack, OpenTelemetry
- **Scripting & OS:** Bash, Python, Linux

### Elsewhere

[LinkedIn](https://www.linkedin.com/in/spandanmandal) · [GitLab](https://gitlab.com/spandanmandal)
