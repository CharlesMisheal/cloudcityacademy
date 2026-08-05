"""
CloudCity Academy — deep school-style lesson packs (V3).

Each week includes:
  objectives, why-it-matters, key concepts, extended notes,
  timed class walkthrough, multi-step practice, success criteria,
  vocabulary, examples, 3 MCQs + written + upload.
"""
from __future__ import annotations

import json
import re
from typing import Any

from curriculum import TOPICS, weeks_for

MARKER = "[[CCA_CURRICULUM_V3]]"


def _mcq(prompt: str, options: list[str], correct: str, points: int = 2, order: int = 1):
    return ("mcq", prompt, json.dumps(options), correct, points, order)


def _build_body(
    course: str,
    week: int,
    total: int,
    title: str,
    objectives: list[str],
    why: str,
    concepts: list[tuple[str, str]],
    theory: str,
    demos: list[str],
    practice: list[str],
    success: list[str],
    mistakes: list[str],
    vocab: list[tuple[str, str]],
    stretch: str,
    homework: str,
) -> str:
    phase = (
        "Foundation"
        if week / total <= 0.34
        else ("Building skill" if week / total <= 0.67 else "Application & mastery")
    )
    lines = [
        MARKER,
        f"Course: {course}",
        f"Week {week} of {total} · {phase}",
        f"Estimated study time this week: 4–6 hours (class + practice)",
        "",
        f"Lesson title: {title}",
        "",
        "1) Learning objectives",
        "By the end of this week you should be able to:",
        *[f"  • {o}" for o in objectives],
        "",
        "2) Why this week matters",
        why.strip(),
        "",
        "3) Key concepts",
    ]
    for name, meaning in concepts:
        lines.append(f"  • {name}: {meaning}")
    lines += [
        "",
        "4) Detailed lesson notes",
        theory.strip(),
        "",
        "5) Teacher walkthrough (about 25–40 minutes in class)",
        *[f"  {i}. {s}" for i, s in enumerate(demos, 1)],
        "",
        "6) Guided + independent practice",
        *[f"  {i}. {s}" for i, s in enumerate(practice, 1)],
        "",
        "7) What “good work” looks like (success criteria)",
        *[f"  • {s}" for s in success],
        "",
        "8) Common mistakes",
        *[f"  • {m}" for m in mistakes],
        "",
        "9) Vocabulary",
        *[f"  • {t}: {d}" for t, d in vocab],
        "",
        "10) Stretch challenge",
        f"  {stretch.strip()}",
        "",
        "11) Home practice before next class",
        f"  {homework.strip()}",
        "",
        "12) Weekly assessment",
        "  Complete all quiz items, write the reflection carefully, and upload a clear",
        "  screenshot that proves you finished this week’s main practice (readable text,",
        "  full window/file name where possible).",
    ]
    return "\n".join(lines)


def _week(
    course: str,
    week: int,
    total: int,
    title: str,
    objectives: list[str],
    why: str,
    concepts: list[tuple[str, str]],
    theory: str,
    demos: list[str],
    practice: list[str],
    success: list[str],
    mistakes: list[str],
    vocab: list[tuple[str, str]],
    stretch: str,
    homework: str,
    examples: str,
    mcqs: list[tuple],
    subjective: str,
    upload: str,
) -> dict[str, Any]:
    body = _build_body(
        course,
        week,
        total,
        title,
        objectives,
        why,
        concepts,
        theory,
        demos,
        practice,
        success,
        mistakes,
        vocab,
        stretch,
        homework,
    )
    questions = []
    for i, (prompt, opts, correct) in enumerate(mcqs, 1):
        questions.append(_mcq(prompt, opts, correct, 2, i))
    questions.append(("subjective", subjective, None, None, 4, len(questions) + 1))
    questions.append(("upload", upload, None, None, 4, len(questions) + 1))
    return {
        "week": week,
        "title": f"Week {week}: {title}",
        "topic": title,
        "content": body,
        "examples": examples.strip(),
        "questions": questions,
    }


# ── Deep 1-month office + AI packs ────────────────────────────


def _office_word(course: str, total: int) -> list[dict]:
    return [
        _week(
            course,
            1,
            total,
            "Word interface, new documents, typing and saving",
            [
                "Name and use the Ribbon, document area, title bar, and status bar",
                "Create a new document, type multi-paragraph text, and navigate with keyboard and mouse",
                "Save and re-open a .docx using professional file naming",
                "Use Undo, Redo, Select All, and Find at a beginner level",
            ],
            "Almost every office job and many school tasks begin in Word. If you cannot confidently "
            "create, type, save, and reopen a document, later formatting and reports will fail. "
            "This week builds the non-negotiable habits of professional document work.",
            [
                ("Ribbon", "Tool tabs at the top (Home, Insert, Layout, etc.)"),
                ("Document area", "The white page where you type"),
                ("Save vs Save As", "Save updates the current file; Save As creates a named copy or new location"),
                (".docx", "Modern Word file format used for school and work"),
            ],
            """Microsoft Word is a word processor: software for writing letters, reports, notes, and forms.

A) Understand the window
- Title bar shows the file name once saved (Document1 means “not properly named yet”).
- The Ribbon groups tools: Home (type appearance), Insert (tables/pictures), Layout (margins).
- The insertion point (flashing cursor) is where text appears when you type.
- Status bar shows page number and word count — useful for school assignments with length limits.

B) Typing with intent
Type in full sentences. Press Enter only for a new paragraph, not for every line.
Use Backspace to fix mistakes and Ctrl+Z (Undo) when you delete too much.
Select text by dragging; double-click a word; triple-click a paragraph.

C) Saving is part of the work, not an afterthought
Choose File → Save As the first time. Pick the class folder or USB path teachers require.
Name pattern: Firstname_Lastname_Week01_Intro.docx
Then use Ctrl+S regularly. Closing Word without saving can destroy a full lesson’s work.

D) Prove the save worked
Close the file completely, reopen it from the folder (not from memory). If your text is there, you saved correctly.

E) Accessibility and neatness baseline
Use a readable font even this week (e.g. Calibri or Times New Roman 12pt). Avoid typing in all caps for long text.""",
            [
                "Project the blank Word window; name each major region while students point",
                "Type a sample paragraph and deliberately use Undo/Redo",
                "Save As into the class folder with the naming pattern on screen",
                "Close Word, reopen from File Explorer/Finder, and add one sentence to prove the workflow",
            ],
            [
                "Create YourName_Week01_Intro.docx",
                "Write a title line (your full name) and 3 short paragraphs: (1) about you, (2) course goal, (3) computer experience",
                "Each paragraph must be at least 3 sentences",
                "Save, close Word, reopen the file, add a 4th paragraph “What I will practise daily”, Save again",
                "Write the full folder path (or clear folder name) where the file lives at the top of the document",
            ],
            [
                "File reopens with all paragraphs present",
                "File name follows class pattern and is visible on the title bar",
                "Paragraphs are real paragraphs (not one long line of Enter spam)",
                "Path/folder note is written accurately",
            ],
            [
                "Relying on auto-recover instead of intentional Save",
                "Saving to Downloads with name Document1.docx",
                "Pressing Enter after every few words",
                "Working on the wrong language keyboard layout unnoticed",
            ],
            [
                ("Cursor / insertion point", "Blinking line showing where typing will appear"),
                ("Word wrap", "Text moves to the next line automatically at the margin"),
                ("Title bar", "Top bar showing program and file name"),
            ],
            "Add a fifth short paragraph listing three computer lab rules you will follow.",
            "Repeat the full close-and-reopen test at home or in the next free period and note the time it took.",
            """FILE HABITS
Save As → choose Class/Office/Word/
Name: Ada_Okoro_Week01_Intro.docx
Then Ctrl+S every few minutes.

KEYBOARD
Ctrl+S Save | Ctrl+Z Undo | Ctrl+Y Redo | Ctrl+A Select all

CHECK
Title bar must NOT say Document1 after Save As.""",
            [
                (
                    "Where do you choose the folder and name the first time?",
                    ["Home → Bold", "File → Save As", "View → Zoom", "Layout → Columns"],
                    "File → Save As",
                ),
                (
                    "Document1 on the title bar usually means:",
                    [
                        "The file is fully named and archived",
                        "The document may not yet have a proper Save As name",
                        "Word is offline only",
                        "The keyboard is broken",
                    ],
                    "The document may not yet have a proper Save As name",
                ),
                (
                    "Best student naming example:",
                    ["final", "asdf.docx", "Ada_Okoro_Week01_Intro.docx", "New Microsoft Word Document (5)"],
                    "Ada_Okoro_Week01_Intro.docx",
                ),
            ],
            "Describe step-by-step how you created, saved, closed, and reopened your file. Include the folder name and final file name.",
            "Screenshot of Word with your text visible AND the correct file name on the title bar.",
        ),
        _week(
            course,
            2,
            total,
            "Formatting text — emphasis, lists, alignment, styles habit",
            [
                "Apply font, size, bold/italic, and highlight sparingly for meaning",
                "Create bullet and numbered lists the correct way (not manual dashes only)",
                "Align title and body appropriately",
                "Use Format Painter to copy formatting consistently",
            ],
            "Readers judge documents in seconds. Clear hierarchy (title vs body vs lists) makes school work "
            "look intentional and easier to mark. Formatting is communication, not decoration.",
            [
                ("Hierarchy", "Visual order: what is most important appears stronger"),
                ("Bullets vs numbers", "Bullets for unordered items; numbers for sequences"),
                ("Alignment", "Left, centre, right, justify — each has a purpose"),
                ("Format Painter", "Copies formatting from one selection to another"),
            ],
            """A) Body text standards
For school documents, body text is commonly 11–12 pt. Titles may be 16–22 pt and bold.
Use one font family for body text. Changing fonts every sentence looks unprofessional.

B) Emphasis without chaos
Bold = key term or heading. Italic = light emphasis or titles of works (when taught).
Underline is rare in modern print docs (links online are the exception).
Never format an entire page in bold italic rainbow colours.

C) Lists that work
Type the items, select them, then Home → Bullets or Numbering.
If you renumber later, Word updates automatic numbers — manual “1)” typed by hand breaks easily.
Use Increase/Decrease Indent for sub-points when needed.

D) Alignment
Letters: left-aligned body. Title lines may be centred.
Justify spreads text to both margins — acceptable for longer reports if spacing looks even.

E) Consistency with Format Painter
Select well-formatted title → Format Painter → click another title. This prevents uneven sizing.""",
            [
                "Demonstrate messy vs clean hierarchy with the same text",
                "Build a 5-item numbered procedure live",
                "Show Format Painter across two headings",
            ],
            [
                "Open your Week 01 intro (or recreate it) as YourName_Week02_Formatted.docx",
                "Add a centred title “About Me — Digital Skills”",
                "Body paragraphs: left-aligned 12 pt",
                "Add a numbered list: 5 weekly study habits",
                "Add a bullet list: 4 software tools you hope to learn this term",
                "Bold exactly five important keywords in the whole document (not whole sentences)",
                "Use Format Painter so both list headings match each other",
            ],
            [
                "Clear title distinct from body",
                "Both list types present and properly formatted",
                "No more than two fonts total",
                "Readable spacing (not cramped, not huge empty gaps randomly)",
            ],
            [
                "Manual spaces instead of centre align",
                "Bullet symbols typed as random characters inconsistently",
                "Entire paragraph bold for no reason",
            ],
            [
                ("Point size (pt)", "Unit for font height"),
                ("Indent", "Space from margin to text start"),
                ("Selection", "Highlighted text ready for a command"),
            ],
            "Add a small two-level list (main bullets + one indented sub-bullet under two items).",
            "Re-read your document aloud and fix any sentence that is hard to say — clarity first.",
            """HOME TAB MAP
Font group: font name, size, B I U
Paragraph group: bullets, numbering, align buttons
Clipboard: Format Painter (paintbrush)

RULE OF THUMB
Title = larger + bold
Body = 12pt regular
Lists = automatic bullets/numbers""",
            [
                (
                    "Automatic numbered lists are better than typing 1) 2) by hand because:",
                    [
                        "They look colourful",
                        "Renumbering stays consistent when you insert items",
                        "They remove the need to save",
                        "They lock the file",
                    ],
                    "Renumbering stays consistent when you insert items",
                ),
                (
                    "A clean body text size for letters is usually:",
                    ["6 pt", "12 pt", "48 pt", "1 pt"],
                    "12 pt",
                ),
                (
                    "Format Painter is used to:",
                    [
                        "Copy formatting",
                        "Delete pages",
                        "Translate language",
                        "Compress images only",
                    ],
                    "Copy formatting",
                ),
            ],
            "Explain three formatting decisions you made and how each helps a teacher read your work faster.",
            "Screenshot showing title, body, numbered list, and bullet list on one screen if possible.",
        ),
        _week(
            course,
            3,
            total,
            "Page layout — margins, headers, footers, images, multi-page control",
            [
                "Set margins and orientation for print-ready pages",
                "Insert headers, footers, and page numbers correctly",
                "Insert, resize, and wrap images without covering text",
                "Build a mini two-page document with stable structure",
            ],
            "Multi-page school reports fail when margins are wrong, page numbers missing, or images explode the layout. "
            "This week you learn publication basics expected in secondary/college submissions.",
            [
                ("Margin", "Blank border between text and page edge"),
                ("Header / footer", "Repeating zones at top/bottom of pages"),
                ("Text wrapping", "How text flows around an image"),
                ("Orientation", "Portrait vs landscape page direction"),
            ],
            """A) Page setup
Layout → Margins → Normal is a safe default. Narrow margins can make printing cut off text.
Portrait is standard for essays; landscape is for wide tables/posters (rare in classic essays).

B) Headers and footers
Double-click the top of the page or use Insert → Header.
Put your name / class ID in the header; page numbers often go in the footer (Insert → Page Number).
Different first page can hide header on a title page when required.

C) Images that behave
Insert → Pictures. Select the image → Picture Format → Wrap Text → Square or Tight for layout control.
In line with text is simplest but harder to move.
Resize from corners to keep proportion. Blurry stretched images look careless.

D) Multi-page thinking
As content grows, check Print Preview. Avoid a last page with a single lonely line (“orphan” feel).
Keep image captions if you include figures in subject reports.""",
            [
                "Set margins live and show Print Preview difference",
                "Add page numbers bottom centre",
                "Insert image with Square wrap and caption paragraph under it",
            ],
            [
                "Create YourName_Week03_Report.docx — at least two pages",
                "Topic: any school subject summary (e.g. photosynthesis, local history, computer ethics)",
                "Include: centred title, intro, two subheadings, body text, one image with wrap, header with your name, footer page numbers",
                "Write a one-line caption under the image",
            ],
            [
                "≥2 pages in Print Preview",
                "Header name + page numbers visible",
                "Image does not cover text",
                "Subheadings clearly stronger than body",
            ],
            [
                "Images dragged so text is unreadable",
                "Page numbers only typed manually on page 1",
                "Margins at zero",
            ],
            [
                ("Print Preview", "Screen view of how the page will print"),
                ("Wrap Text", "Controls collision between image and paragraph text"),
                ("Caption", "Short description of a figure"),
            ],
            "Add an automatic table of contents later if teacher shows References tools; optional challenge only.",
            "Print Preview checklist: margins, page numbers, image, no cut-off.",
            """LAYOUT SHORTCUTS
Layout → Margins → Normal
Insert → Header / Footer / Page Number
Insert → Pictures
Picture Format → Wrap Text → Square

HEADER EXAMPLE
Ada Okoro | SS2 Digital Skills""",
            [
                (
                    "Page numbers should usually be inserted via:",
                    [
                        "Drawing shapes only",
                        "Insert → Page Number (header/footer system)",
                        "Random text boxes with no update",
                        "File → Options only",
                    ],
                    "Insert → Page Number (header/footer system)",
                ),
                (
                    "If an image hides text, fix it with:",
                    ["Wrap Text / resize / move", "Delete all text always", "Zoom to 500%", "Disable keyboard"],
                    "Wrap Text / resize / move",
                ),
                (
                    "Normal margins help mainly with:",
                    ["Print safety and readability", "Faster CPU", "Internet speed", "Battery life"],
                    "Print safety and readability",
                ),
            ],
            "Describe how you set margins, headers, and image wrap. What problem did you solve while placing the image?",
            "Screenshot of Print Preview or page view showing header, page number, and image.",
        ),
        _week(
            course,
            4,
            total,
            "Capstone — formal letter or multi-page report to school standard",
            [
                "Plan structure before typing",
                "Combine Weeks 1–3 skills into one polished submission",
                "Proofread with a checklist and submit final naming",
            ],
            "Capstone proves you can produce work that could be handed to a principal, employer, or examiner without embarrassment. "
            "Depth, neatness, and complete structure matter more than fancy effects.",
            [
                ("Formal letter structure", "Addresses, date, salutation, body, complimentary close, name"),
                ("Report structure", "Title, introduction, body sections, conclusion"),
                ("Proofreading", "Check spelling, spacing, names, dates, completeness"),
            ],
            """Choose ONE track:

TRACK A — Formal letter (≈1–2 pages)
Request for permission / complaint with politeness / application interest letter (school-appropriate).
Include sender details, date, recipient line, greeting, 3 body paragraphs (purpose, details, polite close), sign-off.

TRACK B — Short report (2–3 pages)
Title, introduction, at least two section headings, conclusion, one supporting image, header name, page numbers.
Topic examples: cyber safety, benefits of learning Excel, a historical figure, a science process.

Quality bar
- Consistent fonts and spacing
- Lists where they help (optional but recommended)
- Spelling checked
- File name: YourName_Week04_Capstone.docx
- Human tone: clear, respectful, specific (dates, names, reasons)""",
            [
                "Show a model letter and a model report side by side",
                "Walk the rubric: structure 30%, formatting 25%, completeness 25%, proofreading 20%",
            ],
            [
                "Draft outline on paper (5 minutes) then build in Word",
                "Complete Track A or B fully",
                "Run spelling check; fix all flagged real errors",
                "Self-mark with the rubric before upload",
            ],
            [
                "Structure matches the chosen track",
                "No Document1 name; capstone file name correct",
                "Formatting consistent; image OK if report track",
                "You can explain every paragraph’s purpose aloud",
            ],
            [
                "Mixing letter and report randomly without structure",
                "Informal slang in a formal letter",
                "Skipping proofreading",
            ],
            [
                ("Salutation", "Greeting line such as Dear Sir/Madam,"),
                ("Complimentary close", "Yours sincerely / Yours faithfully"),
                ("Rubric", "Scoring guide describing quality levels"),
            ],
            "Add a final reflection paragraph: strongest skill gained in Word this month + one remaining weakness.",
            "Ask a classmate to mark your rubric and fix one issue they found.",
            """LETTER SKELETON
[Your address]
[Date]
[Recipient]
Dear …,
Paragraph 1 purpose
Paragraph 2 details
Paragraph 3 polite action requested
Yours sincerely,
[Name]

REPORT SKELETON
Title
1. Introduction
2. Section
3. Section
4. Conclusion
Figure + caption""",
            [
                (
                    "A formal letter should include:",
                    ["Only stickers", "Salutation and closing", "No date ever", "All caps body only"],
                    "Salutation and closing",
                ),
                (
                    "Before final submit you should:",
                    ["Proofread and correctly name the file", "Delete the introduction", "Remove your name", "Turn off the monitor"],
                    "Proofread and correctly name the file",
                ),
                (
                    "Capstone depth means:",
                    [
                        "One incomplete sentence",
                        "Complete structure with clear paragraphs and school-standard formatting",
                        "Only a blank page",
                        "Icons without text",
                    ],
                    "Complete structure with clear paragraphs and school-standard formatting",
                ),
            ],
            "State which track you chose, summarise your document in 4–6 sentences, and list the rubric scores you would give yourself.",
            "Screenshot of your final pages (structure visible) including file name on the title bar.",
        ),
    ]


def _pack_office_excel(course: str, total: int) -> list[dict]:
    # shortened names reused via generic deep builder for week structure
    return _deep_month_course(
        course,
        total,
        "excel",
        [
            (
                "Workbook basics — cells, data entry, navigation, save",
                "Excel stores data in rows and columns so calculations and charts become automatic later.",
            ),
            (
                "Formulas and references — calculations that update",
                "Formulas turn spreadsheets into tools instead of static posters of numbers.",
            ),
            (
                "Organisation — sort, filter, clean tables, charts",
                "Decision-makers need sorted tables and honest charts, not messy dumps of cells.",
            ),
            (
                "Capstone workbook — scores or budget with formulas + chart",
                "Prove you can design a useful sheet someone else can understand in one minute.",
            ),
        ],
    )


def _pack_office_ppt(course: str, total: int) -> list[dict]:
    return _deep_month_course(
        course,
        total,
        "powerpoint",
        [
            (
                "Slides, layouts, and message-first structure",
                "Presentations persuade and teach; crowded slides hide the message.",
            ),
            (
                "Visual design systems — consistency, images, alignment",
                "Audiences trust clean alignment and consistent style more than decorative chaos.",
            ),
            (
                "Delivery tools — notes, light motion, rehearsal",
                "You present to humans; slides support the talk rather than replace thinking.",
            ),
            (
                "Capstone deck — 8–10 slides for a real school topic",
                "A complete arc (hook → teaching points → close) is a professional standard.",
            ),
        ],
    )


def _pack_graphic_ai(course: str, total: int) -> list[dict]:
    return _deep_month_course(
        course,
        total,
        "graphic-ai",
        [
            (
                "Generative design workflow, ethics, and prompt foundations",
                "AI accelerates drafting, but you own judgment, safety, and communication goals.",
            ),
            (
                "Composition systems and iterative critique",
                "Strong pictures still fail as designs if hierarchy and contrast are weak.",
            ),
            (
                "Multi-format brand assets and consistency rules",
                "Real campaigns need matching pieces across sizes, not one random image.",
            ),
            (
                "Capstone campaign pack with rationale",
                "Designers explain choices; schools and clients expect process as well as pixels.",
            ),
        ],
    )


def _pack_video_ai(course: str, total: int) -> list[dict]:
    return _deep_month_course(
        course,
        total,
        "video-ai",
        [
            (
                "Project setup, imports, and intentional cutting",
                "Editing is decision-making about time; rough cuts force clarity about story.",
            ),
            (
                "Narrative audio, captions, and viewer comprehension",
                "If viewers cannot hear or follow text, the edit fails regardless of fancy effects.",
            ),
            (
                "Polish, AI assist with human review, export masters",
                "Delivery formats and backups are part of professional production, not extras.",
            ),
            (
                "Capstone short film/tutorial (45–90 seconds)",
                "A finished, shareable piece proves end-to-end production skill.",
            ),
        ],
    )


def _deep_month_course(
    course: str, total: int, domain: str, weeks: list[tuple[str, str]]
) -> list[dict]:
    """Build four (or n) deep weeks from title+why pairs + domain enrichment."""
    out = []
    for i, (title, why) in enumerate(weeks, 1):
        concepts, theory, demos, practice, success, mistakes, vocab, stretch, homework, examples, mcqs = (
            _domain_enrich(domain, course, i, total, title)
        )
        out.append(
            _week(
                course,
                i,
                total,
                title,
                [
                    f"Explain the purpose of this week’s skill: {title.split('—')[0].strip()}",
                    "Complete the full guided practice sequence without skipping saves",
                    "Meet the listed success criteria with evidence (screenshot)",
                    "Use class vocabulary accurately in your written reflection",
                ],
                why,
                concepts,
                theory,
                demos,
                practice,
                success,
                mistakes,
                vocab,
                stretch,
                homework,
                examples,
                mcqs,
                (
                    f"Write a structured reflection (6–10 sentences): what you built, how you used "
                    f"this week’s techniques on “{title}”, one error you fixed, and what you will improve next."
                ),
                (
                    f"Upload a clear screenshot proving completion of the main practice for week {i} "
                    f"({title.split('—')[0].strip()})."
                ),
            )
        )
    return out


def _domain_enrich(domain: str, course: str, week: int, total: int, title: str):
    """Return deep materials for month-long packs."""
    t = title.lower()
    if domain == "excel":
        return _enrich_excel(week, total, title)
    if domain == "powerpoint":
        return _enrich_ppt(week, total, title)
    if domain == "graphic-ai":
        return _enrich_gai(week, total, title)
    if domain == "video-ai":
        return _enrich_video(week, total, title)
    # fallback
    return (
        [("Skill focus", title)],
        f"Deep practice on {title} for {course}.",
        ["Demonstrate core technique", "Show save/export"],
        ["Complete main exercise", "Save correctly", "Prepare screenshot"],
        ["Task complete", "Named file", "Readable result"],
        ["Skipping steps", "Poor naming"],
        [("Deliverable", "The file or output you submit")],
        "Extend the task with one improvement.",
        "Review notes 15 minutes before next class.",
        f"Focus: {title}",
        [
            (f"Main goal of week {week}?", ["Skip work", f"Master: {title}", "Delete files", "Ignore teacher"], f"Master: {title}"),
            ("Evidence should include:", ["Nothing", "Clear finished work screenshot", "Blank screen", "Only wallpaper"], "Clear finished work screenshot"),
            ("Professional habit:", ["Never save", "Name files clearly and verify results", "Work unsaved only", "Random rename later"], "Name files clearly and verify results"),
        ],
    )


def _enrich_excel(week, total, title):
    if week == 1:
        theory = """A workbook (.xlsx) can hold many worksheets (tabs). Each cell has an address like B3.
Row 1 should hold headers (labels). Keep numbers in numeric cells — do not type currency symbols inside
every number if you will calculate later; format currency after.

Build tables as rectangles without random blank rows in the middle. Blank columns break many later tools.
Navigation: Ctrl+arrow jumps edges; Ctrl+Home returns near A1. Use Freeze Panes later for long sheets.

Saving: YourName_Week01_Supplies.xlsx in the class Excel folder. Create a second sheet named RawData if you like,
but start simple: one clean table."""
        concepts = [
            ("Cell reference", "Address such as A1 or C12"),
            ("Worksheet vs workbook", "Tab vs the whole file"),
            ("Header row", "Labels describing each column"),
            ("Data type", "Text vs number vs date — numbers should be true numbers"),
        ]
        demos = [
            "Create headers Item | Qty | UnitPrice",
            "Enter five school supply rows with realistic numbers",
            "Widen columns; align headers centre; numbers right-align by default",
            "Save As + reopen test",
        ]
        practice = [
            "Build a 8-row supplies or market list with 3+ columns",
            "No merged decorative chaos in the data rectangle",
            "Add your name in a cell above the table (not inside header row)",
            "Save, close, reopen, add one more row",
        ]
        examples = "A1:Item B1:Qty C1:UnitPrice\nA2:Exercise book B2:6 C2:400\n..."
        mcqs = [
            ("B4 means:", ["Row B col 4", "Column B row 4", "A chart", "A macro"], "Column B row 4"),
            ("Headers belong in:", ["A hidden sheet only", "Usually row 1 of the table", "The file name only", "Print settings only"], "Usually row 1 of the table"),
            ("Numbers for calculation should be typed as:", ["With stories in the same cell", "Clean numeric values in their own cells", "Only as images", "Inside comments only"], "Clean numeric values in their own cells"),
        ]
    elif week == 2:
        theory = """Formulas begin with =. Prefer references (=B2*C2) over typing 6*400 so updates stay live.
SUM adds ranges: =SUM(D2:D9). AVERAGE ignores text but fails if errors exist in the range.
Relative references change when filled down; that is usually what you want for line totals.
Order of operations matters: =A1+B1*C1 multiplies before adding — use parentheses deliberately.
Show formulas with Ctrl+` when teaching/debugging."""
        concepts = [
            ("Formula", "Expression starting with = that calculates"),
            ("Range", "A block of cells like D2:D9"),
            ("Fill handle", "Drag to copy formulas down/right"),
            ("Order of operations", "Rules for which math happens first"),
        ]
        demos = ["Line total column", "Grand total SUM under column", "Change a qty to show live update"]
        practice = [
            "Add LineTotal formulas for each row",
            "Grand total under LineTotal",
            "Average unit price with AVERAGE",
            "Break and fix a formula deliberately once (learn the error, then correct)",
        ]
        examples = "D2:=B2*C2\nD10:=SUM(D2:D9)\n=AVERAGE(C2:C9)"
        mcqs = [
            ("Formulas start with:", ["#", "=", "@", "%"], "="),
            ("=SUM(E2:E5) does what?", ["Adds E2 through E5", "Multiplies only E2", "Deletes E2:E5", "Sorts E"], "Adds E2 through E5"),
            ("If Qty changes and LineTotal is a formula:", ["It can update automatically", "It never updates", "Excel closes", "Data vanishes"], "It can update automatically"),
        ]
    elif week == 3:
        theory = """Convert ranges to a clean table mindset: no blank header cells, consistent types.
Sort to order data (A→Z, largest values). Filters hide non-matching rows for analysis.
Charts need correct selection including headers. Choose chart type for the question:
column for comparing categories, pie for parts of a whole (few categories), line for trends over time.
Always title charts. Remove chart junk (useless legends) when it confuses."""
        concepts = [
            ("Sort", "Reorder rows by a key column"),
            ("Filter", "Temporarily hide rows not matching criteria"),
            ("Chart title", "Text naming what the chart shows"),
            ("Category axis", "Labels for each bar/point"),
        ]
        demos = ["Sort by UnitPrice descending", "Filter Qty > a threshold", "Insert column chart with title"]
        practice = [
            "Sort your dataset meaningfully",
            "Apply at least one filter and describe what remains",
            "Create one correct chart with title matching the question you answer",
            "Write one sentence insight near the chart (in a cell)",
        ]
        examples = "Select A1:D9 → Insert → Recommended Charts\nTitle: Total Cost by Item"
        mcqs = [
            ("Filters help you:", ["Hide non-matching rows", "Increase RAM", "Rename Windows", "Draw freehand"], "Hide non-matching rows"),
            ("A chart should start from:", ["Selected data including headers", "A random empty sheet only", "Only the file path", "Task Manager"], "Selected data including headers"),
            ("Pie charts work best when:", ["You have few parts of one whole", "You have 500 categories", "You need live video", "You sort photos"], "You have few parts of one whole"),
        ]
    else:
        theory = """Capstone options:

A) Assessment scores sheet: StudentName, T1, T2, T3, Average (=AVERAGE), class chart of averages.
B) Mini budget: Item, Planned, Actual, Difference (=Actual-Planned), totals, chart of Actual vs Planned.

Include a cover cell block: title, your name, date, one-sentence conclusion of what the numbers show.
Protect readers from confusion: clear headers, number formats, readable chart.
Optional challenge: conditional formatting to highlight averages below pass mark."""
        concepts = [
            ("Dashboard thinking", "Title + key numbers + chart + takeaway"),
            ("Difference formula", "Subtract to find variance"),
            ("Conclusion statement", "Human sentence interpreting results"),
        ]
        demos = ["Show both score and budget skeletons", "Rubric walkthrough"]
        practice = [
            "Build A or B with ≥8 data rows",
            "All required formulas working",
            "One chart + written insight",
            "Name YourName_Week04_Capstone.xlsx",
        ]
        examples = "Average: =AVERAGE(B2:D2)\nDifference: =C2-B2\nTotals: =SUM()"
        mcqs = [
            ("Capstone should include:", ["Data, formulas, chart, insight", "Only colours", "Empty file", "Password for teacher only with no data"], "Data, formulas, chart, insight"),
            ("Variance Actual−Planned is useful because:", ["It shows over/under spending or targets", "It deletes rows", "It sorts photos", "It prints automatic essays"], "It shows over/under spending or targets"),
            ("A pass average formula uses:", ["AVERAGE of the score cells", "SUM of names", "Random numbers", "Zoom only"], "AVERAGE of the score cells"),
        ]
    success = [
        "Formulas or structure required for this week are correct",
        "File named properly and reopens",
        "A classmate could understand the sheet without verbal explanation",
    ]
    mistakes = [
        "Numbers stored as text (green corners / formula issues)",
        "Charts on wrong ranges including totals twice",
        "Merged cells inside data tables",
    ]
    vocab = concepts[:3]
    stretch = "Add a second chart type comparing a different question on the same data."
    homework = "Check every formula by changing one input and confirming outputs recompute."
    demos = demos
    practice = practice
    return concepts, theory, demos, practice, success, mistakes, vocab, stretch, homework, examples, mcqs


def _enrich_ppt(week, total, title):
    theories = {
        1: """Slides are scenes in a talk. Start with audience outcomes: after this talk, what should they know or do?
Title slide: topic, name, class. Agenda slide optional. Content slides: short headlines + ≤6 bullets or a single diagram.
Avoid paragraphs. If you need a paragraph, you may need a handout, not a slide.
Themes enforce consistency — pick once.""",
        2: """Design systems: repeat fonts, colours, logo placement, margins from slide edges.
Images must be high enough resolution; crop distractions. Align left edges of text boxes using Align tools.
Contrast: light text only on dark shapes with enough opacity. Decorative lines should be subtle.""",
        3: """Speaker notes hold the script. Transitions: prefer Fade; avoid noisy random effects.
Animations: emphasise one element, not every bullet spinning.
Rehearse with Presenter View if available; time yourself. Goal: calm delivery, not fireworks.""",
        4: """Capstone structure (8–10 slides): Title, Hook/Why it matters, 4–5 teaching slides, Example, Summary, Q&A/Thank you.
Topic must be school-safe and specific. Apply design system + light motion + notes on teaching slides.""",
    }
    theory = theories.get(week, theories[1])
    concepts = [
        ("Slide master ideas", "Shared layout decisions"),
        ("Signal-to-noise", "Keep only elements that help meaning"),
        ("Call to attention", "What the eye should see first"),
    ]
    demos = ["Build 3-slide mini deck live following rules for this week"]
    practice = [
        f"Apply this week’s emphasis: {title}",
        "Save progressive file YourName_Week%02d_PPT.pptx" % week,
        "Peer critique: remove one clutter item",
    ]
    if week == 4:
        practice = [
            "Deliver 8–10 slide capstone with notes on ≥4 slides",
            "Include summary + thank you",
            "Export PDF backup if required",
        ]
    success = ["Readable at a glance", "Consistent theme", "File named correctly"]
    mistakes = ["Walls of text", "Too many effects", "Low-contrast text"]
    vocab = [("Deck", "The full presentation file"), ("Presenter view", "Speaker screen with notes")]
    stretch = "Add a simple diagram slide instead of bullets for one idea."
    homework = "Rehearse out loud once end-to-end."
    examples = "Headline\n- Point\n- Point\n(Visual)\nNotes: what you will say…"
    mcqs = [
        ("Best slide text style:", ["Short bullets", "Essays", "Tiny 6pt paragraphs", "No titles ever"], "Short bullets"),
        ("A title slide usually needs:", ["Topic and name", "Only file path", "Task Manager", "Hidden text"], "Topic and name"),
        ("Animations should be:", ["Rare and purposeful", "On every word", "Faster than readable", "Random each click"], "Rare and purposeful"),
    ]
    return concepts, theory, demos, practice, success, mistakes, vocab, stretch, homework, examples, mcqs


def _enrich_gai(week, total, title):
    theories = {
        1: """Generative image tools map language to pixels. Your prompt is a brief: subject, setting, style, lighting, mood, constraints (school-safe).
Process: draft prompt → generate variants → critique → refine one variable at a time → export PNG/JPG → log prompt in a text note.
Ethics: no harassment, hate, sexual content, or impersonation. Respect class policy on copyrighted characters.
You are the designer-in-charge; AI is a junior assistant.""",
        2: """Composition: subject weight, balance, negative space for text, colour contrast, focal point.
Build a scorecard 1–5 for clarity, relevance, text-space, consistency. Keep only heroes that score high.
Learn lighting terms (soft light, golden hour, studio light) to control mood.""",
        3: """Campaign thinking: one message, three touchpoints (square feed, vertical story, simple mark).
Create micro brand rules: 2–3 colours, 3 mood words, do/don’t list. Export assets with systematic names.""",
        4: """Capstone: school campaign with audience, promise, three assets, and written rationale linked to composition/brand rules.
Quality over novelty. Document process for grading fairness.""",
    }
    theory = theories.get(week, theories[1])
    concepts = [
        ("Prompt", "Text instructions to the model"),
        ("Variant", "Alternative generation from related prompt"),
        ("Negative prompt", "What to avoid when tool supports it"),
        ("Asset", "Final image used in the campaign"),
    ]
    demos = ["Live critique of bad vs good prompts", "Show export + prompt log"]
    practice = [
        f"Complete deep practice for: {title}",
        "Keep prompt log with at least 5 iterations",
        "Export finals into a dated folder",
    ]
    success = ["School-safe", "Clear subject", "Documented prompt process", "Named exports"]
    mistakes = ["Unsafe content", "No process log", "Inconsistent style in a set"]
    vocab = concepts[:3]
    stretch = "Make a monochrome version for contrast testing."
    homework = "Collect 3 reference images (links or screenshots) that match your target style."
    examples = "Prompt formula:\n[Subject] + [Environment] + [Style] + [Lighting] + [Composition] + school-safe poster aesthetic"
    mcqs = [
        ("Good prompts usually specify:", ["Subject and style context", "Only one emoji", "Passwords", "Nothing"], "Subject and style context"),
        ("Designers iterate by:", ["Changing one factor to learn cause/effect", "Changing everything always randomly", "Never regenerating", "Ignoring safety"], "Changing one factor to learn cause/effect"),
        ("A campaign pack should be:", ["Visually related assets", "Unrelated styles", "Secret unlabelled files", "Audio only"], "Visually related assets"),
    ]
    return concepts, theory, demos, practice, success, mistakes, vocab, stretch, homework, examples, mcqs


def _enrich_video(week, total, title):
    theories = {
        1: """Editing is selecting moments. Project settings (resolution/frame rate) should match delivery target when possible.
Bins/folders organise footage. Rough cut: order clips for sense before beauty.
Use keyboard shortcuts for cut/trim. Save project files separately from media when the tool allows.""",
        2: """Story spine: hook, development, payoff. Audio first audience test: watch once with eyes half-closed, only listening.
Captions: accuracy, reading time, safe margins for platform UI. Titles should not collide with faces.""",
        3: """Colour and cleanup: fix exposure before creative looks. AI tools for captions/noise need human QA.
Export masters (high quality) and publish proxies if needed. Record export presets used.""",
        4: """Capstone brief: educational tutorial OR school event promo, 45–90s, captions, end card credits,
music licensed for class, clear message. Deliver MP4 + short process note.""",
    }
    theory = theories.get(week, theories[1])
    concepts = [
        ("Timeline", "Horizontal arrangement of clips over time"),
        ("J-cut / L-cut", "Audio/video leading each other (intro if tool allows)"),
        ("Bitrate", "Data rate affecting quality/size"),
        ("Room tone", "Background ambience for clean edits"),
    ]
    demos = ["Trim exercise", "Levels check", "Export dialog tour"]
    practice = [
        f"Apply week focus: {title}",
        "Maintain organised project media",
        "Export a review cut if at week ≥3",
    ]
    success = ["Audible voice", "Readable titles", "Sensible pacing", "Correct export"]
    mistakes = ["Music ≥ voice", "Jump cuts that confuse story without purpose", "Wrong aspect ratio for target"]
    vocab = concepts[:3]
    stretch = "Create a 9:16 reframe for mobile."
    homework = "Note timestamps of three weak moments to fix next session."
    examples = "Hook 0–3s | Teach 3–50s | CTA/End 50–60s\nMusic quieter than dialogue"
    mcqs = [
        ("Rough cut prioritises:", ["Order and story", "Final colour only", "Poster design only", "File encryption"], "Order and story"),
        ("Captions should be:", ["Accurate and readable", "Random language", "One frame long", "Decorative only"], "Accurate and readable"),
        ("Common school delivery format:", ["MP4", "SYS", "DLL", "RAW unedited only always"], "MP4"),
    ]
    return concepts, theory, demos, practice, success, mistakes, vocab, stretch, homework, examples, mcqs


# ── Multi-month expansion (deep) ──────────────────────────────


def _expand_from_topics(slug: str, course_title: str) -> list[dict]:
    topics = TOPICS.get(slug) or [f"Module {i}" for i in range(1, weeks_for(slug) + 1)]
    total = weeks_for(slug)
    topics = (topics + [f"Extended practice {i}" for i in range(len(topics) + 1, total + 1)])[:total]
    out = []
    for i, topic in enumerate(topics, 1):
        title = topic.split("—")[0].strip() if "—" in topic else topic
        detail = topic.split("—", 1)[1].strip() if "—" in topic else topic
        short = title if len(title) < 72 else title[:69] + "…"
        concepts = _concepts_for(slug, title, detail)
        theory = _deep_theory(slug, course_title, i, total, title, detail)
        demos = [
            f"Connect today’s idea (“{title}”) to last week in 2 minutes",
            f"Live demo covering: {detail}",
            "Show a finished sample that meets success criteria",
            "Cold-call one prediction (“What happens if we skip this step?”) and test it",
            "Students complete first practice minute together (I do / we do)",
        ]
        practice = [
            f"Notes check: write the definition of each key concept for “{title}” in your own words",
            f"Guided task: complete the core exercise for {detail}",
            "Independent task: produce a second version with one deliberate improvement",
            "Quality pass: compare against success criteria and fix gaps",
            "Evidence: prepare a screenshot showing the critical finished state + file name if relevant",
        ]
        if i == total:
            practice.append(
                "Capstone assembly: combine the term’s skills into the final specified deliverable and self-mark with the course rubric"
            )
        success = [
            f"You can teach a classmate the meaning of “{title}” without reading notes",
            "Main practice file/project exists, opens, and matches the brief",
            "Screenshot evidence is sharp and complete",
            "Reflection uses vocabulary from this week accurately",
        ]
        mistakes = _mistakes_for(slug, i, total)
        vocab = concepts[:4]
        stretch = (
            f"Create a mini tutorial (5 bullets or a 30-second plan) teaching “{title}” to a beginner."
        )
        homework = (
            f"Spaced practice: re-do one small drill from this week for 15 minutes before next class. "
            f"Bring one question about “{detail}”."
        )
        examples = _examples_for(slug, course_title, i, total, title, detail)
        mcqs = _mcqs_for(slug, title, detail, i, total)
        subjective = (
            f"Write 8–12 sentences: (1) explain “{title}”, (2) describe what you built, "
            f"(3) one bug/mistake and how you fixed it, (4) how this skill connects to earlier weeks, "
            f"(5) what you will practise next."
        )
        if i == total:
            subjective = (
                f"Capstone report (10–15 sentences): project purpose, features/skills used from the whole "
                f"{course_title} course, demo walkthrough, limitations, and next improvements."
            )
        upload = (
            f"Upload a clear screenshot of finished work for week {i} — {short}."
            if i < total
            else "Upload screenshot(s) of the finished capstone (overview + one detail view if needed)."
        )
        why = (
            f"Week {i}/{total} builds the {('foundation' if i<=total*0.34 else 'skill stack' if i<=total*0.67 else 'performance fluency')} "
            f"required for later {course_title} work. Skipping it creates holes that appear during the capstone."
        )
        out.append(
            _week(
                course_title,
                i,
                total,
                short,
                [
                    f"Define and apply: {title}",
                    f"Execute the class demonstration workflow for {detail}",
                    "Produce an independent deliverable meeting success criteria",
                    "Document learning with vocabulary-rich reflection",
                ],
                why,
                concepts,
                theory,
                demos,
                practice,
                success,
                mistakes,
                vocab,
                stretch,
                homework,
                examples,
                mcqs,
                subjective,
                upload,
            )
        )
    return out


def _concepts_for(slug: str, title: str, detail: str) -> list[tuple[str, str]]:
    base = [
        (title if len(title) < 40 else "This week’s skill", detail if len(detail) < 120 else detail[:117] + "…"),
        ("Deliverable", "The concrete file, page, diagram, or project piece you finish"),
        ("Iteration", "Improving work through tested changes, not one lucky try"),
        ("Evidence", "Screenshot or output that proves completion"),
    ]
    extras = {
        "python": ("Syntax", "Spelling/grammar rules of the Python language"),
        "android": ("Activity/Screen", "A user-facing page in an app"),
        "website": ("HTML element", "A building block like p, h1, a, img"),
        "cloud": ("Shared responsibility", "Which security tasks are yours vs the provider’s"),
        "corel": ("Vector", "Shapes defined by maths so they scale cleanly"),
        "scratch": ("Event", "A trigger such as green flag clicked"),
        "ai-engineer": ("Evaluation", "Measuring whether AI output is good enough"),
        "system": ("Trade-off", "Choosing among cost, speed, simplicity, reliability"),
        "data": ("Clean data", "Consistent, correctly typed values ready for analysis"),
    }
    for key, pair in extras.items():
        if key in slug:
            base.insert(1, pair)
            break
    return base[:5]


def _deep_theory(slug: str, course: str, week: int, total: int, title: str, detail: str) -> str:
    phase = "early foundations" if week <= total * 0.34 else ("mid-course skill building" if week <= total * 0.67 else "advanced application")
    open_p = (
        f"Welcome to week {week} of {total} in {course}. You are in the {phase} phase. "
        f"Today’s focus is “{title}”. In plain language, you will work on: {detail}."
    )

    domain_blocks = {
        "graphic-coreldraw": f"""
CorelDRAW skills stack from structure to style. Professionals set page size and guides before decorative work.
Vectors (lines/curves) remain sharp when scaled — ideal for logos and print.
This week, treat “{title}” as a craft move: watch the demo, replicate exactly once, then create a second original variation that still follows alignment/colour discipline.
Always keep editable .cdr sources; export PNG/PDF for sharing. Name layers/objects when the file grows.
Critique questions: Is the page size correct? Is there enough margin? Is the hierarchy obvious at arm’s length?
""",
        "python-for-beginners": f"""
Python executes instructions in order. Small files beat giant messy scripts. Read error messages from the bottom up — they usually name the line.
For “{title}”, write the smallest program that proves the idea, then extend.
Habits: meaningful variable names, comments for why (not what), run after every few lines, save before running large changes.
You are training precision; almost-correct code still fails.
""",
        "python-developer": f"""
Developer practice prioritises clarity, reuse, and testing. As programs grow, structure (functions/modules) prevents chaos.
This week’s skill “{title}” should show up as clean code with at least one reusable piece and a manual test plan (inputs → expected outputs).
Consider edge cases (empty input, zero, wrong type). Professional work anticipates failure modes.
""",
        "python-data-apps": f"""
Data work starts with a question, not a chart. Define the question, inspect the table, clean problems, compute summaries, then visualise.
For “{title}”: document assumptions (what a column means, units, missing values). Misleading charts can be worse than no chart.
""",
        "python-blocks": f"""
Blocks make structure visible: sequence, loops, conditionals, events. Say your script aloud as “when… then… forever… if…”.
If behaviour is wrong, isolate which block cluster is responsible. Copy your working script into screenshots for evidence.
Bridge note: each block maps later to a typed Python idea.
""",
        "scratch": f"""
Scratch projects combine sprites, scripts, and the stage. Debugging is normal: use “click a stack to run it” mentally by predicting.
Keep costumes/sounds organised. Credit remixes. This week’s “{title}” should produce a playable or presentable interaction, not only unfinished experiments.
""",
        "android-app-development": f"""
Android UIs are hierarchies of views. Navigation and state (what the screen shows after a tap) must be intentional.
Design touch targets large enough; text readable; labels clear. Test on emulator/device after each meaningful change.
“{title}” this week should result in a runnable behaviour you can demonstrate in under 30 seconds.
""",
        "website-development": f"""
HTML structures meaning; CSS controls appearance; JS adds behaviour later. Validate structure before heavy styling.
Accessibility: good headings, alt text for images, colour contrast. Mobile widths matter.
For “{title}”, build a page section that would make sense to a visitor with no explanation.
""",
        "cloud-computing": f"""
Cloud services are remote resources with APIs, identity controls, and bills. Diagram first: actors, components, data stores, trust boundaries.
“{title}” should connect concept → simple diagram → real-world school/business example → risk note (security/cost/outage).
""",
        "system-design-thinking": f"""
Systems have goals, parts, flows, and feedback. Design thinking adds user empathy and iteration.
Sketch boxes and arrows. Name assumptions. Ask who breaks if a part fails.
Apply that method to “{title}”/“{detail}” with both a diagram and a short written rationale.
""",
        "ai-engineer": f"""
Applied AI is a pipeline: goal → inputs → model/tooling → outputs → evaluation → safeguards.
Avoid magical language. Define success metrics (accuracy, helpfulness, latency, cost, safety).
This week, operationalise “{title}” with a mini experiment plan you could run.
""",
    }
    body = open_p + "\n"
    for key, text in domain_blocks.items():
        if key in slug:
            body += text
            break
    else:
        body += (
            f"\nStudy “{title}” as both knowledge and skill. Knowledge is explanation; skill is repeated correct performance "
            f"under light pressure (time-limited practice).\n\nClass pattern: connect → demo → guided → independent → critique → evidence.\n"
        )

    body += f"""
Progression check
- Earlier weeks: simpler tools and vocabulary.
- This week: combine those habits with new technique “{title}”.
- Later weeks: recombine multiple skills in projects and the final capstone.

Academic integrity
Do your own work. If you use a template or classmate help, be able to explain every step. Understanding is assessed, not only files.
"""
    return body.strip()


def _mistakes_for(slug: str, week: int, total: int) -> list[str]:
    m = [
        "Skipping the guided demo and guessing under time pressure",
        "Unclear file/project names that hide which week the work belongs to",
        "Screenshots that are cropped too tightly or too blurry to assess",
        "Not reading error messages or feedback panels before asking for help",
    ]
    if week == total:
        m.append("Submitting an incomplete capstone missing required sections of the brief")
    if "python" in slug:
        m.append("Writing one giant untested script instead of small runnable steps")
    if "website" in slug:
        m.append("Styling before structure is valid")
    if "corel" in slug or "graphic" in slug:
        m.append("Decorating before page size, margins, and hierarchy are set")
    return m[:5]


def _examples_for(slug, course, week, total, title, detail) -> str:
    if "python" in slug:
        return f'''# {course} — Week {week}/{total}
# Topic: {title}
# Detail: {detail}

"""Student workflow
1) Write the smallest demo that runs
2) Add one feature
3) Run again
4) Save checkpoint
"""

def week_{week:02d}_demo():
    """Demonstrate: {title}"""
    print("Week {week}: {title}")
    # TODO: implement class exercise for — {detail}
    return "ok"

if __name__ == "__main__":
    result = week_{week:02d}_demo()
    print("Result:", result)
    # Manual test notes:
    # Input: ...
    # Expected: ...
'''
    if "website" in slug:
        return f"""<!-- {course} Week {week}: {title} -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <style>
    :root {{ font-family: Georgia, serif; }}
    body {{ margin: 0; padding: 1.5rem; line-height: 1.5; max-width: 40rem; }}
    h1 {{ font-size: 1.6rem; }}
    .note {{ color: #333; border-left: 3px solid #0b6b75; padding-left: .75rem; }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  <p class="note">{detail}</p>
  <!-- Build out required sections for this week below -->
</body>
</html>
"""
    if "corel" in slug or "graphic" in slug:
        return f"""DESIGN PRODUCTION SHEET — Week {week}
Course: {course}
Focus: {title}
Brief detail: {detail}

Preflight
[ ] Page size set
[ ] Margins/guides
[ ] Colour palette limited (2–4 colours)
[ ] Hierarchy obvious at 50% zoom

Build order
1. Structure  2. Main shapes/images  3. Text  4. Align/distribute  5. Export

Exports
- Source: YourName_Week{week:02d}.cdr (or project format)
- Share: PNG/PDF preview
"""
    if "scratch" in slug or "blocks" in slug:
        return f"""SCRIPT PLAN — Week {week}: {title}
Goal: {detail}

when green flag clicked
  // setup positions/variables
  forever
    // core behaviour for this week
    if <condition> then
      // response

Test cases
1) Normal path
2) Edge path (what if key held / sprite touching edge)
"""
    if "android" in slug:
        return f"""SCREEN SPEC — Week {week}
Title: {title}
User goal: {detail}

Components
- Top app bar / title
- Primary content
- Primary button (verb: Save/Submit/Next)
- Feedback text (success/error)

Acceptance
[ ] Rotates or scrolls without breaking layout (as applicable)
[ ] Button does something visible
[ ] User can explain navigation
"""
    if "cloud" in slug or "system" in slug:
        return f"""SYSTEM SKETCH — Week {week}
Focus: {title}

[User] → [Interface] → [Logic/Service] → [Data]
                 ↘ [Logs / Auth]

Write:
- Goal:
- Assumption:
- Failure mode:
- Mitigation:
Detail: {detail}
"""
    if "ai-engineer" in slug or slug == "ai-engineer":
        return f"""EXPERIMENT CARD — Week {week}
Hypothesis about {title}:
Metric:
Dataset/examples:
Method:
Safety note:
Result:
Next change:
({detail})
"""
    if "data" in slug:
        return f"""DATA LOG — Week {week}
Question:
Columns needed:
Cleaning steps:
Summary stats:
Chart choice + why:
Insight sentence:
({title} / {detail})
"""
    return f"""PRACTICE CONTRACT — Week {week}
Course: {course}
Skill: {title}
Task detail: {detail}

I will produce: __________________
I will verify by: __________________
I will save as: YourName_Week{week:02d}_...
"""


def _mcqs_for(slug, title, detail, week, total):
    a = (
        f"What is the central skill for week {week}?",
        [
            "Avoiding the assigned topic",
            f"Understanding and practising: {title}",
            "Only changing wallpaper",
            "Deleting previous evidence",
        ],
        f"Understanding and practising: {title}",
    )
    b = (
        "Best study order for a technical class is:",
        [
            "Skip demo, guess, submit blank",
            "Watch/demo → guided practice → independent work → evidence",
            "Only screenshot random screens",
            "Never save until the term ends",
        ],
        "Watch/demo → guided practice → independent work → evidence",
    )
    if week == total:
        c = (
            "A strong capstone includes:",
            [
                "Empty folder",
                "Complete brief, working result, and clear explanation",
                "Only a meme",
                "Unnamed files with no structure",
            ],
            "Complete brief, working result, and clear explanation",
        )
    else:
        c = (
            f"When stuck on “{detail}”, you should first:",
            [
                "Delete the OS",
                "Re-read notes/error output and retry a smaller step",
                "Submit immediately empty",
                "Change every setting at once with no test",
            ],
            "Re-read notes/error output and retry a smaller step",
        )
    return [a, b, c]


def syllabus_for(slug: str, course_title: str) -> list[dict]:
    total = weeks_for(slug)
    builders = {
        "office-ms-word": lambda: _office_word(course_title, total),
        "office-excel": lambda: _pack_office_excel(course_title, total),
        "office-powerpoint": lambda: _pack_office_ppt(course_title, total),
        "graphic-ai": lambda: _pack_graphic_ai(course_title, total),
        "video-editing-ai": lambda: _pack_video_ai(course_title, total),
    }
    if slug in builders:
        return builders[slug]()
    return _expand_from_topics(slug, course_title)
