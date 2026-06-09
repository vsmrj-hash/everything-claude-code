#!/usr/bin/env python3
"""Generate 7 region-specific PDF resumes for Manish Rohan James."""

import os
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import mm, inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY   = colors.HexColor("#1a2f5a")
BLUE   = colors.HexColor("#2563eb")
STEEL  = colors.HexColor("#374151")
GREY   = colors.HexColor("#6b7280")
LGREY  = colors.HexColor("#f3f4f6")
WHITE  = colors.white
BLACK  = colors.HexColor("#111111")
EURO_GREEN = colors.HexColor("#003399")
EURO_GOLD  = colors.HexColor("#FFCC00")
JP_RED     = colors.HexColor("#c0392b")
AUS_GREEN  = colors.HexColor("#00843D")
NZ_BLACK   = colors.HexColor("#1a1a1a")

# ── Candidate data ──────────────────────────────────────────────────────────
NAME = "Manish Rohan James"
TITLE = "AI Operations & Automation Specialist"
EMAIL = "manishrohan2.rj@proton.me"
PHONE = "+91-9700035385"
LINKEDIN = "linkedin.com/in/vsmrj"
LOCATION_FULL = "Hyderabad, India"

SUMMARY = (
    "AI operations and automation professional with 6+ years in digital operations, "
    "including 2+ years focused on AI-driven workflow automation. Combines no-code "
    "automation (Make, Zapier, n8n) and generative AI (Claude, GPT-4) with a publisher's "
    "discipline in process and delivery — cutting manual effort, tightening workflows, and "
    "improving reporting and decision-making. Background spans content operations, business "
    "intelligence, and global delivery coordination."
)

SUMMARY_DE = (
    "AI-Operations- und Automatisierungsfachmann mit über 6 Jahren Erfahrung in digitalen "
    "Betriebsabläufen, davon 2+ Jahre mit Fokus auf KI-gestützte Workflow-Automatisierung. "
    "Verbindet No-Code-Automatisierung (Make, Zapier, n8n) und generative KI (Claude, GPT-4) "
    "mit strukturierter Prozess- und Lieferdisziplin. Lernender Deutschsprecher (A2), offen "
    "für Relocation nach Deutschland oder in die Niederlande."
)

SKILLS = [
    ("AI & Automation", "Generative AI (Claude, Claude Code, GPT-4, Gemini), agentic AI workflows, "
     "prompt engineering, no-code automation (Make, Zapier, n8n), AI content systems"),
    ("Operations", "Process design & optimisation, digital operations, project coordination, "
     "workflow standardisation, change management"),
    ("Business Intelligence", "GA4, Excel (Advanced), KPI reporting, data visualisation, "
     "data-driven decision-making"),
    ("Ways of Working", "Agile/Scrum, stakeholder management, cross-functional coordination, "
     "multi-timezone delivery"),
    ("Growth & Content", "Content operations, social media management, SEO / GEO / AEO"),
]

EXPERIENCE = [
    {
        "title": "AI Operations & Automation Consultant (Freelance)",
        "company": "Independent", "location": "Remote, India",
        "dates": "Mar 2025 – Present",
        "bullets": [
            "Built AI-assisted and no-code automation workflows (Make, Zapier, n8n) for B2B clients, "
            "cutting manual operational effort by ~60% while scaling output.",
            "Integrated generative AI (Claude, GPT-4) into content, reporting, and operational processes; "
            "designed KPI dashboards that drive data-led decisions.",
            "Owned client engagements end-to-end: scoping, delivery, reporting, and process improvement "
            "as the single point of contact.",
        ],
    },
    {
        "title": "Social Media Manager",
        "company": "Spotlit AI", "location": "Remote",
        "dates": "Jan 2024 – Mar 2025",
        "bullets": [
            "Ran LinkedIn and Instagram content operations on automation-driven workflows, scaling daily "
            "output while reducing manual publishing effort by ~60%.",
            "Deployed AI-assisted content systems and real-time analytics loops, improving average post "
            "reach quarter-over-quarter.",
            "Applied GEO and AEO principles to improve discoverability on AI-powered search surfaces.",
        ],
    },
    {
        "title": "Social Media Manager & Content Designer",
        "company": "Keyblocks Strategy", "location": "Hyderabad, India",
        "dates": "Mar 2023 – Dec 2023",
        "bullets": [
            "Built and executed content strategies for B2B technology and business clients; introduced "
            "AI-assisted content systems for efficiency and consistency.",
            "Led content production workflows and coordinated a small content team across client accounts.",
            "Ran multi-channel digital campaigns and aligned initiatives with stakeholder objectives.",
        ],
    },
    {
        "title": "Content Moderator (Meta, via Wipro)",
        "company": "Wipro", "location": "Hyderabad, India",
        "dates": "Aug 2021 – Jan 2023",
        "bullets": [
            "Reviewed and actioned high volumes of user-generated content against Meta's platform "
            "policies, meeting strict accuracy and throughput SLAs.",
            "Applied detailed, frequently-updated policy guidelines consistently across large content "
            "queues in a metrics-driven trust & safety operation.",
            "Maintained daily quality and productivity targets while adapting to changing policy "
            "and escalation workflows.",
        ],
    },
    {
        "title": "Media Delivery Coordinator",
        "company": "Cambridge University Press", "location": "Hyderabad, India",
        "dates": "Jun 2019 – Aug 2021",
        "bullets": [
            "Central coordination point between editorial, legal, and production for digital-asset QA "
            "and worldwide distribution, managing workflows to global deadlines.",
            "Coordinated artwork commissioning and rights compliance across international markets with "
            "zero compliance breaches across tenure.",
            "Managed voiceover and audio asset production end-to-end, liaising with studios and rights "
            "holders across multiple time zones.",
        ],
    },
]

PROJECTS = [
    ("AI-Powered Content Automation System",
     "Designed AI-assisted workflows for content generation and publishing; reduced manual effort "
     "through standardisation and integrated generative AI into daily operations."),
    ("Business Intelligence Reporting Framework",
     "Built KPI tracking and structured reporting that improved visibility into operational and "
     "marketing performance, enabling data-driven decisions."),
]

EDUCATION = ("Bachelor of Pharmacy (B.Pharm)",
             "Jawaharlal Nehru Technological University Hyderabad (JNTUH), India",
             "2011 – 2015")

CERTIFICATIONS = [
    "Siemens Project Manager Job Simulation — Forage (Jan 2026): KPI development, project dashboards",
    "Claude Code in Action — Anthropic (Mar 2026)",
    "Claude 101 — Anthropic (2026)",
]

LANGUAGES = [
    ("English", "Native", "C2"),
    ("Hindi", "Native", "C2"),
    ("Telugu", "Native", "C2"),
    ("German", "Elementary", "A2"),
]


# ── Style helpers ────────────────────────────────────────────────────────────

def base_styles(accent=NAVY):
    return {
        "name_style": ParagraphStyle("name", fontSize=22, fontName="Helvetica-Bold",
                                     textColor=accent, spaceAfter=2, alignment=TA_CENTER),
        "title_style": ParagraphStyle("title_s", fontSize=11, fontName="Helvetica",
                                      textColor=STEEL, spaceAfter=4, alignment=TA_CENTER),
        "contact_style": ParagraphStyle("contact_s", fontSize=8.5, fontName="Helvetica",
                                        textColor=GREY, spaceAfter=6, alignment=TA_CENTER),
        "section_style": ParagraphStyle("section_s", fontSize=10.5, fontName="Helvetica-Bold",
                                        textColor=accent, spaceBefore=10, spaceAfter=3,
                                        borderPadding=(0, 0, 2, 0)),
        "job_title_style": ParagraphStyle("jt_s", fontSize=10, fontName="Helvetica-Bold",
                                          textColor=BLACK, spaceAfter=1),
        "company_style": ParagraphStyle("co_s", fontSize=9, fontName="Helvetica-Oblique",
                                        textColor=GREY, spaceAfter=2),
        "dates_style": ParagraphStyle("dt_s", fontSize=9, fontName="Helvetica",
                                      textColor=GREY, alignment=TA_RIGHT),
        "body_style": ParagraphStyle("body_s", fontSize=9.2, fontName="Helvetica",
                                     textColor=BLACK, leading=13, spaceAfter=2),
        "bullet_style": ParagraphStyle("bullet_s", fontSize=9, fontName="Helvetica",
                                       textColor=BLACK, leading=12.5, leftIndent=12,
                                       firstLineIndent=-8, spaceAfter=2),
        "skill_label": ParagraphStyle("sl_s", fontSize=9, fontName="Helvetica-Bold",
                                      textColor=BLACK),
        "skill_value": ParagraphStyle("sv_s", fontSize=9, fontName="Helvetica",
                                      textColor=STEEL),
        "small_style": ParagraphStyle("sm_s", fontSize=8.5, fontName="Helvetica",
                                      textColor=GREY, leading=12),
    }


def hr(accent=NAVY, thickness=0.8):
    return HRFlowable(width="100%", thickness=thickness, color=accent, spaceAfter=4, spaceBefore=2)


def section_heading(text, styles, accent=NAVY):
    elems = [Paragraph(text.upper(), styles["section_style"]), hr(accent)]
    return elems


def job_block(exp, styles):
    elems = []
    row = Table(
        [[Paragraph(exp["title"], styles["job_title_style"]),
          Paragraph(exp["dates"], styles["dates_style"])]],
        colWidths=["70%", "30%"],
    )
    row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    elems.append(row)
    co_loc = f"{exp['company']} · {exp['location']}"
    elems.append(Paragraph(co_loc, styles["company_style"]))
    for b in exp["bullets"]:
        elems.append(Paragraph(f"• {b}", styles["bullet_style"]))
    elems.append(Spacer(1, 4))
    return elems


# ══════════════════════════════════════════════════════════════════════════════
# 1. USA — ATS-Optimised
# ══════════════════════════════════════════════════════════════════════════════
def build_usa(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    s = base_styles(NAVY)
    story = []

    story.append(Paragraph(NAME, s["name_style"]))
    story.append(Paragraph(TITLE, s["title_style"]))
    story.append(Paragraph(
        f"{EMAIL}  |  {PHONE}  |  {LINKEDIN}  |  Hyderabad, India (Open to relocation)",
        s["contact_style"]))
    story.append(Spacer(1, 2))

    # Professional Summary
    story += section_heading("Professional Summary", s)
    story.append(Paragraph(SUMMARY + " Currently learning German (A2); open to relocation "
                            "to Germany or the Netherlands.", s["body_style"]))

    # Core Competencies (keyword-dense table)
    story += section_heading("Core Competencies", s)
    kw = ["Generative AI (Claude, GPT-4, Gemini)", "No-Code Automation (Make, Zapier, n8n)",
          "Agentic AI Workflows", "Prompt Engineering", "AI Content Systems",
          "KPI Reporting & Dashboards", "GA4 & Data Analytics", "Process Optimisation",
          "Digital Operations", "Agile / Scrum", "Stakeholder Management",
          "Content Operations", "SEO / GEO / AEO", "Cross-functional Coordination",
          "Project Delivery"]
    rows = [kw[i:i+3] for i in range(0, len(kw), 3)]
    tbl = Table([[Paragraph(c, s["body_style"]) for c in r] for r in rows],
                colWidths=["33%", "33%", "34%"])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LGREY),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#d1d5db")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(tbl)

    # Experience
    story += section_heading("Professional Experience", s)
    for exp in EXPERIENCE:
        story += job_block(exp, s)

    # Projects
    story += section_heading("Projects", s)
    for proj_title, proj_desc in PROJECTS:
        story.append(Paragraph(proj_title, s["job_title_style"]))
        story.append(Paragraph(f"• {proj_desc}", s["bullet_style"]))
        story.append(Spacer(1, 3))

    # Education
    story += section_heading("Education", s)
    story.append(Paragraph(
        f"<b>{EDUCATION[0]}</b> · {EDUCATION[1]} · {EDUCATION[2]}", s["body_style"]))

    # Certifications
    story += section_heading("Certifications", s)
    for c in CERTIFICATIONS:
        story.append(Paragraph(f"• {c}", s["bullet_style"]))

    # Languages
    story += section_heading("Languages", s)
    story.append(Paragraph(
        " | ".join(f"{l} ({p})" for l, _, p in LANGUAGES), s["body_style"]))

    doc.build(story)
    print(f"  ✓ {os.path.basename(filename)}")


# ══════════════════════════════════════════════════════════════════════════════
# 2. UK — Professional CV
# ══════════════════════════════════════════════════════════════════════════════
def build_uk(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    s = base_styles(NAVY)
    story = []

    story.append(Paragraph(NAME, s["name_style"]))
    story.append(Paragraph(TITLE, s["title_style"]))
    story.append(Paragraph(
        f"{EMAIL}  |  {PHONE}  |  {LINKEDIN}  |  Hyderabad, India",
        s["contact_style"]))
    story.append(Spacer(1, 2))

    # Personal Profile
    story += section_heading("Personal Profile", s)
    story.append(Paragraph(
        "AI Operations and Automation Specialist with over six years' experience in digital operations, "
        "including two years' focused delivery of AI-driven workflow automation. I bring a "
        "publisher's rigour to process design and delivery, combining no-code automation platforms "
        "(Make, Zapier, n8n) and generative AI (Claude, GPT-4) to reduce manual effort, streamline "
        "workflows, and sharpen data-led reporting. My background encompasses content operations, "
        "business intelligence, and global coordination across time zones. Currently learning "
        "German (A2) and open to relocation within Europe.",
        s["body_style"]))

    # Key Skills
    story += section_heading("Key Skills", s)
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["body_style"]))

    # Career History
    story += section_heading("Career History", s)
    for exp in EXPERIENCE:
        story += job_block(exp, s)

    # Notable Projects
    story += section_heading("Notable Projects", s)
    for proj_title, proj_desc in PROJECTS:
        story.append(Paragraph(proj_title, s["job_title_style"]))
        story.append(Paragraph(f"• {proj_desc}", s["bullet_style"]))
        story.append(Spacer(1, 3))

    # Education & Qualifications
    story += section_heading("Education & Qualifications", s)
    story.append(Paragraph(f"<b>{EDUCATION[0]}</b>", s["job_title_style"]))
    story.append(Paragraph(f"{EDUCATION[1]} | {EDUCATION[2]}", s["company_style"]))

    # Professional Development
    story += section_heading("Professional Development", s)
    for c in CERTIFICATIONS:
        story.append(Paragraph(f"• {c}", s["bullet_style"]))

    # Languages
    story += section_heading("Languages", s)
    story.append(Paragraph(
        " | ".join(f"{l} — {p}" for l, lvl, p in LANGUAGES), s["body_style"]))

    # References
    story += section_heading("References", s)
    story.append(Paragraph("Available on request.", s["body_style"]))

    doc.build(story)
    print(f"  ✓ {os.path.basename(filename)}")


# ══════════════════════════════════════════════════════════════════════════════
# 3. EU — Europass-Inspired
# ══════════════════════════════════════════════════════════════════════════════
def build_eu(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=14*mm, bottomMargin=14*mm)
    s = base_styles(EURO_GREEN)
    story = []

    # Header bar
    header_tbl = Table(
        [[Paragraph(f"<b><font color='white'>{NAME}</font></b>",
                    ParagraphStyle("hn", fontSize=18, fontName="Helvetica-Bold",
                                   textColor=WHITE, alignment=TA_LEFT)),
          Paragraph(f"<font color='white'>{TITLE}</font>",
                    ParagraphStyle("ht", fontSize=10, fontName="Helvetica",
                                   textColor=WHITE, alignment=TA_RIGHT))]],
        colWidths=["60%", "40%"],
    )
    header_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), EURO_GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(header_tbl)
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        f"✉ {EMAIL}  |  ✆ {PHONE}  |  🔗 {LINKEDIN}  |  📍 Hyderabad, India",
        s["contact_style"]))
    story.append(Spacer(1, 4))

    # Personal Statement
    story += section_heading("Personal Statement", s, EURO_GREEN)
    story.append(Paragraph(SUMMARY_DE + " " + SUMMARY, s["body_style"]))

    # Work Experience
    story += section_heading("Work Experience", s, EURO_GREEN)
    for exp in EXPERIENCE:
        story += job_block(exp, s)

    # Education & Training
    story += section_heading("Education and Training", s, EURO_GREEN)
    story.append(Paragraph(f"<b>{EDUCATION[0]}</b>", s["job_title_style"]))
    story.append(Paragraph(f"{EDUCATION[1]} | {EDUCATION[2]}", s["company_style"]))
    story.append(Spacer(1, 4))
    story += section_heading("Continuing Professional Development", s, EURO_GREEN)
    for c in CERTIFICATIONS:
        story.append(Paragraph(f"• {c}", s["bullet_style"]))

    # Digital Skills
    story += section_heading("Digital Competences", s, EURO_GREEN)
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["body_style"]))

    # Language Grid (CEFR)
    story += section_heading("Language Skills (CEFR)", s, EURO_GREEN)
    lang_rows = [["Language", "Understanding", "Speaking", "Writing", "Level"]]
    cefr_map = {"C2": "C2 — Mastery", "A2": "A2 — Elementary"}
    for lang, lvl, cefr in LANGUAGES:
        c = cefr_map.get(cefr, cefr)
        lang_rows.append([lang, cefr, cefr, cefr, c])
    lang_tbl = Table(lang_rows, colWidths=["18%", "16%", "16%", "16%", "34%"])
    lang_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), EURO_GREEN),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#9ca3af")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LGREY]),
    ]))
    story.append(lang_tbl)

    # GDPR
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "I hereby give consent for my personal data included in my application to be processed "
        "for the purposes of the recruitment process in accordance with the EU GDPR.",
        ParagraphStyle("gdpr", fontSize=7.5, fontName="Helvetica-Oblique",
                       textColor=GREY, alignment=TA_CENTER)))

    doc.build(story)
    print(f"  ✓ {os.path.basename(filename)}")


# ══════════════════════════════════════════════════════════════════════════════
# 4. Japan — Rirekisho-Inspired
# ══════════════════════════════════════════════════════════════════════════════
def build_japan(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=14*mm, bottomMargin=14*mm)
    s = base_styles(JP_RED)
    story = []

    # Bilingual header
    story.append(Paragraph(
        f"<b>{NAME}</b> / <font size='14'>マニッシュ・ロハン・ジェームズ</font>",
        ParagraphStyle("jp_name", fontSize=20, fontName="Helvetica-Bold",
                       textColor=JP_RED, spaceAfter=2, alignment=TA_CENTER)))
    story.append(Paragraph(
        f"{TITLE} / AIオペレーション・自動化スペシャリスト",
        ParagraphStyle("jp_title", fontSize=10, fontName="Helvetica",
                       textColor=STEEL, spaceAfter=4, alignment=TA_CENTER)))
    story.append(Paragraph(
        f"{EMAIL}  |  {PHONE}  |  {LINKEDIN}  |  Hyderabad, India",
        s["contact_style"]))
    story.append(Spacer(1, 4))

    # Personal Info Grid (Rirekisho style)
    info_tbl = Table([
        [Paragraph("<b>氏名 / Full Name</b>", s["skill_label"]),
         Paragraph(NAME, s["body_style"]),
         Paragraph("<b>国籍 / Nationality</b>", s["skill_label"]),
         Paragraph("Indian", s["body_style"])],
        [Paragraph("<b>現住所 / Address</b>", s["skill_label"]),
         Paragraph("Hyderabad, India", s["body_style"]),
         Paragraph("<b>就労資格 / Work Auth.</b>", s["skill_label"]),
         Paragraph("Requires sponsorship", s["body_style"])],
    ], colWidths=["22%", "28%", "22%", "28%"])
    info_tbl.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e5e7eb")),
        ("BACKGROUND", (0, 0), (0, -1), LGREY),
        ("BACKGROUND", (2, 0), (2, -1), LGREY),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ]))
    story.append(info_tbl)
    story.append(Spacer(1, 6))

    # Self-PR (自己PR)
    story += section_heading("自己PR / Self-PR", s, JP_RED)
    story.append(Paragraph(
        "I am an AI Operations professional with 6+ years in digital and global operations. "
        "My strength lies in bridging technology and process — designing automation workflows "
        "that free teams from repetitive tasks and enable focus on higher-value work. "
        "I have demonstrated reliability and precision in high-stakes content operations at "
        "Cambridge University Press and Meta (via Wipro), and now bring those disciplines to "
        "AI-era delivery. I am a motivated learner of Japanese business culture and am "
        "actively studying German (A2) to prepare for international roles.",
        s["body_style"]))

    # 職歴 / Career History
    story += section_heading("職歴 / Career History", s, JP_RED)
    for exp in EXPERIENCE:
        story += job_block(exp, s)

    # 学歴 / Education
    story += section_heading("学歴 / Education", s, JP_RED)
    story.append(Paragraph(f"<b>{EDUCATION[0]}</b>", s["job_title_style"]))
    story.append(Paragraph(f"{EDUCATION[1]} | {EDUCATION[2]}", s["company_style"]))

    # スキル / Skills
    story += section_heading("スキル / Skills", s, JP_RED)
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["body_style"]))

    # 語学力 / Languages
    story += section_heading("語学力 / Language Proficiency", s, JP_RED)
    lang_rows = [["Language", "Proficiency", "CEFR"]]
    for lang, lvl, cefr in LANGUAGES:
        lang_rows.append([lang, lvl, cefr])
    lt = Table(lang_rows, colWidths=["35%", "35%", "30%"])
    lt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), JP_RED),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#e5e7eb")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LGREY]),
    ]))
    story.append(lt)

    # 資格・免許 / Certifications
    story += section_heading("資格・研修 / Certifications & Training", s, JP_RED)
    for c in CERTIFICATIONS:
        story.append(Paragraph(f"• {c}", s["bullet_style"]))

    doc.build(story)
    print(f"  ✓ {os.path.basename(filename)}")


# ══════════════════════════════════════════════════════════════════════════════
# 5. India — Standard Indian CV
# ══════════════════════════════════════════════════════════════════════════════
def build_india(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    accent = colors.HexColor("#ff6600")
    s = base_styles(accent)
    story = []

    story.append(Paragraph(NAME, s["name_style"]))
    story.append(Paragraph(TITLE, s["title_style"]))
    story.append(Paragraph(
        f"{EMAIL}  |  {PHONE}  |  {LINKEDIN}  |  Hyderabad, Telangana, India",
        s["contact_style"]))
    story.append(Spacer(1, 2))

    # Personal Details (Indian CV standard)
    story += section_heading("Personal Details", s, accent)
    details = [
        ["Father's Name:", "Rohan James"],
        ["Date of Birth:", "Available on request"],
        ["Nationality:", "Indian"],
        ["Current Location:", "Hyderabad, Telangana"],
        ["Languages Known:", "English (C2), Hindi (C2), Telugu (C2), German (A2)"],
        ["Marital Status:", "Available on request"],
        ["Notice Period:", "Immediate / Negotiable"],
        ["Current CTC:", "Available on request"],
        ["Expected CTC:", "Negotiable based on role and location"],
    ]
    det_tbl = Table(
        [[Paragraph(k, s["skill_label"]), Paragraph(v, s["body_style"])]
         for k, v in details],
        colWidths=["30%", "70%"])
    det_tbl.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [WHITE, LGREY]),
        ("GRID", (0, 0), (-1, -1), 0.2, colors.HexColor("#e5e7eb")),
    ]))
    story.append(det_tbl)

    # Career Objective
    story += section_heading("Career Objective", s, accent)
    story.append(Paragraph(
        "Results-driven AI Operations and Automation Specialist with 6+ years of progressive "
        "experience in digital operations, content systems, and business intelligence. "
        "Seeking a challenging role where I can leverage expertise in generative AI, no-code "
        "automation, and process optimisation to deliver measurable business impact for "
        "forward-thinking organisations.", s["body_style"]))

    # Core Competencies
    story += section_heading("Core Competencies", s, accent)
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["body_style"]))

    # Work Experience
    story += section_heading("Work Experience", s, accent)
    for exp in EXPERIENCE:
        story += job_block(exp, s)

    # Key Projects
    story += section_heading("Key Projects", s, accent)
    for proj_title, proj_desc in PROJECTS:
        story.append(Paragraph(proj_title, s["job_title_style"]))
        story.append(Paragraph(f"• {proj_desc}", s["bullet_style"]))
        story.append(Spacer(1, 3))

    # Educational Qualifications
    story += section_heading("Educational Qualifications", s, accent)
    edu_tbl = Table(
        [["Qualification", "Institution", "Year"],
         [EDUCATION[0], EDUCATION[1], EDUCATION[2]]],
        colWidths=["28%", "50%", "22%"])
    edu_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#e5e7eb")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LGREY]),
    ]))
    story.append(edu_tbl)

    # Certifications
    story += section_heading("Certifications", s, accent)
    for c in CERTIFICATIONS:
        story.append(Paragraph(f"• {c}", s["bullet_style"]))

    # Declaration
    story += section_heading("Declaration", s, accent)
    story.append(Paragraph(
        "I hereby declare that the above information is true and correct to the best of my "
        "knowledge and belief. I take responsibility for the authenticity of all details "
        "provided herein.", s["body_style"]))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Date:  _______________   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "
                            "Place: Hyderabad &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "
                            "Signature: _______________",
                            ParagraphStyle("sig", fontSize=9, fontName="Helvetica",
                                           textColor=GREY)))

    doc.build(story)
    print(f"  ✓ {os.path.basename(filename)}")


# ══════════════════════════════════════════════════════════════════════════════
# 6. Australia — Professional Resume
# ══════════════════════════════════════════════════════════════════════════════
def build_australia(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    s = base_styles(AUS_GREEN)
    story = []

    story.append(Paragraph(NAME, s["name_style"]))
    story.append(Paragraph(TITLE, s["title_style"]))
    story.append(Paragraph(
        f"{EMAIL}  |  {PHONE}  |  {LINKEDIN}  |  Hyderabad, India",
        s["contact_style"]))
    story.append(Spacer(1, 2))

    # Professional Summary
    story += section_heading("Professional Summary", s, AUS_GREEN)
    story.append(Paragraph(
        SUMMARY + " Open to relocating to Australia and available to commence in a new role "
        "with appropriate notice.", s["body_style"]))

    # Work Rights
    story += section_heading("Work Rights", s, AUS_GREEN)
    story.append(Paragraph(
        "Indian national — would require employer-sponsored visa (e.g. TSS 482 or equivalent) "
        "to work in Australia. Open to discussing relocation assistance and visa sponsorship.",
        s["body_style"]))

    # Key Skills
    story += section_heading("Key Skills", s, AUS_GREEN)
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["body_style"]))

    # Professional Experience
    story += section_heading("Professional Experience", s, AUS_GREEN)
    for exp in EXPERIENCE:
        story += job_block(exp, s)

    # Projects
    story += section_heading("Projects", s, AUS_GREEN)
    for proj_title, proj_desc in PROJECTS:
        story.append(Paragraph(proj_title, s["job_title_style"]))
        story.append(Paragraph(f"• {proj_desc}", s["bullet_style"]))
        story.append(Spacer(1, 3))

    # Education
    story += section_heading("Education", s, AUS_GREEN)
    story.append(Paragraph(f"<b>{EDUCATION[0]}</b>", s["job_title_style"]))
    story.append(Paragraph(f"{EDUCATION[1]} | {EDUCATION[2]}", s["company_style"]))

    # Certifications
    story += section_heading("Professional Development", s, AUS_GREEN)
    for c in CERTIFICATIONS:
        story.append(Paragraph(f"• {c}", s["bullet_style"]))

    # Languages
    story += section_heading("Languages", s, AUS_GREEN)
    story.append(Paragraph(
        " | ".join(f"{l} ({p})" for l, _, p in LANGUAGES), s["body_style"]))

    # Licences / Checks
    story += section_heading("Licences & Background Checks", s, AUS_GREEN)
    story.append(Paragraph(
        "Willing to undertake a National Police Check and any role-required background "
        "verification. No Australian licences held at this time (relocating).",
        s["body_style"]))

    # Referees
    story += section_heading("Referees", s, AUS_GREEN)
    story.append(Paragraph("Available on request.", s["body_style"]))

    doc.build(story)
    print(f"  ✓ {os.path.basename(filename)}")


# ══════════════════════════════════════════════════════════════════════════════
# 7. New Zealand — Professional CV
# ══════════════════════════════════════════════════════════════════════════════
def build_nz(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    s = base_styles(NZ_BLACK)
    story = []

    story.append(Paragraph(NAME, s["name_style"]))
    story.append(Paragraph(TITLE, s["title_style"]))
    story.append(Paragraph(
        f"{EMAIL}  |  {PHONE}  |  {LINKEDIN}  |  Hyderabad, India",
        s["contact_style"]))
    story.append(Spacer(1, 2))

    # Professional Summary
    story += section_heading("Professional Summary", s, NZ_BLACK)
    story.append(Paragraph(
        SUMMARY + " Open to relocating to New Zealand and keen to contribute to the "
        "growing AI and tech operations sector.", s["body_style"]))

    # Work Rights
    story += section_heading("Work Rights & Visa", s, NZ_BLACK)
    story.append(Paragraph(
        "Indian national — would require employer-supported Essential Skills Work Visa or "
        "equivalent to work in New Zealand. Open to sponsorship conversations.",
        s["body_style"]))

    # Cultural Statement (valued in NZ CVs)
    story += section_heading("Cultural Fit & Values", s, NZ_BLACK)
    story.append(Paragraph(
        "I respect the principles of Te Tiriti o Waitangi and the bicultural foundations of "
        "Aotearoa. I bring genuine curiosity, team orientation, and a collaborative approach "
        "to every role, aligned with New Zealand's inclusive workplace culture.",
        s["body_style"]))

    # Key Skills
    story += section_heading("Key Skills", s, NZ_BLACK)
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["body_style"]))

    # Work Experience
    story += section_heading("Work Experience", s, NZ_BLACK)
    for exp in EXPERIENCE:
        story += job_block(exp, s)

    # Projects
    story += section_heading("Projects", s, NZ_BLACK)
    for proj_title, proj_desc in PROJECTS:
        story.append(Paragraph(proj_title, s["job_title_style"]))
        story.append(Paragraph(f"• {proj_desc}", s["bullet_style"]))
        story.append(Spacer(1, 3))

    # Education
    story += section_heading("Education", s, NZ_BLACK)
    story.append(Paragraph(f"<b>{EDUCATION[0]}</b>", s["job_title_style"]))
    story.append(Paragraph(f"{EDUCATION[1]} | {EDUCATION[2]}", s["company_style"]))

    # Professional Development
    story += section_heading("Professional Development", s, NZ_BLACK)
    for c in CERTIFICATIONS:
        story.append(Paragraph(f"• {c}", s["bullet_style"]))

    # Languages
    story += section_heading("Languages", s, NZ_BLACK)
    story.append(Paragraph(
        " | ".join(f"{l} ({p})" for l, _, p in LANGUAGES), s["body_style"]))

    # Referees
    story += section_heading("Referees", s, NZ_BLACK)
    story.append(Paragraph("Two referees available on request.", s["body_style"]))

    doc.build(story)
    print(f"  ✓ {os.path.basename(filename)}")


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    builds = [
        ("01_Manish_USA_Resume.pdf", build_usa),
        ("02_Manish_UK_CV.pdf", build_uk),
        ("03_Manish_EU_Europass_CV.pdf", build_eu),
        ("04_Manish_Japan_Resume.pdf", build_japan),
        ("05_Manish_India_CV.pdf", build_india),
        ("06_Manish_Australia_Resume.pdf", build_australia),
        ("07_Manish_NewZealand_CV.pdf", build_nz),
    ]

    print("Generating PDFs...\n")
    for fname, fn in builds:
        filepath = os.path.join(OUT_DIR, fname)
        try:
            fn(filepath)
        except Exception as e:
            print(f"  ✗ {fname}: {e}")
            import traceback; traceback.print_exc()

    print("\nAll done!")
