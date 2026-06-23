---
title: "Announcing Sitemap Generator version 1.3: Improved encoding support | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2005/09/announcing-sitemap-generator-version
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2005-09-15
---

# Announcing Sitemap Generator version 1.3: Improved encoding support | Google Search Central Blog | Google for Developers

September 15, 2005

The
[Sitemap Generator version 1.3](https://sourceforge.net/project/showfiles.php?group_id=137793&package_id=153422)
is now available and provides improved encoding support. If your webserver uses an encoding other
than UTF-8 or if your domain name or some the URLs in your site use non-ASCII characters, and you
plan to use the Sitemap Generator to create your Sitemap, you should download this latest version.

Generally, non-ASCII URLs should be
[encoded](/search/docs/crawling-indexing/sitemaps/build-sitemap#general-guidelines)
using UTF-8 before being percent-escaped. However, some webservers respond correctly only if URLs
are encoded specifically for the webserver's configuration. All URLs within your Sitemap, as well
as the URL of the Sitemap itself, must be encoded for readability by the web server on which they
are located.

If you are using the
[Sitemap Generator](/search/docs/crawling-indexing/sitemaps/overview),
you can specify the encoding of the URLs contained in the Sitemap from within the
`config.xml`

file. Within the
[site definition section](/search/docs/crawling-indexing/sitemaps/overview#config_reference)
of that config file, use the optional default_encoding attribute to specify the
[encoding](/search/docs/crawling-indexing/sitemaps/overview#encoding)
used by your webserver. If you don't use this attribute and your webserver uses an encoding other
than UTF-8, the Sitemap Generator can't know which encoding to use, although it does attempt to
determine the correct encoding. If the generated Sitemap doesn't list the URLs correctly, you
should explicitly indicate the encoding with the default_encoding attribute and run the Sitemap
Generator again.

If your URLs contain non-ASCII characters, we recommend that you run the Sitemap Generator script
using Python 2.3 or higher. This version of Python has increased non-ASCII support. If your domain
name contains non-ASCII characters, you must use Python 2.3 or later, as
[Internationalizing Domain Names in Applications (IDNA)](https://www.rfc-editor.org/rfc/rfc3490.txt)
support wasn't added until this version. Without IDNA support, the Sitemap Generator can't
correctly encode a non-ASCII domain name.
