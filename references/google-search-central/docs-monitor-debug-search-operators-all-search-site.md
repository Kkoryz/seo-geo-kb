---
title: "How To Use the Site Search Operator | Google Search Central | Documentation | Google for Developers"
source_url: https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2025-12-10
---

# How To Use the Site Search Operator | Google Search Central | Documentation | Google for Developers

`site:`

search operator

A `site:`

query is a search operator that allows you to request search results from
the particular domain, URL, or URL prefix specified in the operator. For example:

`site:` examples |
|
|---|---|
`site:example.com`
|
Show results only from the `example.com` domain (`www.example.com`
and `recipes.example.com` ).
|
`site:https://www.example.com/ramen` tsukemen
|
Shows results for pages that contain URLs that start with
`https://www.example.com/ramen` and are relevant to the term tsukemen.
|

The `site:`

search operator is available on all Google Search properties.

## Uses for site owners

A `site:`

query can help in a few ways with debugging a site. A few examples:

`site:` examples |
|
|---|---|
`site:example.com` |
Returns a list of indexed and serving URLs. |
`site:https://example.com/recipes/tsukemen.html` |
May help you understand whether a specific URL is indexed and served. |
`site:example.com viagra casino` |
Helps with identifying and monitoring spam problems on your site. |
`site:https://example.com/` lemon |
Shows which URLs on the site can show up for the term "lemon". |
`site:https://example.com/recipes/tsukemen.html` lemon |
Shows whether the specific URL is indexed for the term "lemon". |

## Limitations

The `site:`

operator was designed primarily for search users and so it has some
restrictions that site owners might find limiting. Specifically:

-
The
`site:`

operator doesn't necessarily return all the URLs that are indexed under the prefix specified in the query. Keep this in mind if you want to use the`site:`

operator for tasks like identifying how many URLs are indexed and serving under a prefix. -
A
`site:`

operator without a query (for example`site:example.com`

) doesn't rank the results. It will generally show the shortest URL for the prefix at the top, but otherwise the results are relatively random.
