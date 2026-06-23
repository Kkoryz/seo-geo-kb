---
title: "Using schema.org markup for videos | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/02/using-schemaorg-markup-for-videos
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-02-21
---

# Using schema.org markup for videos | Google Search Central Blog | Google for Developers

Tuesday, February 21, 2012

Videos are one of the most common types of results on Google and we want to make sure that your
videos get indexed. Today, we're also launching video support for schema.org.
[Schema.org](https://schema.org/) is a joint effort between
Google, Microsoft, Yahoo! and Yandex and is now the recommended way to describe videos on the web.
The markup is very simple and can be easily added to most websites.

Adding [schema.org video markup](https://schema.org/VideoObject)
is just like adding any other schema.org data. Simply define an `itemscope`

, an
`itemtype="https://schema.org/VideoObject"`

, and make sure to set the `name`

,
`description`

, and `thumbnailUrl`

properties. You'll also need either the
`embedURL`

—the location of the video player—or the
`contentURL`

—the location of the video file. A typical video player with markup
might look like this:

<div itemscope itemtype="https://schema.org/VideoObject"> <h2>Video: <span itemprop="name">Title</span></h2> <meta itemprop="duration" content="T1M33S" /> <meta itemprop="thumbnailUrl" content="thumbnail.jpg" /> <meta itemprop="embedURL" content="https://www.example.com/videoplayer.swf?video=123" /> <object ...> <embed type="application/x-shockwave-flash" ...> </object> <span itemprop="description">Video description</span> </div>

Using schema.org markup will not affect any
[Video Sitemaps](/search/docs/crawling-indexing/sitemaps/video-sitemaps) or
[mRSS feeds](/search/docs/crawling-indexing/sitemaps/video-sitemaps#sitemap_alternatives)
you're already using. In fact, we still recommend that you also use a Video Sitemap because it
alerts us of any new or updated videos faster and provides advanced functionality such as country
and platform restrictions.

Since this means that there are now a number of ways to tell Google about your videos, choosing the right format can seem difficult. In order to make the video indexing process as easy as possible, we've put together a series of videos and articles about video indexing in our new Webmasters EDU microsite.

For more information, you can go through the
[Webmasters EDU video articles](/search/docs/appearance/video),
read the full
[schema.org VideoObject specification](https://schema.org/VideoObject),
or ask questions in the
[Webmaster Help Forum](https://support.google.com/webmasters/community/label?lid=3db4effde15c5be6&hl=en).
We look forward to seeing more of your video content in Google Search.
