---
title: "Google Videos best practices | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/06/google-videos-best-practices
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-06-12
---

# Google Videos best practices | Google Search Central Blog | Google for Developers

Saturday, June 12, 2010

We'd like to highlight three [best practices](/search/docs/appearance/video)
that address some of the most common problems found when crawling and indexing video content.
These best practices include ensuring your video URLs are crawlable, stating what countries your
videos may be played in, and that if your videos are removed, you clearly indicate this state to
search engines.

## Best Practice 1: Verify your video URLs are crawlable: check your robots.txt

Sometimes publishers unknowingly include video URLs in their Sitemap that are
[robots.txt](/search/docs/crawling-indexing/robots/intro) disallowed. Please make sure your
robots.txt file isn't blocking any of the URLs specified in your Sitemap. This includes URLs for
the:

- Playpage
- Content and player
- Thumbnail

## Best Practice 2: Tell us what countries the video may be played in

Is your video only available in some locales? The optional attribute "restriction" has recently
been added (see our documentation about
[video best practices](/search/docs/appearance/video)), which you can use to
tell us whether the video can only be played in certain territories. Using this tag, you have the
option of either including a list of all countries where it can be played, or just telling us the
countries where it can't be played. If your videos can be played everywhere, then you don't need
to include this.

## Best Practice 3: Indicate clearly when videos are removed—protect the user experience

Sometimes publishers take videos down but don't signal to search engines that they've done so. This can result in the search engine's index not accurately reflecting content of the web. Then when users click on a search result, they're taken to a page either indicating that the video doesn't exist, or to a different video. Users find this experience dissatisfying. Although we have mechanisms to detect when search results are no longer available, we strongly encourage following community standards.

To signal that a video has been removed:

-
**Return a**, you can still return a helpful page to be displayed to your users. Check out these`404 (Not found)`

HTTP response code[guidelines for creating useful](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors).`404`

pages -
**Indicate expiration dates**for each video listed in a Video Sitemap (use the`<video:expiration_date>`

element) or mRSS feed (`<dcterms:valid>`

tag) submitted to Google.

For more information on Google Videos please visit our
[Help Center](/search/docs/appearance/video), and to post questions and search
answers check out our
[Help Forum](https://support.google.com/webmasters/community/thread?tid=5216d9b9a700866a).
