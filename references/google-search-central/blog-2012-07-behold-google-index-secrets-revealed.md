---
title: "Behold Google index secrets, revealed! | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/07/behold-google-index-secrets-revealed
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-07-24
---

# Behold Google index secrets, revealed! | Google Search Central Blog | Google for Developers

Tuesday, July 24, 2012

Since Googlebot was born, webmasters around the world have been asking one question: Google, oh,
Google, are my pages in the index? Now is the time to answer that question using the new Index
Status feature in Webmaster Tools. Whether one or one million, Index Status will show you how
many pages from your site have been included in
[Google's index](https://support.google.com/webmasters/bin/answer.py?answer=2642366).

Index Status is under the Health menu. After clicking on it you'll see a graph like the following:

It shows how many pages are currently indexed. The legend shows the latest count and the graph shows up to one year of data. If you see a steadily increasing number of indexed pages, congratulations! This should be enough to confirm that new content on your site is being discovered, crawled and indexed by Google.

However, some of you may find issues that require looking a little bit deeper. That's why we added an Advanced tab to the feature. You can access it by clicking on the button at the top, and it will look like this:

The advanced section will show not only totals of indexed pages, but also the cumulative number of pages crawled, the number of pages that we know about which are not crawled because they are blocked by robots.txt, and also the number of pages that were not selected for inclusion in our results.

Notice that the counts are always totals. So, for example, if on June 17th the count for indexed pages is 92, that means that there are a total of 92 pages indexed at this point in time, not that 92 pages were added to the index on that day only. In particular for sites with a long history, the count of pages crawled may be very big in comparison with the number of pages indexed.

All this data can be used to identify and debug a variety of indexing-related problems. For
example, if some of your content doesn't appear any more on Google and you notice that the graph
of pages indexed has a sudden drop, that may be an indication that you introduced a site-wide
error when using `meta="noindex"`

and now Google isn't including your content in search
results.

Another example: if you change the URL structure of your site and don't follow our
[recommendations for moving your site](/search/docs/crawling-indexing/site-move-with-url-changes),
you may see a jump in the count of "Not selected". Fixing the redirects or `rel="canonical"`

tags
should help get better indexing coverage.

We hope that Index Status will bring more transparency into Google's index selection process and
help you identify and fix indexing problems with your sites. And if you have questions, don't
hesitate to ask in our [Help Forum](https://support.google.com/webmasters/community).
