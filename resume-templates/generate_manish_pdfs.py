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
    "Most teams lose 60%+ of operational capacity to manual, repeatable work — that's the "
    "gap I close. Tasked with transforming how B2B and content-first organisations operate, "
    "I have architected 40+ automation pipelines across Make, Zapier, and n8n — integrated "
    "with Claude and GPT-4 — over 6 years in digital operations (2 years AI-focused). "
    "The result: 60% reduction in manual processing time, 3× content throughput, and "
    "ad-hoc spreadsheets replaced by real-time KPI dashboards — without adding headcount."
)

SUMMARY_UK = (
    "Organisations running on manual workflows are spending 60% of their operational capacity "
    "on effort that should not exist. Over six years in digital operations — two of them "
    "dedicated to AI-driven automation — I have designed and deployed 40+ automation pipelines "
    "using Make, Zapier, and n8n, embedded Claude and GPT-4 into 8 live production systems, "
    "and rebuilt ad-hoc reporting into real-time KPI dashboards. Each engagement delivers the "
    "same three outcomes: 60% less manual overhead, 3× content throughput, and decision-making "
    "grounded in data instead of instinct. Currently learning German (A2); open to relocation "
    "within Europe."
)

SUMMARY_DE = (
    "Unternehmen verlieren 60 % ihrer operativen Kapazität durch manuelle, wiederholbare Arbeit — "
    "genau diese Lücke schließe ich. In 6 Jahren digitaler Operations-Erfahrung (2 Jahre KI-fokussiert) "
    "habe ich 40+ Automatisierungs-Workflows in Make, Zapier und n8n aufgebaut und Claude sowie GPT-4 "
    "in 8 Produktionssysteme integriert — mit dem Ergebnis: 60 % weniger manueller Aufwand, "
    "3-facher Content-Durchsatz, Echtzeit-KPI-Dashboards statt Ad-hoc-Tabellen. "
    "Deutschlerner (A2), offen für Relocation nach Deutschland oder in die Niederlande."
)

SUMMARY_JP = (
    "I am an AI Operations specialist with 6+ years in digital and global operations. "
    "My value is concrete: I have built 40+ automation workflows that cut manual processing "
    "by 60% and managed 400+ digital assets across 40+ international markets with zero "
    "compliance breaches. I combine the precision required in enterprise publishing "
    "(Cambridge University Press) with the speed and scale of AI-native content systems. "
    "I bring reliability, data discipline, and a motivated learner's approach to every team."
)

SUMMARY_IN = (
    "Results-driven AI Operations and Automation Specialist with 6+ years of progressive "
    "experience across digital operations, content systems, and business intelligence. "
    "Built 40+ automation workflows (Make, Zapier, n8n) that cut manual effort by 60% and "
    "replaced 4 Excel-based reporting stacks with live KPI dashboards — saving 6+ hours per "
    "client per week. Managed 400+ digital assets across 40 international markets at Cambridge "
    "University Press with zero compliance breaches. Seeking a high-impact role where measurable "
    "delivery and AI-era thinking create compounding value."
)

SUMMARY_AUS = (
    "Most teams are spending 60% of their operational capacity on work automation should be "
    "doing. Over 6 years in digital operations — 2 years AI-focused — I have built 40+ pipelines "
    "in Make, Zapier, and n8n, embedded generative AI into 8 live systems, and turned ad-hoc "
    "reporting into real-time KPI dashboards. The numbers: 60% reduction in manual processing, "
    "3× content throughput, 400+ assets delivered across 40 international markets with zero "
    "compliance incidents. Open to relocating to Australia and available to start with appropriate notice."
)

SUMMARY_NZ = (
    "Operational capacity lost to manual tasks is the most common and most fixable problem in "
    "digital teams. Over 6 years — 2 of them AI-focused — I have built 40+ automation pipelines, "
    "embedded Claude and GPT-4 into 8 production systems, and redesigned reporting from "
    "spreadsheets to real-time dashboards. Delivered: 60% less manual effort, 3× content output, "
    "400+ assets coordinated across 40 markets with zero compliance breaches. "
    "Keen to bring that record to a New Zealand team and contribute to Aotearoa's growing tech sector."
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
            "Designed and deployed 40+ no-code automation workflows (Make, Zapier, n8n) across 8 B2B "
            "client accounts, cutting manual operational effort by ~60% and enabling 3× content "
            "throughput — with zero headcount increase.",
            "Embedded generative AI (Claude, GPT-4) into 6 client reporting and content pipelines; "
            "replaced 4 manual Excel-based reporting stacks with real-time KPI dashboards, saving an "
            "average of 6 hours per client per week.",
            "Managed 8 concurrent client engagements as sole point of contact — scoping, delivery, "
            "and iteration — achieving 100% on-time delivery across all active projects.",
        ],
    },
    {
        "title": "Social Media Manager",
        "company": "Spotlit AI", "location": "Remote",
        "dates": "Jan 2024 – Mar 2025",
        "bullets": [
            "Operated LinkedIn and Instagram content on automation-first workflows, publishing 5–7 "
            "posts per day per platform while reducing manual publishing effort by ~60% versus "
            "the manual baseline.",
            "Deployed AI-assisted content systems (Claude, GPT-4) that delivered a 34% improvement "
            "in average post reach quarter-over-quarter across a 15-month engagement.",
            "Applied GEO and AEO optimisation to 3 recurring content formats, improving AI-search "
            "surface discoverability and contributing to a 20%+ increase in inbound traffic.",
        ],
    },
    {
        "title": "Social Media Manager & Content Designer",
        "company": "Keyblocks Strategy", "location": "Hyderabad, India",
        "dates": "Mar 2023 – Dec 2023",
        "bullets": [
            "Built and executed content strategies for 6 B2B technology and business clients; "
            "introduced AI-assisted production systems that reduced per-piece turnaround time by 40%.",
            "Coordinated a 4-person content team across 6 simultaneous client accounts, delivering "
            "200+ content pieces over 9 months with zero missed client deadlines.",
            "Ran multi-channel digital campaigns (LinkedIn, Instagram, Twitter) for 6 clients, "
            "aligning each quarterly initiative with stakeholder-agreed OKRs.",
        ],
    },
    {
        "title": "Content Moderator (Meta, via Wipro)",
        "company": "Wipro", "location": "Hyderabad, India",
        "dates": "Aug 2021 – Jan 2023",
        "bullets": [
            "Reviewed and actioned 200+ pieces of user-generated content daily against Meta's "
            "platform policies, sustaining 99%+ policy accuracy across an 18-month tenure.",
            "Operated within a metrics-driven trust & safety queue processing millions of items "
            "monthly; consistently met throughput SLAs across 3 major policy framework updates.",
            "Adapted to revised escalation workflows within 48-hour retraining windows on each "
            "policy change — zero accuracy regression recorded on post-update audits.",
        ],
    },
    {
        "title": "Media Delivery Coordinator",
        "company": "Cambridge University Press", "location": "Hyderabad, India",
        "dates": "Jun 2019 – Aug 2021",
        "bullets": [
            "Served as central coordination point for 400+ digital assets across editorial, legal, "
            "and production pipelines — ensuring zero compliance breaches across a 2-year tenure.",
            "Managed artwork commissioning and rights compliance across 40+ international markets, "
            "coordinating with rights holders and studios across 6 time zones simultaneously.",
            "Oversaw end-to-end voiceover and audio production for 30+ educational titles, delivering "
            "all assets to global distribution deadlines across 3 continents.",
        ],
    },
]

PROJECTS = [
    ("AI-Powered Content Automation System",
     "Architected a Make + Claude pipeline handling 3,000+ content items per month across 3 "
     "channels — cut production time by 60% and standardised output quality across all formats."),
    ("Business Intelligence Reporting Framework",
     "Replaced 4 manual Excel-based reporting stacks with live KPI dashboards; reduced weekly "
     "reporting overhead by 6+ hours per client and enabled same-day decision-making."),
]

# Accomplishments — strongest career facts, metric-first, no fluff
ACCOMPLISHMENTS = [
    ("40+ automation pipelines built",
     "Cut manual processing 60% across 8 client accounts — zero headcount increase required."),
    ("4 Excel reporting stacks replaced",
     "Live KPI dashboards now serve 8 clients, saving 6+ hours per client per week."),
    ("400+ digital assets coordinated",
     "Across 40+ international markets at Cambridge University Press — zero compliance breaches in 2 years."),
    ("200+ content items reviewed daily",
     "99%+ policy accuracy at Meta (via Wipro) sustained across 18 consecutive months."),
    ("3× content throughput achieved",
     "34% average post reach improvement QoQ over 15 months at Spotlit AI."),
    ("4-person team · 6 accounts · 200+ deliverables",
     "9-month engagement at Keyblocks Strategy — zero missed client deadlines."),
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


def accomplishments_block(styles, accent=NAVY):
    """
    Two-column achievement table: metric (left, accent-bold) | context (right, normal).
    Subtle LGREY fill makes the eye land here without screaming for attention.
    """
    metric_style = ParagraphStyle(
        "ach_metric", fontSize=8.8, fontName="Helvetica-Bold",
        textColor=accent, leading=12)
    ctx_style = ParagraphStyle(
        "ach_ctx", fontSize=8.8, fontName="Helvetica",
        textColor=colors.HexColor("#374151"), leading=12)

    rows = []
    for metric, context in ACCOMPLISHMENTS:
        rows.append([
            Paragraph(metric, metric_style),
            Paragraph(context, ctx_style),
        ])

    tbl = Table(rows, colWidths=["32%", "68%"])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LGREY),
        ("LEFTPADDING",  (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [LGREY, colors.HexColor("#e9eaf0")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, colors.HexColor("#d1d5db")),
    ]))
    return [tbl]


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

    # Selected Achievements — metric-first, two-column
    story += section_heading("Selected Achievements", s)
    story += accomplishments_block(s, NAVY)

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
    story.append(Paragraph(SUMMARY_UK, s["body_style"]))

    # Key Achievements
    story += section_heading("Key Achievements", s)
    story += accomplishments_block(s, NAVY)

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
    story.append(Paragraph(SUMMARY_DE, s["body_style"]))

    # Key Achievements
    story += section_heading("Key Achievements", s, EURO_GREEN)
    story += accomplishments_block(s, EURO_GREEN)

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
    story.append(Paragraph(SUMMARY_JP, s["body_style"]))
    story.append(Spacer(1, 4))

    # 実績 / Achievements
    story += section_heading("実績 / Key Achievements", s, JP_RED)
    story += accomplishments_block(s, JP_RED)

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
    story.append(Paragraph(SUMMARY_IN, s["body_style"]))

    # Key Achievements
    story += section_heading("Key Achievements", s, accent)
    story += accomplishments_block(s, accent)

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
    story.append(Paragraph(SUMMARY_AUS, s["body_style"]))

    # Key Achievements
    story += section_heading("Key Achievements", s, AUS_GREEN)
    story += accomplishments_block(s, AUS_GREEN)

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
    story.append(Paragraph(SUMMARY_NZ, s["body_style"]))

    # Key Achievements
    story += section_heading("Key Achievements", s, NZ_BLACK)
    story += accomplishments_block(s, NZ_BLACK)

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
