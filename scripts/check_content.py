#!/usr/bin/env python3
"""
Friendly checker for the website's content files.

It runs automatically on GitHub every time someone edits the site (see
.github/workflows/check-content.yml), and you can also run it yourself:

    pip install pyyaml
    python scripts/check_content.py

It catches the mistakes that are easy to make when editing by hand:
a missing quote, a photo name that doesn't match the uploaded file,
a date written the wrong way, or a YouTube link that isn't a video link.

Errors (red X) must be fixed. Warnings are only reminders, for example
that sample text is still on the site.
"""

import datetime
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("This checker needs PyYAML. Install it with:  pip install pyyaml")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "_data")
IMAGES = os.path.join(ROOT, "assets", "images")

PLACEHOLDER_HINTS = ["20XX", "Sample Name", "example.com", "Replace this", "Your major", "Campus venue name"]
YOUTUBE_PATTERNS = [
    r"youtu\.be/([\w-]{11})",
    r"youtube\.com/shorts/([\w-]{11})",
    r"youtube\.com/embed/([\w-]{11})",
    r"[?&]v=([\w-]{11})",
]

errors = []
warnings = []
on_github = os.environ.get("GITHUB_ACTIONS") == "true"


def report(kind, filename, message):
    bucket = errors if kind == "error" else warnings
    bucket.append((filename, message))
    if on_github:
        print(f"::{kind} file=_data/{filename}::{message}")
    else:
        label = "ERROR  " if kind == "error" else "warning"
        print(f"  {label}  {filename}: {message}")


def load(filename):
    path = os.path.join(DATA, filename)
    if not os.path.exists(path):
        report("error", filename, "this file is missing. Restore it from the repository history.")
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        where = f" (around line {mark.line + 1})" if mark else ""
        report(
            "error",
            filename,
            f"the file could not be read{where}. Usual causes: a missing or extra quotation mark, "
            "or a line that is not lined up with the ones around it.",
        )
        return None


def text(value):
    return "" if value is None else str(value).strip()


def check_image(filename, label, value, folder=""):
    """Make sure an image named in a data file really exists in assets/images/<folder>."""
    name = text(value)
    if not name:
        return
    directory = os.path.join(IMAGES, folder) if folder else IMAGES
    where = f"assets/images/{folder}/" if folder else "assets/images/"
    if os.path.exists(os.path.join(directory, name)):
        if " " in name:
            report("warning", filename, f'{label}: "{name}" has a space in its name. Spaces can break links; use dashes instead.')
        return
    hint = ""
    if os.path.isdir(directory):
        for existing in os.listdir(directory):
            if existing.lower() == name.lower():
                hint = f' Did you mean "{existing}"? Capital letters matter.'
                break
    report("error", filename, f'{label}: no photo named "{name}" in {where}.{hint}')


def check_placeholders(filename, data):
    found = set()

    def walk(node):
        if isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
        elif isinstance(node, str):
            for hint in PLACEHOLDER_HINTS:
                if hint.lower() in node.lower():
                    found.add(hint)

    walk(data)
    if found:
        report("warning", filename, "still has sample text to replace (" + ", ".join(sorted(found)) + ").")


def as_list(value):
    return value if isinstance(value, list) else []


# --------------------------------------------------------------------------

def check_group():
    f = "group.yml"
    data = load(f)
    if data is None:
        return
    if not isinstance(data, dict):
        report("error", f, "this file should be a list of settings like  name: \"The Frequency\".")
        return
    if not text(data.get("name")):
        report("error", f, "name is empty.")
    check_image(f, "logo", data.get("logo"))
    check_image(f, "hero_photo", data.get("hero_photo"), "hero")
    email = text(data.get("email"))
    if email and "@" not in email:
        report("error", f, f'email "{email}" does not look like an email address.')
    auditions = data.get("auditions") or {}
    if "open" in auditions and not isinstance(auditions["open"], bool):
        report("error", f, "auditions: open must be exactly true or false, with no quotes.")
    check_placeholders(f, data)


def check_about():
    f = "about.yml"
    data = load(f)
    if data is None:
        return
    if not isinstance(data, dict):
        report("error", f, "this file should be a list of settings.")
        return
    for item in as_list(data.get("story_images")):
        check_image(f, "story_images", (item or {}).get("file"), "about")
    for item in as_list(data.get("milestones")):
        check_image(f, "milestones", (item or {}).get("image"), "about")
    if not isinstance(data.get("story", []), list):
        report("error", f, "story must be a list: each paragraph on its own line starting with a dash.")
    check_placeholders(f, data)


def check_board():
    f = "board.yml"
    data = load(f)
    if data is None:
        return
    if not isinstance(data, list):
        report("error", f, "this file should be a list. Each person starts with a dash.")
        return
    for i, person in enumerate(data, start=1):
        person = person or {}
        label = text(person.get("name")) or f"board member #{i}"
        if not text(person.get("name")):
            report("error", f, f"board member #{i} has no name.")
        check_image(f, label, person.get("photo"), "board")
    check_placeholders(f, data)


def check_videos():
    f = "videos.yml"
    data = load(f)
    if data is None:
        return
    if not isinstance(data, list):
        report("error", f, "this file should be a list. Each video starts with a dash.")
        return
    for i, video in enumerate(data, start=1):
        video = video or {}
        label = text(video.get("title")) or f"video #{i}"
        url = text(video.get("url"))
        if not url:
            continue
        if not any(re.search(p, url) for p in YOUTUBE_PATTERNS):
            report("error", f, f'{label}: "{url}" is not a link to a single YouTube video. '
                               "Open the video on YouTube and copy the address from your browser.")
        if "list=" in url and "v=" not in url:
            report("error", f, f"{label}: this looks like a playlist link. Use a link to one video.")


def check_shows():
    f = "shows.yml"
    data = load(f)
    if data is None:
        return
    if not isinstance(data, list):
        report("error", f, "this file should be a list. Each show starts with a dash.")
        return
    for i, show in enumerate(data, start=1):
        show = show or {}
        label = text(show.get("title")) or f"show #{i}"
        raw = show.get("date")
        if isinstance(raw, (datetime.date, datetime.datetime)):
            report("warning", f, f'{label}: put the date in quotes, like "{raw:%Y-%m-%d}".')
            continue
        value = text(raw)
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            report("error", f, f'{label}: the date "{value}" must look like "2026-11-14" (year-month-day).')
        if not text(show.get("title")):
            report("error", f, f"show #{i} has no title.")
    check_placeholders(f, data)


def check_gallery():
    f = "gallery.yml"
    data = load(f)
    if data is None:
        return
    if not isinstance(data, list):
        report("error", f, "this file should be a list. Each photo starts with a dash.")
        return
    for item in data:
        item = item or {}
        check_image(f, "gallery photo", item.get("file"), "gallery")
        if text(item.get("file")) and not text(item.get("alt")):
            report("warning", f, f'photo "{item.get("file")}" has no alt text (a short description for people who cannot see it).')


def main():
    print("Checking the website content...")
    for check in (check_group, check_about, check_board, check_videos, check_shows, check_gallery):
        check()
    print()
    if errors:
        print(f"{len(errors)} problem(s) to fix, {len(warnings)} reminder(s).")
        return 1
    print(f"All good. {len(warnings)} reminder(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
