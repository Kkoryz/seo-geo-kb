---
title: "Googlebot evergreen rendering in our testing tools | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2019/08/evergreen-googlebot-in-testing-tools
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2019-08-07
---

# Googlebot evergreen rendering in our testing tools | Google Search Central Blog | Google for Developers

Wednesday, August 07, 2019

Today we updated most of [our testing tools](/search/tools) so they are using the
evergreen Chromium renderer. This affects our testing tools like the mobile-friendly test or the
URL inspection tool in Search Console. In this post we look into what this means and what went
into making this update happen.

## The evergreen Chromium renderer

At Google I/O this year we were happy to announce
[the new evergreen Googlebot](https://www.youtube.com/watch/ufcijo46LCU?t=10m43s).

At its core the update is a switch from Chrome 41 as the rendering engine to the latest stable Chromium. Googlebot is now using the latest stable Chromium to run JavaScript and render pages. We will continue to update Googlebot along with the stable Chromium, hence we call it "evergreen".

## What this means for your websites

We are very happy to bring the latest features of the web platform not only to Googlebot but to
the tools that let you see what Googlebot sees as well. This means websites using ES6+, Web
Components and
[1000+ new web platform features](https://chromereleases.googleblog.com/)
are now rendered with the latest stable Chromium, both in Googlebot and our testing tools.

## What the update changes in our testing tools

Our testing tools reflect how Googlebot processes your pages as closely as possible. With the update to the new Googlebot, we had to update them to use the same renderer as Googlebot.

The change will affect the rendering within the following tools:

-
[Search Console](https://search.google.com/search-console)'s URL inspection tool -
[Mobile-friendly test](https://developer.chrome.com/docs/lighthouse/overview) -
[Rich results test](https://search.google.com/test/rich-results) -
[AMP test](https://search.google.com/test/amp)

We tested these updates and based on the feedback we have switched the tools listed previously to
the new evergreen Googlebot. A lot of the feedback came from Googlers and the community.
[Product Experts](https://productexperts.withgoogle.com/) and
[Google Developer Experts](/community/experts)
helped us make sure the update works well.

Note: The new Googlebot still uses the same
[user agent](/search/docs/crawling-indexing/overview-google-crawlers)
as before the update. There will be more information about an update to the user agent in the near
future. For now, Googlebot's user agent and the user agent used in the testing tools does not
change.

We are excited about this update and are looking forward to your feedback and questions on
[Twitter](https://twitter.com/googlesearchc), the
[webmaster forum](https://support.google.com/webmasters/community)
or in our
[webmaster office hours](https://google.com/webmasters/connect).
