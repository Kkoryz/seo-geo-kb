---
title: "The four steps to appiness | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2014/12/the-four-steps-to-appiness
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2014-12-09
---

# The four steps to appiness | Google Search Central Blog | Google for Developers

Tuesday, December 09, 2014

[App deep links](https://firebase.google.com/docs/app-indexing/) are
the new kid on the block in organic search, and they're picking up speed faster than you can say
"schema.org ViewAction"! For signed-in users, 15% of Google searches
on Android now return deep links to apps through App Indexing. And over just the past quarter,
we've seen the number of clicks on app deep links jump by 10x.

We've gotten a lot of feedback from developers and seen a lot of implementations gone right and
others that were good learning experiences since we
[opened up App Indexing back in June](/search/blog/2014/06/android-app-indexing-is-now-open-for).
We'd like to share with you four key steps to monitor app performance and drive user engagement:

## Give your app developer access to Webmaster Tools

App indexing is a team effort between you (as a webmaster) and your app development team. We show information in Webmaster Tools that is key for your app developers to do their job well. Here's what's available right now:

- Errors in indexed pages within apps
- Weekly clicks and impressions from app deep link via Google search
- Stats on your sitemap (if that's how you implemented the app deep links)

...and we plan to add a lot more in the coming months!

We've noticed that very few developers have access to Webmaster Tools. So if you want your app development team to get all of the information they need to fix app-related issues, it's essential for them to have access to Webmaster Tools.

Any verified site owner can
[add a new user](https://www.google.com/webmasters/tools/user-admin).
Pick restricted or full permissions, depending on the
[level of access](https://support.google.com/webmasters/answer/2451999)
you'd like to give:

## Understand how your app is doing in search results

How are users engaging with your app from search results? We've introduced two new ways for you to track performance for your app deep links:

-
We now send a weekly clicks and impressions update to the
[Message center](https://support.google.com/webmasters/answer/140528)in your Webmaster Tools account. -
You can now track how much traffic app deep links drive to your app using referrer
information—specifically, the referrer extra in the
`ACTION_VIEW`

intent. We're working to integrate this information with Google Analytics for even easier access. Learn[how to track referrer information](https://firebase.google.com/docs/app-indexing/)on our Developer site.

## Make sure key app resources can be crawled

Blocked resources are one of the top reasons for the "content mismatch" errors you see in
Webmaster Tools'
[Crawl Errors report](https://support.google.com/webmasters/answer/9679690).
We need access to all the resources necessary to render your app page. This allows us to assess
whether your associated web page has the same content as your app page.

To help you find and fix these issues, we now show you the specific resources we can't access that are critical for rendering your app page. If you see a content mismatch error for your app, look out for the list of blocked resources in "Step 5" of the details dialog:

## Watch out for Android App errors

To help you identify errors when indexing your app, we'll send you messages for all app errors we
detect, and will also display most of them in the "Android apps" tab of the
[Crawl Errors report](https://support.google.com/webmasters/answer/9679690).

In addition to the currently available "Content mismatch" and "Intent URI not supported" error alerts, we're introducing three new error types:

-
**APK not found**: we can't find the package corresponding to the app. -
**No**: the link to your app does not lead directly to the content, but requires login to access.[first-click free](/search/blog/2008/10/first-click-free-for-web-search) -
**Back button violation**: after following the link to your app, the back button did not return to search results.

In our experience, the majority of errors are usually caused by a general setting in your app (for example, a blocked resource, or a region picker that pops up when the user tries to open the app from search). Taking care of that generally resolves it for all involved URIs.

Good luck in the pursuit of appiness! As always, if you have questions, you can drop by our
[Webmaster help forum](https://support.google.com/webmasters/go/community).
