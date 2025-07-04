## 🛡️ DevSecOps CI/CD Pipeline

This repository demonstrates a secure and automated CI/CD pipeline using GitHub Actions, with integrated security scanning tools to enhance code and image integrity before deployment.

## 🔧 Tools & Stack

- **Docker** – Containerization and image distribution
- **Trivy** – Scanning for vulnerabilities in files and Docker images
- **Gitleaks** – Scanning for hardcoded secrets and credentials
- **SonarQube** - Improve code quality and catch problems before deploying
- **GitHub Actions** – CI/CD automation

---

## Struktur :

```
my-devsecops/
├── .github/
│   └── workflows/
│       └── ci-cd-devsecops.yml        # GitHub Actions pipeline untuk CI/CD + security scan (Gitleaks dan Trivy)
|       └── ci-sonarqube-pipeline.yml  # Github Actions pipeline untuk CI/CD + SonarQube
├── app/
│   └── main.py                        # Source code aplikasi utama
├── Dockerfile                         # Instruksi build Docker image
├── requirements.txt                   # Daftar dependency Python (jika ada)
├── .gitleaks.toml                     # Konfigurasi rule untuk Gitleaks
├── trivy-ignore.yaml                  # Daftar CVE yang di-ignore oleh Trivy
├── sonar-project.properties           # File konfigurasi untuk SonarQube
└── README.md                          # Dokumentasi project
```
---

## 🧪 How to Run Locally
```bash

# Build the Docker image
docker build -t my-devsecops .

# Run the container (adjust port if needed)
docker run -p 5100:5100 my-devsecops

---  Thank You  ---
