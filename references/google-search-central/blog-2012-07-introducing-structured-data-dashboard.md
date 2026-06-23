---
title: "Introducing the Structured Data Dashboard | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/07/introducing-structured-data-dashboard
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-08-01
---

# Introducing the Structured Data Dashboard | Google Search Central Blog | Google for Developers

Wednesday, August 01, 2012

Structured data is becoming an increasingly important part of the web ecosystem. Google makes use
of structured data in a number of ways including
[rich snippets](/search/docs/appearance/structured-data/intro-structured-data)
which allow websites to highlight specific types of content in search results. Websites
participate by marking up their content using industry-standard formats and schemas.

To provide webmasters with greater visibility into the structured data that Google knows about for their website, we're introducing today a new feature in Webmaster Tools - the Structured Data Dashboard. The Structured Data Dashboard has three views: site, item type and page-level.

## Site-level view

At the top level, the Structured Data Dashboard, which is under Optimization, aggregates this data
(by root item type and vocabulary schema). Root item type means an item that is not an attribute
of another on the same page. For example, the site below has about 2 million Schema.Org
annotations for `Books`

("[https://schema.org/Book](https://schema.org/Book)").

## Itemtype-level view

It also provides per-page details for each item type, as seen below:

Google parses and stores a fixed number of pages for each site and item type. They are stored in
decreasing order by the time in which they were crawled. We also keep all their structured data
markup. For certain
[item types](/search/docs/appearance/structured-data/intro-structured-data)
we also provide specialized preview columns as seen in this example below (for example,
`Name`

is specific to schema.org
[ Product](https://schema.org/Product)).

The default sort order is such that it would facilitate inspection of the most recently added Structured Data.

## Page-level view

Last but not least, we have a details page showing all attributes of every item type on the given
page (as well as a link to the
[Rich Snippet testing tool](https://www.google.com/webmasters/tools/richsnippets)
for the page in question).

Webmasters can use the Structured Data Dashboard to verify that Google is picking up new markup, as well as to detect problems with existing markup, for example monitor potential changes in instance counts during site redesigns.
