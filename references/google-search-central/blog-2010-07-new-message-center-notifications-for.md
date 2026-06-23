---
title: "New Message Center notifications for detecting an increase in Crawl Errors | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/07/new-message-center-notifications-for
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-07-26
---

# New Message Center notifications for detecting an increase in Crawl Errors | Google Search Central Blog | Google for Developers

Monday, July 26, 2010

When Googlebot crawls your site, it's expected that most URLs will return a `200`

response code, some a `404`

response, some will be disallowed by robots.txt, etc.
Whenever we're unable to reach your content, we show this information in the
[Crawl errors](https://support.google.com/webmasters/answer/9679690)
section of Webmaster Tools (even though it might be intentional and not actually an error).
Continuing with our effort to provide useful and actionable information to webmasters, we're now
sending **SiteNotice** messages when we detect a significant increase in the number of crawl
errors impacting a specific site. These notifications are meant to alert you of potential
crawl-related issues and provide a sample set of URLs for diagnosing and fixing them.

A SiteNotice for a spike in the number of unreachable URLs, for example, will look like this:

We hope you find SiteNotices helpful for discovering and dealing with issues that, if left
unattended, could negatively affect your crawl coverage. You'll only receive these notifications
if you've verified your site in Webmaster Tools and we detect significant changes to the number of
crawl errors we encounter on your site. And if you don't want to miss out on any these important
messages, you can use the
[email forwarding feature](https://www.google.com/support/webmasters/bin/answer.py?answer=140528)
to receive these alerts in your inbox.

If you have any questions, please post them in our
[Webmaster Help Forum](https://support.google.com/webmasters/community)
or leave your comments below.
