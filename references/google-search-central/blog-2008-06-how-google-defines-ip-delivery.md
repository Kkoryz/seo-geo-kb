---
title: "How Google defines IP delivery, geolocation, and cloaking | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/06/how-google-defines-ip-delivery
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-06-02
---

# How Google defines IP delivery, geolocation, and cloaking | Google Search Central Blog | Google for Developers

Monday, June 02, 2008

Many of you have asked for more information regarding webserving techniques (especially related to
[Googlebot](/search/docs/crawling-indexing/googlebot)), so we made a short
glossary of some of the more unusual methods.

-
**Geolocation**: Serving targeted/different content to users based on their location. As a webmaster, you may be able to determine a user's location from preferences you've stored in their cookie, information pertaining to their login, or their IP address. For example, if your site is about baseball, you may use geolocation techniques to highlight the Yankees to your users in New York.The key is to treat Googlebot as you would a typical user from a similar location, IP range, etc. (that is, don't treat Googlebot as if it came from its own separate country—that's cloaking).

-
**IP delivery**: Serving targeted/different content to users based on their IP address, often because the IP address provides geographic information. Because IP delivery can be viewed as a specific type of geolocation, similar rules apply. Googlebot should see the same content a typical user from the same IP address would see.*(Author's warning: This 7.5-minute video may cause drowsiness. Even if you're really interested in IP delivery or multi-language sites, it's a bit uneventful.)* -
**Cloaking**: Serving different content to users than to Googlebot. This is a violation of our[webmaster guidelines](/search/docs/essentials). If the file that Googlebot sees is not identical to the file that a typical user sees, then you're in a high-risk category. A program such as md5sum or diff can compute a hash to verify that two different files are identical. -
**First Click Free**: Implementing[Google News' First Click Free policy](https://googlenewsblog.blogspot.com/2007/09/first-click-free.html)for your content allows you to include your premium or subscription-based content in Google's websearch index without violating our quality guidelines. You allow all users who find your page using Google search to see the full text of the document, even if they have not registered or subscribed. The user's first click to your content area is free. However, you can block the user with a login or payment request when he clicks away from that page to another section of your site.If you're using First Click Free, the page displayed to users who visit from Google must be identical to the content that is shown to the Googlebot.


Still have questions? We'll see you at the related thread in our
[Webmaster Help Group](https://support.google.com/webmasters/community).
