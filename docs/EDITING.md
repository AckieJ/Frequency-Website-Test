# How to edit the website (no coding needed)

Everything you would ever want to change is in two places:

- **`_data/`** holds the words, links, dates, and board bios.
- **`assets/images/`** holds the photos.

You can do all of this in your web browser on github.com. You never need to install anything.

## The five rules for editing text files

The files in `_data/` look a bit like a form. Each one has a few simple rules:

1. **Keep the quotation marks.** Change what is between them, not the marks themselves.
2. **Keep the spacing at the start of each line.** The little indents line things up. Don't add or remove them.
3. **A line starting with `-` is one item** (one person, one video, one show). To add an item, copy the whole block and paste it below.
4. **Lines starting with `#` are notes to you.** The website ignores them.
5. **Don't put a straight double quote `"` inside your text.** Use a curly one or rewrite the sentence.

If you make a mistake, GitHub puts a red X next to your change and explains what went wrong. Nothing breaks on the live site until you fix it.

## Change some text

1. On the repository's main page, open the **`_data`** folder.
2. Click the file you want (see the table below).
3. Click the **pencil icon** at the top right of the file.
4. Edit the text.
5. Click **Commit changes** (top right), then **Commit changes** again in the pop-up.
6. Wait about a minute and refresh the website.

| I want to change... | Open this file |
|---|---|
| Group name, tagline, intro, email, social links, logo, home page group photo, auditions banner | `_data/group.yml` |
| Performance videos | `_data/videos.yml` |
| Shows and events | `_data/shows.yml` |
| Home page photo gallery | `_data/gallery.yml` |
| About page: founding year, story, timeline | `_data/about.yml` |
| Board members | `_data/board.yml` |

## Upload a photo

1. Resize it first. Under 2000 pixels wide and under 500 KB loads fast. [squoosh.app](https://squoosh.app) does this free in your browser.
2. Give it a simple file name with no spaces: `jane-doe.jpg`, `winter-show-2026.jpg`. **Capital letters matter**: `Jane.JPG` and `jane.jpg` are different files.
3. In the repository, open the right folder inside `assets/images/`:

| Photo of... | Folder |
|---|---|
| Logo | `assets/images/` (the main images folder) |
| Home page group photo | `assets/images/hero/` |
| Board member | `assets/images/board/` |
| About page story or timeline | `assets/images/about/` |
| Home page gallery | `assets/images/gallery/` |

4. Click **Add file → Upload files**, drop the photo in, and click **Commit changes**.
5. Open the matching `_data` file and type the photo's file name next to `photo:` (or `file:` or `image:`). Commit again.

## Common tasks

### Add a performance video
Open `_data/videos.yml`. Copy a block, paste it at the top (the first video is shown biggest), paste the YouTube link after `url:`, and type a title. Use the link from your browser's address bar while watching the video. Playlist links won't work; use a link to one video.

### Add a show
Open `_data/shows.yml`, copy a block, and fill it in. The date must look exactly like `"2026-11-14"`. You never need to delete old shows: the site moves them into "Past shows" on its own.

### Update the board for a new year
Open `_data/board.yml`. For each person, change their name, role, major, part, fun fact, and photo in place. To add someone, copy a block. To remove someone, delete their whole block (from the `-` down to the line before the next `-`). Upload new photos to `assets/images/board/`.

### Turn on the auditions banner
Open `_data/group.yml`, find `auditions:`, and change `open: false` to `open: true`. Add your sign-up link. Change it back to `false` when auditions end.

### Add your logo
Upload it to `assets/images/`, then type its file name after `logo:` in `_data/group.yml`. A transparent PNG or SVG works best. Until then, the site shows a sound-wave mark.

### Hide something you don't want
Leave it empty. A social link with `url: ""` is hidden. A video with no link shows a placeholder card, so delete the block if you don't want one.

## Undo a mistake

Every change is saved forever, so nothing is ever lost.

1. Click the **clock icon / History** on the file you changed.
2. Click the change you want to undo.
3. Click the **three dots (...) → Revert**, then create the change. Merge it if GitHub asks.

## Where do I look if the site didn't change?

1. Open the **Actions** tab in the repository.
2. A **green check** means it worked; give it another minute and hard-refresh the page.
3. A **red X** means something needs fixing. Click it. The message tells you which file and what is wrong, for example *"no photo named jane-doe.jpg in assets/images/board/. Did you mean Jane-Doe.JPG?"*

You can also ask for help: open an issue with **Request a website change**.
