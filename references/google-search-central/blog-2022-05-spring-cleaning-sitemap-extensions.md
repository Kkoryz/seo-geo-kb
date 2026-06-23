---
title: "Spring cleaning: some sitemap extension tags are going away | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2022/05/spring-cleaning-sitemap-extensions
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2022-05-06
---

# Spring cleaning: some sitemap extension tags are going away | Google Search Central Blog | Google for Developers

Friday, May 06, 2022

Over the years, we introduced a number of tags and tag attributes for Google sitemap extensions,
specifically the [Image](/search/docs/crawling-indexing/sitemaps/image-sitemaps) and
[Video](/search/docs/crawling-indexing/sitemaps/video-sitemaps) extensions. Most of these tags
were added to allow site owners to deliver data more easily to Search.

Upon evaluating the value of the Google sitemap extension tags, we decided to officially deprecate some tags and attributes, and remove them from our documentation. The deprecated tags will have no effect on indexing and search features after August 6, 2022.

If you are a sitemap plugin developer or manage your own sitemaps, there's no immediate action
required; you can leave these tags and attributes in place without drawbacks. In the future,
Search Console may show warnings once these updates are included in the next schema versions of
the [Image](/search/docs/crawling-indexing/sitemaps/image-sitemaps) and
[Video](/search/docs/crawling-indexing/sitemaps/video-sitemaps) extensions.

The following tags and attributes are affected:

| Sitemap extension | Deprecated XML tag or attribute | Recommendation |
|---|---|---|
|

`caption`

[images best practices](/search/docs/appearance/google-images#use-descriptive-alt-text).`geo_location`

`title`

`license`

[Video sitemap](/search/docs/crawling-indexing/sitemaps/video-sitemaps)`category`

[video best practices](/search/docs/appearance/video).`player_loc[@allow_embed]`

`player_loc[@autoplay]`

`gallery_loc`

`price[@all]`

`tvshow[@all]`

By simplifying sitemap extensions, we hope you can also reduce complexity of your codebases, and
sitemaps will be less cluttered in general. If you have questions or comments, check out our
[sitemaps documentation](/search/docs/crawling-indexing/sitemaps/build-sitemap), or catch us on
[Twitter](https://twitter.com/googlesearchc) or in the
[Search Central forums](https://support.google.com/webmasters/community).
