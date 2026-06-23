---
title: "Upcoming changes in Google's HTTP Referrer | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/03/upcoming-changes-in-googles-http
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-03-19
---

# Upcoming changes in Google's HTTP Referrer | Google Search Central Blog | Google for Developers

Monday, March 19, 2012

Protecting users' privacy is a priority for us and it's helped drive
[recent](https://googleblog.blogspot.com/2011/10/making-search-more-secure.html)
[changes](https://insidesearch.blogspot.com/2012/03/bringing-more-secure-search-around.html).
Helping users save time is also very important; it's explicitly mentioned as a part of
[our philosophy](https://www.google.com/about/company/tenthings).
Today, we're happy to announce that Google Web Search will soon be using a
[new proposal](https://wiki.whatwg.org/wiki/Meta_referrer) to
reduce latency when a user of Google's SSL-search clicks on a search result with a modern browser
such as Chrome.

Starting in April, for browsers with the appropriate support, we will be using the "referrer" meta
tag to automatically simplify the
[referring URL](https://en.wikipedia.org/wiki/HTTP_referer) that
is sent by the browser when visiting a page linked from an organic search result. This results in
a faster time to result and more streamlined experience for the user.

What does this mean for sites that receive clicks from Google search results? You may start to see
[ origin](https://tools.ietf.org/html/rfc6454)
referrers—Google's home pages (see the

[meta referrer specification](https://wiki.whatwg.org/wiki/Meta_referrer)for further detail)—as a source of organic SSL search traffic. This change will only affect the subset of SSL search referrers which already didn't include the query terms. Non-HTTPS referrals will continue to behave as they do today. Again, the primary motivation for this change is to remove an unneeded redirect so that signed-in users reach their destination faster.

Website analytics programs can detect these organic search requests by detecting bare Google host
names using SSL (like "https://www.google.co.uk/"). Webmasters will continue see the same data in
[Webmasters Tools](https://search.google.com/search-console)
just as before, you'll receive an aggregated list of the
[top search queries](https://support.google.com/webmasters/answer/7576553#zippy=%2Cqueries)
that drove traffic to their site.

We will continue to look into further improvements to how search query data is surfaced through
Webmaster Tools. If you have questions, feedback or suggestions, please let us know through the
[Webmaster Tools Help Forum](https://groups.google.com/a/googleproductforums.com/forum/#!categories/webmasters).
