---
title: "A new Google Sitemap Generator for your website | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2009/01/new-google-sitemap-generator-for-your
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2009-01-13
---

# A new Google Sitemap Generator for your website | Google Search Central Blog | Google for Developers

Tuesday, January 13, 2009

It's been well over three years since we initially announced the
[Python Sitemap generator](https://code.google.com/p/sitemap-generators/downloads/list)
in
[June 2005](https://googleblog.blogspot.com/2005/06/webmaster-friendly.html).
In this time, we've seen lots of people create great
[third-party sitemap generators](https://code.google.com/p/sitemap-generators/wiki/SitemapGenerators)
to help webmasters create better sitemap files. While most sitemap
generators either crawl websites or list the files on a server, we have created a different kind
of sitemap generator that uses several ways to find URLs on your website and then allows you to
automatically create and maintain different kinds of sitemap files.

## About Google Sitemap Generator

Our new open-source
[Google Sitemap Generator](https://code.google.com/p/googlesitemapgenerator/)
finds new and modified URLs based on your webserver's traffic, its log
files, or the files found on the server. By combining these methods, Google Sitemap Generator can
be very fast in finding these URLs and calculating relevant metadata, thereby making your sitemap
files as effective as possible. Once Google Sitemap Generator has collected the URLs, it can
create the following [sitemap files](/search/docs/crawling-indexing/sitemaps/overview) for you:

-
XML sitemaps for Web Search according to
the
[sitemaps.org](https://www.sitemaps.org/)standard - Mobile sitemaps for mobile-friendly websites
- Code Search sitemaps for source code that you make available to users

In addition, Google Sitemap Generator can send a
[ping to Google Blog Search](https://www.google.com/help/blogsearch/about_pinging)
for all of your new or modified URLs. You can optionally include the URLs of the sitemap files in
your robots.txt file as well as "ping" the other search engines that support the
[sitemaps.org](https://www.sitemaps.org/) standard.

Sending the URLs to the right sitemap files is simple thanks to the web-based administration console. This console gives you access to various features that make administration a piece of cake while maintaining a high level of security by default.

## Getting started

Google Sitemap Generator is a server plug-in that can be installed on both Linux/Apache and
Microsoft IIS Windows-based servers. As with other server-side plug-ins, you will need to have
administrative access to the server to install it. You can find detailed information for the
installation in the
[Google Sitemap Generator documentation](https://code.google.com/archive/p/googlesitemapgenerator/).

We're excited to release Google Sitemap Generator with the source code and hope that this will encourage more web hosters to include this or similar tools in their hosting packages!

Do you have any questions? You can drop by our
[Help Group for Google Sitemap Generator](https://groups.google.com/group/google-sitemap-generator)
or ask general sitemaps question in our
[Webmaster Help Forum](https://support.google.com/webmasters).
