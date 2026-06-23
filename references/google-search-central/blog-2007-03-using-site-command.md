---
title: "Using the site: command | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2007/03/using-site-command
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2007-03-02
---

# Using the site: command | Google Search Central Blog | Google for Developers

Friday, March 02, 2007

The `site:`

command enables you to search through a particular site. For instance, a
searcher could look for references to Buffy in this blog by doing the
following search:
`site:googlewebmastercentral.blogspot.com buffy`


Webmasters sometimes use this command to see a list of indexed pages for a site, like this:
`site:www.google.com`


Note that with this command, there's no space between the colon and the URL. A search for
www.site.com returns URLs that begin with www and a search for site.com returns URLs for all
subdomains. (So,
[ site:google.com](https://www.google.com/search?q=site%3Agoogle.com)
returns URLs such as www.google.com, checkout.google.com, and finance.google.com). You can do this
search from Google or you can go to your Webmaster Tools account and use the link under
Statistics > Index stats. Note that whether this link
includes the www depends on how you have added the site to your account.

Historically, Google has avoided showing pages that appear to be duplicate (for example, pages
with the same title and description) in search results. Our goal is to provide useful results to
the searcher. However, with a `site:`

command, searchers are likely looking for a full
list of results from that site, so we are making a change to do that. In some cases, a
`site:`

search doesn't show a full list of results even when the pages are different,
and we are resolving that issue as well. Note that this is a display issue only and doesn't in any
way affect search rankings. If you see this behavior, simply click the "repeat the search with
omitted results included" link to see the full list. The pages that initially don't display
continue to show up for regular queries. The display issue affects only a `site:`

search with no associated query. In addition, this display issue is unrelated to supplemental
results. Any pages in supplemental results display "Supplemental Result" beside the URL.

Because this change to show all results for `site:`

queries doesn't affect search
rankings at all, it will probably happen in the normal course of events as we merge this change
into the next time that we push a new executable for handling the `site:`

command. As a
result, it may be several weeks or so before you start to see this change, but we'll keep
monitoring it to make sure the change goes out.
