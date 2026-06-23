---
title: "Search Analytics API now supports Discover, Google News, and Regex | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2021/10/search-analytics-discover-gnews
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2021-10-25
---

# Search Analytics API now supports Discover, Google News, and Regex | Google Search Central Blog | Google for Developers

Monday, October 25, 2021

The Google Search Console [Performance reports](https://support.google.com/webmasters/answer/7576553) already show data about Search,
Discover, and Google News to site owners that have this type of traffic. Since we launched the [Discover](https://support.google.com/webmasters/answer/9216516)
and [Google News](https://support.google.com/webmasters/answer/10083653) performance reports, we’ve been receiving requests from
users to also add these stats to the [Search Analytics API](/webmaster-tools/search-console-api-original/v3/searchanalytics).
We are happy to announce that this is happening today.

The `searchType`

parameter, which previously enabled you to filter API calls by `news`

,
`video`

, `image`

, and `web`

, will be renamed to
`type`

and will support two additional parameters: `discover`

(for Google Discover) and
`googleNews`

(for Google News). Please note that while we renamed the parameter to `type`

,
we’re still supporting the old name `searchType`

.

In the Search Console Performance reports, some metrics and dimensions are compatible only with some data types; for example, queries and positions are not supported by the Google Discover report. In the same way, if an unsupported dimension is requested, the API will return an error message.

In addition, we are adding [Regex support](/search/blog/2021/06/regex-negative-match) to the query and page dimensions.
Two new operators will be added to the existing match operations: `includingRegex`

and `excludingRegex`

.

Check out the [Search Analytics API documentation](/webmaster-tools/search-console-api-original/v3/searchanalytics/query) to learn more.
If you have any questions, you can ask in the [Search Central community](https://support.google.com/webmasters/community) or
[on Twitter](https://twitter.com/googlesearchc).
