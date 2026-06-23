---
title: "Android app indexing is now open for everyone! | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2014/06/android-app-indexing-is-now-open-for
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2014-06-25
---

# Android app indexing is now open for everyone! | Google Search Central Blog | Google for Developers

Wednesday, June 25, 2014

Do you have an Android app in addition to your website? You can now connect the two so that users searching from their smartphones and tablets can easily find and reach your app content.

App deep links in search results help your users find your content more easily and re-engage with your app after they've installed it. As a site owner, you can show your users the right content at the right time—by connecting pages of your website to the relevant parts of your app you control when your users are directed to your app and when they go to your website.

Hundreds of apps have
[already implemented app indexing](https://firebase.google.com/docs/app-indexing/).
This week at Google I/O, we're announcing a set of new features that will make it even easier to
set up deep links in your app, connect your site to your app, and keep track of performance and
potential errors.

## Getting started is easy

We've greatly simplified the process to get your app deep links indexed. If your app supports HTTP deep linking schemes, here's what you need to do:

-
[Add deep link support to your app](https://firebase.google.com/docs/app-indexing/) -
[Connect your site and your app](https://firebase.google.com/docs/app-indexing/) - There is no step 3 (:

As we index your URLs, we'll discover and index the app / site connections and may begin to surface app deep links in search results.

We can discover and index your app deep links on our own, but we recommend you publish the deep links. This is also the case if your app only supports a custom deep link scheme. You can publish them in one of the following ways:

-
Add a

`rel=alternate`

`<link />`

element to specify the corresponding app URI. You can insert it in the`<head>`

section of each web page, or in your sitemap.[Find out how to implement these methods](https://firebase.google.com/docs/app-indexing/)on our developer site. -
[Use the App indexing API](https://firebase.google.com/docs/app-indexing/)

There's one more thing: we've added a
[new feature in Webmaster Tools](https://support.google.com/webmasters/answer/9679690)
to help you debug any issues that might arise during app indexing. It will show you what type of
errors we've detected for the app page-web page pairs, together with example app URIs so you can
debug:

We'll also give you detailed instructions on how to debug each issue, including a QR code for the app deep links, so you can easily open them on your phone or tablet. We'll send you Webmaster Tools error notifications as well, so you can keep up to date.

Give app indexing a spin, and as always, if you need more help ask questions on the
[Webmaster help forum](https://support.google.com/webmasters/community/).
