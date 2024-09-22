## GitHub Action Workflow: Simple CI Pipeline
```Simple Continuous Integration (CI)``` Pipeline using ```GitHub Actions```. The Python application performs basic addition and subtraction operations, with automated tests running through the CI pipeline every time code is pushed or a pull request is made.

### Features
- Adds two numbers
- Subtracts one number from another

### GitHub Actions CI Workflow

This repository is set up with GitHub Actions for continuous integration. Every push and pull request triggers an automated workflow to test the code, ensuring that it functions as expected.

The workflow is defined in ```.github/workflows/python-app.yml``` and performs the following steps:

- ```Checkout code:``` Retrieve the latest code from the repository.
-   ```Set up Python:``` Configure the environment to use Python 3.10
-   ```Install dependencies:``` Install required packages using pip.
-   ```Run tests:``` Execute Python unit tests.