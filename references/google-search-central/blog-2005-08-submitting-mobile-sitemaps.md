---
title: "Submitting mobile Sitemaps | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2005/08/submitting-mobile-sitemaps
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2005-08-31
---

# Submitting mobile Sitemaps | Google Search Central Blog | Google for Developers

August 31, 2005

If you've created and submitted Sitemaps for your non-mobile pages, or just want to submit a mobile Sitemap for the first time, here are a few helpful tips to help you get started:

## Identify your mobile Sitemaps content

- If you have content other than XHTML mobile profile, WML, and cHTML, you should create a separate non-mobile Sitemap for those and submit it using the Add a Sitemap page.
- If your site serves multiple mobile markup languages, you should create a separate mobile Sitemap for each markup language.
- If you have URLs that serve multiple markup languages, you should include those URLs in each mobile Sitemap that applies. For instance, if you have a URL that serves both XHTML and WML content, include that URL in two mobile Sitemaps, one for each markup language.
- If you have a large site and use Sitemap index files to manage a large number of mobile Sitemaps, make sure that each Sitemap index file only includes mobile Sitemaps for one markup language.

## Create your mobile Sitemaps

-
You can
[create mobile Sitemaps](/search/docs/crawling-indexing/sitemaps/overview)in the same way as other Sitemaps. The only format not supported is OAI-PMH. - If you are submitting a syndication feed, and the URLs listed in that feed serve multiple markup languages, decide which markup language fits best. You can't submit the syndication feed multiple times, each for a different markup language, since each Sitemap (within the same directory) must have a unique name.

## Submit your mobile Sitemaps

-
Once you've created your Sitemap, log in to your Google Account and
[submit it](/search/docs/crawling-indexing/sitemaps/build-sitemap#addsitemap)using the[Add a Mobile Sitemap page](https://support.google.com/webmasters/answer/7451001). - Specify the markup language that the URLs listed in the mobile Sitemap serve.
- Once you've submitted the mobile Sitemap it will be listed on your My Sitemaps page as a "Mobile" type.
