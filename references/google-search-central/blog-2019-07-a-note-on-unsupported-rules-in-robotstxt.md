---
title: "A note on unsupported rules in robots.txt | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2019/07/a-note-on-unsupported-rules-in-robotstxt
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2019-07-02
---

# A note on unsupported rules in robots.txt | Google Search Central Blog | Google for Developers

Tuesday, July 02, 2019

Yesterday we announced that we're
[open-sourcing Google's production robots.txt parser](/search/blog/2019/07/repp-oss).
It was an exciting moment that paves the road for potential Search open sourcing projects in the
future! Feedback is helpful, and we're eagerly collecting questions from
[developers](https://github.com/google/robotstxt) and
[webmasters](https://twitter.com/googlesearchc) alike. One question
stood out, which we'll address in this post:

Why isn't a code handler for other rules like crawl-delay included in the code?

[The internet draft](/search/blog/2019/07/rep-id) we published yesterday provides an
extensible architecture for rules that are not part of the standard. This means that if a
crawler wanted to support their own line like `unicorns: allowed`

,
they could. To demonstrate how this would look in a parser, we included a very common line,
sitemap, in our [open-source robots.txt parser](https://github.com/google/robotstxt).

While open-sourcing our parser library, we analyzed the usage of robots.txt rules. In particular,
we focused on rules unsupported by the internet draft, such as
`crawl-delay`

, `nofollow`

, and
`noindex`

. Since these rules were never documented by Google,
naturally, their usage in relation to Googlebot is very low. Digging further, we saw their usage
was contradicted by other rules in all but 0.001% of all robots.txt files on the internet.
These mistakes hurt websites' presence in Google's search results in ways we don't think
webmasters intended.

In the interest of maintaining a healthy ecosystem and preparing for potential future open source
releases, we're retiring all code that handles unsupported and unpublished rules (such as
`noindex`

) on September 1, 2019. For those of you who relied on the
`noindex`

indexing rule in the
`robots.txt`

file, which controls crawling, there are a number of
alternative options:

-
Supported both in the HTTP response headers and in HTML, thein robots`noindex`

`meta`

tags:`noindex`

rule is the most effective way to remove URLs from the index when crawling is allowed. -
Both status codes mean that the page does not exist, which will drop such URLs from Google's index once they're crawled and processed.:`404`

and`410`

HTTP status codes -
**Password protection:**Unless markup is used to indicate[subscription or paywalled content](/search/docs/appearance/structured-data/paywalled-content), hiding a page behind a login will generally remove it from Google's index. -
Search engines can only index pages that they know about, so blocking the page from being crawled usually means its content won't be indexed. While the search engine may also index a URL based on links from other pages, without seeing the content itself, we aim to make such pages less visible in the future.`Disallow`

in`robots.txt`

: -
The tool is a quick and easy method to remove a URL temporarily from Google's search results.[Search Console Remove URL tool](https://support.google.com/webmasters/answer/1663419):

For more guidance about how to remove information from Google's search results, visit our
[Help Center](/search/docs/guides/advanced/remove-information?ref_topic=1724262).
If you have questions, you can find us on [Twitter](https://twitter.com/googlesearchc)
and in our [Webmaster Community](https://support.google.com/webmasters/community),
both [offline](/search/events/search-central-live) and online.
