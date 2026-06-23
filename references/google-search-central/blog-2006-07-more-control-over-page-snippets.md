---
title: "More control over page snippets | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/07/more-control-over-page-snippets
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-07-13
---

# More control over page snippets | Google Search Central Blog | Google for Developers

July 13, 2006

The way we generate the descriptions (snippets) that appear under a page in the search results is completely automated. The process uses both the content on a page as well as references to it that appear on other sites.

One source we use to generate snippets is the
[Open Directory Project](https://www.dmoz.org/),
or ODP. Some site owners want to be to able to request not using the ODP for generating snippets,
and we're happy to let you all know we've added support for this. All you have to do is add a
`meta`

tag to your pages.

To direct all search engines that support the `meta`

tag not to use ODP information for the page's
description, use the following:

<meta name="robots" content="noodp">

Note that not all search engines may support this `meta`

tag, so check with each for more
information.

To direct Google specifically from using this information to describe a page, use the following:

<meta name="googlebot" content="noodp">

For more information, visit the
[webmaster help center.](/search/docs/appearance/snippet)

Once you add this `meta`

tag to your pages, it may take some time for changes to your snippets to
appear. Once we've recrawled your pages and refreshed our index, you should see the updated
snippet in search results.
