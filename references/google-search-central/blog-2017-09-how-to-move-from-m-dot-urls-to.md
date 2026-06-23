---
title: "How to move from m-dot URLs to responsive site | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2017/09/how-to-move-from-m-dot-urls-to
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2017-09-14
---

# How to move from m-dot URLs to responsive site | Google Search Central Blog | Google for Developers

Thursday, September 14, 2017

With more sites moving towards responsive web design, many webmasters have questions about
migrating from
[separate mobile URLs](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing),
also frequently known as "m-dot URLs", to using
[responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).
Here are some recommendations on how to move from separate urls to one responsive URL in a way
that gives your sites the best chance of performing well on Google's search results.

## Moving to responsive sites in a Googlebot-friendly way

Once you have your responsive site ready, moving is something you can definitely do with just a
bit of forethought. Considering your URLs stay the same for desktop version, all you have to do is
to configure `301`

redirects from the mobile URLs to the responsive web URLs.

Here are the detailed steps:

- Get your responsive site ready
-
Configure
`301`

redirects on the old mobile URLs to point to the responsive versions (the new pages). These redirects need to be done on a per-URL basis, individually from each mobile URLs to the responsive URLs. - Remove any mobile-URL specific configuration your site might have, such as conditional redirects or a vary HTTP header.
-
As a good practice,
[setup](/search/docs/crawling-indexing/consolidate-duplicate-urls)on the responsive URLs pointing to themselves (self-referential canonicals).`rel=canonical`


If you're currently using dynamic serving and want to move to responsive design, you don't need to add or change any redirects.

## Some benefits for moving to responsive web design

Moving to a responsive site should make maintenance and reporting much easier for you down the road. Aside from no longer needing to manage separate URLs for all pages, it will also make it much easier to adopt practices and technologies such as hreflang for internationalization, AMP for speed, structured data for advanced search features and more.

As always, if you need more help you can ask a question in our
[webmaster forum](https://support.google.com/webmasters/community).
