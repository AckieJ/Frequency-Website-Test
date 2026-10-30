# The Frequency — After Dark redesign

This refresh is a drop-in update to the original Jekyll site. It keeps YAML-driven content, URLs, YouTube embeds, show date sorting, and GitHub Pages configuration.

## Visual design
- Dark concert-inspired palette, lavender and electric-lime accents
- Typographic hero and subtle sound-wave treatment
- New visual hierarchy across Home and About
- Responsive accessible hamburger menu
- Updated performance, concert, photo, team, and contact cards
- Reduced-motion-aware interactions

## Before publishing
- Replace sample copy and contact email in `_data/group.yml`
- Add real photos to `assets/images/hero`, `gallery`, `board`, and `about`; set YAML filenames
- Replace sample video URLs, sample show dates/venues, team roster
- Confirm `url` and `baseurl` in `_config.yml` match your deployment

## Run locally
`bundle install` then `bundle exec jekyll serve` from `frequency-site/`.

No new build dependencies or third-party JavaScript were introduced.
