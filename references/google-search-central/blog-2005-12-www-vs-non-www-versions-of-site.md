---
title: "www vs non-www versions of a site | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2005/12/www-vs-non-www-versions-of-site
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2005-12-21
---

# www vs non-www versions of a site | Google Search Central Blog | Google for Developers

December 21, 2005

Two URLs to a site—one that is prefaced with www and one that is not (for instance,
**https://www.example.com/** and **https://example.com/**)—often point to the same
location on a server. But depending on the server configuration, they may point to different
locations, so search engines can't assume they are the same.

This post provides tips for
[viewing stats](https://support.google.com/webmasters/answer/9008080)
if the www and non-www version of your site point to the same location.

If you have added your site without prefacing the domain with www (for instance,
**https://example.com/**), and the www version of this domain points to the same location,
try [adding](/search/docs/crawling-indexing/sitemaps/overview#add_site) the www version
of the domain (for instance, **https://www.example.com/**) to your account. You may see a wider
variety of stats for the www version of the domain.

You can add a site by:

- Clicking the
**Add**tab. - Scrolling to the "If you don't have a Sitemap" area and entering the site URL.
- Clicking
**Add Site**.

Similarly, if you have added the www version of the domain and the non-www version points to the same location, you can add the non-www version to see stats for that version.

If the verification file still exists in the root of your site and both versions of the domain
point to the same location, you can
[verify](https://support.google.com/webmasters/answer/9008080)
the second version simply by accessing the **Verify** tab and clicking the **Verify**
button.

Note that having both versions of the site's URL listed in your account won't affect the indexing of your site as long as you have submitted a Sitemap for only one version—the version you want to be indexed. Don't submit a Sitemap for both versions if the location and content are the same.

If both domains point to the same location and you have pages indexed under both versions, see our
[Google Help Center](https://support.google.com/webmasters/answer/34592)
for more information on consolidating the listings under one domain.

We hear requests for help with this often, so we'll be looking at ways to improve this issue in the coming months.
