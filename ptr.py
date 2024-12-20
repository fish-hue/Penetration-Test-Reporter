import re
import time
from datetime import datetime

# Function to validate date format (YYYY-MM-DD)
def validate_date(date_str):
    return re.match(r"\d{4}-\d{2}-\d{2}", date_str) is not None

# Function to validate risk rating
def validate_risk_rating(risk_rating):
    valid_ratings = {'critical', 'high', 'medium', 'low'}
    return risk_rating.lower() in valid_ratings

# Function to sanitize file names (to handle invalid characters)
def sanitize_filename(file_name):
    return re.sub(r'[<>:"/\\|?*]', '_', file_name)

# Function to gather user input for the report
def gather_report_info():
    report_info = {}

    print("=== Penetration Testing Report Generator ===")

    # Gather general information with validation
    report_info['title'] = input("Enter the report title: ")
    while not report_info['title']:
        print("Title is required.")
        report_info['title'] = input("Enter the report title: ")

    report_info['date'] = input("Enter the date of the test (e.g., YYYY-MM-DD): ")
    while not report_info['date'] or not validate_date(report_info['date']):
        print("Valid date is required in YYYY-MM-DD format.")
        report_info['date'] = input("Enter the date of the test (e.g., YYYY-MM-DD): ")

    report_info['organization'] = input("Enter the organization/client name: ")
    while not report_info['organization']:
        print("Organization is required.")
        report_info['organization'] = input("Enter the organization/client name: ")

    report_info['contact_info'] = input("Enter contact information of the testing team: ")
    report_info['confidentiality'] = input("Enter confidentiality statement: ")

    # Gather executive summary
    report_info['executive_summary'] = input("Enter executive summary: ")
    while not report_info['executive_summary']:
        print("Executive summary is required.")
        report_info['executive_summary'] = input("Enter executive summary: ")

    # Gather introduction
    report_info['introduction'] = input("Enter introduction details: ")
    while not report_info['introduction']:
        print("Introduction details are required.")
        report_info['introduction'] = input("Enter introduction details: ")

    # Gather methodology information
    report_info['methodology'] = input("Describe the methodology used: ")
    while not report_info['methodology']:
        print("Methodology description is required.")
        report_info['methodology'] = input("Describe the methodology used: ")

    # Gather scope of testing
    report_info['scope'] = input("Define the scope of testing: ")
    while not report_info['scope']:
        print("Scope of testing is required.")
        report_info['scope'] = input("Define the scope of testing: ")

    # Gather findings
    findings = []
    while True:
        finding = input("Enter a finding (or type 'done' to finish): ")
        if finding.lower() == 'done':
            break
        risk_rating = input("Enter risk rating (e.g., critical, high, medium, low): ")
        while not validate_risk_rating(risk_rating):
            print("Valid risk rating is required: critical, high, medium, low.")
            risk_rating = input("Enter risk rating (e.g., critical, high, medium, low): ")
        evidence = input("Enter evidence for this finding: ")
        findings.append({
            'finding': finding,
            'risk_rating': risk_rating,
            'evidence': evidence
        })

    if not findings:
        print("At least one finding is required.")
        return None

    report_info['findings'] = findings

    # Gather recommendations
    recommendations = []
    while True:
        recommendation = input("Enter a recommendation (or type 'done' to finish): ").strip()
        if recommendation.lower() == 'done':
            break
        if recommendation:  # Only add if the recommendation is not just empty
            recommendations.append(recommendation)

    if not recommendations:
        print("At least one recommendation is required.")
        return None

    report_info['recommendations'] = recommendations

    # Gather conclusion
    report_info['conclusion'] = input("Enter a conclusion: ")
    while not report_info['conclusion']:
        print("Conclusion is required.")
        report_info['conclusion'] = input("Enter a conclusion: ")

    return report_info

# Function to create a report file from the gathered information
def create_report_file(report_info):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{sanitize_filename(report_info['title'])}_{report_info['date']}_{timestamp}.txt"

    try:
        with open(file_name, 'w') as file:
            file.write(f"Title: {report_info['title']}\n")
            file.write(f"Date: {report_info['date']}\n")
            file.write(f"Organization: {report_info['organization']}\n")
            file.write(f"Contact Info: {report_info['contact_info']}\n")
            file.write(f"Confidentiality Statement: {report_info['confidentiality']}\n\n")

            file.write("=== Executive Summary ===\n")
            file.write(report_info['executive_summary'] + "\n\n")

            file.write("=== Introduction ===\n")
            file.write(report_info['introduction'] + "\n\n")

            file.write("=== Methodology ===\n")
            file.write(report_info['methodology'] + "\n\n")

            file.write("=== Scope of Testing ===\n")
            file.write(report_info['scope'] + "\n\n")

            file.write("=== Findings ===\n")
            for finding in report_info['findings']:
                file.write(f"Finding: {finding['finding']}\n")
                file.write(f"Risk Rating: {finding['risk_rating']}\n")
                file.write(f"Evidence: {finding['evidence']}\n\n")

            file.write("=== Recommendations ===\n")
            for recommendation in report_info['recommendations']:
                file.write(f"- {recommendation}\n")
            file.write("\n")

            file.write("=== Conclusion ===\n")
            file.write(report_info['conclusion'] + "\n")

        print(f"Report successfully generated and saved as {file_name} in the current directory.")
    except IOError as e:
        print(f"An error occurred while writing the report file: {e}")

def main():
    report_info = gather_report_info()
    if report_info:
        create_report_file(report_info)

if __name__ == "__main__":
    main()
