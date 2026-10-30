# One-page navigation update

Header links now use on-page anchors on the homepage: Home → #top, Watch → #watch, Shows → #shows, About → #about, Book us → #contact. The About content, including story, milestones, and board, is also embedded on the homepage using `_includes/about-on-home.html`. The original `/about/` page remains available as a standalone URL for compatibility, but the header no longer depends on it.

The stylesheet uses smooth scrolling unless reduced motion is requested and offsets anchored sections below the sticky header. The existing JavaScript closes the mobile menu after navigation.

Preview using `bundle exec jekyll serve --baseurl ""` and `http://localhost:4000/`. Avoid opening the Liquid template directly as plain HTML.
