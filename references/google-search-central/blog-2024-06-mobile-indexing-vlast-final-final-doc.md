---
title: "Mobile-indexing-vLast-final-final.doc | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2024/06/mobile-indexing-vlast-final-final.doc
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2024-06-03
---

# Mobile-indexing-vLast-final-final.doc | Google Search Central Blog | Google for Developers

Monday, June 3, 2024

We're embarking on our final last step (that's the plan!) of our migration to a mobile-first index for Google Search: the small set of sites we've still been crawling with desktop Googlebot will be crawled with mobile Googlebot after July 5, 2024. Don't worry, most websites don't need to do anything!

As we mentioned in our
[last update
on mobile indexing](/search/blog/2023/10/mobile-first-is-here), Google crawls and indexes almost all websites using a smartphone
crawler.
Over the years, the number of sites that aren't accessible on mobile has continued to shrink.
To simplify our systems, and to make it easier for sites to debug issues related to device types,
we'll soon crawl all sites for Search with the
[Googlebot
Smartphone crawler](/search/docs/crawling-indexing/googlebot).

The largest part of the web is already being crawled like this, and there is no change in crawling for these sites. After July 5, 2024, we'll crawl and index these sites with only Googlebot Smartphone. If your site's content is not accessible at all with a mobile device, it will no longer be indexable.

You may still find Googlebot Desktop in your server logs and reporting.
For example, among a few other Search features, Googlebot Desktop is sometimes used when
crawling for
[product
listings](https://support.google.com/merchants/answer/9199328) and
[Google for Jobs](https://jobs.google.com/about/).
