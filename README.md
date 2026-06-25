# Playwright SauceDemo Test Suite

## Overview

This project is a UI test automation framework built with Playwright and Pytest.

The application under test is SauceDemo, a sample e-commerce website commonly used for automation practice.

The purpose of this project is to demonstrate:

* UI test automation with Playwright
* Page Object Model (POM)
* Pytest fixtures
* Test organization and maintainability
* Automation framework design principles
* Environment variable management
* GitHub Actions CI integration

---

## Tech Stack

* Python
* Playwright
* Pytest
* GitHub Actions
* pytest-html
* JUnit XML Reporting

---

## Features

* UI test automation with Playwright and Pytest
* Page Object Model (POM)
* Environment variable configuration
* Test categorization using Pytest markers
* HTML test reports
* JUnit XML reports
* GitHub Actions Continuous Integration
* CI artifact publishing
* Maintainable test structure and reusable page objects

---

## Test Coverage

### Login

* Valid login
* Invalid login
* Input field validation
* Error handling verification

---

## Test Categorization

Tests are organized using Pytest markers.

Current markers include:

* `smoke` → Critical happy-path scenarios
* `negative` → Negative and error-handling scenarios

Examples:

Run smoke tests only:

```bash
pytest -m smoke
```

Run negative tests only:

```bash
pytest -m negative
```

Run smoke tests excluding negative scenarios:

```bash
pytest -m "smoke and not negative"
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
.\venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Environment Variables

This project uses environment variables for credentials management.

The test suite expects the following variables:

| Variable                | Value         |
| ----------------------- | ------------- |
| SAUCE_STANDARD_USERNAME | standard_user |
| SAUCE_PASSWORD          | secret_sauce  |

### Local Execution

Windows PowerShell:

```powershell
$env:SAUCE_STANDARD_USERNAME="standard_user"
$env:SAUCE_PASSWORD="secret_sauce"
```

Linux / macOS:

```bash
export SAUCE_STANDARD_USERNAME="standard_user"
export SAUCE_PASSWORD="secret_sauce"
```

Verify the variables are available:

```bash
python -c "import os; print(os.getenv('SAUCE_STANDARD_USERNAME'))"
```

> Although SauceDemo credentials are publicly available, environment variables and GitHub Secrets are used to demonstrate configuration management practices commonly applied in real-world automation frameworks.

---

## Running Tests

Run all tests:

```bash
pytest
```

Run smoke tests:

```bash
pytest -m smoke
```

Run negative tests:

```bash
pytest -m negative
```

Run smoke tests excluding negative scenarios:

```bash
pytest -v -m "smoke and not negative"
```

Run a specific file:

```bash
pytest tests/test_login.py
```

Run tests in headed mode:

```bash
pytest --headed
```

---

## Reports

### HTML Report

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

### JUnit XML Report

Generate a JUnit XML report:

```bash
pytest --junitxml=reports/results.xml
```

These reports can be consumed locally or by CI/CD pipelines for test result analysis.

---

## CI/CD

This project includes a GitHub Actions workflow that automatically:

* Creates the execution environment
* Installs project dependencies
* Installs Playwright browsers
* Executes the smoke test suite
* Generates HTML and JUnit XML reports
* Uploads reports as workflow artifacts

### CI Execution Strategy

The CI pipeline executes:

```bash
pytest -v -m "smoke and not negative"
```

This approach ensures that:

* Critical user journeys are continuously validated
* Fast feedback is provided on every execution
* Negative scenarios remain available for dedicated validation runs

### Artifacts

After every workflow execution, GitHub Actions publishes:

* HTML Test Report
* JUnit XML Report

These artifacts can be downloaded directly from the workflow run page for result analysis.

### GitHub Secrets

The workflow consumes the following repository secrets:

| Secret Name             | Value         |
| ----------------------- | ------------- |
| SAUCE_STANDARD_USERNAME | standard_user |
| SAUCE_PASSWORD          | secret_sauce  |

To configure them:

1. Open the repository on GitHub.
2. Navigate to **Settings** → **Secrets and variables** → **Actions**.
3. Create the required secrets.
4. Save the values.

---

## Design Decisions

This framework follows the Page Object Model pattern.

### Page Objects

Page Objects contain:

* Locators
* UI interactions
* Reusable page actions

Assertions remain in the test layer to maintain a clear separation of responsibilities.

### Configuration Management

Environment variables are used for configuration management, keeping credentials outside the codebase and enabling seamless integration with CI/CD pipelines.

### CI Strategy

The pipeline executes only smoke scenarios by default to provide fast and reliable feedback while keeping broader test coverage available for future pipeline stages.

---

## Future Improvements

* Screenshots on failure
* Trace collection
* Additional functional coverage
* Test data management
* Cart, Products and Checkout tests coverague
