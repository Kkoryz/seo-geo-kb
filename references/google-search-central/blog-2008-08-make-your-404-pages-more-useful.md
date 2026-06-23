---
title: "Make your 404 pages more useful | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/08/make-your-404-pages-more-useful
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-08-19
---

# Make your 404 pages more useful | Google Search Central Blog | Google for Developers

Tuesday, August 19, 2008

Your visitors may stumble into a
[ 404 "Not found"](https://google.com/not-very+found)
page on your website for a variety of reasons:

- A mistyped URL, or a copy-and-paste mistake
- Broken or truncated links on web pages or in an email message
- Moved or deleted content

Confronted by a `404`

page, they may then attempt to manually correct the URL, click
the back button, or even navigate away from your site. As hinted in an
[earlier post](/search/blog/2008/08/farewell-to-soft-404s)
for
[" 404 week at Webmaster Central"](/search/blog/2008/08/its-404-week-at-webmaster-central),
there are various ways to help your visitors get out of the dead-end situation. In our quest to
make

`404`

pages more useful, we've just added a section in
[Webmaster Tools](https://search.google.com/search-console)called "Enhance

`404`

pages". If you've created a
[custom](/search/docs/crawling-indexing/http-network-errors#pagegone)this allows you to embed a widget in your

`404`

page`404`

page that helps your visitors find what
they're looking for by providing suggestions based on the incorrect URL.
Example: Jamie receives the link `www.example.com/activities/adventurecruise.html`

in an email message. Because of formatting due to a bad email client, the URL is truncated to
`www.example.com/activities/adventur`

. As a result it returns a `404`

page.
With the `404`

widget added, however, she could instead see the following:

In addition to attempting to correct the URL, the `404`

widget also suggests the
following, if available:

- a link to the parent subdirectory
- a sitemap webpage
- site search query suggestions and search box

How do you add the widget? Visit the "Enhance `404`

pages" section in Webmaster Tools,
which allows you to generate a JavaScript snippet. You can then copy and paste this into your
custom `404`

page's code. As always, don't forget to
[return a proper 404 code](/search/blog/2008/08/farewell-to-soft-404s).

Can you change the way it looks? Sure. We leave the HTML unstyled initially, but you can edit the
CSS block that we've included. For more information, check out our
[guide on how to customize the look of your 404 widget](https://www.google.com/support/webmasters/bin/answer.py?answer=100044&hl=en).

This feature is currently experimental—we might not provide corrections and suggestions for
your site but we'll be working to improve the coverage. In the meantime, let us know what you
think in the comments below or in our
[group discussion](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/8043e56a67baa401).
Thanks for helping us make the Internet a more friendly place!
