---
title: "Updating the user agent of Googlebot | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2019/10/updating-user-agent-of-googlebot
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2019-10-02
---

# Updating the user agent of Googlebot | Google Search Central Blog | Google for Developers

Wednesday, October 02, 2019

Googlebot uses a Chrome-based browser to render webpages, as
[we announced at Google I/O](/search/blog/2019/05/the-new-evergreen-googlebot) earlier
this year. As part of this, in December 2019 we'll update Googlebot's user agent strings to
reflect the new browser version, and periodically update the version numbers to match Chrome
updates in Googlebot.

See [Google crawlers (user agents)](/search/docs/crawling-indexing/overview-google-crawlers)
and
[Make sure Google can index JavaScript](/search/docs/crawling-indexing/javascript/fix-search-javascript)
for background reading about user agent strings and rendering.

## Googlebot user agents today

**Mobile:**

`Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/`

**41.0.2272.96** Mobile Safari/537.36 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)

**Desktop:**

`Mozilla/5.0 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)`


*OR*

`Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +https://www.google.com/bot.html) Safari/537.36`


## The new evergreen Googlebot and its user agent

In December we'll start periodically updating the above user agent strings to reflect the version
of Chrome used in Googlebot. In the following user agent strings,
`W.X.Y.Z`

will be substituted with the
[Chrome version](https://www.chromium.org/developers/version-numbers)
we're using. For example, instead of `W.X.Y.Z`

you'll see something similar to
`76.0.3809.100`

. This version number will update on a regular basis.

**Mobile:**

`Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/`

**W.X.Y.Z** Mobile Safari/537.36 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)

**Desktop:**

`Mozilla/5.0 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)`


*OR*

`Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +https://www.google.com/bot.html) Chrome/`

**W.X.Y.Z** Safari/537.36

## How to test your site

We've run an evaluation, so are confident that most websites will not be affected by the change.

Sites that follow our recommendations to use feature detection and progressive enhancement instead of user agent sniffing should continue to work without any changes.

If your site looks for a specific user agent, it may be affected. You should use feature detection instead of user agent sniffing. If you cannot use feature detection and need to detect Googlebot via the user agent, then look for "Googlebot" within the user agent.

Some common issues we saw while evaluating this change include:

- Pages that present an error message instead of normal page contents. For example, a page may assume Googlebot is a user with an ad-blocker, and accidentally prevent it from accessing page contents.
- Pages that redirect to a roboted or noindex document.

If you're not sure if your site is affected or not, you can try loading your webpage in your
browser using the new Googlebot user agent.
[These instructions](/web/tools/chrome-devtools/device-mode/override-user-agent)
show how to override your user agent in Chrome.

If you have any questions, be sure to reach out to our
[webmaster help community](https://support.google.com/webmasters/community),
join our
[webmaster office hours on YouTube](https://google.com/webmasters/connect) or
[follow us on Twitter](https://twitter.com/googlesearchc).
