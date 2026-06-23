---
title: "Googlebot activity reports | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/10/googlebot-activity-reports
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-10-19
---

# Googlebot activity reports | Google Search Central Blog | Google for Developers

Thursday, October 19, 2006

The [Webmaster Tools](https://search.google.com/search-console)
team has a very exciting mission: we dig into our logs, find as much useful information as
possible, and pass it on to you, the webmasters. Our reward is that you more easily understand
what Google sees, and why some pages don't make it to the index.

The latest batch of information that we've put together for you is the amount of traffic between Google and a given site. We show you the number of requests, number of kilobytes (yes, yes, I know that tech-savvy webmasters can usually dig this out, but our new charts make it really easy to see at a glance), and the average document download time. You can see this information in chart form, as well as in hard numbers (the maximum, minimum, and average).

For instance, here's the number of pages Googlebot has crawled in the Webmaster Central blog over
the last 90 days. The maximum number of pages Googlebot has crawled in one day is 24 and the
minimum is 2. That makes sense, because the blog was launched less than 90 days ago, and the chart
shows that the number of pages crawled per day has increased over time. The number of pages
crawled is sometimes more than the total number of pages in the site—especially if the same
page can be accessed via several URLs. So
[/search/blog/2006/10/learn-more-about-googlebots-crawl-of](/search/blog/2006/10/learn-more-about-googlebots-crawl-of)
and
[/search/blog/2006/10/learn-more-about-googlebots-crawl-of#enhanced-image-search](/search/blog/2006/10/learn-more-about-googlebots-crawl-of#enhanced-image-search)
are different, but point to the same page (the second points to an anchor within the page).

And here's the average number of kilobytes downloaded from this blog each day. As you can see, as the site has grown over the last two and a half months, the number of average kilobytes downloaded has increased as well.

The first two reports can help you diagnose the impact that changes in your site may have on its coverage. If you overhaul your site and dramatically reduce the number of pages, you'll likely notice a drop in the number of pages that Googlebot accesses.

The average document download time can help pinpoint subtle networking problems. If the average time spikes, you might have network slowdowns or bottlenecks that you should investigate. Here's the report for this blog that shows that we did have a short spike in early September (the maximum time was 1057 ms), but it quickly went back to a normal level, so things now look OK.

In general, the load time of a page doesn't affect its ranking, but we wanted to give this info because it can help you spot problems. We hope you will find this data as useful as we do!
