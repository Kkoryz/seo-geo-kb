---
title: "Farewell to soft 404s | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/08/farewell-to-soft-404s
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-08-12
---

# Farewell to soft 404s | Google Search Central Blog | Google for Developers

Tuesday, August 12, 2008

We see two kinds of
[ 404 ("File not found") responses](/search/docs/crawling-indexing/http-network-errors)
on the web: "hard

`404`

error" and "soft `404`

error." We discourage the use
of so-called `soft 404`

because they can be a confusing experience for users and search
engines. Instead of returning a `404`

response code for a non-existent URL, websites
that serve `soft 404`

errors *return a*. The content of the

`200`

response code`200`

response is often the home page of the site, or an error page.
How does a `soft 404`

look to the user? Here's a mockup of a `soft 404`

:
This site returns a `200`

response code and the site's home page for URLs that don't
exist.

As exemplified above, `soft 404`

errors are confusing for users, and furthermore search
engines may spend much of their time crawling and indexing non-existent, often duplicative URLs
on your site. This can negatively impact your site's crawl coverage—because of the time Googlebot
spends on non-existent pages, your unique URLs may not be discovered as quickly or visited as
frequently.

## What should you do instead of returning a `soft 404`

?

It's much better to *return a 404 response code and clearly explain to users that
the file wasn't found*. This makes search engines and many users happy.

Can your webserver return `404`

, but send a helpful "Not found" message to the user? Of
course! More info as
"[ 404 week](/search/blog/2008/08/its-404-week-at-webmaster-central)"
continues!
