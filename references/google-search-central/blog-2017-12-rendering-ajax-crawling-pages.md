---
title: "Rendering AJAX-crawling pages | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2017/12/rendering-ajax-crawling-pages
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2017-12-04
---

# Rendering AJAX-crawling pages | Google Search Central Blog | Google for Developers

Monday, December 04, 2017

The
[AJAX crawling scheme](https://web.archive.org/web/20151201031357/developers.google.com/webmasters/ajax-crawling/docs/learn-more)
was introduced as a way of making JavaScript-based webpages accessible to Googlebot, and we've
previously announced our
[plans to turn it down](/search/blog/2015/10/deprecating-our-ajax-crawling-scheme).
Over time, Google engineers have significantly improved rendering of JavaScript for Googlebot.
Given these advances, in the second quarter of 2018, we'll be switching to rendering these pages
on Google's side, rather than on requiring that sites do this themselves. In short, we'll no
longer be using the AJAX crawling scheme.

As a reminder, the AJAX crawling scheme accepts pages with either a `#!`

in the URL or a
[fragment meta tag](https://web.archive.org/web/20151101113107/developers.google.com/webmasters/ajax-crawling/docs/getting-started#3-handle-pages-without-hash-fragments)
on them, and then crawls them with an

`?_escaped_fragment_=`

in the URL. That escaped
version needs to be a fully-rendered and/or equivalent version of the page, created by the website
itself.
With this change, Googlebot will render the `#!`

URL directly, making it unnecessary
for the website owner to provide a rendered version of the page. We'll continue to support these
URLs in our search results.

We expect that most AJAX-crawling websites won't see significant changes with this update. Webmasters can double-check their pages as detailed below, and we'll be sending notifications to any sites with potential issues.

If your site is currently using either `#!`

URLs or the fragment `meta`

tag, we
recommend:

-
Verify ownership of the website in
[Google Search Console](https://search.google.com/search-console)to gain access to the tools there, and to allow Google to notify you of any issues that might be found. -
Test with Search Console's
[Fetch and Render](https://support.google.com/webmasters/answer/6066468). Compare the results of the #! URL and the escaped URL to see any differences. Do this for any significantly different part of the website. Check our[developer documentation](/search/docs/crawling-indexing/javascript/fix-search-javascript)for more information on supported APIs, and see our[debugging guide](/search/help/debug)when needed. -
Use Chrome's
[Inspect Element](/web/tools/chrome-devtools/inspect-styles)to confirm that links useand include a`a`

HTML elementswhere appropriate (for example, in user-generated content)`rel=nofollow`

-
Use Chrome's
[Inspect Element](/web/tools/chrome-devtools/inspect-styles)to check the page's[title](/search/docs/appearance/title-link)and[description](/search/docs/appearance/snippet), any robots`meta`

tag`meta`

tag, and other meta data. Also check that any[structured data](/search/docs/appearance/structured-data/intro-structured-data)is available on the rendered page. - Content in Flash, Silverlight, or other plugin-based technologies needs to be converted to either JavaScript or "normal" HTML, if their content should be indexed in search.

We hope that this change makes it a bit easier for your website, and reduces the need to render
pages on your end. Should you have any questions or comments, drop by our
[webmaster help forums](https://support.google.com/webmasters/go/community),
or to join our
[JavaScript sites working group](https://groups.google.com/forum/#!forum/js-sites-wg).
