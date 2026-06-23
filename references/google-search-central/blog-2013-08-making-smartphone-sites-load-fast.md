---
title: "Making smartphone sites load fast | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2013/08/making-smartphone-sites-load-fast
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2013-08-08
---

# Making smartphone sites load fast | Google Search Central Blog | Google for Developers

Thursday, August 08, 2013

Users
[tell us](https://www.google.com/think/research-studies/creating-moments-that-matter)
they use smartphones to search online because it's quick and convenient, but today's average
mobile page typically
[takes more than 7 seconds to load](https://analytics.blogspot.com/2013/04/is-web-getting-faster.html).
Wouldn't it be great if mobile pages loaded in under one second? Today we're announcing new
[guidelines](/speed/docs/insights/mobile) and an updated
[PageSpeed Insights tool](https://pagespeed.web.dev/) to help
webmasters optimize their mobile pages for best rendering performance.

## Prioritizing above-the-fold content

Research
[shows](https://www.nngroup.com/articles/response-times-3-important-limits/)
that users' flow is interrupted if pages take longer than one second to load. To deliver the best
experience and keep the visitor engaged, our guidelines focus on rendering some content, known as
the above-the-fold content, to users in one second (or less!) while the rest of the page continues
to load and render in the background. The above-the-fold HTML, CSS, and JS is known as the
[critical rendering path](https://www.youtube.com/watch?v=YV1nKLWoARQ).

We can achieve sub-second rendering of the above-the-fold content on mobile networks by applying the following best practices:

- Server must render the response (< 200 ms)
- Number of redirects should be minimized
- Number of roundtrips to first render should be minimized
- Avoid external blocking JavaScript and CSS in above-the-fold content
- Reserve time for browser layout and rendering (200 ms)
- Optimize JavaScript execution and rendering time

These are explained in more details in the
[mobile-specific help pages](/speed/docs/insights/mobile),
and, when you're ready, you can test your pages and the improvements you make using the
[PageSpeed Insights](https://pagespeed.web.dev/) tool.

As always, if you have any questions or feedback, please post in our
[discussion group](https://groups.google.com/forum/#!forum/page-speed-discuss).
