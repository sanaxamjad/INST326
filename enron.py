import re
import argparse

import re

class Email:
    def __init__(self, raw_email):
        self.raw_email = raw_email
        self.headers = {}
        self.body = ''
        self.parse_email()

    def parse_email(self):
        # Use regex to parse the raw email and populate the headers and body attributes
        header_pattern = re.compile(r'([^:\s]+):\s*(.*)')
        body_pattern = re.compile(r'\r\n\r\n(.*)', re.DOTALL)

        # Split the raw email into header and body
        header_end = self.raw_email.find('\r\n\r\n')
        header_str = self.raw_email[:header_end]
        body_str = self.raw_email[header_end+4:]

        # Parse the headers
        for match in header_pattern.finditer(header_str):
            self.headers[match.group(1)] = match.group(2)

        # Parse the body
        body_match = body_pattern.search(body_str)
        if body_match:
            self.body = body_match.group(1)

class Server:
    def __init__(self, path):
        self.emails = []
        self.parse_emails(path)

    def parse_emails(self, path):
        with open(path, 'r') as f:
            raw_email = ''
            for line in f:
                raw_email += line
                if line.strip() == '':
                    email = Email(raw_email)
                    self.emails.append(email)
                    raw_email = ''
            if raw_email:
                email = Email(raw_email)
                self.emails.append(email)

def main():
    # Parse command line arguments
    args = parse_args()

    # Create a Server object and parse emails
    server = Server(args.path)

    # Do further analysis on emails
    for email in server.emails:
        # print the raw email
        print(email.raw_email)
        # access the email headers
        print(email.headers)
        # access the email body
        print(email.body)

def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to emails file')
    return parser.parse_args()

if __name__ == '__main__':
    main()