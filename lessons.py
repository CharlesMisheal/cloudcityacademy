"""
Full CloudCity Academy lesson packs.

Each week dict:
  title, objectives (list), body (str), practice (list), examples (str),
  mcqs: list of (prompt, [options], correct), subjective, upload
"""
from __future__ import annotations

import json
from typing import Any

from curriculum import COURSE_DURATION_MONTHS, TOPICS, weeks_for


MARKER = "[[CCA_CURRICULUM_V2]]"


def _mcq(prompt: str, options: list[str], correct: str, points: int = 2, order: int = 1):
    return ("mcq", prompt, json.dumps(options), correct, points, order)


def _build_body(
    course: str,
    week: int,
    total: int,
    title: str,
    objectives: list[str],
    theory: str,
    demos: list[str],
    practice: list[str],
    mistakes: list[str],
    stretch: str,
) -> str:
    phase = (
        "Foundation"
        if week <= total * 0.34
        else ("Building skill" if week <= total * 0.67 else "Application & mastery")
    )
    return "\n".join(
        [
            MARKER,
            f"Course: {course}",
            f"Week {week} of {total} · {phase}",
            "",
            f"Lesson: {title}",
            "",
            "Learning objectives",
            *[f"• {o}" for o in objectives],
            "",
            "Lesson notes",
            theory.strip(),
            "",
            "Teacher demonstration (class)",
            *[f"{i}. {s}" for i, s in enumerate(demos, 1)],
            "",
            "Student practice (do this week)",
            *[f"{i}. {s}" for i, s in enumerate(practice, 1)],
            "",
            "Common mistakes to avoid",
            *[f"• {m}" for m in mistakes],
            "",
            "Stretch (optional if you finish early)",
            stretch.strip(),
            "",
            "Assessment readiness",
            "Complete the quiz questions honestly, write the short reflection, "
            "and upload a clear screenshot of the finished practice for this week.",
        ]
    )


def _week(
    course: str,
    week: int,
    total: int,
    title: str,
    objectives: list[str],
    theory: str,
    demos: list[str],
    practice: list[str],
    mistakes: list[str],
    stretch: str,
    examples: str,
    mcqs: list[tuple],
    subjective: str,
    upload: str,
) -> dict[str, Any]:
    body = _build_body(
        course, week, total, title, objectives, theory, demos, practice, mistakes, stretch
    )
    questions = []
    for i, (prompt, opts, correct) in enumerate(mcqs, 1):
        questions.append(_mcq(prompt, opts, correct, 2, i))
    questions.append(("subjective", subjective, None, None, 3, len(questions) + 1))
    questions.append(("upload", upload, None, None, 3, len(questions) + 1))
    return {
        "week": week,
        "title": f"Week {week}: {title}",
        "topic": title,
        "content": body,
        "examples": examples.strip(),
        "questions": questions,
    }


# ── Per-course full builders ─────────────────────────────────


def _office_word(course: str, total: int) -> list[dict]:
    return [
        _week(
            course, 1, total,
            "Word interface, new document, typing and saving",
            [
                "Identify the ribbon, document area, status bar, and Save command",
                "Create, type into, and save a .docx with a clear file name",
                "Use Undo/Redo and basic navigation keys confidently",
            ],
            """Microsoft Word is the school and office standard for letters, reports, and long text documents.
This week you learn the work area before fancy formatting. The Ribbon holds tools (Home, Insert, Layout).
The blank page is where you type. Always know where your file is saved on the computer or USB/class folder.
Good habits: save early, save often, use YourName_Week01_Document.docx naming.""",
            [
                "Show the blank document and name the ribbon tabs",
                "Type a short paragraph and save to the class folder",
                "Close Word and reopen the same file to prove the save worked",
            ],
            [
                "Create a new document and type a 5–7 sentence introduction about yourself",
                "Save as YourName_Week01_Intro.docx",
                "Reopen it and add one more sentence, then Save again",
            ],
            [
                "Leaving the file only open (not saved) and closing Word",
                "Saving with names like Document1 or New without your name",
                "Typing in the wrong language input or caps-lock by mistake",
            ],
            "Add your class name and today’s date on a new line at the top.",
            "Ribbon tour\nHome → Font & Paragraph\nInsert → Pictures / Tables later\nFile → Save As → choose class folder\n\nName pattern:\nAda_Okoro_Week01_Intro.docx",
            [
                ("Where do you usually find Save / Save As in Word?",
                 ["Home tab only", "File menu", "Layout tab", "View tab"], "File menu"),
                ("A good student file name for week 1 is:",
                 ["doc", "YourName_Week01_Intro.docx", "final!!!", "AAA"],
                 "YourName_Week01_Intro.docx"),
            ],
            "Explain in your own words why saving early matters, and write the full path or folder name you used.",
            "Screenshot of your Word window showing your intro text and the file name on the title bar.",
        ),
        _week(
            course, 2, total,
            "Text formatting — fonts, emphasis, alignment, lists",
            [
                "Apply font, size, bold, italic, underline appropriately",
                "Align text (left, centre, right, justify) for different purposes",
                "Create bullet and numbered lists",
            ],
            """Formatting makes documents easier to read. Titles are larger; body text stays calm (usually 11–12 pt).
Use bold for important words, not for whole pages. Lists help instructions and agendas.
Alignment: letters often left-aligned; titles may be centred. School work should look neat, not decorative and chaotic.""",
            [
                "Format a title vs body text live",
                "Build a short numbered list of class rules",
                "Show Format Painter to copy formatting",
            ],
            [
                "Format your week‑1 intro: title, body, one bullet list of 4 skills you hope to learn",
                "Use at least 2 font sizes and correct list style",
                "Save as YourName_Week02_Formatted.docx",
            ],
            [
                "Rainbow fonts on every sentence",
                "Huge italics body text that is hard to read",
                "Using spaces instead of real bullet lists",
            ],
            "Add a justified paragraph explaining why formatting helps readers.",
            "Home → Font\n• Title: 18–22 pt, bold\n• Body: 12 pt\nHome → Paragraph\n• Bullets / Numbering\n• Align Left / Center",
            [
                ("Best body text size for a school letter is usually:",
                 ["6 pt", "12 pt", "48 pt", "72 pt"], "12 pt"),
                ("To make a list of steps in order, use:",
                 ["Only bold", "Numbered list", "Text box only", "WordArt only"],
                 "Numbered list"),
            ],
            "Describe three formatting choices you made and why each improves clarity.",
            "Screenshot of the formatted document with title, body, and list visible.",
        ),
        _week(
            course, 3, total,
            "Page setup — margins, headers, footers, page numbers, images",
            [
                "Set margins and page orientation",
                "Insert header, footer, and page numbers",
                "Insert and resize an image without breaking the layout",
            ],
            """Page layout controls how print and screen previews look. Margins keep text away from edges.
Headers/footers carry name, class, or page numbers without retyping each page.
Images should support the message—resized, aligned, and not covering text. Use Insert carefully.""",
            [
                "Open Layout → Margins and show Normal vs Narrow",
                "Insert page number bottom centre",
                "Insert a small image and Wrap Text → Square",
            ],
            [
                "Create a 2-page mini report for any school subject",
                "Include header with your name, footer with page numbers, one relevant image",
                "Save as YourName_Week03_Report.docx",
            ],
            [
                "Images stretched until unreadable",
                "Text overflow outside margins",
                "No page numbers on multi-page work",
            ],
            "Add a caption under the image describing what it shows.",
            "Layout → Margins → Normal\nInsert → Header / Footer / Page Number\nInsert → Pictures → This Device\nPicture Format → Wrap Text → Square",
            [
                ("Page numbers are usually placed in the:",
                 ["Header or footer", "Only in the file name", "Task Manager", "Recycle Bin"],
                 "Header or footer"),
                ("If an image covers text, you should:",
                 ["Leave it", "Change Wrap Text / resize / move it", "Delete all text", "Zoom to 10%"],
                 "Change Wrap Text / resize / move it"),
            ],
            "Explain how headers, margins, and images make a multi-page report more professional.",
            "Screenshot showing header, page number, and the image in place.",
        ),
        _week(
            course, 4, total,
            "Capstone — formal letter or short multi-page report",
            [
                "Plan structure before typing",
                "Apply weeks 1–3 skills in one polished document",
                "Proofread and submit school-standard work",
            ],
            """Capstone week proves you can produce real school/office work.
Choose either (A) a formal request letter to a principal or manager, or (B) a short 2–3 page report
with title, introduction, body sections, conclusion, and one image.
Check: clear name, consistent formatting, list where useful, margins, page numbers, spelling.""",
            [
                "Show a model formal letter layout (addresses, date, salutation, body, closing)",
                "Checklist review against a rubric of neatness and completeness",
            ],
            [
                "Produce one complete letter OR report meeting the standards above",
                "Self-check with a 6-point checklist (name, structure, formatting, image/list, pages, spellcheck)",
                "Save as YourName_Week04_Capstone.docx",
            ],
            [
                "Submitting draft notes as ‘final’",
                "Missing salutation/closing in a letter",
                "Skipping spell check",
            ],
            "Add a one-paragraph reflection at the end: skill gained and one next goal.",
            "Letter skeleton:\nYour address\nDate\nRecipient\nDear …,\nBody paragraphs\nYours sincerely,\nName\n\nReport skeleton:\nTitle\n1. Introduction\n2. Main points\n3. Conclusion",
            [
                ("A formal letter should include:",
                 ["Only emojis", "Salutation and closing", "No date", "Random fonts each line"],
                 "Salutation and closing"),
                ("Before final submit you should:",
                 ["Never open the file", "Proofread and save clearly named final", "Delete pages", "Remove your name"],
                 "Proofread and save clearly named final"),
            ],
            "Summarise what your capstone document is about and the checklist items you verified.",
            "Screenshot of the final page(s) showing polished formatting and your name.",
        ),
    ]


def _office_excel(course: str, total: int) -> list[dict]:
    return [
        _week(
            course, 1, total,
            "Excel basics — sheets, cells, data entry, save",
            [
                "Navigate workbook, worksheets, rows, columns, and cells",
                "Enter text and numbers cleanly",
                "Save a .xlsx with correct naming",
            ],
            """Excel stores data in a grid. Columns are letters (A, B, C), rows are numbers (1, 2, 3).
Cell B3 means column B, row 3. Each sheet is a tab. Start with clean headers in row 1.
Never mix labels and numbers poorly — put numbers in their own cells so formulas can work later.""",
            [
                "Create headers Item, Qty, Price",
                "Enter 3 sample rows and save",
            ],
            [
                "Build a 5-row list of classroom supplies with Item, Qty, Price",
                "Save YourName_Week01_Supplies.xlsx",
            ],
            ["Typing two values in one cell when they should be separate", "Blank file name"],
            "Add a second sheet named ‘Notes’ with your name and date.",
            "A1: Item | B1: Qty | C1: Price\nA2: Pencil | B2: 12 | C2: 50",
            [
                ("Cell D5 is:", ["Row D column 5", "Column D row 5", "A formula only", "A chart"],
                 "Column D row 5"),
                ("Row 1 is best used for:", ["Random numbers", "Column headers", "Hidden passwords", "Macros only"],
                 "Column headers"),
            ],
            "Explain the difference between a worksheet and a workbook.",
            "Screenshot of your supplies table with headers visible.",
        ),
        _week(
            course, 2, total,
            "Formulas — SUM, AVERAGE, simple references",
            [
                "Write formulas starting with =",
                "Use cell references instead of retyping numbers",
                "Apply AutoSum for totals",
            ],
            """Formulas always start with =. Example: =B2*C2 calculates line total.
=SUM(D2:D6) adds a range. If you change a number, the formula updates automatically —
that is Excel’s power. Do not type the result by hand if a formula can compute it.""",
            ["Demonstrate =B2*C2 and drag fill", "Show SUM on a total row"],
            [
                "Add Line Total column with multiplication formula for each row",
                "Add Grand Total with SUM",
                "Save YourName_Week02_Formulas.xlsx",
            ],
            ["Forgetting =", "Summing text labels", "Hard-coding totals"],
            "Add AVERAGE of prices with =AVERAGE(C2:C6).",
            "D2: =B2*C2\nD7: =SUM(D2:D6)\nAverage price: =AVERAGE(C2:C6)",
            [
                ("Every formula begins with:", ["+", "=", "#", "@"], "="),
                ("=SUM(A1:A5) means:", ["Multiply A1 by A5", "Add cells A1 through A5", "Delete A1:A5", "Sort A1:A5"],
                 "Add cells A1 through A5"),
            ],
            "Describe one calculation you automated and why a formula is better than typing the answer.",
            "Screenshot showing formulas (or results) and a total row.",
        ),
        _week(
            course, 3, total,
            "Tables, sort, filter, and basic charts",
            [
                "Sort and filter a list",
                "Create a simple chart from data",
                "Label chart title clearly",
            ],
            """Sorting brings order (A→Z or largest price). Filters hide rows that do not match a choice.
Charts turn numbers into pictures — column and pie charts are common in school presentations.
Select the data including headers before Insert → Chart.""",
            ["Sort by Qty", "Insert Clustered Column chart"],
            [
                "Sort your table and create one chart with a clear title",
                "Save YourName_Week03_Chart.xlsx",
            ],
            ["Chart without title", "Selecting wrong range including empty rows"],
            "Add a second filter demo on one column and capture it in notes.",
            "Insert → Charts → Column\nChart title: Class Supplies Cost",
            [
                ("To show parts of a whole you might use a:", ["Pie chart", "WordArt only", "Header", "Filter arrow alone"],
                 "Pie chart"),
                ("Filter is used to:", ["Hide non-matching rows", "Print only", "Rename the file", "Encrypt Excel"],
                 "Hide non-matching rows"),
            ],
            "Explain what your chart communicates to a teacher in two sentences.",
            "Screenshot of the chart with title visible.",
        ),
        _week(
            course, 4, total,
            "Capstone — student scores or simple budget workbook",
            [
                "Design a useful multi-column sheet",
                "Combine data entry, formulas, and a chart",
                "Present results cleanly",
            ],
            """Build either (A) Student scores: Name, Test1, Test2, Test3, Average, with AVERAGE formulas and a chart,
or (B) Mini budget: Item, Planned, Actual, Difference formulas and total row.
Capstone must look intentional and school-ready.""",
            ["Show a sample score sheet structure"],
            [
                "Complete option A or B with at least 6 data rows + formulas + one chart",
                "Save YourName_Week04_Capstone.xlsx",
            ],
            ["Missing totals", "Chart of wrong data"],
            "Add a short text box or cell note: key insight from the numbers.",
            "Scores example:\nName | T1 | T2 | T3 | Average\nAverage: =AVERAGE(B2:D2)",
            [
                ("Average of numeric scores is best calculated with:",
                 ["AVERAGE formula", "Eye estimate only", "Bold button", "Zoom"], "AVERAGE formula"),
                ("A complete Excel capstone should include:",
                 ["Only colours", "Data, formulas, and a clear chart", "Nothing saved", "Only one cell"],
                 "Data, formulas, and a clear chart"),
            ],
            "State which project you chose and one insight from your results.",
            "Screenshot of the full capstone sheet and chart.",
        ),
    ]


def _office_ppt(course: str, total: int) -> list[dict]:
    return [
        _week(
            course, 1, total,
            "PowerPoint basics — slides, layout, text",
            [
                "Create a new presentation and add slides",
                "Use title and bullet layouts correctly",
                "Save as .pptx with a clear name",
            ],
            """PowerPoint presents ideas slide by slide. One idea per slide works better than walls of text.
Start with a title slide (topic + your name). Content slides use short bullets, not essays.
Design themes help consistency — pick one theme and keep it.""",
            ["New presentation, Title Slide, New Slide"],
            [
                "Create 4 slides: Title, About me, Favourite subject, Goals",
                "Save YourName_Week01_Intro.pptx",
            ],
            ["Paragraphs of 20 lines on one slide", "Mixed random themes"],
            "Add footer with your class name if available.",
            "Slide 1: Title + Name\nSlide 2: 3 bullets about you\nHome → New Slide",
            [
                ("Best practice for slide text is:",
                 ["Tiny essays", "Short bullets", "No titles", "Only images forever"],
                 "Short bullets"),
                ("Title slide should usually show:",
                 ["Topic and presenter name", "File path only", "Task Manager", "Random clipart chaos"],
                 "Topic and presenter name"),
            ],
            "Why is one main idea per slide helpful for the audience?",
            "Screenshot of slide sorter or title + one content slide.",
        ),
        _week(
            course, 2, total,
            "Visual design — images, alignment, consistency",
            [
                "Insert and size images",
                "Keep consistent fonts and colours",
                "Align objects neatly",
            ],
            """Design is not decoration overload. Use images that support the message.
Align left edges of text boxes. Limit fonts to one or two families.
White space (empty space) helps reading. School presentations should look calm and clear.""",
            ["Insert picture, align tools"],
            [
                "Improve week‑1 deck: add images, consistent fonts, aligned text",
                "Save YourName_Week02_Design.pptx",
            ],
            ["Stretched photos", "Five font styles on one slide"],
            "Apply one theme across all slides.",
            "Picture → Wrap/size carefully\nUse Align → Left on selected shapes",
            [
                ("Consistent theme means:",
                 ["Same fonts/colours family across slides", "New theme every slide", "No titles", "Black text only on black"],
                 "Same fonts/colours family across slides"),
                ("Images should:",
                 ["Distract from the topic", "Support the message", "Cover all text always", "Be unreadable"],
                 "Support the message"),
            ],
            "List three design rules you followed.",
            "Screenshot of two improved slides.",
        ),
        _week(
            course, 3, total,
            "Delivery craft — transitions, animations, speaker notes",
            [
                "Apply light transitions",
                "Use animation sparingly for emphasis",
                "Write speaker notes for presenters",
            ],
            """Transitions move between slides; animations move objects on a slide.
Too much motion looks unprofessional. Prefer subtle fades.
Speaker notes help you talk without packing every word onto the slide.""",
            ["Add Fade transition", "Show Notes pane"],
            [
                "Add consistent transitions, 1–2 meaningful animations total, notes on 3 slides",
                "Save YourName_Week03_Delivery.pptx",
            ],
            ["Spinning text on every bullet", "Reading walls of text word-for-word from slides"],
            "Rehearse 90 seconds and note timing.",
            "Transitions → Fade\nAlt / View → Notes",
            [
                ("Animations should be:",
                 ["Everywhere always", "Rare and purposeful", "Faster than readable", "Random"],
                 "Rare and purposeful"),
                ("Speaker notes are for:",
                 ["The presenter", "Replacing all slides", "Hiding bad design only", "Deleting content"],
                 "The presenter"),
            ],
            "What will you say on your most important slide? Write it as notes text.",
            "Screenshot of Notes view on one slide.",
        ),
        _week(
            course, 4, total,
            "Capstone — 8–10 slide school presentation",
            [
                "Structure a full talk with clear arc",
                "Deliver polished slides for a real topic",
            ],
            """Build 8–10 slides on a school-approved topic (environment, career, history figure, science idea).
Structure: Title → Why it matters → 3–5 teaching points → Example → Summary → Q&A/Thank you.
Apply design + light motion + notes.""",
            ["Show sample outline"],
            [
                "Finish 8–10 slide capstone and save YourName_Week04_Capstone.pptx",
            ],
            ["Off-topic memes only", "Missing conclusion"],
            "Export PDF backup if teacher requests.",
            "Outline:\n1 Title\n2 Agenda\n3–7 Content\n8 Summary\n9 Thanks",
            [
                ("A strong ending slide often includes:",
                 ["Summary or thank you / questions", "Nothing", "Only a huge GIF", "Broken links only"],
                 "Summary or thank you / questions"),
                ("Capstone length target here is:",
                 ["1 slide", "8–10 slides", "100 slides", "0 slides"],
                 "8–10 slides"),
            ],
            "State your topic and the three main points the audience should remember.",
            "Screenshot of slide sorter showing the full deck.",
        ),
    ]


def _four_week_creative_ai_design(course: str, total: int) -> list[dict]:
    return [
        _week(
            course, 1, total,
            "AI design tools, safety, and export basics",
            [
                "Explain what generative image tools can and cannot do",
                "Write a clear simple prompt",
                "Export/download results into a class folder",
            ],
            """AI image tools generate pictures from text prompts. They help brainstorm visuals quickly,
but you remain responsible for quality, school-safe content, and honesty (you guided the tool).
Prompts should name subject, setting, style, and mood. Avoid harmful, violent, or copyrighted character requests
outside school rules. Always save finals into YourName_AI_Design folder.""",
            ["Live write a prompt and generate 2 variants", "Show download PNG"],
            [
                "Generate 3 school-safe images for one theme (e.g. library week)",
                "Save with clear names and note prompts used in a txt/docx",
            ],
            ["Unsafe prompts", "No saving of prompt history"],
            "Write a better prompt by adding lighting and camera angle words.",
            "Prompt pattern:\nA [subject] in [place], [style], [lighting], school-friendly poster look --ar 1:1",
            [
                ("A complete prompt usually includes:",
                 ["Only one random word", "Subject + context + style", "Your password", "Nothing"],
                 "Subject + context + style"),
                ("School AI art should be:",
                 ["Violent for fun", "Safe and respectful", "Copied from classmates without credit", "Hidden from teacher"],
                 "Safe and respectful"),
            ],
            "Paste one prompt you used and explain why it worked or failed.",
            "Screenshot of the AI tool with your result and prompt area if visible.",
        ),
        _week(
            course, 2, total,
            "Composition and readable design",
            [
                "Use hierarchy: main subject large, background calm",
                "Apply contrast so text (if any) remains readable",
            ],
            """Beautiful images still fail if composition is messy. Place the subject off-centre sometimes (rule of thirds).
Leave space if you will add titles later. High contrast (dark text on light areas) helps posters.
Iterate: change one prompt factor at a time so you learn what matters.""",
            ["Compare weak vs strong composition side by side"],
            [
                "Create 4 improved images; pick 1 ‘hero’ visual for a poster base",
                "Document before/after prompts",
            ],
            ["Busy backgrounds with unreadable future text areas"],
            "Crop thoughtfully if the tool allows outpainting/region focus.",
            "Checklist:\n• Clear subject\n• Space for title\n• Limited clutter\n• Consistent style across set",
            [
                ("Rule of thirds helps you:",
                 ["Ignore subject", "Place interest off dead-centre", "Delete images", "Encrypt files"],
                 "Place interest off dead-centre"),
                ("When comparing versions you should change:",
                 ["Everything at once always", "One factor at a time when learning", "Nothing ever", "Only the file name"],
                 "One factor at a time when learning"),
            ],
            "Describe the composition rule you applied to your hero image.",
            "Screenshot of your selected hero image.",
        ),
        _week(
            course, 3, total,
            "Brand kit & social formats",
            [
                "Create matching assets for more than one size",
                "Keep colour/mood consistent",
            ],
            """Brands feel real when assets match. Build a mini set: profile/square post, story/vertical concept, and simple logo-mark idea
using AI + any text tool allowed in class. Name colours roughly (teal, cream, ink). Export organised files.""",
            ["Show 1:1 vs 9:16 framing"],
            [
                "Deliver 3 matching assets + a one-page note of brand rules (colours, mood words)",
            ],
            ["Every asset a totally different style"],
            "Make a monochrome version for accessibility contrast test.",
            "Files:\nbrand_square.png\nbrand_story.png\nbrand_mark.png\nrules.txt",
            [
                ("A brand kit should feel:",
                 ["Random every post", "Visually related", "Impossible to open", "Unlabelled"],
                 "Visually related"),
                ("Vertical 9:16 is common for:",
                 ["Stories/reels style frames", "Only floppy disks", "Excel charts alone", "Word mail merge"],
                 "Stories/reels style frames"),
            ],
            "List your 3 mood words and primary colour idea.",
            "Screenshot collage or folder showing the three assets.",
        ),
        _week(
            course, 4, total,
            "Capstone — mini campaign (3 assets)",
            [
                "Plan a message for a real audience (school event / club / product idea)",
                "Ship 3 polished assets + written rationale",
            ],
            """Capstone: invent a positive school campaign (reading club, sports day, coding week).
Deliver three coordinated AI-assisted visuals and a short rationale (audience, message, where each asset is used).
Quality over quantity — neat exports, clear names, school-safe content.""",
            ["Rubric: clarity, consistency, safety, completeness"],
            [
                "Submit campaign pack + rationale doc YourName_AI_Capstone",
            ],
            ["Offensive content", "Incomplete set"],
            "Add a mockup (phone frame) if tools allow.",
            "Rationale template:\nAudience:\nMessage:\nAsset A use:\nAsset B use:\nAsset C use:",
            [
                ("A campaign pack is stronger when assets are:",
                 ["Unrelated", "Coordinated", "Hidden", "Unnamed"],
                 "Coordinated"),
                ("Rationale explains:",
                 ["Why design choices fit the audience", "Your Wi-Fi password", "Nothing", "Only the file size"],
                 "Why design choices fit the audience"),
            ],
            "Write your campaign message in one sentence and name the three assets.",
            "Screenshot of all three final assets together.",
        ),
    ]


def _four_week_video_ai(course: str, total: int) -> list[dict]:
    return [
        _week(
            course, 1, total,
            "Timeline, imports, and clean cuts",
            [
                "Create a project with correct resolution",
                "Import clips and perform rough cuts",
            ],
            """Video editing arranges clips on a timeline. Set project frame size early (e.g. 1920×1080).
Import media into bins/folders when possible. Cut removes sections — prefer many short clean cuts over one messy take.
Name your project YourName_Week01_Edit.""",
            ["Import 2 clips, trim start/end"],
            [
                "Build a 20–30 second rough cut from classroom-safe footage or free stock",
                "Save project file",
            ],
            ["Editing the only copy without backup", "Huge untrimmed clips"],
            "Label tracks Video1 / Audio1 clearly if available.",
            "Workflow:\nNew project → Import → Drag to timeline → Blade/Trim → Save",
            [
                ("A timeline is where you:",
                 ["Arrange clips over time", "Write Excel formulas", "Browse only folders", "Design fonts only"],
                 "Arrange clips over time"),
                ("Rough cut means:",
                 ["Final colour grade only", "Early assembly of order and length", "Deleting the project", "Export fail"],
                 "Early assembly of order and length"),
            ],
            "List your clip sources and total rough-cut length.",
            "Screenshot of timeline with at least two clips.",
        ),
        _week(
            course, 2, total,
            "Story, audio levels, and captions",
            [
                "Order clips for a clear beginning-middle-end",
                "Balance voice vs music",
                "Add basic captions or titles",
            ],
            """Story first: hook viewers in 3 seconds, teach one idea, end with a clear finish.
Audio issues fail student videos quickly — voice should be clear; music quieter than speech.
Captions help classmates and accessibility. Keep titles on screen long enough to read.""",
            ["Show audio meters; add simple caption"],
            [
                "Upgrade rough cut to 30–45s with titles/captions and balanced audio",
            ],
            ["Music drowning voice", "Flash titles for 5 frames"],
            "Add an end card with your name and topic.",
            "Hook (0–3s) → Main point → Example → End card\nMusic ~ −20 to −12 dB under voice",
            [
                ("Music should usually be:",
                 ["Louder than speech", "Quieter than speech", "Silent always only", "Distorted on purpose"],
                 "Quieter than speech"),
                ("Captions help:",
                 ["Accessibility and noisy environments", "Only GPU temperature", "Excel pivot tables", "Nothing"],
                 "Accessibility and noisy environments"),
            ],
            "Write the one sentence main message of your video.",
            "Screenshot with captions/titles visible on the program monitor.",
        ),
        _week(
            course, 3, total,
            "AI helpers, polish, multi-format export",
            [
                "Use permitted AI assist (captions cleanup / enhance) carefully",
                "Export 16:9 and one vertical or square if required",
            ],
            """AI tools can speed captions or cleanup, but you still edit for truth and clarity.
Do not invent fake harmful footage. Export settings: H.264/MP4 is common for school sharing.
Keep masters and exports in separate folders.""",
            ["Demonstrate export dialog"],
            [
                "Export final 45–60s MP4 + keep project file",
            ],
            ["Exporting ultra bitrate files that cannot be submitted", "Overwriting project with export"],
            "Create a 9:16 reframed version if tool supports auto-reframe.",
            "Export preset ideas:\nMP4 H.264\n1080p\nPublish folder: /Exports",
            [
                ("A common student upload format is:",
                 ["MP4", "SYS32", "DLL only", "RAW camera without edit only always"],
                 "MP4"),
                ("AI caption tools still need:",
                 ["Human review for errors", "No review ever", "Deleted audio", "Random languages only"],
                 "Human review for errors"),
            ],
            "Which export settings did you use (resolution/format)?",
            "Screenshot of export settings or file properties of the MP4.",
        ),
        _week(
            course, 4, total,
            "Capstone — 45–90 second promo or tutorial",
            [
                "Ship a complete short video with story, titles, sound, export",
            ],
            """Capstone topic: school event promo OR how-to tutorial (e.g. how to save a Word file).
Must include hook, main content, captions/titles, end card, and clean export.
Rubric: clarity, audio, pacing, completeness.""",
            ["Show gold-standard sample length pacing"],
            [
                "Submit final MP4 + project if teacher asks + 3 sentence description",
            ],
            ["Off-topic long rambling", "No end card"],
            "Add subtle background music with license allowed in class.",
            "Capstone checklist:\nHook\nMain demo\nCaption\nEnd card\nExport MP4",
            [
                ("Target length for this capstone is about:",
                 ["45–90 seconds", "2 hours", "1 frame", "10 minutes minimum always"],
                 "45–90 seconds"),
                ("A tutorial video should:",
                 ["Show steps clearly", "Hide the cursor always", "Skip saving steps", "Use inaudible audio"],
                 "Show steps clearly"),
            ],
            "Describe your video purpose and the three steps a viewer should learn or feel.",
            "Screenshot of the finished timeline and first frame of export.",
        ),
    ]


def _expand_from_topics(slug: str, course_title: str) -> list[dict]:
    """Full notes for multi-month courses based on topic list + domain packs."""
    topics = TOPICS.get(slug) or [f"Module {i}" for i in range(1, weeks_for(slug) + 1)]
    total = weeks_for(slug)
    topics = (topics + [f"Extended practice {i}" for i in range(len(topics) + 1, total + 1)])[:total]
    domain = slug
    out = []
    for i, topic in enumerate(topics, 1):
        title = topic.split("—")[0].strip() if "—" in topic else topic
        detail = topic.split("—", 1)[1].strip() if "—" in topic else topic
        objectives = [
            f"Explain the key idea: {title}",
            f"Complete a guided practice on {detail}",
            "Save evidence of work for assessment",
        ]
        theory = _domain_theory(domain, course_title, i, total, title, detail)
        demos = [
            f"Teacher walks through core idea of “{title}” with a live example",
            "Show the finished look of this week’s practice file/project piece",
            "Highlight common error class historically makes and how to fix it",
        ]
        practice = [
            f"Complete main exercise for: {detail}",
            "Produce a neat version following class naming rules",
            "Prepare screenshot of the completed critical step",
        ]
        if i == total:
            practice.append("Assemble final capstone package meeting the checklist")
        mistakes = _domain_mistakes(domain, i, total)
        stretch = _domain_stretch(domain, title)
        examples = _domain_examples(domain, course_title, i, title, detail)
        mcqs = _domain_mcqs(domain, title, detail, i, total)
        subjective = (
            f"Explain what you built or practised for “{title}” and one problem you solved."
            if i < total
            else f"Describe your final {course_title} project, skills used, and one improvement for later."
        )
        upload = (
            f"Upload a clear screenshot of this week’s completed work ({title})."
            if i < total
            else "Upload a screenshot of your finished capstone (readable and complete)."
        )
        out.append(
            _week(
                course_title,
                i,
                total,
                title if len(title) < 70 else title[:67] + "…",
                objectives,
                theory,
                demos,
                practice,
                mistakes,
                stretch,
                examples,
                mcqs,
                subjective,
                upload,
            )
        )
    return out


def _domain_theory(domain: str, course: str, week: int, total: int, title: str, detail: str) -> str:
    base = (
        f"This is week {week} of {total} in {course}. Focus: {title}.\n\n"
        f"Context: {detail}.\n\n"
    )
    packs = {
        "graphic-coreldraw": (
            "CorelDRAW is a vector program — shapes stay sharp when scaled. Build with shapes, text, and colour, "
            "then arrange with alignment tools. Always keep the .cdr source file and export copies (PNG/PDF) for sharing. "
            "Work from structure (page size, guides) before decoration. "
            f"This week emphasise mastery of: {title}."
        ),
        "scratch": (
            "Scratch teaches computational thinking with blocks: sequence, loops, conditions, events. "
            "Scripts run top to bottom; events start actions. Test often with the green flag. "
            f"Today’s lab centres on {title} — build small, test, then extend."
        ),
        "python-for-beginners": (
            "Python programs are plain text instructions the computer runs line by line. "
            "Readable names and small tests beat one giant messy file. "
            f"This week you will use Python to work with: {title}."
        ),
        "python-blocks": (
            "Block coding mirrors Python ideas visually. Each block is an instruction. "
            "Order matters. When you can explain the block flow aloud, you are ready for text Python later. "
            f"Focus: {title}."
        ),
        "python-developer": (
            "Professional Python emphasises clear structure, reusable functions, and careful testing. "
            "You will gradually move from scripts to modules and larger program design. "
            f"This week’s craft skill: {title}."
        ),
        "python-data-apps": (
            "Data work is questions first, charts second. Clean tables, honest summaries, and simple visuals "
            "help people decide. Document assumptions. "
            f"Apply that lens to: {title}."
        ),
        "ai-engineer": (
            "Applied AI systems need goals, data/inputs, model or API behaviour, evaluation, and safety limits. "
            "Hype language is not enough — define what success means in measurable terms. "
            f"Deepen understanding of: {title}."
        ),
        "android-app-development": (
            "Android apps present screens (layouts) that respond to user events and sometimes store data. "
            "Think through navigation and readable touch targets. Test on emulator or device frequently. "
            f"Implementation focus: {title}."
        ),
        "website-development": (
            "Websites combine structure (HTML), appearance (CSS), and optional behaviour (JavaScript). "
            "Build simple pages first; responsiveness and accessibility are part of quality. "
            f"This week: {title}."
        ),
        "cloud-computing": (
            "Cloud computing rents compute, storage, and networking with pay-as-you-go models. "
            "You must still plan security, backup, and cost. Diagrams clarify who talks to whom. "
            f"Concept for practice: {title}."
        ),
        "system-design-thinking": (
            "System design and design thinking combine user needs with structured components and flows. "
            "Sketch before you build. Name assumptions. Consider failure cases. "
            f"This week’s lens: {title}."
        ),
    }
    for key, text in packs.items():
        if key in domain:
            return base + text
    return base + (
        f"Study the concept “{title}” carefully, practise with the demo, then produce your own complete attempt. "
        "Difficulty increases across the course; solid foundations earlier weeks pay off later."
    )


def _domain_mistakes(domain: str, week: int, total: int) -> list[str]:
    common = [
        "Skipping save / unclear file names",
        "Rushing without testing the practice steps",
        "Submitting incomplete screenshots that hide the work",
    ]
    if week == total:
        common.append("Missing capstone checklist items")
    if "python" in domain:
        common.append("Ignoring error messages instead of reading them")
    if "graphic" in domain or "corel" in domain:
        common.append("Decorating before setting page size and structure")
    return common[:4]


def _domain_stretch(domain: str, title: str) -> str:
    return f"Create a second mini version of this week’s task focusing on one improvement related to {title}."


def _domain_examples(domain: str, course: str, week: int, title: str, detail: str) -> str:
    if "python" in domain or "python" in course.lower():
        return (
            f"# {course} — Week {week}: {title}\n"
            f"# Focus: {detail}\n\n"
            "def demo():\n"
            f'    print("Practising:", "{title}")\n'
            "    # TODO: complete class exercise here\n"
            "    return True\n\n"
            "if __name__ == '__main__':\n"
            "    demo()\n"
        )
    if "website" in domain or "html" in detail.lower():
        return (
            f"<!-- Week {week}: {title} -->\n"
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            f"  <meta charset=\"utf-8\">\n  <title>{title}</title>\n"
            "  <style>body{font-family:sans-serif;margin:2rem}</style>\n"
            "</head>\n<body>\n"
            f"  <h1>{title}</h1>\n  <p>{detail}</p>\n"
            "</body>\n</html>\n"
        )
    if "corel" in domain or "graphic" in domain:
        return (
            f"CorelDRAW / design checklist — Week {week}\n"
            f"Topic: {title}\n"
            "1) Set page size  2) Guides/margins  3) Main objects  4) Text last  5) Export PNG + keep source\n"
            f"Detail: {detail}\n"
        )
    if "scratch" in domain or "blocks" in domain:
        return (
            f"Block plan — Week {week}: {title}\n"
            "when green flag clicked\n"
            "  // setup\n"
            "  forever\n"
            "    // response to events for this week's skill\n"
        )
    if "android" in domain:
        return (
            f"Screen plan — Week {week}: {title}\n"
            "- Title text\n- Primary action button\n- Result / content area\n"
            f"Implement focus: {detail}\n"
        )
    if "cloud" in domain or "system" in domain:
        return (
            f"Diagram labels — Week {week}\n"
            f"{title}\n"
            "User → Component A → Component B → Data store\n"
            f"Notes: {detail}\n"
        )
    if "video" in domain:
        return (
            f"Edit plan — Week {week}: {title}\n"
            "Hook / Main / Supporting B-roll / End card\n"
            f"Skill: {detail}\n"
        )
    if "data" in domain:
        return (
            f"Data table sketch — Week {week}\n"
            "ColumnA | ColumnB | ColumnC\n"
            " … rows …\n"
            f"Analysis focus: {detail}\n"
        )
    return (
        f"Practice sheet — Week {week}\nCourse: {course}\nTopic: {title}\n"
        f"Instructions: {detail}\nDeliverable: completed file + screenshot\n"
    )


def _domain_mcqs(domain: str, title: str, detail: str, week: int, total: int) -> list[tuple]:
    a = (
        f"What is the main learning target for “{title}”?",
        [
            "Avoid the topic completely",
            f"Understand and practise: {title}",
            "Only change the wallpaper",
            "Delete last week’s work permanently",
        ],
        f"Understand and practise: {title}",
    )
    if week == total:
        b = (
            "A capstone submission should be:",
            [
                "Empty",
                "Complete, named clearly, and explainable",
                "Someone else’s file without credit",
                "Unsaved forever",
            ],
            "Complete, named clearly, and explainable",
        )
    else:
        b = (
            f"When practising “{detail}”, you should:",
            [
                "Never test the steps",
                "Follow guided practice then try your own version",
                "Skip saving",
                "Only watch without doing",
            ],
            "Follow guided practice then try your own version",
        )
    return [a, b]


def syllabus_for(slug: str, course_title: str) -> list[dict]:
    total = weeks_for(slug)
    if slug == "office-ms-word":
        return _office_word(course_title, total)
    if slug == "office-excel":
        return _office_excel(course_title, total)
    if slug == "office-powerpoint":
        return _office_ppt(course_title, total)
    if slug == "graphic-ai":
        return _four_week_creative_ai_design(course_title, total)
    if slug == "video-editing-ai":
        return _four_week_video_ai(course_title, total)
    return _expand_from_topics(slug, course_title)


def all_slugs() -> list[str]:
    return list(COURSE_DURATION_MONTHS.keys())
