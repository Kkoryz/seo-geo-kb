---
title: "Improving things behind the scenes | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/03/improving-things-behind-scenes
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-03-15
---

# Improving things behind the scenes | Google Search Central Blog | Google for Developers

March 15, 2006

We've just made some enhancements to the infrastructure that processes Sitemaps. You shouldn't
notice many changes, although you may see new and more
[detailed error messages](https://support.google.com/webmasters/answer/7451001)
for your Sitemaps. If you see a different error message than you've seen before, you can click on
it to view more information about it.

This change may cause some Sitemaps that used to have a status of OK to display an error message.
This is because we've enhanced our reporting to provide error information that wasn't available
to you before. For instance, if you see an "Invalid file format" error, make sure that you've
declared the namespace in your Sitemap file correctly and that the
[header matches the examples we provide](/search/docs/crawling-indexing/sitemaps/build-sitemap#xml)
in our documentation.

As part of this change, you can no longer list
[Sitemap index files](/search/docs/crawling-indexing/sitemaps/large-sitemaps)
within Sitemap index files. Each Sitemap index file can list only Sitemaps. Remember that you can
list up to 1,000 Sitemaps in each Sitemap index file. If you have more than 1,000 Sitemaps for a
site, you can submit multiple Sitemap index files.

We've also changed the verification
[error message](/search/blog/2006/03/if-you-see-we-couldnt-find-your)
we talked about in a recent blog post. If you request verification and we receive a status other
than `200`

or `404`

when we try to access a non-existent file on your site,
you'll now see an "HTTP error".

We expect this change to be a smooth one, but please let us know in our
[Google Group](https://support.google.com/webmasters/community)
if you experience any trouble.
