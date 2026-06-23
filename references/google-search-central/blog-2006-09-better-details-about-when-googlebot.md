---
title: "Better details about when Googlebot last visited a page | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/09/better-details-about-when-googlebot
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-09-05
---

# Better details about when Googlebot last visited a page | Google Search Central Blog | Google for Developers

Tuesday, September 05, 2006

Most people know that Googlebot downloads pages from web servers to crawl the web. Not as many
people know that if Googlebot accesses a page and gets a

response to a [304](/crawling/docs/troubleshooting/http-status-codes#3xx-redirection) (Not-Modified)`If-Modified-Since`

qualified request, Googlebot doesn't download the
contents of that page. This reduces the bandwidth consumed on your web server.

When you look at Google's cache of a page (for instance, by using the
[ cache: operator](/search/docs/monitor-debug/search-operators/web-search-cache)
or clicking the Cached link under a URL in the search results), you can see the date that
Googlebot retrieved that page. Previously, the date we listed for the page's cache was the date
that we last successfully fetched the content of the page. This meant that even if we visited a
page very recently, the cache date might be quite a bit older if the page hadn't changed since the
previous visit. This made it difficult for webmasters to use the cache date we display to
determine Googlebot's most recent visit. Consider the following example:

- Googlebot crawls a page on April 12, 2006.
-
Our cached version of that page notes that "This is Google's cache of
`https://www.example.com/`

as retrieved on April 12, 2006 20:02:06 GMT." -
Periodically, Googlebot checks to see if that page has changed, and each time, receives a
`Not-Modified`

response. For instance, on August 27, 2006, Googlebot checks the page, receives a`Not-Modified`

response, and therefore, doesn't download the contents of the page. - On August 28, 2006, our cached version of the page still shows the April 12, 2006 date—the date we last downloaded the page's contents, even though Googlebot last visited the day before.

We've recently changed the date we show for the cached page to reflect when Googlebot last
*accessed* it (whether the page had changed or not).
This should make it easier for you to determine the most recent date Googlebot visited the
page. For instance, in the above example, the cached version of the page would now say "This is
Google's cache of `https://www.example.com/`

as retrieved on August 27, 2006 13:13:37
GMT."

Note that this change will be reflected for individual pages as we update those pages in our index.
