---
title: "Improved Search Queries stats for separate mobile sites | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2014/01/improved-search-queries-stats
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2014-01-07
---

# Improved Search Queries stats for separate mobile sites | Google Search Central Blog | Google for Developers

Tuesday, January 07, 2014

Search Queries in
[Webmaster Tools](https://search.google.com/search-console) just
became more cohesive for those who manage a mobile site on a separate URL from desktop, such as
mobile on m.example.com and desktop on www. In
[Search Queries](https://support.google.com/webmasters/answer/35252),
when you view your m. site* and set Filters to "Mobile," from Dec 31, 2013 onwards, you'll now
see:

- Queries where your m. pages appeared in search results for mobile browsers
-
Queries where Google applied
[Skip Redirect](/search/blog/2011/12/introducing-smartphone-googlebot-mobile). This means that, while search results displayed the desktop URL, the user was automatically directed to the corresponding m. version of the URL (thus saving the user from latency of a server-side redirect).

Prior to this Search Queries improvement, Webmaster Tools reported Skip Redirect impressions with the desktop URL. Now we've consolidated information when Skip Redirect is triggered, so that impressions, clicks, and CTR are calculated solely with the verified m. site, making your mobile statistics more understandable.

## Best practices if you have a separate m. site

Here are a few search-friendly recommendations for those publishing content on a separate m. site:

-
Follow our advice on
[Building Smartphone-Optimized Websites](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) -
On the desktop page, add a special link
`rel="alternate"`

tag pointing to the corresponding mobile URL. This helps Googlebot discover the location of your site's mobile pages. -
On the mobile page, add a link
tag pointing to the corresponding desktop URL.`rel="canonical"`

-
Use the
`HTTP Vary: User-Agent`

header if your servers automatically redirect users based on their user agent/device. - Verify ownership of both the desktop (www) and mobile (m.) sites in Webmaster Tools for improved communication and troubleshooting information specific to each site.

Be sure you've verified ownership for your mobile site!
