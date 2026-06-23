---
title: "How to discover and suggest Google-selected canonical URLs for your pages | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2019/03/how-to-discover-suggest-google-selected
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2019-03-26
---

# How to discover and suggest Google-selected canonical URLs for your pages | Google Search Central Blog | Google for Developers

Tuesday, March 26, 2019

Sometimes a web page can be reached by using more than one URL. In such cases, Google tries to determine the best URL to display in search and to use in other ways. We call this the "canonical URL." There are ways site owners can help us better determine what should be the canonical URLs for their content.

If you suspect we've not selected the best canonical URL for your content, you can check by
entering your page's address into the
[URL Inspection tool](https://support.google.com/webmasters/answer/9012289)
within
[Search Console](https://search.google.com/search-console/about). It
will show you the
[Google-selected canonical](https://support.google.com/webmasters/answer/9012289#google-selected-canonical).
If you believe there's a better canonical that should be used, follow the steps on our
[duplicate URLs](/search/docs/crawling-indexing/consolidate-duplicate-urls) help page
on how to suggest a preferred choice for consideration.

Please be aware that if you search using the `site:`

or `inurl:`

commands,
you will be shown the domain you specified in those, even if these aren't the Google-selected
canonical. This happens because we're fulfilling the exact request entered. Behind-the-scenes, we
still use the Google-selected canonical, including for when people see pages without using the
`site:`

or `inurl:`

commands.

We've also changed URL Inspection tool so that it will display any Google-selected canonical for a
URL, not just those for properties you manage in Search Console. With this change, we're also
retiring the `info:`

command. This was an alternative way of discovering canonicals. It
was relatively underused, and URL Inspection tool provides a more comprehensive solution to help
publishers with URLs.
