# Phase 3 — Security Scanning Pipeline

A GitHub Actions DevSecOps security pipeline that automates:

- SAST with Bandit
- SCA with Trivy
- DAST with a custom OWASP smoke testing framework
- SARIF report generation
- GitHub Code Scanning uploads
- hard failure gates for HIGH and CRITICAL vulnerabilities

---

## Purpose

This project demonstrates a job-ready DevSecOps security pipeline designed to shift security left in CI/CD.

It builds on earlier portfolio projects by integrating automated security scanning directly into GitHub Actions.

---

## Security Tools

| Category | Tool | Purpose |
|---|---|---|
| SAST | Bandit | Scans Python source code for insecure patterns |
| SCA | Trivy | Scans dependencies and filesystem for vulnerabilities |
| DAST | Custom OWASP Smoke Tester | Runs lightweight application security checks |
| Reporting | SARIF + Artifacts | Uploads security findings to GitHub and workflow artifacts |

---

## Failure Gates

The pipeline is designed to fail when HIGH or CRITICAL vulnerabilities are detected.

Security gates include:

- Bandit HIGH severity findings
- Trivy HIGH/CRITICAL vulnerabilities
- DAST smoke test failures

---

## Project Structure

```text
phase-3-security-scanning-pipeline/
├── .github/
│   └── workflows/
│       └── security-pipeline.yml
├── docs/
├── reports/
├── screenshots/
├── scripts/
├── src/
├── tests/
├── .bandit
├── .gitignore
├── README.md
└── requirements.txt