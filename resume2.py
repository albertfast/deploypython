from fpdf import FPDF


class ResumePDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)  # Slightly smaller font for header
        self.cell(0, 10, 'Resume', 0, 1, 'C')
        self.ln(3)  # Less space after the header

    def add_section(self, title, content):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 8, title, 0, 1, 'L')
        self.set_font('Arial', '', 8)
        # Replace problematic characters with simpler alternatives
        substitutions = {
            '•': '-',
            '’': "'",
            '“': '"',
            '”': '"',
            '–': '-',  # EN DASH
            '—': '-',  # EM DASH
            '…': '...',  # Ellipsis
            '→': '->'  # Arrow
        }
        for old, new in substitutions.items():
            content = content.replace(old, new)
        self.multi_cell(0, 4, content)  # Reduced line height

    def add_columns_section(self, title, content_list):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 8, title, 0, 1, 'L')
        self.set_font('Arial', '', 8)
        col_width = self.w / 2.5  # Approximate column width
        row_height = 4
        y_start = self.get_y()

        # Replace problematic characters with simpler alternatives
        substitutions = {
            '•': '-',
            '’': "'",
            '“': '"',
            '”': '"',
            '–': '-',  # EN DASH
            '—': '-',  # EM DASH
            '…': '...',  # Ellipsis
            '→': '->'  # Arrow
        }

        for i, row in enumerate(content_list):
            if i % 2 == 0 and i > 0:  # Move to the next line after two columns
                self.set_y(y_start + (i // 2) * row_height * 8)
            col_x = self.l_margin + (i % 2) * col_width
            self.set_x(col_x)
            for item in row:
                item_sanitized = item
                for old, new in substitutions.items():
                    item_sanitized = item_sanitized.replace(old, new)
                self.multi_cell(col_width, row_height, item_sanitized, border=0, align='L')


# Creating the PDF
pdf = ResumePDF()
pdf.add_page()

# Reducing margins for compact layout
pdf.set_left_margin(8)
pdf.set_right_margin(8)

# Adding content
pdf.add_section("EDUCATION", """City College of San Francisco - Expected Graduation May 2025
Advanced Web Development Techniques / Front-End Web Development Certificate
GPA: 3.67
Relevant Coursework: Programming Fundamentals: Python, Introduction to HTML and CSS, Intermediate HTML and CSS, JavaScript, jQuery, AJAX, Mobile Web w/HTML, CSS & JS, Computing Talent Initiative - 201: Python Practice

Soft Innovas Bootcamp - Graduated Nov 2023
Salesforce Administration & Development
Relevant Coursework: Salesforce Fundamentals, Apex Programming, LWC, HTML, CSS, JavaScript, Data Integration, Process Automation, Deployment & CI/CD, Project Management, Sales Cloud, CPQ, Billing Cloud""")

pdf.add_section("SKILLS", """Programming Languages: JavaScript, HTML, CSS, Python, JSON, SQL, Bootstrap, ReactJS
Software Tools: VS Code, PyCharm, MuleSoft, Postman, Salesforce Data Loader, GitHub, REST API, JSON, Google SEO, Heroku.""")

programming_projects = [
    [
        "TOYTOPIA, Mobile Web Development with Bootstrap",
        """Languages and Tools Utilized: JavaScript, HTML, CSS, Bootstrap, Google Maps API, Leaflet, WURFL Capabilities
        - Designed a mobile-friendly web app for TOYTOPIA, a toy-focused platform, using Bootstrap for a seamless user experience across devices
        - Integrated Google Maps API and Geolocation to display users’ current location on an interactive map
        - Created collapsible product listings and a contact form for enhanced user engagement
        - Leveraged WURFL Capabilities to detect user device information and optimize content accordingly"""
    ],
    [
        "Art and Logic Programming Challenge: Encoder / Decoder App",
        """Languages and Tools Utilized: Python, JavaScript, HTML, CSS
        Developed an encoding/decoding application to handle data in proprietary bit manipulation formats.
        - Part 1 (Python): Built an encoder to transform 4-character blocks into 32-bit scrambled integer values.
        - Part 2 (JavaScript): Expanded functionality to process strings of any length by encoding as lists of integers and decoding back to text.
        - Integrated a user-friendly interface for encoding/decoding with interactive buttons and field updates."""
    ],
    [
        "Donor Management Application (Internship Project)",
        """Languages and Tools Utilized: Apex, HTML, CSS, JS, LWC
        Payment Integration: Integrated the Give Lively payment system for online donations.
        Automation: Implemented automated donation tracking workflows with real-time updates.
        User Experience: Improved navigation for staff with an enhanced user interface.
        Reporting & Analytics: Developed dashboards for insights into donation trends and financial performance.
        Social Impact: Supported the organization’s mission by improving donor management transparency."""
    ],
    [
        "Leasing Management Application",
        """Languages and Tools Utilized: Apex, HTML, CSS, JS, LWC
        Custom REST API Integration, Role-Based Access Controls, Data Encryption & Validation, Workflow Automation, Reporting & Analytics."""
    ]
]

pdf.add_columns_section("PROGRAMMING PROJECTS", programming_projects)

pdf.add_section("WORK EXPERIENCE", """Salesforce Development Intern
Developed a donation management system using Apex and integrated JSON data.
Enhanced data processing time by 20% and reduced user input errors.    August 2023 – November 2023    

Engine Cadet           
Various Shipping Companies – Istanbul, Turkey
September 2018 – June 2019

Conducted routine maintenance on vessels, showcasing strong technical and problem-solving skills.""")

pdf.add_section("HONORS & AWARDS",
                """Bootcamp Excellence Award (Soft Innovas, 2022) – Awarded for leadership and excellence in developing the Donor Management Application, a Salesforce-based system that streamlined donation tracking and enhanced user experience for a non-profit organization.""")

# Saving the PDF
pdf_output_path = "myresume.pdf"
pdf.output(pdf_output_path)

print(f"PDF successfully saved to {pdf_output_path}")
