---
title: "Protecting your site with Gruyere | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2011/06/supporting-relcanonical-http-headers
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2011-06-17
---

# Protecting your site with Gruyere | Google Search Central Blog | Google for Developers

Friday, June 17, 2011

Based on your feedback, we’re happy to announce that Google web search now supports
[ link rel="canonical" relationships](/search/docs/crawling-indexing/consolidate-duplicate-urls)
specified in HTTP headers as per the syntax described in


[section 5 of IETF RFC 5988](https://tools.ietf.org/html/rfc5988#section-5). Webmasters can use

`rel="canonical"`

HTTP headers to signal the canonical URL for both
HTML documents and other types of content such as PDF files.
To see the `rel="canonical"`

HTTP header in action, let’s look at the scenario of a
website offering a white paper both as an HTML page and as a downloadable PDF alternative, under
these two URLs:

- https://www.example.com/white-paper.html
- https://www.example.com/white-paper.pdf

In this case, the webmaster can signal to Google that the canonical URL for the PDF download is
the HTML document by using a `rel="canonical"`

HTTP header when the PDF file is
requested; for example:

GET /white-paper.pdf HTTP/1.1 Host: www.example.com (...rest of HTTP request headers...) HTTP/1.1 200 OK Content-Type: application/pdfLink: <https://www.example.com/white-paper.html>; rel="canonical"Content-Length: 785710 (... rest of HTTP response headers...)

Another common situation in which `rel="canonical"`

HTTP headers may help is when a
website serves the same file from multiple URLs (for example when using a content distribution
network) and the webmaster wishes to signal to Google the preferred URL.

We currently support these link header elements for web search only. As we see how webmasters are
using these elements, we're hoping to add support for them in our other properties. For more
information, please see our Help Center articles about
[canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls) and the
[ rel="canonical" element](/search/docs/crawling-indexing/consolidate-duplicate-urls).
If you have any questions, please ask in our

[Webmaster Help Forum](https://www.google.com/support/forum/p/Webmasters?hl=en).
