# Orange_Automation
Run automation
In this series, we are implementing Page Object Modeling (POM), which helps organize our automation scripts to be clear and comprehensible.

In the script below, we automated the 
We used Python with Selenium and Pytest for test execution and HTML to generate reports.
1. Login page
2. Add yml file for GitHub action(whenever you push your automation from your local system it will trigger the GitHub action, when the test fails it means something is wrong. then you have to debug your code)


   ** STEP TO SETUP A GITHUB ACTION**

   Setting up GitHub Actions involves creating workflows that automate various tasks in your repository. Here’s a step-by-step guide to get you started:

### Step 1: Create or Navigate to Your Repository
1. Go to GitHub and navigate to the repository where you want to set up GitHub Actions.
2. If you don’t have a repository yet, create a new one by clicking the "New" button on your GitHub dashboard and following the prompts.

### Step 2: Create a Workflow File
1. In your repository, click on the "Actions" tab.
2. GitHub will suggest some workflows based on your project type. You can choose one of the suggestions or set up a workflow yourself.

### Step 3: Set Up a Basic Workflow
1. Click on "Set up a workflow yourself" or select one of the suggested workflows to start with a template.
2. This will create a `.yml` file in the `.github/workflows/` directory of your repository.

### Step 4: Define the Workflow
Edit the `.yml` file to define your workflow. Here’s an example of a simple CI (Continuous Integration) workflow for a Node.js project:

```yaml
name: Node.js CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '14'
          
      - name: Install dependencies
        run: npm install
        
      - name: Run tests
        run: npm test
```

### Step 5: Commit and Push the Workflow File
1. After editing the `.yml` file, commit your changes.
2. Push the commit to your GitHub repository.

### Step 6: Verify the Workflow
1. Go to the "Actions" tab in your repository.
2. You should see your workflow running or completed based on the triggers defined (e.g., push to the main branch).

### Example: More Complex Workflow
Here’s an example of a more complex workflow that includes building, testing, and deploying a Python application:

```yaml
name: Python Application

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
          
      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
          
      - name: Run tests
        run: |
          source venv/bin/activate
          pytest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
          
      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
          
      - name: Deploy to Production
        run: |
          source venv/bin/activate
          ./deploy.sh
```

### Tips and Best Practices
- **Use Secrets:** For sensitive data like API keys, use GitHub Secrets to store and access them securely.
- **Reusable Workflows:** If you have common workflows, consider using reusable workflows to keep your code DRY (Don’t Repeat Yourself).
- **Test Locally:** Test your scripts and commands locally before adding them to your workflow to ensure they work as expected.

By following these steps and examples, you can set up GitHub Actions to automate various tasks in your project, improving efficiency and ensuring consistency across your development workflow.
