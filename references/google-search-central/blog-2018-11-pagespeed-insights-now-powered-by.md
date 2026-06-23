---
title: "PageSpeed Insights, now powered by Lighthouse | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2018/11/pagespeed-insights-now-powered-by
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2018-11-12
---

# PageSpeed Insights, now powered by Lighthouse | Google Search Central Blog | Google for Developers

Monday, November 12, 2018

At Google, we know that
[speed matters](/web/fundamentals/performance/why-performance-matters)
and we provide a
[variety of tools](/web/fundamentals/performance/speed-tools) to
help everyone understand the performance of a page or site. Historically, these tools have used
different analysis engines. Unfortunately, this caused some confusion because the recommendations
from each tool were different. Today, we're happy to announce that Pagespeed Insights (PSI) now
uses
[Lighthouse](/web/tools/lighthouse) as its analysis engine. This
allows developers to get the same performance audits and recommendations everywhere: on the web,
from the command line, and in Chrome DevTools. PSI also incorporates field data provided by the
[Chrome User Experience Report](/web/tools/chrome-user-experience-report)
(CrUX). Version 5 of the PageSpeed Insights API will now provide CrUX data and all of the
Lighthouse audits. Previous versions of the PSI API will be deprecated in six months.

PageSpeed Insights provides the following information:

-
: PSI fetches and analyzes the page using[Lab Data](/web/fundamentals/performance/speed-tools#lab_data)[Lighthouse](/web/tools/lighthouse), which simulates how a mobile device loads a page. It computes a set of[performance metrics](/web/fundamentals/performance/user-centric-performance-metrics)for the page (such as First Contentful Paint and Time to Interactive) and summarizes these metrics with a performance score from 0-100. Scores are categorized into three levels; 90 and up is considered to be a good score. -
: PSI also displays real-world performance metrics (First Contentful Paint and First Input Delay) for the page and its[Field Data](/web/fundamentals/performance/speed-tools#field_data)[origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). (As a result, we've also deprecated the origin: query in PSI). Note that not all sites may have field data available for display. The data set relies on a version of the Chrome User Experience Report that is updated daily and is aggregated over the previous 28 days. Keep in mind that the metrics here may be different from the ones in the Lab Data section as they capture a wide spectrum of real-world network conditions and devices used by Chrome users. **Opportunities**: PSI provides suggestions on how to improve the page's performance metrics. Each suggestion in this section estimates how much faster the page will load if the improvement is implemented.-
**Diagnostics**: This section provides additional information about how a page adheres to best practices for web development.

The
[PSI v5 API](/speed/docs/insights/v5/get-started)
now returns this new analysis together with CrUX data, and all Lighthouse category data
(Performance, Progressive Web App, Accessibility, Best Practices, and SEO) for a given URL.

We have more information about the changes in our
[FAQ](/speed/docs/insights/v5/about#faq).
If you have a specific, answerable question about using PageSpeed Insights, ask the question in
English on
[Stack Overflow](https://stackoverflow.com/questions/tagged/pagespeed-insights).
For general questions, feedback, and discussion, start a thread in the
[mailing list](https://groups.google.com/forum/#!forum/pagespeed-insights-discuss).
