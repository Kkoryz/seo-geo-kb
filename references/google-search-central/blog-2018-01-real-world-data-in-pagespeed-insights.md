---
title: "Real-world data in PageSpeed Insights | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2018/01/real-world-data-in-pagespeed-insights
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2018-01-10
---

# Real-world data in PageSpeed Insights | Google Search Central Blog | Google for Developers

Wednesday, January 10, 2018

[PageSpeed Insights](https://pagespeed.web.dev/)
provides information about how well a page adheres to a set of best practices. In the past, these
recommendations were presented without the context of how fast the page performed in the real
world, which made it hard to understand when it was appropriate to apply these optimizations.
Today, we're announcing that PageSpeed Insights will use data from the
[Chrome User Experience Report](https://blog.chromium.org/2017/10/introducing-chrome-user-experience-report.html)
to make better recommendations for developers and the optimization score has been tuned to be more
aligned with the real-world data.

The PSI report now has several different elements:

-
The Speed score categorizes a page as being Fast, Average, or Slow. This is determined by
looking at the median value of two metrics: First Contentful Paint
(
[FCP](/web/updates/2017/06/user-centric-performance-metrics)) and DOM Content Loaded ([DCL](/web/fundamentals/performance/critical-rendering-path/measure-crp)). If both metrics are in the top one-third of their category, the page is considered fast. - The Optimization score categorizes a page as being Good, Medium, or Low by estimating its performance headroom. The calculation assumes that a developer wants to keep the same appearance and functionality of the page.
- The Page Load Distributions section presents how this page's FCP and DCL events are distributed in the data set. These events are categorized as Fast (top third), Average (middle third), and Slow (bottom third) by comparing to all events in the Chrome User Experience Report.
-
The Page Stats section describes the round trips required to load the page's
[render-blocking resources](/web/fundamentals/performance/critical-rendering-path), the total bytes used by the page, and how it compares to the median number of round trips and bytes used in the dataset. It can indicate if the page might be faster if the developer modifies the appearance and functionality of the page. -
Optimization Suggestions is a list of
[best practices](/speed/docs/insights/rules)that could be applied to this page. If the page is fast, these suggestions are hidden by default, as the page is already in the top third of all pages in the data set.

For more details on these changes, see
[About PageSpeed Insights](/speed/docs/insights/about).
As always, if you have any questions or feedback, please visit our
[forums](https://groups.google.com/forum/)
and please remember to include the URL that is being evaluated.
