# Publishing and handing off the site

## Put the site online (one time, about 5 minutes)

The site is a standard GitHub Pages site. GitHub builds and hosts it for free.

1. Create the repository on GitHub and upload these files (or push them).
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose branch **main** and folder **/ (root)**, then **Save**.
4. After a minute or two the page shows your link, usually `https://<owner>.github.io/<repo>/`.
5. Fill in `url` and `baseurl` in `_config.yml`:
   - If the address is `https://<owner>.github.io/` (a repository named exactly `<owner>.github.io`), leave `baseurl` empty.
   - If the address ends in `/<repo>/`, set `baseurl: "/<repo>"`. Otherwise the CSS and photos will not load.

## Keep it alive after you graduate

Student groups lose their website when the person who set it up leaves. To avoid that:

- **Create a GitHub Organization for the group** (free) and put the repository there instead of on a personal account. The organization can have several owners, and ownership stays with the group.
- **Make at least two current board members owners** (Organization → People → change role to Owner). Each year, add the incoming board and remove people who left.
- **Use a shared group email** for the organization's account recovery, not a personal one.
- Add each year's new board under **Settings → Collaborators and teams** so they can edit.

## Custom domain or github.io link?

| | `github.io` link | Custom domain (like `thefrequency.org`) |
|---|---|---|
| Cost | Free | Yearly fee set by the domain registrar |
| Setup | Nothing | Buy the domain, add DNS records, enter it in Settings → Pages |
| Looks | Long address | Short, easy to say and remember |
| Risk | None | The domain can expire if no one renews it |

Start with the free link. You can add a custom domain later without rebuilding anything. If you do, follow GitHub's own instructions for the exact DNS records, since they are the source of truth: search for "GitHub Pages custom domain" in the GitHub docs. Put the renewal date in the group's shared calendar and make sure the registrar account uses the group email.

## Preview on your own computer (optional)

Only needed if you want to see changes before publishing. You need Ruby installed.

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
