---
title: "All About Googlebot | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/08/all-about-googlebot
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-08-19
---

# All About Googlebot | Google Search Central Blog | Google for Developers

Saturday, August 19, 2006

I've seen a lot of questions lately about robots.txt files and Googlebot's behavior. Last week
at SES, I spoke on a new panel called
[the Bot Obedience course](https://www.searchenginestrategies.com/sew/summer06/agenda2.html#115-5).
And a few days ago, some other Googlers and I fielded questions on the
[WebmasterWorld forums](https://www.webmasterworld.com/google/3044757.htm).
Here are some of the questions we got:

**
If my site is down for maintenance, how can I tell Googlebot to come back later rather than to
index the "down for maintenance" page?
** You should configure your server to return a
[status](/search/docs/crawling-indexing/http-network-errors) of
`503 (network unavailable)`

rather than `200 (successful)`

. That lets
Googlebot know to try the pages again later.

**What should I do if Googlebot is crawling my site too much?** You can
[contact us](https://support.google.com/webmasters/answer/48620)
—we'll work with you to make sure we don't overwhelm your server's bandwidth. We're
experimenting with a feature in our Webmaster Tools for you to provide input on your crawl rate,
and have gotten great feedback so far, so we hope to offer it to everyone soon.

**Is it better to use the robots meta tag or a robots.txt file?** Googlebot obeys either, but

`meta`

tags apply to single pages only. If you have a number of pages you want to exclude from
crawling, you can structure your site in such a way that you can easily use a robots.txt file to
block those pages (for instance, put the pages into a single directory).
**
If my robots.txt file contains a rule for all bots as well as a specific rule for
Googlebot, how does Googlebot interpret the line addressed to all bots?
** If your robots.txt file contains a global rule plus a rule specifically
for Googlebot, Googlebot obeys the lines specifically directed at it. For instance, for this
robots.txt file:

User-agent: * Disallow: / User-agent: Googlebot Disallow: /cgi-bin/

Googlebot will crawl everything in the site other than pages in the cgi-bin directory.

For this robots.txt file:

User-agent: * Disallow: /

Googlebot won't crawl any pages of the site.

If you're not sure how Googlebot will interpret your robots.txt file, you can use our
[robots.txt analysis tool](https://www.google.com/webmasters/tools/robots-testing-tool)
to test it. You can also test how Googlebot will interpret changes to the file.

For complete information on how Googlebot and Google's other user agents treat robots.txt files,
see our [webmaster help center](/search/docs/crawling-indexing/robots/intro).
