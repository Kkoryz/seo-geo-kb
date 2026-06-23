---
title: "Update to Top Search Queries data | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/01/update-to-top-search-queries-data
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-01-25
---

# Update to Top Search Queries data | Google Search Central Blog | Google for Developers

Wednesday, January 25, 2012

Starting today, we're updating our Top Search Queries feature to make it better match expectations about search engine rankings. Previously we reported the average position of all URLs from your site for a given query. As of today, we'll instead average only the top position that a URL from your site appeared in.

## An example

Let's say Nick searched for "bacon" and URLs from your site appeared in positions 3, 6, and 12. Jane also searched for "bacon" and URLs from your site appeared in positions 5 and 9. Previously, we would have averaged all these positions together and shown an Average Position of 7. Going forward, we'll only average the highest position your site appeared in for each search (3 for Nick's search and 5 for Jane's search), for an Average Position of 4.

We anticipate that this new method of calculation will more accurately match your expectations about how a link's position in Google Search results should be reported.

## How will this affect my Top Search Queries data?

This change will affect your Top Search Queries data going forward.
**Historical data will not change.** Note that the change in calculation means that the Average
Position metric will usually stay the same or decrease, as we will no longer be averaging in
lower-ranking URLs.

[Check out the updated Top Search Queries data](https://google.com/webmasters/tools/home)
in the Your site on the web section of Webmaster Tools. And remember, you can also
[download Top Search Queries data programmatically](/search/blog/2011/12/download-search-queries-data-using)!

We look forward to providing you a more representative picture of your Google Search data. Let us
know what you think in our
[Webmaster Forum](https://support.google.com/webmasters/community).
