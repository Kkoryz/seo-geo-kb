---
title: "A few questions from our Google Group | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/05/few-questions-from-our-google-group
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-05-24
---

# A few questions from our Google Group | Google Search Central Blog | Google for Developers

May 24, 2006

In this post, we thought we'd answer a couple of the questions we've been seeing in the
[Google Group](https://support.google.com/webmasters/community) lately.

## Why do I have to add my Sitemap file to my Google Sitemaps account? Can't I just link to it from my site?

There are several reasons we ask you to add the Sitemap file. Here are a couple of them:

-
If you aren't yet indexed,
[submitting a Sitemap file](/search/docs/crawling-indexing/sitemaps/overview)lets us know about your site—you can proactively tell us about it rather than wait for us to find it. -
When you add your Sitemap file to your Google Sitemaps account, we can let you know if the
[file has any errors](https://support.google.com/webmasters/answer/7451001), and then you can resubmit the file once you've fixed the errors.

## My site is indexed using both the www and non-www versions of the domain. How can I fix this?

This can happen when both versions of the domain (for instance,
`https://www.example.com/`

and `https://example.com/`

) point to the same
physical location, and links to your site use both versions of the URL. To tell us which version
you want the content indexed under, we recommend you do a `301`

redirect from one version to the
other. If your site runs on an Apache server, you can do this using an `.htaccess`

file. You can also use a script. Do a Google search for
[ 301 redirect](https://www.google.com/search?q=301+redirect)
for more information on how to set this up for your site. Note that once you implement the

`301`

redirect, it may take some time for Googlebot to recrawl the pages, follow the
redirects, and adjust the index.
If your pages are listed under both versions of the domain,
[don't use our URL removal tool](https://support.google.com/webmasters/answer/7479439)
to remove one version of the pages. Since the pages are at the same physical location for both
versions of the domain, using the URL removal tool will remove both versions from the index.

We also suggest you link to other pages of your site using absolute, rather than relative, links
with the version of the domain you want to be indexed under. For instance, from your home page,
rather than link to `products.html`

, link to
`https://www.example.com/products.html`

. And whenever possible, make sure that other
sites are linking to you using the version of the domain name that you prefer.
