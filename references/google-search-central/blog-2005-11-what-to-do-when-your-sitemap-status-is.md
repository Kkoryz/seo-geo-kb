---
title: "What to do when your Sitemap status is \"Denied URLs\" | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2005/11/what-to-do-when-your-sitemap-status-is
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2005-11-01
---

# What to do when your Sitemap status is "Denied URLs" | Google Search Central Blog | Google for Developers

November 01, 2005

If your Sitemap status is "Denied URLs" and the error listed is "URL not under Sitemap path", here are some things to check.

## Make sure the URL root matches

If you submit your Sitemap using the path `https://example.com/sitemap.xml`

, then the
URLs in your Sitemap should begin with `example.com`

. Any URLs that begin with
`www.example.com`

aren't considered to be under the Sitemap path. Along those lines,
if you Submit your Sitemap using the path `https://www.example.com/sitemap.xml`

, the
URLs in that Sitemap should begin with `www.example.com`

.

To fix this problem, you can either edit the URLs listed in your Sitemap file to match the submitted path, or you can delete the Sitemap and then submit it again using the path that matches the URLs listed in it.

## Make sure the Sitemap is at the highest-level directory

If you submit your Sitemap using the path
`https://www.example.com/sample_folder/sitemap.xml`

, then all URLs in that Sitemap must
begin with that path. This means that
`https://www.example.com/sample.html`

wouldn't be considered a valid URL in the
Sitemap.

If all possible, place your Sitemap at the root location of your site to avoid these types of problems. If you can't place the Sitemap at the root, then list only URLs from the Sitemap location and lower.

See the
[Sitemaps documentation](/search/docs/crawling-indexing/sitemaps/overview#deniedurls_error)
for more details.
