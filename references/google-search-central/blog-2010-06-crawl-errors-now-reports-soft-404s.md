---
title: "Crawl Errors now reports soft 404s | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/06/crawl-errors-now-reports-soft-404s
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-06-07
---

# Crawl Errors now reports soft 404s | Google Search Central Blog | Google for Developers

Monday, June 07, 2010

Today we're releasing a feature to help you discover if your site serves undesirable
`soft`

or `crypto`

`404`

s. A `soft 404`

occurs
when a webserver responds with a `200 OK`

[HTTP response code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
for a page that doesn't exist rather than the appropriate `404 Not Found`

.
`Soft 404`

s can limit a site's crawl coverage by search engines because these duplicate
URLs may be crawled instead of pages with unique content.

The web is infinite, but the time search engines spend crawling your site is limited. Properly
reporting non-existent pages with a `404`

or `410`

response code can improve
the crawl coverage of your site's best content. Additionally, `soft 404`

s can
potentially be confusing for your site's visitors as described in our past blog post,
[Farewell to soft 404 pages](/search/blog/2008/08/farewell-to-soft-404s).

You can find the new `soft 404`

reporting feature under the Crawl errors section in
[Webmaster Tools](https://search.google.com/search-console).

Here's a list of steps to correct `soft 404`

errors to help both Google and your users:

- Check whether you have
`soft 404`

errors listed in Webmaster Tools - For the
`soft 404`

errors, determine whether the URL: -
Contains the correct content and properly returns a
`200`

response (not actually a`soft 404`

) - Should
`301`

redirect to a more accurate URL - Doesn't exist and should return a
`404`

or`410`

response -
Confirm that you've configured the proper HTTP Response by using
[Fetch as Googlebot](/search/blog/2009/10/fetch-as-googlebot-and-malware-details)in Webmaster Tools -
If you now return
`404`

errors, you may want to customize your`404`

page to aid your users. Our[custom](/search/docs/crawling-indexing/http-network-errors#pagegone)can help.`404`

widget

We hope that you're now better enabled to find and correct `soft 404`

errors on your
site. If you have feedback or questions about the new `soft 404`

error reporting
feature or any other Webmaster Tools feature, please share your thoughts with us in the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
