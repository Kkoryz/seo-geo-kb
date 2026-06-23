---
title: "What's in a name? | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2005/08/whats-in-name
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2005-08-25
---

# What's in a name? | Google Search Central Blog | Google for Developers

August 25, 2005

How should you name your Sitemap? What extension should you give it?

The short answer is that you can name your Sitemap anything you want. You can use any extension. Just submit the URL to us, and we'll go pick it up.

The better answer is a little longer. We recommend that you give your Sitemap an extension that
identifies the file type. For instance, if you create
[a simple text file](/search/docs/crawling-indexing/sitemaps/overview#text_file)
that lists URLs, we suggest giving that Sitemap a `.txt`

extension.

If you create an XML Sitemap that uses our
[Sitemap protocol](/search/docs/crawling-indexing/sitemaps/overview),
give it an `.xml`

extension. If you compress that file using gzip, give it an
`.xml.gz`

extension.

If you use our [Sitemap Generator](/search/docs/crawling-indexing/sitemaps/overview)
to create a Sitemap, you specify the resulting Sitemap name in the `config.xml`

file.
The default name is `sitemap.xml.gz`

. If you keep the `.gz`

extension, the
resulting Sitemap file will be compressed. If you change this name to have an `.xml`

extension, the resulting file will not be compressed. We suggest you compress the file so that
your webserver will take less of a bandwidth used when we download it.

You can submit the URL of a script that dynamically generates an XML Sitemap when we download it.
That script might have an extension such as `.asp`

or `.php`

(depending on
the script type). The extension of the file isn't a problem, but if your script takes a long time
to run, the delay will look like a server timeout and we'll try again later. If you have trouble
getting this type of Sitemap submitted, make sure your script is responsive. Also ensure that your
webserver doesn't automatically add things (such as HTML headers and footers) to the generated
files, since that would cause the resulting XML file to have parsing errors.

One more thing about naming. You can name your Sitemap anything you want... almost. You can't name
it robots.txt. And if you use a
[robots.txt file](/search/docs/crawling-indexing/robots/intro) for your site, make sure
that it doesn't restrict our access to your Sitemap file.
