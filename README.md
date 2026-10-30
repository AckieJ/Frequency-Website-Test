# The Frequency

Website for **The Frequency**, an a cappella group at UC San Diego.

The site has two pages:

- **Home**: logo, group photo, performance videos from YouTube, upcoming and past shows, photo gallery, and a way to book the group.
- **About**: when the group was founded, its story with photos, an optional timeline, and the board (name, role, major, part, and a fun fact for each member).

It is built to be edited by people who don't code. All the content lives in plain text files, and everything can be changed from a web browser.

## Edit the site

**Start here: [docs/EDITING.md](docs/EDITING.md)**

| To change... | Edit |
|---|---|
| Group name, tagline, email, social links, logo, auditions banner | [`_data/group.yml`](_data/group.yml) |
| Videos | [`_data/videos.yml`](_data/videos.yml) |
| Shows | [`_data/shows.yml`](_data/shows.yml) |
| Home page photo gallery | [`_data/gallery.yml`](_data/gallery.yml) |
| About page text and timeline | [`_data/about.yml`](_data/about.yml) |
| Board members | [`_data/board.yml`](_data/board.yml) |
| Photos | [`assets/images/`](assets/images/) |

Every file has comments that explain what to type. The site rebuilds by itself about a minute after you save a change.

## Put it online

See [docs/PUBLISHING.md](docs/PUBLISHING.md) for turning on GitHub Pages, keeping the site alive after current members graduate, and the custom domain question.

## Repository map

```
.
├── _data/                 Words, links, dates, board bios (the files you edit)
├── assets/
│   ├── images/            Photos: hero/, about/, board/, gallery/ (+ logo here)
│   ├── css/style.css      Colors and layout
│   └── js/site.js         Click-to-play videos, past-show sorting
├── _layouts/ _includes/   Page templates
├── index.html             Home page
├── about.html             About page
├── docs/                  Guides for editing and publishing
├── scripts/               Content checker
└── .github/               Automatic checks and request forms
```

## Automatic checks

When someone edits `_data/` or `assets/images/`, GitHub runs [`scripts/check_content.py`](scripts/check_content.py). It flags a missing quote, a photo name that doesn't match an uploaded file, a date in the wrong format, or a YouTube link that isn't a single video, and explains the fix in plain English. You can run it yourself:

```bash
pip install pyyaml
python scripts/check_content.py
```

## How it works

The site uses [Jekyll](https://jekyllrb.com/), which GitHub Pages builds automatically (no build setup needed). Pages read their content from `_data/*.yml`. Photos are looked up by file name, and anything left blank shows a tidy placeholder instead of a broken image.

## License

Code is MIT licensed (see [LICENSE](LICENSE)). The group's name, logo, photos, and recordings belong to The Frequency and their owners.
