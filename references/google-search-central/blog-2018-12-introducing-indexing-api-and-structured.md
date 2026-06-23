---
title: "Introducing the Indexing API and structured data for livestreams | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2018/12/introducing-indexing-api-and-structured
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2018-12-05
---

# Introducing the Indexing API and structured data for livestreams | Google Search Central Blog | Google for Developers

Wednesday, December 05, 2018

Over the past few years, it's become easier than ever to stream live videos online, from celebrity updates to special events. But it's not always easy for people to determine which videos are live and know when to tune in.

Today, we're introducing new tools to help more people discover your livestreams in Search and Assistant. With livestream structured data and the Indexing API, you can let Google know when your video is live, so it will be eligible to appear with a red LIVE badge.

## Add livestream structured data to your page

If your website streams live videos,
[use the livestream developer documentation](/search/docs/appearance/structured-data/video#livestream-guidelines)
to flag your video as a live broadcast and mark the start and end times. In addition,
`VideoObject`

structured data is required to tell Google that there's a video on your
page.

## Update Google quickly with the Indexing API

The Indexing API now supports pages with livestream structured data. We encourage you to
[call the Indexing API](/search/apis/indexing-api/v3/quickstart) to request that your
site is crawled in time for the livestream. We recommend calling the Indexing API when your livestream
begins and ends, and if the structured data changes.

For more information, visit our
[developer documentation](/search/docs/appearance/structured-data/video#livestream-guidelines).
If you have any questions, ask us in the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
We look forward to seeing your live videos on Google!
