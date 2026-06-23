---
title: "Making site moves easier | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2014/06/making-site-moves-easier
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2014-06-06
---

# Making site moves easier | Google Search Central Blog | Google for Developers

Friday, June 06, 2014

Few topics confuse and scare webmasters more than site moves. To help you avoid surprises, we've created an in-depth guide on how to handle site moves in a Googlebot-friendly way. So what, exactly, is a site move and how do you go about moving a site correctly?

## Basics of site moves

A site move is, broadly, one of two types of content migrations:

-
[Site moves without URL changes](/search/docs/crawling-indexing/site-move-no-url-changes): Only the underlying infrastructure serving the website is changed without any visible changes to the URL structure. For example, you might move www.example.com to a different hosting provider while keeping the same URLs and site structure on www.example.com. -
[Site moves with URL changes](/search/docs/crawling-indexing/site-move-with-url-changes): Here, the URLs on the website change in any number of ways:- The protocol: https://www.example.com to https://www.example.com
- The domain name: example.com to example.net
- The URL paths: https://example.com/page.php?id=1 to https://example.com/widget


We've seen cases where webmasters implemented site moves incorrectly, or missed out steps that
would have greatly increased the chances of the site move completing successfully. To help
webmasters design and implement site moves correctly, we've updated the
[site move guidelines](/search/docs/crawling-indexing/site-move-with-url-changes). In parallel,
we continue to improve our crawling and indexing systems to detect and handle site moves if you
follow our guidelines.

## Moving to responsive web design

A related increasingly-common question we're seeing is how can a website move from having separate
mobile URLs or dynamic serving to using responsive web design. Learn more about
[responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

And, as always, please ask on our
[Webmaster Help forums](https://support.google.com/webmasters/community/)
if you have more questions.
