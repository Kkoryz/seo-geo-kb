---
title: "Crawling December: Faceted navigation | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2024/12/crawling-december-faceted-nav
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2024-12-17
---

# Crawling December: Faceted navigation | Google Search Central Blog | Google for Developers

Tuesday, December 17, 2024

We just published
[a new document about faceted navigation best practices](/search/docs/crawling-indexing/crawling-managing-faceted-navigation),
which was
[originally published as a blog post](/search/blog/2014/02/faceted-navigation-best-and-5-of-worst).
This is a summary of some of the important parts of the new documentation page.

Faceted navigation is a great way to help users find what they need on your site, but it can create an SEO nightmare if not implemented carefully. Why? Because it can generate a near-infinite number of URLs, leading to:

-
**Overcrawling:**Search engines waste time crawling countless URLs that aren't valuable to search users. -
**Slower discovery:**This overcrawling slows down the discovery of your important, new content.

In fact, faceted navigation is by far the most common source of overcrawl issues site owners report to us, and in the vast majority of the cases the issue could've been avoided by following some best practices. But let's back up a little.

## The problem with URLs

Each filter combination in a faceted navigation generally creates a unique URL. For example:

https://example.com/items.shtm?products=fish&color=radioactive_green&size=tiny

Changing any parameter — `product`

, `color`

, or `size`

— creates a new URL, leading to a potential explosion of URLs. And that's the problem: a
virtually infinite number of new URLs waiting to be discovered. Let's fix it.

## Two approaches

-
**Block faceted navigation URLs:**-
If you don't need these URLs indexed, use
`robots.txt`

to disallow crawling. -
Or use URL fragments (
`#`

) for filters, as search engines generally ignore them.

-
If you don't need these URLs indexed, use
-
**Optimize faceted navigation URLs (if you need them crawled, no matter the cost):**-
Use the standard
`&`

separator for URL parameters. 💩 is not a good parameter separator character. - Maintain a consistent order of filters in the URL path.
- Return a
`404`

status code for filter combinations with no results. -
Unless you have no other options (for example,
[you have a single-page app](/search/docs/crawling-indexing/javascript/javascript-seo-basics#avoid-soft-404s)), avoid redirecting empty results to a generic "not found" page.

-
Use the standard

## Important considerations

-
You can also use
`rel="canonical"`

to help consolidate signals by pointing variations to a main page. This one takes time to get picked up. -
`rel="nofollow"`

on filter links can discourage crawling, but must be applied consistently. As in, every link pointing to these pages, internal and external, must have a`rel="nofollow"`

attribute. - Crawling faceted navigation URLs will always consume server resources and may impact the discovery of new content.

If you have suggestions or need clarification about our
[new document about faceted navigation best practices](/search/docs/crawling-indexing/crawling-managing-faceted-navigation),
use the feedback tool on that doc. If you are really into faceted navigation and wanna chat about
it with others, the
[Search Central community](https://goo.gle/sc-forum) is the place
to go, but you can also find us on
[LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/).
