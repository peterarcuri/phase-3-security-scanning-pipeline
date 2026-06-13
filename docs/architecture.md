# Security Scanning Pipeline Architecture

## Overview

This project demonstrates a multi-stage DevSecOps security pipeline implemented with GitHub Actions. The pipeline automates Static Application Security Testing (SAST), Software Composition Analysis (SCA), and Dynamic Application Security Testing (DAST) to identify security issues early in the software development lifecycle.

The primary objective is to enforce a **shift-left security** approach by integrating automated security validation into every code change before deployment.

---

# High-Level Architecture

```text
Developer Push / Pull Request
                │
                ▼
      GitHub Actions Workflow
                │
                ▼
    ┌─────────────────────────┐
    │ Install Dependencies    │
    └─────────────────────────┘
                │
                ▼
    ┌─────────────────────────┐
    │ SAST - Bandit           │
    │ Python Source Analysis  │
    └─────────────────────────┘
                │
                ▼
    ┌─────────────────────────┐
    │ SCA - Trivy             │
    │ Dependency/File Scan    │
    └─────────────────────────┘
                │
                ▼
    ┌─────────────────────────┐
    │ DAST - OWASP Smoke      │
    │ Testing Framework       │
    └─────────────────────────┘
                │
                ▼
    ┌─────────────────────────┐
    │ SARIF & Report Uploads  │
    └─────────────────────────┘
                │
                ▼
     Build Pass / Build Fail
```

---

# Pipeline Components

## Static Application Security Testing (SAST)

Bandit analyzes the Python source code for common security issues, including:

* insecure function usage
* hardcoded credentials
* weak cryptography
* command injection risks
* unsafe deserialization
* insecure file operations

Build failures can be configured based on severity thresholds.

---

## Software Composition Analysis (SCA)

Trivy scans the repository and installed dependencies for known vulnerabilities.

The scan focuses on:

* vulnerable packages
* outdated dependencies
* filesystem issues
* security advisories
* HIGH and CRITICAL CVEs

The pipeline enforces failure gates when unacceptable risk levels are detected.

---

## Dynamic Application Security Testing (DAST)

The project integrates a custom OWASP Smoke Testing Framework developed earlier in the DevSecOps portfolio.

The framework performs lightweight runtime security validation, including checks for:

* SQL injection indicators
* SSRF behavior
* CORS misconfigurations
* missing HTTP security headers

This demonstrates how internally developed security tooling can be incorporated into automated CI/CD workflows.

---

# Security Reporting

Security findings are exported as artifacts for later review.

Generated reports may include:

* Bandit results
* Trivy results
* SARIF output
* DAST execution logs

These artifacts provide traceability and support security auditing.

---

# Failure Gates

The pipeline is designed to stop insecure code from progressing through CI.

Builds may fail when:

* HIGH or CRITICAL vulnerabilities are identified
* configured security thresholds are exceeded
* required security checks do not complete successfully

---

# DevSecOps Concepts Demonstrated

* Shift-left security
* Automated security validation
* CI/CD pipeline security
* SAST integration
* SCA integration
* DAST integration
* Security report generation
* Vulnerability-based quality gates
* GitHub Actions automation
* Secure software development lifecycle (SSDLC)
