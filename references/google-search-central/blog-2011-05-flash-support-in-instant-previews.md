---
title: "Flash support in Instant Previews | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2011/05/flash-support-in-instant-previews
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2011-05-06
---

# Flash support in Instant Previews | Google Search Central Blog | Google for Developers

Friday, May 06, 2011

With
[Instant Previews](/search/blog/2010/11/instant-previews), users can see a snapshot of
a search result before clicking on it. We've made a number of
[improvements](https://googleblog.blogspot.com/2011/04/this-week-in-search-41511)
to the feature since its introduction last November, and if you own a site, one of the most
relevant changes for you is that Instant Previews now supports Flash.

In most cases, when the preview for a page is generated through our regular crawl, we will now render a snapshot of any Flash components on the page. This will replace the "puzzle piece" icon that previously appeared to indicate Flash components, and should improve the accuracy of the previews.

However, for pages that are fetched on demand by the "Google Web Preview" user-agent, we will generate a preview without Flash in order to minimize latency. In these cases the preview will appear as if the page were visited by someone using a browser without Flash enabled, and "Install Flash" messages may appear in the preview, depending on how your website handles users without Flash.

To improve your previews for these on-demand renders, here are some guidelines for using Flash on your site:

-
**Make sure that your site has a reasonable, seamless experience for visitors without Flash.**This may involve creating HTML-only equivalents for your Flash-based content that will automatically be shown to visitors who can't view Flash. Providing a good experience for this case will improve your preview and make your visitors happier. -
If Flash components are rendering but appear as loading screens instead of actual content,
**try reducing the loading time for the component**. This makes it more likely we'll render it properly. -
If you have Flash videos on your site,
**consider**which helps us to generate thumbnails for your videos in Instant Previews.[submitting a Video Sitemap](/search/docs/crawling-indexing/sitemaps/video-sitemaps) - If most of the page is rendering properly but you still see puzzle pieces appearing for some smaller components, these may be fixed in future crawls of your page.

If you have additional questions, you can post them in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).

As always, we'll keep you updated as we continue to make improvements to Instant Previews.
