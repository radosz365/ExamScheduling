# MkDocs CI Workflow

## Overview

This document explains how the MkDocs documentation is automatically built and deployed using a Continuous Integration (CI) workflow. The CI pipeline ensures that any updates to the documentation in the repository are reflected in the live documentation site.

---

## Workflow Description

The CI pipeline for MkDocs is configured to:
1. Automatically trigger on specific events, such as commits to the `main` branch or pull requests.
2. Build the MkDocs site to validate that the documentation compiles correctly.
3. Deploy the generated site to GitHub Pages for public access.

---

## Workflow File

The workflow file is located at `.github/workflows/mkdocs.yml` in the repository. Below is an overview of its configuration:

### Triggers

The workflow is triggered by:
- Pushes to the `main` branch.
- Manual workflow dispatch.

### Steps

1. **Setup Environment**: 
   - Use the official Python image to set up the environment.
   - Install the required dependencies listed in `requirements.txt`.

2. **Build Documentation**:
   - Run the MkDocs build command to compile the documentation.
   - Validate that there are no errors or missing files.

3. **Deploy to GitHub Pages**:
   - Use the `peaceiris/actions-gh-pages` GitHub Action to deploy the built site to the `gh-pages` branch.

---

## Example Workflow File

Here is an example of a GitHub Actions workflow configuration for MkDocs:

```yaml
name: MkDocs CI

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.9

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Build MkDocs Site
        run: |
          mkdocs build --strict

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site

