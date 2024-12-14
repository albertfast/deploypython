from fpdf import FPDF


class ResumePDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'AHMET SAHINER', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5,
                  'ahmethasimsahiner@gmail.com | 628.256.8909 | github.com/albertfast | linkedin.com/in/ahmetsahiner',
                  0, 1, 'C')
        self.ln(5)

    def add_section(self, title, content):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 8, title, 0, 1, 'L')
        self.set_font('Arial', '', 8)

        # Substitute symbols to ensure compatibility with PDF display
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

        self.multi_cell(0, 5, content)  # Reducing line height for compact layout
        self.ln(4)  # Small space between sections


# Create the PDF
pdf = ResumePDF()
pdf.add_page()

# Adding sections with content
pdf.add_section("EDUCATION", """City College of San Francisco - Expected Graduation May 2025
Advanced Web Development Techniques / Front-End Web Development Certificate, GPA: 3.67
Relevant Coursework: Programming Fundamentals: Python, Introduction to HTML and CSS, Intermediate HTML and CSS, JavaScript, jQuery, AJAX, Mobile Web Development with HTML, CSS & JS, Computing Talent Initiative - 201: Python Practice.

Soft Innovas Bootcamp - Graduated Nov 2023
Salesforce Administration & Development
Relevant Coursework: Salesforce Fundamentals (User Management, Data Security, Administration, Development), Apex Programming (Apex Triggers, Asynchronous Apex), LWC (Lightning Web Components), HTML, CSS, JavaScript, Data Integration (JSON, REST and SOAP API, MuleSoft), Process Automation (Workflow Rules, Process Builder, Flow), Deployment & CI/CD (Git, Copado), Project Management (Agile methodology, Trello), Sales Cloud, CPQ, Billing Cloud .

Adnan Menderes University - Graduated January 2015
Bachelor’s degree of Finance GPA: 2.16
Relevant Coursework: Microeconomics, Macroeconomics, Public Finance, Monetary Theory, Econometrics, Tax Law, Commercial Law, Accounting, and Research Methods""")

pdf.add_section("SKILLS", """Programming Languages: JavaScript, HTML, CSS, Python, SQL, Bootstrap, ReactJS
Software Tools: VS Code, PyCharm, MuleSoft, Postman, GitHub, REST - SOAP API, Google SEO, Heroku.""")

pdf.add_section("PROGRAMMING PROJECTS", """TOYTOPIA, Mobile Web Development with Bootstrap
Languages and Tools Utilized: JavaScript, HTML, CSS, Bootstrap, Google Maps API, Leaflet, WURFL Capabilities
- Designed a mobile-friendly web app for TOYTOPIA, a toy-focused platform, using Bootstrap for a seamless user experience across devices
- Integrated Google Maps API and Geolocation to display users’ current location on an interactive map
- Created collapsible product listings and a contact form for enhanced user engagement
- Leveraged WURFL Capabilities to detect user device information and optimize content accordingly


Art and Logic Programming Challenge: Encoder / Decoder App
Languages and Tools Utilized: Python, JavaScript, HTML, CSS , Pycharm, VScode
Developed an encoding/decoding application to handle data in proprietary bit manipulation formats, using both Python and JavaScript
- Part 1 (Python): Built an encoder to transform 4-character blocks into 32-bit scrambled integer values using a custom bit-mapping algorithm.
- Part 2 (JavaScript): Expanded functionality to process strings of any length by encoding them as lists of integers and decoding these values back to text.
- Integrated a user-friendly interface for encoding and decoding strings, with buttons for direct interaction and clear field updates. Applied best practices in code structure and modularity, making the app reusable as a library.


Donor Management Application (Internship Project):
Languages and Tools Utilized: Apex, HTML, CSS, JS, LWC
- Payment Integration: Successfully integrated the Give Lively payment system to facilitate secure and efficient online donations.
- Automation: Implemented automated donation tracking workflows, ensuring real-time updates for donor contributions and acknowledgments.
- Enhanced User Experience: Improved the system's user interface for seamless navigation, simplifying data entry and tracking for organization staff.
- Reporting & Analytics: Developed dashboards and custom reports to provide insights into donation trends, donor demographics, and financial performance.
- Social Impact: Supported the organization’s mission by increasing transparency and efficiency in managing donor relationships and fostering stronger community engagement.

Leasing Management Application:
Language Utilized: Languages and Tools Utilized: Apex, HTML, CSS, JS, LWC
- Custom REST API Integration: Enabled seamless data exchange and third-party integrations.
- Role-Based Access Controls: Implemented secure access tailored to agents, clients, and managers.
- Data Encryption & Validation: Ensured compliance and data integrity with encrypted data fields and robust validation.
- Automation: Streamlined workflows, reducing manual tasks in property and lease management.
- Reporting & Analytics: Provided actionable insights with real-time dashboards and customized reports.
""")

pdf.add_section("WORK EXPERIENCE", """Salesforce Development Intern
August 2023 – November 2023
- Developed a donation management system using Apex and integrated JSON data.
Enhanced data processing time by 20% and reduced user input errors.

Engine Cadet
Various Shipping Companies – Istanbul, Turkey
September 2018 – June 2019
- Conducted routine maintenance on vessels, demonstrating technical and problem-solving skills.""")

pdf.add_section("HONORS & AWARDS", """Bootcamp Excellence Award (Soft Innovas, 2023)
- Awarded for leadership and excellence in developing the Donor Management Application, a Salesforce-based system that streamlined donation tracking and enhanced user experience for a non-profit organization.""")

# Saving the PDF
pdf_output_path = "single_page_resume.pdf"
pdf.output(pdf_output_path)

print(f"PDF successfully saved to {pdf_output_path}")
