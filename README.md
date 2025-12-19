# GreetBot CLI

[![CI - Test and Lint](https://github.com/abhishekverma4676/greetbot-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR-USERNAME/greetbot-cli/actions/workflows/ci.yml)
[![CD - Build and Simulate Deployment](https://github.com/abhishekverma4676/greetbot-cli/actions/workflows/cd.yml/badge.svg)](https://github.com/YOUR-USERNAME/greetbot-cli/actions/workflows/cd.yml)

A simple CLI greeting tool built as an end-to-end DevOps/Cloud learning project. Demonstrates professional Git workflows, CI/CD pipelines, and industry best practices.

## 🚀 Features

- Simple command-line interface with `--name` argument
- Unit tested with pytest (100% coverage of core function)
- Automated CI/CD using GitHub Actions
- Cross-platform testing (Linux, macOS, Windows)
- Package building and artifact management
- Simulated deployment pipeline with environments

## 📁 Project Structure
greetbot-cli/
├── .github/workflows/
│ ├── ci.yml # CI pipeline: test matrix + linting
│ └── cd.yml # CD pipeline: build + deploy simulation
├── greetbot.py # Main CLI application
├── test_greetbot.py # Unit tests
├── requirements.txt # Python dependencies
├── setup.py # Packaging configuration
└── README.md # This file


## 🔧 Installation

```bash
# Install from local source
pip install -e .

# Run the tool
greetbot --name "Your Name"
```
## CI/CD Pipeline Overview
Continuous Integration (CI)
Trigger: On every push and pull request to main

Jobs:

Test Matrix: Runs pytest across Python 3.9, 3.10, 3.11

Linting: Code formatting validation with Black

Features: Dependency caching, job dependencies, failure handling

Continuous Delivery (CD)
Trigger: Manual or on version tags (v*)

Jobs:

Build & Test: Package building, version extraction

Simulate Deployment: Artifact handling, secret management, environment deployment

Features: Artifact upload/download, GitHub Environments, secrets handling

## 🛠 Development Workflow
This project demonstrates industry Git workflow:

Issue Tracking: All features start as GitHub Issues

Branching: issue-<number>-<description> naming convention

Pull Requests: Code review with automated checks

Merge: Squash or merge commits with issue closing

CI/CD: Automated testing and deployment simulation

## 📈 GitHub Features Utilized
GitHub Issues: Feature tracking with acceptance criteria

GitHub Actions: CI/CD pipelines with matrix builds

GitHub Secrets: Secure credential management

GitHub Environments: Staging deployment target

GitHub Artifacts: Build output storage

Branch Protection: (Recommended) Require CI passing before merge

## 🤝 Contributing
Create an issue describing the proposed change

Fork the repository and create a feature branch

Implement changes with tests

Ensure CI passes

Submit a pull request referencing the issue
