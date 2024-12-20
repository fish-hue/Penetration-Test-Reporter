# Penetration-Testing-Report Generator

## Overview

The Penetration-Testing-Report Generator is a Python script designed to help security professionals easily create comprehensive reports following penetration testing engagements. The script prompts the user for essential information such as findings, risk ratings, recommendations, and general details about the test and organization.

## Features

- **Input Validation**: Ensures that the user inputs valid data, such as dates and risk ratings.
- **User-Friendly Interface**: Step-by-step prompts make it easy to gather essential information for the report.
- **Output Format**: Generates a text file containing the collected information formatted in a clear and structured manner.
- **Sanitization**: Removes invalid characters from filenames to ensure compatibility with different file systems.

## Requirements

- Python 3.x
- Standard libraries: `re`, `time`, `datetime`

## Installation

1. **Clone the Repository** (or download the script):
   ```bash
   git clone https://github.com/fish-hue/Penetration-Test-Reporter.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd penetration-testing-report-generator
   ```

3. **Run the Script**:
   ```bash
   python ptr.py
   ```

## Usage

1. Run the script in your terminal or command prompt.
2. Follow the step-by-step prompts to input the required information:
   - Enter the title of the report.
   - Provide the date of the test.
   - Enter the organization's name and contact information.
   - Input your confidentiality statement, executive summary, introduction, methodology, and scope.
   - For each finding, enter the details and risk rating.
   - Add recommendations.
   - Finally, provide a conclusion for your report.

3. Upon completing the prompts, a text file will be generated in the current working directory, named:
   ```
   {title}_{date}_{timestamp}.txt
   ```

## Example

```
=== Penetration Testing Report Generator ===
Enter the report title: My First Pen Test Report
Enter the date of the test (e.g., YYYY-MM-DD): 2023-10-01
Enter the organization/client name: Example Corp
...
```
