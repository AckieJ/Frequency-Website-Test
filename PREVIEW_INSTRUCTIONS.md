# Preview The Frequency website

This is a Jekyll site, not a standalone HTML page. Do not double-click `index.html` or use a basic Live Server extension directly on the source files: Jekyll must process the templates.

## Local preview

1. Install Ruby and Bundler.
2. In the `frequency-site` folder, run:

```sh
bundle install
bundle exec jekyll serve --baseurl ""
```

3. Open `http://127.0.0.1:4000/`.

## GitHub Pages

The `_config.yml` currently uses `baseurl: "/Frequency-Website-Test"`, which is correct only if the site is served at that repository subpath. If publishing to a different repository path, update `baseurl` to exactly that path; for a custom domain or user root site, set it to `""`.

The main CSS is now included in the rendered HTML so that a wrong CSS asset URL cannot cause the entire design to disappear. Other assets still depend on the correct baseurl.
