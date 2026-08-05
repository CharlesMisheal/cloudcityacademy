"""
CloudCity Academy — school-style curricula.

Durations (weeks ≈ months × 4):
  Office suite → 1 month (4 weeks)
  Intro / creative foundations → 3 months (12 weeks)
  Intermediate applied skills → 4 months (16 weeks)
  Professional tracks → 6 months (24 weeks)
"""

from __future__ import annotations

import json

# slug → duration months
COURSE_DURATION_MONTHS = {
    "office-ms-word": 1,
    "office-excel": 1,
    "office-powerpoint": 1,
    "graphic-ai": 1,
    "video-editing-ai": 1,
    "graphic-coreldraw": 3,
    "scratch": 3,
    "python-for-beginners": 3,
    "python-blocks": 3,
    "system-design-thinking": 4,
    "python-data-apps": 4,
    "website-development": 4,
    "cloud-computing": 4,
    "ai-engineer": 6,
    "python-developer": 6,
    "android-app-development": 6,
}


def weeks_for(slug: str) -> int:
    return COURSE_DURATION_MONTHS.get(slug, 3) * 4


def duration_label(slug: str) -> str:
    m = COURSE_DURATION_MONTHS.get(slug, 3)
    return f"{m} month" if m == 1 else f"{m} months"


# Progressive topic lists — index 0 = week 1. Must match weeks_for(slug).
TOPICS: dict[str, list[str]] = {
    "office-ms-word": [
        "Getting started — Word window, new document, typing and saving",
        "Text formatting — fonts, sizes, bold/italic, alignment, lists",
        "Page layout — margins, headers, footers, page numbers, images",
        "Capstone week — multi-page formal letter or short report",
    ],
    "office-excel": [
        "Getting started — workbook, sheets, cells, data entry and save",
        "Formulas basics — SUM, AVERAGE, simple arithmetic references",
        "Tables & charts — sort, filter, basic chart types",
        "Capstone week — student results sheet or simple budget workbook",
    ],
    "office-powerpoint": [
        "Getting started — slides, themes, titles and bullet text",
        "Design basics — layouts, images, smart art, consistency",
        "Presentation craft — animations carefully, transitions, speaker notes",
        "Capstone week — 8–10 slide presentation on a school topic",
    ],
    "graphic-coreldraw": [
        "Workspace & tools — interface tour, new document, save .cdr",
        "Shapes & selection — rectangles, ellipses, transform handles",
        "Colour fundamentals — fills, outlines, colour palettes",
        "Text in design — artistic vs paragraph text, kerning intro",
        "Alignment & guides — rulers, snapping, clean layouts",
        "Combining objects — group, weld, trim, intersect basics",
        "Logo craft I — simple marks with shapes and typography",
        "Logo craft II — variants and export for screen",
        "Poster layout — hierarchy, margins, visual balance",
        "Print basics — bleed, export PDF, colour modes overview",
        "Brand mini-kit — logo + colour chips + sample poster",
        "Capstone — client-style brief (flyer or business card set)",
    ],
    "graphic-ai": [
        "AI design foundations — tools overview, safe prompts, file export",
        "Still images & composition — subject, style, contrast, hierarchy",
        "Brand & social assets — logos marks, posts, stories, mockups",
        "Capstone week — mini campaign (3 assets + one clear brand style)",
    ],
    "video-editing-ai": [
        "Editor basics — timeline, import, cuts, project save",
        "Story & sound — B-roll, levels, captions, readable titles",
        "AI assist & polish — cleanup helpers, exports (16:9 and 9:16)",
        "Capstone week — 45–90 second promo or tutorial, finished export",
    ],
    "ai-engineer": [
        "What is AI? — concepts without hype",
        "Data, models, and predictions — pipeline mental model",
        "Prompt engineering fundamentals",
        "Structured prompts — roles, constraints, formats",
        "Classification vs generation vs retrieval",
        "Evaluating outputs — accuracy, bias, hallucination",
        "Working with APIs — keys, requests, responses (conceptual)",
        "Chatbots design — system messages and tool use overview",
        "RAG idea — grounding answers in your documents",
        "Embeddings & similarity (conceptual)",
        "Safety & responsible AI policies",
        "Mini project plan — problem → data → metric",
        "Building a simple AI feature flow",
        "Logging, monitoring, and failures",
        "Fine-tuning vs prompting — when each makes sense",
        "Agents overview — multi-step tasks",
        "Cost & performance trade-offs",
        "Testing AI features",
        "Privacy and local vs cloud models",
        "Documentation for AI systems",
        "Integration patterns in apps",
        "Ethics case studies",
        "Portfolio project assemble",
        "Capstone — design & demo a small AI solution end-to-end",
    ],
    "python-developer": [
        "Python setup & first script",
        "Types, variables, and operators",
        "Control flow — if / else",
        "Loops — for and while",
        "Functions and parameters",
        "Lists, tuples, dictionaries, sets",
        "Strings and file I/O",
        "Errors and exceptions",
        "Modules and packages",
        "Virtual environments & dependencies",
        "OOP I — classes and objects",
        "OOP II — inheritance and composition",
        "Working with JSON and APIs (requests style)",
        "Testing basics — assert and simple tests",
        "Debugging techniques",
        "Git basics for developers",
        "Code style & readability (PEP 8 spirit)",
        "CLI tools with argparse",
        "Data validation patterns",
        "Databases intro (SQLite)",
        "Building a small library module",
        "Refactoring practice",
        "Project structure & packaging intro",
        "Capstone — polished multi-file Python project",
    ],
    "system-design-thinking": [
        "What is a system? — parts, flows, goals",
        "Design thinking — empathise and define",
        "Ideate & prototype mindsets",
        "User stories and problem framing",
        "Requirements vs constraints",
        "Diagrams — simple flowcharts",
        "Data as information flow",
        "Interfaces between parts of a system",
        "Scalability idea (simple language)",
        "Failure modes and resilience thinking",
        "Trade-offs — cost, speed, quality",
        "Architecture sketches for small apps",
        "Feedback loops and iteration",
        "Case study: school registration flow",
        "Case study: marketplace checklist",
        "Capstone — design a system for a local problem",
    ],
    "python-data-apps": [
        "Python review for data work",
        "CSV files and tables of data",
        "Cleaning messy values",
        "Summaries — count, mean, min, max",
        "Charts with a simple plotting approach",
        "Asking good data questions",
        "Filtering and grouping",
        "Joining datasets conceptually",
        "Building a tiny analysis notebook/script",
        "Dashboards idea — inputs and metrics",
        "Streaming vs batch (concepts)",
        "Data ethics and privacy",
        "Exporting results for non-technical readers",
        "Automating a weekly report",
        "App shell for data input (form → table)",
        "Capstone — small data app with chart + insight write-up",
    ],
    "python-blocks": [
        "Block coding environment & drag-drop habits",
        "Sequences — do steps in order",
        "Events — when green flag / when clicked",
        "Loops the visual way",
        "Conditions — if / else blocks",
        "Variables with blocks",
        "Sprites, costumes, motion",
        "Scoring and simple game state",
        "Messages / broadcasts between pieces",
        "From blocks to Python keywords (mapping)",
        "Mini project — quiz or story",
        "Capstone — interactive project + short demo",
    ],
    "scratch": [
        "Scratch stage, sprites, backpacks",
        "Motion and looks blocks",
        "Sound and timing",
        "Events and control",
        "Sensing — touching, keys, mouse",
        "Variables and lists intro",
        "My Blocks (custom blocks)",
        "Storytelling project",
        "Game mechanics — score and lives",
        "Debugging broken scripts",
        "Remix & credit others’ work",
        "Capstone — finished game or interactive story",
    ],
    "android-app-development": [
        "Android ecosystem & tools overview",
        "Project structure of a simple app",
        "Layouts — views and view groups",
        "Text, buttons, images on screen",
        "Activities and navigation",
        "User input and validation",
        "Lists and scrolling content",
        "Resources — colours, strings, assets",
        "Simple state on screen",
        "Intents and moving between screens",
        "Permissions & app safety basics",
        "Data storage intro (preferences / local)",
        "Networking overview (loading remote content)",
        "Material design spirit — spacing and touch",
        "Debugging crashes calmly",
        "App icons and branding assets",
        "Build & run on emulator/device",
        "Testing flows manually",
        "Accessibility basics",
        "Performance awareness",
        "Publishing checklist overview",
        "Iteration from user feedback",
        "Polish week",
        "Capstone — ship-ready simple utility app",
    ],
    "website-development": [
        "How the web works — browser, server, URL",
        "HTML structure — headings, paragraphs, lists",
        "Links, images, and semantic tags",
        "CSS basics — colours, fonts, box model",
        "Layout with flexbox",
        "Responsive design — mobile first idea",
        "Navigation bars and multi-page sites",
        "Forms and inputs",
        "Accessibility basics for web",
        "Images and performance care",
        "Simple JavaScript interactivity",
        "Hosting intro — publishing a static site",
        "Content & UX writing for pages",
        "SEO basics for beginners",
        "Project: multi-section landing page",
        "Capstone — personal or business mini website",
    ],
    "python-for-beginners": [
        "Hello Python — print and comments",
        "Variables and simple data types",
        "User input and conversion",
        "Math and comparison operators",
        "Making decisions with if",
        "While loops for repetition",
        "For loops and ranges",
        "Lists of data",
        "String methods you will use daily",
        "Functions for reusable steps",
        "Reading and writing simple files",
        "Capstone — tiny menu-driven program",
    ],
    "cloud-computing": [
        "What is the cloud? — shared computers far away",
        "IaaS, PaaS, SaaS explained simply",
        "Regions, availability, and reliability idea",
        "Storage types — files vs databases overview",
        "Compute — virtual machines and containers idea",
        "Networking basics in the cloud",
        "Identity and access — accounts and permissions",
        "Security shared responsibility model",
        "Deploying a simple static site to the cloud",
        "Monitoring and logs for ops awareness",
        "Cost awareness and free tiers",
        "Serverless / functions overview",
        "Databases in the cloud landscape",
        "Backup and disaster recovery basics",
        "Case study: school portal on the cloud",
        "Capstone — architecture proposal for a small app",
    ],
}


def _phase(week_num: int, total: int) -> str:
    ratio = week_num / total
    if ratio <= 0.34:
        return "Foundation"
    if ratio <= 0.67:
        return "Building skill"
    return "Application & mastery"


def week_title(week_num: int, topic: str) -> str:
    short = topic.split("—")[0].strip() if "—" in topic else topic
    if len(short) > 52:
        short = short[:49] + "…"
    return f"Week {week_num}: {short}"


def lesson_content(course_title: str, week_num: int, total: int, topic: str) -> str:
    phase = _phase(week_num, total)
    goals = [
        f"Understand the core idea behind: {topic.split('—')[0].strip()}.",
        "Practise with a guided classroom exercise.",
        "Prepare evidence (screenshot) for this week’s assessment.",
    ]
    steps = [
        "Open notes before you open the software/tool.",
        "Follow the example exactly once, then try a small variation.",
        "Save with clear naming: YourName_Week%02d." % week_num,
        "Ask questions early if you are stuck for more than 10 minutes.",
    ]
    if week_num == total:
        steps.append(
            "Complete the capstone to school standard — neat, complete, and explainable."
        )
    elif week_num == 1:
        steps.insert(0, "Create your course folder and save today’s starter file there.")

    return (
        f"[[CCA_CURRICULUM_V1]]\n"
        f"Course: {course_title}\n"
        f"Week {week_num} of {total} ({phase})\n\n"
        f"Topic\n{topic}\n\n"
        f"Learning goals\n"
        + "\n".join(f"• {g}" for g in goals)
        + "\n\nClass flow\n"
        + "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
        + "\n\nStandards\n"
        "Work should be readable, saved correctly, and finished before submission. "
        "Difficulty rises week by week — master this week before rushing ahead."
    )


def lesson_examples(course_title: str, week_num: int, topic: str) -> str:
    key = topic.lower()
    if "python" in course_title.lower() or "python" in key:
        if week_num <= 2:
            return (
                'print("Hello, CloudCity")\n'
                'name = "Ada"\n'
                'print("Welcome,", name)'
            )
        if "if" in key or "decision" in key:
            return (
                "score = 75\n"
                "if score >= 50:\n"
                '    print("Pass")\n'
                "else:\n"
                '    print("Try again")'
            )
        if "loop" in key or "for" in key or "while" in key:
            return (
                "for n in range(1, 6):\n"
                '    print("Practice", n)'
            )
        if "function" in key:
            return (
                "def greet(name):\n"
                '    return "Hello, " + name\n\n'
                'print(greet("CloudCity"))'
            )
        return (
            "# Week %d practice skeleton\n"
            "def main():\n"
            "    # complete the task for: %s\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    main()"
        ) % (week_num, topic.split("—")[0].strip())

    if "excel" in course_title.lower() or "excel" in key:
        return (
            "Sample cells:\n"
            "A1: Item | B1: Qty | C1: Price\n"
            "A2: Pens | B2: 10 | C2: 50\n"
            "D2 formula: =B2*C2\n"
            "Total: =SUM(D2:D20)"
        )
    if "word" in course_title.lower():
        return (
            "Document setup checklist:\n"
            "• Font: clear, 12pt body\n"
            "• Title: large + bold\n"
            "• Margin: Normal\n"
            "• Save as: YourName_Letter.docx"
        )
    if "power" in course_title.lower():
        return (
            "Slide skeleton:\n"
            "1. Title + your name\n"
            "2. Agenda (3 bullets)\n"
            "3–7. One idea per slide\n"
            "8. Summary + thank you"
        )
    if "corel" in course_title.lower() or "graphic" in course_title.lower():
        return (
            "Layout checklist:\n"
            "1. Set page size first\n"
            "2. Create guides / margins\n"
            "3. Place main shape\n"
            "4. Add text last for hierarchy\n"
            "5. Export PNG + keep .cdr source"
        )
    if "android" in course_title.lower():
        return (
            "Screen checklist:\n"
            "• Clear title\n"
            "• One primary button\n"
            "• Readable text size\n"
            "• No overlapping controls"
        )
    if "website" in course_title.lower() or "html" in key:
        return (
            "<!DOCTYPE html>\n<html>\n<head>\n"
            "  <title>My Page</title>\n"
            "</head>\n<body>\n"
            "  <h1>Welcome</h1>\n"
            "  <p>CloudCity practice page.</p>\n"
            "</body>\n</html>"
        )
    if "scratch" in course_title.lower() or "block" in course_title.lower():
        return (
            "Block flow:\n"
            "when green flag clicked\n"
            "  forever\n"
            "    if key space pressed?\n"
            "      change y by 10"
        )
    if "video" in course_title.lower():
        return (
            "Edit rhythm:\n"
            "Hook (0–3s) → Main demo → Caption callout → End card\n"
            "Export: H.264, clear audio, correct aspect ratio"
        )
    if "cloud" in course_title.lower():
        return (
            "Architecture sketch labels:\n"
            "User → Web app → Storage\n"
            "           └→ Database\n"
            "Add: Auth, Backup, Monitor"
        )
    return (
        f"Practice focus (Week {week_num}):\n"
        f"• Topic: {topic}\n"
        f"• Do one guided example with your teacher\n"
        f"• Then complete a variation unsupervised\n"
        f"• Screenshot the finished attempt"
    )


def week_questions(course_title: str, week_num: int, total: int, topic: str) -> list:
    """2 MCQ + 1 subjective + 1 upload, difficulty rising."""
    focus = topic.split("—")[0].strip()
    hard = week_num > total // 2
    mcq1_opts = [
        "Skip practice and only read notes",
        f"Complete a hands-on exercise on: {focus}",
        "Wait until the last day of the term",
        "Ignore saving files",
    ]
    mcq1_ans = mcq1_opts[1]

    if hard:
        mcq2_prompt = f"For Week {week_num}, which approach shows higher skill?"
        mcq2_opts = [
            "Copy without understanding",
            "Explain your steps and produce a clean finished file",
            "Submit empty work",
            "Only take screenshots of others",
        ]
        mcq2_ans = mcq2_opts[1]
    else:
        mcq2_prompt = "Before submitting this week you should:"
        mcq2_opts = [
            "Delete your practice file",
            "Save with a clear name and check your work",
            "Change nothing from last week",
            "Avoid the examples",
        ]
        mcq2_ans = mcq2_opts[1]

    if week_num == total:
        subj = (
            f"Describe your final project for {course_title}: what you built, "
            "what problem it solves, and one improvement you would make next."
        )
        upload = (
            "Upload a screenshot of your finished capstone project "
            "(full work visible, readable, and named correctly)."
        )
    else:
        subj = (
            f"In 3–5 sentences, explain what you practised this week about “{focus}” "
            "and one challenge you faced."
        )
        upload = (
            f"Upload a clear screenshot of this week’s completed task ({focus})."
        )

    return [
        ("mcq", f"The main practical goal of Week {week_num} is to:",
         json.dumps(mcq1_opts), mcq1_ans, 2, 1),
        ("mcq", mcq2_prompt, json.dumps(mcq2_opts), mcq2_ans, 2, 2),
        ("subjective", subj, None, None, 3 if hard else 2, 3),
        ("upload", upload, None, None, 3, 4),
    ]


def curriculum_for(slug: str) -> list[dict]:
    topics = TOPICS.get(slug)
    if not topics:
        n = weeks_for(slug)
        topics = [f"Progressive practice module {i}" for i in range(1, n + 1)]
    # Ensure length matches duration
    target = weeks_for(slug)
    if len(topics) < target:
        topics = topics + [
            f"Extended practice {i}" for i in range(len(topics) + 1, target + 1)
        ]
    topics = topics[:target]
    return [{"week": i + 1, "topic": t} for i, t in enumerate(topics)]
