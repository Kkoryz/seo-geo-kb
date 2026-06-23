---
title: "Promoting modern websites for modern devices in Google search results | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2014/07/promoting-modern-websites-for-modern
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2014-07-15
---

# Promoting modern websites for modern devices in Google search results | Google Search Central Blog | Google for Developers

Tuesday, July 15, 2014

A common annoyance for web users is when websites require browser technologies that are not supported by their device. When users access such pages, they may see nothing but a blank space or miss out a large portion of the page's contents.

Starting today in our English search results in the US, we will indicate to searchers when our algorithms detect pages that may not work on their devices. For example, Adobe Flash is not supported on iOS devices or on Android versions 4.1 and higher, and a page whose contents are mostly Flash may be noted like this:

## Developing modern multi-device websites

Fortunately, making websites that work on all modern devices is not that hard: websites can use
HTML5 since it is universally supported, sometimes exclusively, by all devices. To help webmasters
build websites that work on all types of devices regardless of the type of content they wish to
serve, we recently
[announced](https://googledevelopers.blogspot.com/2014/06/web-fundamentals-and-web-starter-kit.html)
two resources:

-
[Web Fundamentals](/web/fundamentals): a curated source for modern best practices. -
[Web Starter Kit](https://github.com/google/web-starter-kit/): a starter framework supporting the Web Fundamentals best practices out of the box.

By following the best practices described in Web Fundamentals you can build a
[responsive web design](/web/fundamentals/layouts), which has long been
[Google's recommendation](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
for search-friendly sites. Be sure not to block crawling of any Googlebot of the page assets
(CSS, JavaScript, and images) using robots.txt or otherwise. Being able to access these external
files fully helps our algorithms detect your site's responsive web design configuration and treat
it appropriately. You can use the
[Fetch and render as Google](https://support.google.com/webmasters/answer/158587)
feature in Webmaster Tools to test how our indexing algorithms see your site.

As always, if you need more help you can ask a question in
[our webmaster forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking)).
