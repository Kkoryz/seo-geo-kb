---
title: "Easier URL removals for site owners | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2011/05/easier-url-removals-for-site-owners
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2011-05-17
---

# Easier URL removals for site owners | Google Search Central Blog | Google for Developers

Tuesday, May 17, 2011

We recently made a change to the
[Remove URL](https://www.google.com/support/webmasters/bin/answer.py?answer=164734)
tool in
[Webmaster Tools](https://search.google.com/search-console)
to eliminate the requirement that the webpage's URL must first be blocked by a site owner before
the page can be removed from Google's search results. Because you've already verified ownership of
the site, we can eliminate this requirement to make it easier for you, as the site owner, to
remove unwanted pages (for example, pages accidentally made public) from Google's search results.

## Removals persist for at least 90 days

When a page's URL is requested for removal, the request is temporary and persists for at least 90 days. We may continue to crawl the page during the 90-day period but we will not display it in the search results. You can still revoke the removal request at any time during those 90 days. After the 90-day period, the page can reappear in our search results, assuming you haven't made any other changes that could impact the page's availability.

## Permanent removal

In order to permanently remove a URL, you must ensure that one of the following page blocking methods is implemented for the URL of the page that you want removed:

-
indicate that the page no longer exists by returning a
`404`

or`410`

HTTP status code -
block the page from crawling via a
[robots.txt file](/search/docs/crawling-indexing/robots/intro) -
block the page from indexing via a
`noindex`

`meta`

tag

This will ensure that the page is permanently removed from Google's search results for as long as the page is blocked. If at any time in the future you remove the previously implemented page blocking method, we may potentially re-crawl and index the page. For immediate and permanent removal, you can request that a page be removed using the Remove URL tool and then permanently block the page's URL before the 90-day expiration of the removal request.

For more information about URL removals, see our
[URL removal explained](/search/blog/2010/03/url-removal-explained-part-i-urls) blog
series covering this topic. If you still have questions about this change or about URL removal
requests in general, please post in our
[Webmaster Help Forum](https://support.google.com/webmasters/community/label?lid=5489e59697a233d7).
