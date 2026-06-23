---
title: "Smartphone crawl errors in Webmaster Tools | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2013/12/smartphone-crawl-errors-in-webmaster
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2013-12-04
---

# Smartphone crawl errors in Webmaster Tools | Google Search Central Blog | Google for Developers

Wednesday, December 04, 2013

Some smartphone-optimized websites are
[misconfigured](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) in that they don't
show searchers the information they were seeking. For example, smartphone users are shown an error
page or get redirected to an irrelevant page, but desktop users are shown the content they wanted.
Some of these problems, detected by Googlebot as crawl errors, significantly hurt your website's
user experience and are the basis of some of our recently-announced
[ranking changes](/search/blog/2013/06/changes-in-rankings-of-smartphone_11) for
smartphone search results.

Starting today, you can use the expanded Crawl Errors feature in Webmaster Tools to help identify pages on your sites that show these types of problems. We're introducing a new Smartphone errors tab where we share pages we've identified with errors only found with Googlebot for smartphones.

Some of the errors we share include:

-
**Server errors**: A server error is when Googlebot got an[HTTP error status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)when it crawled the page. -
**"Not found" and**: A page can show a "not found" message to Googlebot, either by returning an HTTP`soft 404`

errors`404`

status code or when the page is detected as a.`soft 404`

page -
**Faulty redirects**: A[faulty redirect](https://support.google.com/webmasters/answer/4046647)is a smartphone-specific error that occurs when a desktop page redirects smartphone users to a page that is not relevant to their query. A typical example is when all pages on the desktop site redirect smartphone users to the home page of the smartphone-optimized site. -
**Blocked URLs**: A[blocked URL](https://support.google.com/webmasters/answer/4066608)is when the site's robots.txt explicitly disallows crawling by Googlebot for smartphones. Typically, such smartphone-specific robots.txt disallow rules are erroneous. You should investigate your server configuration if you see blocked URLs reported in Webmaster Tools.

Fixing any issues shown in Webmaster Tools can make your site better for users and help our
algorithms better index your content. You can learn more about how to
[build smartphone websites](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) and
[how to fix common errors](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). As always,
please
[ask in our forums](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking))
if you have any questions.
