"""
CloudCity Academy — real subject notes (V4).

Each week = 3 lectures of actual course content + worked example + lab.
No pedagogy boilerplate (no cold-call scripts, integrity sermons, progression fluff).
"""
from __future__ import annotations

import json
from typing import Any

from curriculum import TOPICS, weeks_for
from real_content import week_content

MARKER = "[[CCA_CURRICULUM_V4]]"


def _mcq(prompt: str, options: list[str], correct: str, points: int = 2, order: int = 1):
    return ("mcq", prompt, json.dumps(options), correct, points, order)


def _render(course: str, week: int, total: int, pack: dict) -> str:
    lines = [
        MARKER,
        f"# Week {week} of {total} — {pack['title']}",
        f"Course: {course}",
        "Class pattern: 3 lectures this week + practice lab. Notes are the subject material.",
        "",
        "## Overview",
        pack["overview"],
        "",
        "## Learning targets",
        *[f"- {o}" for o in pack["objectives"]],
        "",
    ]
    labels = ("Lecture 1", "Lecture 2", "Lecture 3")
    for label, (heading, body) in zip(labels, pack["lectures"]):
        lines += [f"## {label}: {heading}", body.strip(), ""]
    lines += [
        "## Worked example",
        pack["example"],
        "",
        "## Lab (class + home practice)",
        *[f"{i}. {s}" for i, s in enumerate(pack["lab"], 1)],
        "",
        "## Terms",
        *[f"- **{k}** — {v}" for k, v in pack["vocab"]],
        "",
        "Complete the weekly assessment: objective items, short written explanation of the technique, "
        "and a screenshot of your finished lab artefact.",
    ]
    return "\n".join(lines)


def _examples_block(pack: dict) -> str:
    return (
        "WORKED EXAMPLE\n"
        f"{pack['example']}\n\n"
        "LAB\n"
        + "\n".join(f"{i}. {s}" for i, s in enumerate(pack["lab"], 1))
    )


def syllabus_for(slug: str, course_title: str) -> list[dict[str, Any]]:
    total = weeks_for(slug)
    topics = TOPICS.get(slug) or [f"Module {i}" for i in range(1, total + 1)]
    topics = (topics + [f"Extended topic {i}" for i in range(len(topics) + 1, total + 1)])[:total]
    out: list[dict[str, Any]] = []
    for week, topic in enumerate(topics, 1):
        pack = week_content(slug, week, course_title, topic)
        content = _render(course_title, week, total, pack)
        questions = []
        for i, (prompt, opts, correct) in enumerate(pack["mcqs"], 1):
            questions.append(_mcq(prompt, opts, correct, 2, i))
        questions.append(("subjective", pack["subjective"], None, None, 4, len(questions) + 1))
        questions.append(("upload", pack["upload"], None, None, 4, len(questions) + 1))
        out.append(
            {
                "week": week,
                "title": f"Week {week}: {pack['title']}",
                "topic": pack["title"],
                "content": content,
                "examples": _examples_block(pack),
                "questions": questions,
            }
        )
    return out
