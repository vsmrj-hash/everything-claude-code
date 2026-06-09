"""
Generate professional, sell-ready resume/CV templates for 7 regions.
Each template follows the exact hiring conventions of its target market.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os
import copy

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ─── helpers ──────────────────────────────────────────────────────────────────

def set_font(run, name, size, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_para(doc, text="", style=None, align=WD_ALIGN_PARAGRAPH.LEFT,
             space_before=0, space_after=0):
    p = doc.add_paragraph(text, style=style)
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    return p


def add_rule(doc, color=(0, 0, 0)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '%02X%02X%02X' % color)
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p


def section_heading(doc, title, font_name='Calibri', font_size=12,
                    bold=True, color=(31, 73, 125), upper=True,
                    space_before=10, space_after=2, rule=True, rule_color=(31, 73, 125)):
    text = title.upper() if upper else title
    p = add_para(doc, space_before=space_before, space_after=space_after)
    run = p.add_run(text)
    set_font(run, font_name, font_size, bold=bold, color=color)
    if rule:
        add_rule(doc, rule_color)
    return p


def bullet_para(doc, text, indent=0.3, font_name='Calibri', font_size=10.5):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(indent)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    set_font(run, font_name, font_size)
    return p


def set_page_margins(doc, top=1.0, bottom=1.0, left=1.0, right=1.0):
    section = doc.sections[0]
    section.top_margin = Inches(top)
    section.bottom_margin = Inches(bottom)
    section.left_margin = Inches(left)
    section.right_margin = Inches(right)


def set_page_size_a4(doc):
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)


def shade_table_cell(cell, hex_color='1F497D'):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)


def remove_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'none')
        tblBorders.append(border)
    tblPr.append(tblBorders)


# ─── 1. USA Resume ────────────────────────────────────────────────────────────

def create_usa_resume():
    doc = Document()
    set_page_margins(doc, 0.75, 0.75, 0.75, 0.75)

    # Name header
    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    run = p.add_run("ALEX JOHNSON")
    set_font(run, 'Calibri', 22, bold=True, color=(31, 73, 125))

    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    run = p.add_run("San Francisco, CA  |  (415) 555-0192  |  alex.johnson@email.com  |  linkedin.com/in/alexjohnson  |  github.com/alexjohnson")
    set_font(run, 'Calibri', 9.5, color=(80, 80, 80))

    add_rule(doc, (31, 73, 125))

    # Professional Summary
    section_heading(doc, "Professional Summary")
    p = add_para(doc, space_after=4)
    run = p.add_run(
        "Results-driven Senior Software Engineer with 8+ years of experience designing and delivering "
        "scalable cloud-native applications. Proven track record of leading cross-functional teams, "
        "reducing system latency by 40%, and shipping features that drive measurable business growth. "
        "Passionate about clean architecture, mentorship, and turning complex problems into elegant solutions."
    )
    set_font(run, 'Calibri', 10.5)

    # Core Competencies
    section_heading(doc, "Core Competencies")
    skills = [
        ["Python · Go · TypeScript", "AWS · GCP · Azure", "Kubernetes · Docker · Terraform"],
        ["Microservices Architecture", "CI/CD (GitHub Actions, Jenkins)", "PostgreSQL · MongoDB · Redis"],
        ["Agile / Scrum Leadership", "System Design & Scalability", "REST & GraphQL APIs"],
    ]
    table = doc.add_table(rows=3, cols=3)
    remove_table_borders(table)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r, row_data in enumerate(skills):
        for c, cell_text in enumerate(row_data):
            cell = table.cell(r, c)
            cell.paragraphs[0].clear()
            run = cell.paragraphs[0].add_run("• " + cell_text)
            set_font(run, 'Calibri', 10)
            cell.paragraphs[0].paragraph_format.space_after = Pt(1)

    # Professional Experience
    section_heading(doc, "Professional Experience")

    def add_job(title, company, location, dates, bullets):
        p = add_para(doc, space_before=6, space_after=0)
        r1 = p.add_run(title)
        set_font(r1, 'Calibri', 11, bold=True, color=(31, 73, 125))
        p.add_run("  |  ")
        r2 = p.add_run(f"{company}, {location}")
        set_font(r2, 'Calibri', 11, bold=True)

        p2 = add_para(doc, space_after=3)
        r3 = p2.add_run(dates)
        set_font(r3, 'Calibri', 10, italic=True, color=(100, 100, 100))

        for b in bullets:
            bullet_para(doc, b)

    add_job(
        "Senior Software Engineer", "TechCorp Inc.", "San Francisco, CA",
        "March 2021 – Present",
        [
            "Architected and deployed a multi-region microservices platform on AWS, reducing p99 latency from 850 ms to 120 ms (86% improvement) and supporting 5M+ daily active users.",
            "Led a team of 7 engineers to deliver a real-time analytics dashboard, increasing customer retention KPIs by 22% within two quarters post-launch.",
            "Implemented automated CI/CD pipelines with 95% test coverage, cutting production incidents by 60% and deployment time from 4 hours to 18 minutes.",
            "Drove technical interviews and onboarding programs, hiring 12 engineers and reducing ramp-up time by 30%.",
        ]
    )

    add_job(
        "Software Engineer II", "DataStream Solutions", "Austin, TX",
        "June 2018 – February 2021",
        [
            "Built a high-throughput data ingestion service (Kafka + Go) processing 2 billion events/day with 99.99% uptime SLA.",
            "Redesigned PostgreSQL schema and query optimization strategy, reducing report generation time by 70%.",
            "Collaborated with Product and Design on A/B testing framework that improved conversion rate by 15%.",
        ]
    )

    add_job(
        "Software Engineer", "StartupXYZ", "Remote",
        "July 2016 – May 2018",
        [
            "Developed RESTful APIs powering a B2B SaaS platform serving 200+ enterprise clients.",
            "Migrated monolithic Rails application to containerized microservices, enabling independent scaling of critical services.",
        ]
    )

    # Education
    section_heading(doc, "Education")
    p = add_para(doc, space_before=4, space_after=0)
    r = p.add_run("Bachelor of Science in Computer Science")
    set_font(r, 'Calibri', 11, bold=True)
    p2 = add_para(doc, space_after=2)
    r2 = p2.add_run("University of California, Berkeley  |  Graduated May 2016  |  GPA: 3.8/4.0")
    set_font(r2, 'Calibri', 10.5)

    # Certifications
    section_heading(doc, "Certifications & Awards")
    for cert in [
        "AWS Certified Solutions Architect – Professional (2023)",
        "Google Cloud Professional Data Engineer (2022)",
        "Certified Kubernetes Administrator (CKA) (2021)",
        "TechCorp Engineering Excellence Award — Q3 2022",
    ]:
        bullet_para(doc, cert)

    path = os.path.join(OUTPUT_DIR, "01_USA_Resume_ATS_Optimized.docx")
    doc.save(path)
    print(f"  ✓  {os.path.basename(path)}")


# ─── 2. UK CV ─────────────────────────────────────────────────────────────────

def create_uk_cv():
    doc = Document()
    set_page_size_a4(doc)
    set_page_margins(doc, 1.0, 1.0, 1.0, 1.0)

    # Name
    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=0)
    run = p.add_run("Charlotte Davies")
    set_font(run, 'Georgia', 24, bold=True, color=(26, 52, 92))

    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
    run = p.add_run("Senior Marketing Manager")
    set_font(run, 'Georgia', 13, italic=True, color=(80, 80, 80))

    add_rule(doc, (26, 52, 92))

    # Contact line
    p = add_para(doc, space_before=4, space_after=8)
    run = p.add_run(
        "London, UK  •  +44 7700 900123  •  c.davies@email.co.uk  •  linkedin.com/in/charlottedavies"
    )
    set_font(run, 'Calibri', 9.5, color=(80, 80, 80))

    # Personal Profile
    section_heading(doc, "Personal Profile", font_name='Georgia', color=(26, 52, 92), rule_color=(26, 52, 92))
    p = add_para(doc, space_after=6)
    run = p.add_run(
        "A strategic and data-led Senior Marketing Manager with over 10 years' experience driving brand growth "
        "for leading FMCG and technology organisations across the UK and EMEA. Adept at building high-performing "
        "teams, managing multi-million-pound budgets, and translating consumer insight into integrated campaigns "
        "that consistently outperform market benchmarks. Seeking a Director-level opportunity to leverage commercial "
        "acumen and creative vision within a purpose-driven business."
    )
    set_font(run, 'Calibri', 10.5)

    # Career History
    section_heading(doc, "Career History", font_name='Georgia', color=(26, 52, 92), rule_color=(26, 52, 92))

    def add_uk_job(title, company, dates, location, bullets):
        p = add_para(doc, space_before=8, space_after=0)
        r1 = p.add_run(title)
        set_font(r1, 'Calibri', 11, bold=True, color=(26, 52, 92))
        p2 = add_para(doc, space_after=1)
        r2 = p2.add_run(f"{company}, {location}  |  {dates}")
        set_font(r2, 'Calibri', 10, italic=True, color=(100, 100, 100))
        for b in bullets:
            bullet_para(doc, b, font_name='Calibri', font_size=10.5)

    add_uk_job(
        "Senior Marketing Manager", "GlobalBrand Ltd.", "January 2020 – Present", "London",
        [
            "Directed a £4.2M integrated marketing budget across paid, owned and earned channels, delivering 34% YoY revenue growth for the UK flagship brand.",
            "Led a team of 9 marketing professionals, implementing OKR framework that increased team productivity by 28%.",
            "Spearheaded launch of a new product range across 14 European markets, exceeding first-year sales targets by 19%.",
            "Negotiated and managed agency relationships (creative, media, PR), achieving 15% cost saving whilst improving output quality.",
        ]
    )

    add_uk_job(
        "Marketing Manager", "Innovate Digital", "April 2017 – December 2019", "Manchester",
        [
            "Grew organic search traffic by 210% through SEO strategy and content programme overhaul.",
            "Managed £1.8M paid media budget (Google, Meta, LinkedIn) with average ROAS of 4.6x.",
            "Developed and delivered CRM strategy, increasing email open rates from 18% to 31%.",
        ]
    )

    add_uk_job(
        "Marketing Executive", "RetailCo UK", "September 2014 – March 2017", "Birmingham",
        [
            "Supported national ATL and BTL campaigns reaching 8M+ consumers.",
            "Co-ordinated sponsorship activations for major sporting events, managing supplier relationships and on-site logistics.",
        ]
    )

    # Education
    section_heading(doc, "Education & Qualifications", font_name='Georgia', color=(26, 52, 92), rule_color=(26, 52, 92))
    for edu in [
        ("MA Marketing Communications", "University of Leeds  |  Distinction  |  2013–2014"),
        ("BA (Hons) Business Studies", "University of Nottingham  |  2:1  |  2010–2013"),
        ("CIM Chartered Postgraduate Diploma in Marketing", "Chartered Institute of Marketing  |  2016"),
    ]:
        p = add_para(doc, space_before=4, space_after=0)
        r = p.add_run(edu[0])
        set_font(r, 'Calibri', 10.5, bold=True)
        p2 = add_para(doc, space_after=2)
        r2 = p2.add_run(edu[1])
        set_font(r2, 'Calibri', 10)

    # Key Skills
    section_heading(doc, "Key Skills", font_name='Georgia', color=(26, 52, 92), rule_color=(26, 52, 92))
    skills_text = (
        "Brand Strategy  •  Integrated Campaign Management  •  P&L Ownership  •  Team Leadership  •  "
        "Performance Marketing  •  Market Research & Consumer Insight  •  Salesforce Marketing Cloud  •  "
        "Google Analytics 4  •  Adobe Creative Suite  •  Budget Management"
    )
    p = add_para(doc, space_after=4)
    run = p.add_run(skills_text)
    set_font(run, 'Calibri', 10.5)

    # References
    section_heading(doc, "References", font_name='Georgia', color=(26, 52, 92), rule_color=(26, 52, 92))
    p = add_para(doc, space_after=2)
    run = p.add_run("Available upon request.")
    set_font(run, 'Calibri', 10.5, italic=True)

    path = os.path.join(OUTPUT_DIR, "02_UK_CV_Professional.docx")
    doc.save(path)
    print(f"  ✓  {os.path.basename(path)}")


# ─── 3. EU / Europass-style CV ────────────────────────────────────────────────

def create_eu_cv():
    doc = Document()
    set_page_size_a4(doc)
    set_page_margins(doc, 1.0, 1.0, 1.0, 1.0)

    # Header block — navy sidebar style via table
    table = doc.add_table(rows=1, cols=2)
    remove_table_borders(table)
    table.columns[0].width = Cm(5)
    table.columns[1].width = Cm(14)

    left_cell = table.cell(0, 0)
    shade_table_cell(left_cell, '1A3460')
    left_cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    p = left_cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\n[PHOTO]\n")
    set_font(run, 'Calibri', 9, color=(255, 255, 255))
    p2 = left_cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = p2.add_run("(Optional)\n90×120 px")
    set_font(run2, 'Calibri', 8, italic=True, color=(200, 200, 200))

    right_cell = table.cell(0, 1)
    right_cell.paragraphs[0].clear()
    rp = right_cell.paragraphs[0]
    rp.paragraph_format.space_before = Pt(6)
    rp.paragraph_format.left_indent = Inches(0.2)
    rp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    name_run = rp.add_run("Lukas Müller")
    set_font(name_run, 'Calibri', 22, bold=True, color=(26, 52, 92))

    rp2 = right_cell.add_paragraph()
    rp2.paragraph_format.left_indent = Inches(0.2)
    job_run = rp2.add_run("Data Scientist  |  Machine Learning Engineer")
    set_font(job_run, 'Calibri', 12, italic=True, color=(80, 80, 80))

    for line in [
        "Berlin, Germany",
        "+49 170 1234567  •  l.muller@email.de",
        "linkedin.com/in/lukasmuller  •  github.com/lukasmuller",
        "Nationality: German  •  Date of Birth: 14 March 1990",
    ]:
        rp3 = right_cell.add_paragraph()
        rp3.paragraph_format.left_indent = Inches(0.2)
        r = rp3.add_run(line)
        set_font(r, 'Calibri', 9.5, color=(60, 60, 60))

    doc.add_paragraph()

    # Personal Statement
    section_heading(doc, "Personal Statement", color=(26, 52, 92), rule_color=(26, 52, 92))
    p = add_para(doc, space_after=6)
    run = p.add_run(
        "Experienced Data Scientist with 7 years of expertise in machine learning, statistical modelling, "
        "and large-scale data infrastructure across the automotive and financial sectors. Fluent in German, "
        "English, and French. Committed to delivering explainable AI solutions that comply with EU AI Act "
        "requirements and GDPR data governance standards."
    )
    set_font(run, 'Calibri', 10.5)

    # Work Experience
    section_heading(doc, "Work Experience", color=(26, 52, 92), rule_color=(26, 52, 92))

    def add_eu_job(title, company, location, country, dates, bullets):
        p = add_para(doc, space_before=8, space_after=0)
        r1 = p.add_run(title)
        set_font(r1, 'Calibri', 11, bold=True, color=(26, 52, 92))
        p2 = add_para(doc, space_after=1)
        r2 = p2.add_run(f"{company} — {location}, {country}  |  {dates}")
        set_font(r2, 'Calibri', 10, italic=True, color=(100, 100, 100))
        for b in bullets:
            bullet_para(doc, b)

    add_eu_job("Lead Data Scientist", "AutoVision GmbH", "Munich", "Germany",
               "Jan 2021 – Present",
               [
                   "Developed computer vision pipeline for autonomous driving perception system, achieving mAP of 0.94 on internal benchmark — top 3% in KITTI leaderboard.",
                   "Built GDPR-compliant data anonymisation framework processing 12 TB/day of sensor data.",
                   "Delivered EU AI Act conformity assessment documentation ahead of 2024 regulatory deadline.",
                   "Mentored team of 5 junior scientists; introduced MLflow model registry reducing experiment duplication by 45%.",
               ])

    add_eu_job("Senior Data Analyst", "FinServe AG", "Frankfurt", "Germany",
               "Mar 2018 – Dec 2020",
               [
                   "Built credit risk scoring models (XGBoost, LightGBM) reducing non-performing loan ratio by 12 bps.",
                   "Deployed real-time fraud detection API (FastAPI + Kafka) with <50 ms inference latency.",
               ])

    # Education
    section_heading(doc, "Education", color=(26, 52, 92), rule_color=(26, 52, 92))
    for edu in [
        ("MSc Data Science", "Technical University of Munich (TUM)", "Germany", "2015–2017", "Grade: 1.2 (Excellent)"),
        ("BSc Computer Science", "Humboldt-Universität zu Berlin", "Germany", "2012–2015", "Grade: 1.5 (Very Good)"),
    ]:
        p = add_para(doc, space_before=6, space_after=0)
        r = p.add_run(edu[0])
        set_font(r, 'Calibri', 11, bold=True)
        p2 = add_para(doc, space_after=2)
        r2 = p2.add_run(f"{edu[1]}, {edu[2]}  |  {edu[3]}  |  {edu[4]}")
        set_font(r2, 'Calibri', 10.5)

    # Language Skills
    section_heading(doc, "Language Skills", color=(26, 52, 92), rule_color=(26, 52, 92))
    lang_table = doc.add_table(rows=1, cols=4)
    remove_table_borders(lang_table)
    for cell, text in zip(lang_table.rows[0].cells,
                          ["Language", "Understanding", "Speaking", "Writing"]):
        cell.paragraphs[0].clear()
        r = cell.paragraphs[0].add_run(text)
        set_font(r, 'Calibri', 10, bold=True, color=(26, 52, 92))

    for lang_row in [
        ["German", "C2 (Native)", "C2 (Native)", "C2 (Native)"],
        ["English", "C1", "C1", "C1"],
        ["French", "B2", "B1", "B1"],
    ]:
        row = lang_table.add_row()
        for cell, text in zip(row.cells, lang_row):
            cell.paragraphs[0].clear()
            r = cell.paragraphs[0].add_run(text)
            set_font(r, 'Calibri', 10)

    # Technical Skills
    section_heading(doc, "Digital & Technical Skills", color=(26, 52, 92), rule_color=(26, 52, 92))
    for skill_line in [
        "Programming: Python (expert), R (advanced), SQL (advanced), Scala (intermediate)",
        "ML/DL Frameworks: PyTorch, TensorFlow, scikit-learn, Hugging Face Transformers",
        "Data Engineering: Apache Spark, Kafka, Airflow, dbt, Snowflake",
        "Cloud & MLOps: AWS SageMaker, Azure ML, MLflow, Docker, Kubernetes",
    ]:
        bullet_para(doc, skill_line)

    path = os.path.join(OUTPUT_DIR, "03_EU_Europass_CV.docx")
    doc.save(path)
    print(f"  ✓  {os.path.basename(path)}")


# ─── 4. Japan Rirekisho-style Resume ──────────────────────────────────────────

def create_japan_resume():
    doc = Document()
    set_page_size_a4(doc)
    set_page_margins(doc, 1.0, 1.0, 1.0, 1.0)

    # Title
    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    run = p.add_run("RESUME  /  履歴書")
    set_font(run, 'Calibri', 18, bold=True, color=(180, 0, 0))

    add_rule(doc, (180, 0, 0))

    # Personal Information table
    p = add_para(doc, space_before=8, space_after=2)
    run = p.add_run("PERSONAL INFORMATION  /  個人情報")
    set_font(run, 'Calibri', 11, bold=True, color=(180, 0, 0))

    info_table = doc.add_table(rows=7, cols=4)
    info_table.style = 'Table Grid'
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    personal_info = [
        ["Name (氏名)", "Tanaka Haruki (田中 晴輝)", "Date Created (作成日)", "2026年 6月 9日"],
        ["Date of Birth (生年月日)", "1990年 5月 15日", "Age (年齢)", "36歳"],
        ["Gender (性別)", "Male (男性)", "Nationality (国籍)", "Japanese (日本)"],
        ["Address (住所)", "〒150-0001 東京都渋谷区神宮前1-1-1", "", ""],
        ["Phone (電話)", "090-1234-5678", "Email (メール)", "tanaka.haruki@email.jp"],
        ["Photo\n(写真)", "[Attach formal\npassport-style\nphoto here]\n4cm × 3cm", "Nearest Station\n(最寄り駅)", "Harajuku Station (原宿駅)\nJR Yamanote Line"],
        ["Emergency Contact\n(緊急連絡先)", "Tanaka Yuki (Wife)  090-9876-5432", "", ""],
    ]

    for r_idx, row_data in enumerate(personal_info):
        row = info_table.rows[r_idx]
        for c_idx, cell_text in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.paragraphs[0].clear()
            run = cell.paragraphs[0].add_run(cell_text)
            size = 9 if (c_idx % 2 == 0) else 10
            bold = (c_idx % 2 == 0)
            set_font(run, 'Calibri', size, bold=bold)
            cell.paragraphs[0].paragraph_format.space_after = Pt(1)

    doc.add_paragraph()

    # Education & Career History
    p = add_para(doc, space_before=8, space_after=2)
    run = p.add_run("EDUCATION & CAREER HISTORY  /  学歴・職歴")
    set_font(run, 'Calibri', 11, bold=True, color=(180, 0, 0))

    ec_table = doc.add_table(rows=1, cols=3)
    ec_table.style = 'Table Grid'
    for cell, hdr in zip(ec_table.rows[0].cells, ["Year/Month (年月)", "Type (区分)", "Details (事項)"]):
        cell.paragraphs[0].clear()
        run = cell.paragraphs[0].add_run(hdr)
        set_font(run, 'Calibri', 10, bold=True)
        shade_table_cell(cell, 'F2F2F2')

    history = [
        ("2009年 3月", "学歴", "東京都立青山高等学校 卒業  (Tokyo Metropolitan Aoyama High School — Graduated)"),
        ("2009年 4月", "学歴", "早稲田大学 理工学部 情報通信学科 入学  (Waseda University, Dept. of Information & Communication Engineering — Enrolled)"),
        ("2013年 3月", "学歴", "早稲田大学 理工学部 情報通信学科 卒業  (Waseda University — Graduated, B.Eng., GPA 3.7)"),
        ("2013年 4月", "職歴", "株式会社NTTデータ 入社 システムエンジニア職  (Joined NTT DATA Corporation as Systems Engineer)"),
        ("2017年 9月", "職歴", "株式会社NTTデータ 退社  (Resigned from NTT DATA Corporation)"),
        ("2017年 10月", "職歴", "株式会社メルカリ 入社 バックエンドエンジニア職  (Joined Mercari, Inc. as Backend Engineer)"),
        ("2022年 4月", "職歴", "シニアエンジニアに昇進  (Promoted to Senior Engineer)"),
        ("現在に至る", "職歴", "在職中  (Currently employed)"),
        ("以上", "", ""),
    ]

    for year, kind, detail in history:
        row = ec_table.add_row()
        for cell, text in zip(row.cells, [year, kind, detail]):
            cell.paragraphs[0].clear()
            run = cell.paragraphs[0].add_run(text)
            set_font(run, 'Calibri', 9.5)

    doc.add_paragraph()

    # Certifications & Skills
    p = add_para(doc, space_before=8, space_after=2)
    run = p.add_run("CERTIFICATIONS & SPECIAL SKILLS  /  免許・資格・特技")
    set_font(run, 'Calibri', 11, bold=True, color=(180, 0, 0))

    cert_table = doc.add_table(rows=1, cols=2)
    cert_table.style = 'Table Grid'
    for cell, hdr in zip(cert_table.rows[0].cells, ["Year/Month (年月)", "Certification / Skill (資格・特技)"]):
        cell.paragraphs[0].clear()
        r = cell.paragraphs[0].add_run(hdr)
        set_font(r, 'Calibri', 10, bold=True)
        shade_table_cell(cell, 'F2F2F2')

    certs = [
        ("2015年 6月", "基本情報技術者試験 合格  (Fundamental IT Engineer Examination — Passed)"),
        ("2017年 11月", "応用情報技術者試験 合格  (Applied IT Engineer Examination — Passed)"),
        ("2020年 3月", "AWS Certified Solutions Architect – Professional"),
        ("2022年 6月", "TOEIC スコア 890点  (TOEIC Score: 890)"),
        ("特技", "ピアノ演奏 (Piano performance)、フットサル、OSS貢献 (OSS contributions)"),
    ]
    for yr, cert in certs:
        row = cert_table.add_row()
        for cell, text in zip(row.cells, [yr, cert]):
            cell.paragraphs[0].clear()
            run = cell.paragraphs[0].add_run(text)
            set_font(run, 'Calibri', 9.5)

    doc.add_paragraph()

    # Motivation / PR Statement
    p = add_para(doc, space_before=8, space_after=2)
    run = p.add_run("MOTIVATION & SELF-PR  /  志望動機・自己PR")
    set_font(run, 'Calibri', 11, bold=True, color=(180, 0, 0))

    pr_table = doc.add_table(rows=1, cols=1)
    pr_table.style = 'Table Grid'
    cell = pr_table.rows[0].cells[0]
    cell.paragraphs[0].clear()
    run = cell.paragraphs[0].add_run(
        "【志望動機 / Motivation】\n"
        "貴社のグローバル展開とテクノロジードリブンな企業文化に深く共感し、応募いたしました。"
        "これまでの大規模分散システム開発の経験を活かし、貴社サービスのスケールアップに貢献したいと考えております。\n\n"
        "I am deeply aligned with your company's global expansion strategy and technology-driven culture. "
        "I am eager to leverage my experience in large-scale distributed systems to contribute to the growth of your services.\n\n"
        "【自己PR / Self-PR】\n"
        "NTTデータおよびメルカリでの9年間の経験を通じ、マイクロサービスアーキテクチャ設計、"
        "チームリードとしての後輩育成、英語でのグローバルチームとの協働など、幅広いスキルを習得しました。\n"
        "Over 9 years at NTT DATA and Mercari, I have developed broad expertise in microservices design, "
        "team mentorship, and cross-functional collaboration with international teams in English."
    )
    set_font(run, 'Calibri', 10)

    path = os.path.join(OUTPUT_DIR, "04_Japan_Resume_Rirekisho_Style.docx")
    doc.save(path)
    print(f"  ✓  {os.path.basename(path)}")


# ─── 5. India Resume ──────────────────────────────────────────────────────────

def create_india_resume():
    doc = Document()
    set_page_size_a4(doc)
    set_page_margins(doc, 0.85, 0.85, 0.85, 0.85)

    # Name
    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    run = p.add_run("PRIYA SHARMA")
    set_font(run, 'Calibri', 22, bold=True, color=(0, 102, 68))

    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    run = p.add_run("Senior Product Manager  |  Fintech & Digital Payments")
    set_font(run, 'Calibri', 12, italic=True, color=(60, 60, 60))

    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    run = p.add_run(
        "Bengaluru, Karnataka  •  +91 98765 43210  •  priya.sharma@email.in  •  linkedin.com/in/priyasharma"
    )
    set_font(run, 'Calibri', 9.5, color=(80, 80, 80))

    add_rule(doc, (0, 102, 68))

    # Career Objective
    section_heading(doc, "Career Objective", color=(0, 102, 68), rule_color=(0, 102, 68))
    p = add_para(doc, space_after=4)
    run = p.add_run(
        "Dynamic and results-oriented Senior Product Manager with 9+ years of experience in building and scaling "
        "fintech products across India and South-East Asia. Seeking a leadership role where I can drive product "
        "strategy, align cross-functional stakeholders, and deliver consumer-centric solutions in the rapidly "
        "evolving digital payments landscape."
    )
    set_font(run, 'Calibri', 10.5)

    # Personal Details
    section_heading(doc, "Personal Details", color=(0, 102, 68), rule_color=(0, 102, 68))
    det_table = doc.add_table(rows=5, cols=4)
    remove_table_borders(det_table)
    details = [
        ["Date of Birth:", "15 August 1991", "Father's Name:", "Ramesh Sharma"],
        ["Gender:", "Female", "Marital Status:", "Married"],
        ["Nationality:", "Indian", "Languages:", "English, Hindi, Kannada"],
        ["Current CTC:", "₹28 LPA", "Expected CTC:", "₹38 LPA"],
        ["Notice Period:", "30 Days", "Willing to Relocate:", "Yes (Pan-India / Dubai)"],
    ]
    for r_idx, row_data in enumerate(details):
        row = det_table.rows[r_idx]
        for c_idx, text in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.paragraphs[0].clear()
            r = cell.paragraphs[0].add_run(text)
            bold = (c_idx % 2 == 0)
            set_font(r, 'Calibri', 10, bold=bold, color=(0, 102, 68) if bold else (0, 0, 0))

    # Work Experience
    section_heading(doc, "Work Experience", color=(0, 102, 68), rule_color=(0, 102, 68))

    def add_india_job(title, company, location, dates, bullets):
        p = add_para(doc, space_before=8, space_after=0)
        r1 = p.add_run(title)
        set_font(r1, 'Calibri', 11, bold=True, color=(0, 102, 68))
        p2 = add_para(doc, space_after=1)
        r2 = p2.add_run(f"{company}, {location}  |  {dates}")
        set_font(r2, 'Calibri', 10, italic=True, color=(100, 100, 100))
        for b in bullets:
            bullet_para(doc, b)

    add_india_job(
        "Senior Product Manager", "PhonePe Pvt. Ltd.", "Bengaluru", "April 2021 – Present",
        [
            "Own UPI payments product roadmap for 480M+ registered users; launched 'UPI Lite' feature adopted by 12M users within 60 days of release.",
            "Led cross-functional squads (Engineering, Design, Business, Compliance) of 30+ members across 3 time zones.",
            "Drove 27% reduction in transaction failure rate through root-cause analysis and partner bank API renegotiation.",
            "Defined and tracked OKRs; exceeded Q3 FY2025 GMV target by ₹8,500 Cr (+14% vs plan).",
        ]
    )

    add_india_job(
        "Product Manager", "Razorpay Software Pvt. Ltd.", "Bengaluru", "July 2018 – March 2021",
        [
            "Built Razorpay's B2B invoice financing product from 0→1, generating ₹120 Cr GMV in Year 1.",
            "Improved checkout conversion by 18% through data-driven A/B experiments on payment flow.",
            "Collaborated with RBI compliance team to launch BNPL product aligned to digital lending guidelines.",
        ]
    )

    add_india_job(
        "Associate Product Manager", "Flipkart Internet Pvt. Ltd.", "Bengaluru", "June 2016 – June 2018",
        [
            "Managed seller onboarding funnel; reduced time-to-first-sale from 14 days to 4 days.",
            "Rolled out EMI on Debit Card feature, driving 9% uplift in average order value.",
        ]
    )

    # Education
    section_heading(doc, "Educational Qualifications", color=(0, 102, 68), rule_color=(0, 102, 68))
    for edu in [
        ("MBA (Finance & Strategy)", "Indian Institute of Management (IIM) Bangalore", "2014–2016", "CGPA 3.8/4.0"),
        ("B.Tech (Computer Science)", "National Institute of Technology (NIT) Trichy", "2010–2014", "CGPA 8.9/10"),
    ]:
        p = add_para(doc, space_before=4, space_after=0)
        r = p.add_run(edu[0])
        set_font(r, 'Calibri', 11, bold=True)
        p2 = add_para(doc, space_after=2)
        r2 = p2.add_run(f"{edu[1]}  |  {edu[2]}  |  {edu[3]}")
        set_font(r2, 'Calibri', 10.5)

    # Key Skills
    section_heading(doc, "Key Skills", color=(0, 102, 68), rule_color=(0, 102, 68))
    for skill in [
        "Product Strategy & Roadmapping  •  OKR Framework  •  Agile / Scrum  •  Data Analytics (SQL, Mixpanel, Amplitude)",
        "UPI / NPCI Ecosystem  •  Payment Gateway Integration  •  Regulatory & RBI Compliance",
        "Stakeholder Management  •  Go-to-Market Strategy  •  User Research  •  Figma / Miro",
    ]:
        bullet_para(doc, skill)

    # Achievements
    section_heading(doc, "Achievements & Recognitions", color=(0, 102, 68), rule_color=(0, 102, 68))
    for ach in [
        "Forbes India 30 Under 30 — Technology (2024)",
        "PhonePe 'Product Excellence Award' — FY2023",
        "Speaker, India Fintech Forum 2023 — Topic: 'UPI 2.0 and the Future of Credit'",
        "Razorpay internal 'Innovator of the Year' — 2020",
    ]:
        bullet_para(doc, ach)

    # Declaration
    section_heading(doc, "Declaration", color=(0, 102, 68), rule_color=(0, 102, 68))
    p = add_para(doc, space_after=2)
    run = p.add_run(
        "I hereby declare that all the information mentioned above is true and correct to the best of my knowledge and belief."
    )
    set_font(run, 'Calibri', 10, italic=True)
    p2 = add_para(doc, space_after=2)
    r2 = p2.add_run("Place: Bengaluru          Date: 09 June 2026          Signature: ________________")
    set_font(r2, 'Calibri', 10)

    path = os.path.join(OUTPUT_DIR, "05_India_Resume_Professional.docx")
    doc.save(path)
    print(f"  ✓  {os.path.basename(path)}")


# ─── 6. Australia Resume ──────────────────────────────────────────────────────

def create_australia_resume():
    doc = Document()
    set_page_size_a4(doc)
    set_page_margins(doc, 1.0, 1.0, 1.0, 1.0)

    # Header
    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=0)
    run = p.add_run("James O'Connor")
    set_font(run, 'Calibri', 24, bold=True, color=(0, 84, 166))

    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
    run = p.add_run("Project Manager — Construction & Infrastructure")
    set_font(run, 'Calibri', 13, italic=True, color=(80, 80, 80))

    p = add_para(doc, space_after=6)
    run = p.add_run(
        "Sydney NSW 2000  |  +61 412 345 678  |  j.oconnor@email.com.au  |  linkedin.com/in/jamesoconnor"
    )
    set_font(run, 'Calibri', 9.5, color=(80, 80, 80))

    add_rule(doc, (0, 84, 166))

    # Professional Summary
    section_heading(doc, "Professional Summary", color=(0, 84, 166), rule_color=(0, 84, 166))
    p = add_para(doc, space_after=6)
    run = p.add_run(
        "Highly accomplished Project Manager with 12 years' experience delivering major civil infrastructure, "
        "commercial construction, and public sector projects across NSW and QLD. Consistent record of on-time, "
        "on-budget delivery on projects valued up to $220M. Holds PMP and Prince2 Practitioner certifications. "
        "Strong stakeholder communicator with deep expertise in Australian Standards and Work Health & Safety legislation."
    )
    set_font(run, 'Calibri', 10.5)

    # Career History
    section_heading(doc, "Career History", color=(0, 84, 166), rule_color=(0, 84, 166))

    def add_au_job(title, company, location, state, dates, bullets):
        p = add_para(doc, space_before=8, space_after=0)
        r1 = p.add_run(title)
        set_font(r1, 'Calibri', 11, bold=True, color=(0, 84, 166))
        p2 = add_para(doc, space_after=1)
        r2 = p2.add_run(f"{company}, {location} {state}  |  {dates}")
        set_font(r2, 'Calibri', 10, italic=True, color=(100, 100, 100))
        for b in bullets:
            bullet_para(doc, b)

    add_au_job(
        "Senior Project Manager", "Lendlease Group", "Sydney", "NSW",
        "February 2020 – Present",
        [
            "Delivered $220M Western Sydney commercial precinct (8 buildings, 42,000 sqm GFA) 6 weeks ahead of programme and $1.8M under budget.",
            "Led principal contractor team of 180 site personnel; maintained LTI frequency rate of 0 for 36 consecutive months.",
            "Managed stakeholder engagement with NSW Infrastructure, local councils, and 14 subcontractors.",
            "Implemented BIM (Revit/Navisworks) clash detection protocol reducing RFI volume by 38%.",
        ]
    )

    add_au_job(
        "Project Manager", "John Holland Group", "Brisbane", "QLD",
        "March 2016 – January 2020",
        [
            "Managed $85M Cross River Rail enabling works package — delivered on programme within $400K of budget.",
            "Coordinated with Queensland Rail, DTMR and Brisbane City Council on interface works and community impact mitigation.",
            "Achieved 5-star Green Star rating on $42M commercial fitout by introducing sustainable procurement practices.",
        ]
    )

    add_au_job(
        "Assistant Project Manager", "Multiplex", "Sydney", "NSW",
        "January 2013 – February 2016",
        [
            "Supported delivery of $130M mixed-use residential tower (430 apartments) — Kings Cross, Sydney.",
            "Managed subcontractor packages (concrete, structural steel) valued at $28M combined.",
        ]
    )

    # Education
    section_heading(doc, "Education", color=(0, 84, 166), rule_color=(0, 84, 166))
    for edu in [
        ("Bachelor of Civil Engineering (Honours Class I)", "University of New South Wales (UNSW)", "2009–2012"),
        ("Graduate Certificate in Project Management", "RMIT University Online", "2015"),
    ]:
        p = add_para(doc, space_before=4, space_after=0)
        r = p.add_run(edu[0])
        set_font(r, 'Calibri', 11, bold=True)
        p2 = add_para(doc, space_after=2)
        r2 = p2.add_run(f"{edu[1]}  |  {edu[2]}")
        set_font(r2, 'Calibri', 10.5)

    # Licences & Certifications
    section_heading(doc, "Licences, Certifications & Memberships", color=(0, 84, 166), rule_color=(0, 84, 166))
    for lic in [
        "PMP — Project Management Professional (PMI, 2017, renewed 2023)",
        "PRINCE2 Practitioner (AXELOS, 2019)",
        "Construction Induction (White Card) — WorkSafe Australia",
        "MiHi White Card (High Risk Work Licence — Scaffolding)",
        "Member, Australian Institute of Project Management (AIPM) — CPPD",
        "Engineers Australia — MIEAust",
    ]:
        bullet_para(doc, lic)

    # Key Skills
    section_heading(doc, "Key Skills", color=(0, 84, 166), rule_color=(0, 84, 166))
    for skill in [
        "Programme & Cost Management (Primavera P6, MS Project)  •  Risk Management  •  NEC4 / AS 4300 Contracts",
        "BIM Coordination (Revit, Navisworks)  •  WHS Management Systems  •  Stakeholder Engagement",
        "Design Management  •  Community Consultation  •  Tender & Procurement",
    ]:
        bullet_para(doc, skill)

    # Referees
    section_heading(doc, "Referees", color=(0, 84, 166), rule_color=(0, 84, 166))
    p = add_para(doc, space_after=2)
    run = p.add_run("Two professional referees available on request.")
    set_font(run, 'Calibri', 10.5, italic=True)

    path = os.path.join(OUTPUT_DIR, "06_Australia_Resume_Professional.docx")
    doc.save(path)
    print(f"  ✓  {os.path.basename(path)}")


# ─── 7. New Zealand CV ────────────────────────────────────────────────────────

def create_nz_cv():
    doc = Document()
    set_page_size_a4(doc)
    set_page_margins(doc, 1.0, 1.0, 1.0, 1.0)

    # Header
    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=0)
    run = p.add_run("Sophie Walker")
    set_font(run, 'Calibri', 24, bold=True, color=(0, 112, 60))

    p = add_para(doc, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
    run = p.add_run("Registered Nurse — Intensive Care & Critical Care Specialist")
    set_font(run, 'Calibri', 13, italic=True, color=(80, 80, 80))

    p = add_para(doc, space_after=6)
    run = p.add_run(
        "Auckland 1010, New Zealand  |  +64 21 987 654  |  s.walker@email.co.nz  |  NMC Registration: NZ-2018-RN-00123"
    )
    set_font(run, 'Calibri', 9.5, color=(80, 80, 80))

    add_rule(doc, (0, 112, 60))

    # Professional Profile
    section_heading(doc, "Professional Profile", color=(0, 112, 60), rule_color=(0, 112, 60))
    p = add_para(doc, space_after=6)
    run = p.add_run(
        "Compassionate and evidence-based Registered Nurse with 8 years of intensive care experience in tertiary "
        "hospitals across Aotearoa New Zealand and the United Kingdom. Specialises in cardiac and neuro ICU with "
        "expertise in ventilator management, ECMO support, and deteriorating patient recognition. Committed to "
        "whānau-centred care and Te Tiriti o Waitangi principles in all clinical practice."
    )
    set_font(run, 'Calibri', 10.5)

    # Registration & Work Rights
    section_heading(doc, "Registration & Work Rights", color=(0, 112, 60), rule_color=(0, 112, 60))
    for item in [
        "Nursing Council of New Zealand (NCNZ) — Annual Practising Certificate (current, expires Oct 2026)",
        "NZ Citizen — No visa or sponsorship required",
        "NZ Resuscitation Council Level 7 (ALS) — current",
    ]:
        bullet_para(doc, item)

    # Employment History
    section_heading(doc, "Employment History", color=(0, 112, 60), rule_color=(0, 112, 60))

    def add_nz_job(title, org, location, dates, bullets):
        p = add_para(doc, space_before=8, space_after=0)
        r1 = p.add_run(title)
        set_font(r1, 'Calibri', 11, bold=True, color=(0, 112, 60))
        p2 = add_para(doc, space_after=1)
        r2 = p2.add_run(f"{org}, {location}  |  {dates}")
        set_font(r2, 'Calibri', 10, italic=True, color=(100, 100, 100))
        for b in bullets:
            bullet_para(doc, b)

    add_nz_job(
        "Senior Registered Nurse — ICU", "Auckland City Hospital (Te Toka Tumai)", "Auckland, NZ",
        "August 2020 – Present",
        [
            "Provide complex nursing care for ventilated and ECMO patients in a 28-bed Level 3 ICU (>2,200 admissions/year).",
            "Preceptor for 6 graduate nurses annually; developed structured orientation workbook adopted across Auckland DHB ICU.",
            "Led quality improvement project reducing VAP (ventilator-associated pneumonia) rate by 52% over 18 months.",
            "Te Reo Māori speaker; champions culturally safe care aligned to Te Whare Tapa Whā model.",
        ]
    )

    add_nz_job(
        "Staff Nurse — Cardiac ICU", "Waikato Hospital, Te Whatu Ora", "Hamilton, NZ",
        "February 2018 – July 2020",
        [
            "Delivered post-operative cardiac surgery care (CABG, valve replacement, TAVI) for 10–12 patients per shift.",
            "Trained in intra-aortic balloon pump (IABP) and temporary transvenous pacing management.",
        ]
    )

    add_nz_job(
        "Registered Nurse — General ICU", "Royal London Hospital, Barts Health NHS Trust", "London, UK",
        "March 2016 – December 2017",
        [
            "Worked across a 55-bed Major Trauma Centre ICU, developing broad critical care competencies.",
            "Participated in NIHR-funded sepsis management research trial.",
        ]
    )

    # Education
    section_heading(doc, "Education & Professional Development", color=(0, 112, 60), rule_color=(0, 112, 60))
    for edu in [
        ("Postgraduate Diploma in Nursing (Critical Care)", "The University of Auckland", "2019", "Grade A"),
        ("Bachelor of Nursing", "Auckland University of Technology (AUT)", "2012–2015", "GPA 8.1/9.0"),
        ("Te Ara Reo Māori (Level 2)", "Te Wānanga o Aotearoa", "2021", "Completed"),
    ]:
        p = add_para(doc, space_before=4, space_after=0)
        r = p.add_run(edu[0])
        set_font(r, 'Calibri', 11, bold=True)
        p2 = add_para(doc, space_after=2)
        r2 = p2.add_run(f"{edu[1]}  |  {edu[2]}  |  {edu[3]}")
        set_font(r2, 'Calibri', 10.5)

    # Clinical Skills
    section_heading(doc, "Clinical Competencies", color=(0, 112, 60), rule_color=(0, 112, 60))
    for skill in [
        "Mechanical Ventilation (invasive & non-invasive)  •  ECMO Patient Management  •  Haemodynamic Monitoring",
        "Arterial & Central Line Management  •  IABP  •  Continuous Renal Replacement Therapy (CRRT)",
        "MET/Rapid Response Call Leadership  •  Tracheostomy Care  •  Pain & Sedation Management",
        "Software: Epic EMR, Metavision, WebPAS",
    ]:
        bullet_para(doc, skill)

    # Referees
    section_heading(doc, "Referees", color=(0, 112, 60), rule_color=(0, 112, 60))
    p = add_para(doc, space_after=2)
    run = p.add_run(
        "Two professional clinical referees (Charge Nurse Manager and Clinical Nurse Specialist) available upon request."
    )
    set_font(run, 'Calibri', 10.5, italic=True)

    path = os.path.join(OUTPUT_DIR, "07_NewZealand_CV_Professional.docx")
    doc.save(path)
    print(f"  ✓  {os.path.basename(path)}")


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\nGenerating global resume templates...\n")
    create_usa_resume()
    create_uk_cv()
    create_eu_cv()
    create_japan_resume()
    create_india_resume()
    create_australia_resume()
    create_nz_cv()
    print("\nAll 7 templates generated successfully.\n")
