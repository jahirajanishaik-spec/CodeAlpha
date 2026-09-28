import re

def extract_emails():
    input_filename = "input_text.txt"
    output_filename = "extracted_emails.txt"

    # Creating a sample input file for demonstration purposes
    sample_content = """
    Hello team, please reach out to support@codealpha.tech or admin@codealpha.tech for queries.
    You can also contact john.doe123@gmail.com or Jane_Doe@yahoo.co.uk for further assistance.
    Invalid emails like user@.com or test@domain should be ignored.
    """
    
    with open(input_filename, "w") as f:
        f.write(sample_content)

    print(f"Reading content from {input_filename}...")
    with open(input_filename, "r") as f:
        content = f.read()

    # Regular expression pattern for matching valid email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    # Find all unique email addresses
    found_emails = sorted(list(set(re.findall(email_pattern, content))))

    print(f"Found {len(found_emails)} unique email(s). Saving to {output_filename}...")
    
    with open(output_filename, "w") as f:
        for email in found_emails:
            f.write(email + "\n")

    print("Extraction complete! Extracted emails:")
    for email in found_emails:
        print(f" - {email}")

if __name__ == "__main__":
    extract_emails()