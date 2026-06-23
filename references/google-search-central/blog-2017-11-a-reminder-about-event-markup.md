---
title: "A reminder about \"event\" markup | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2017/11/a-reminder-about-event-markup
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2017-11-27
---

# A reminder about "event" markup | Google Search Central Blog | Google for Developers

Monday, November 27, 2017

Lately we've been receiving feedback from users seeing non-events like coupons or vouchers showing
up in search results where "events" snippets appear. This is really confusing for users and also
against our guidelines, where we have added
[additional clarification](/search/docs/appearance/structured-data/event).

So, what's the problem?

We've seen a number of publishers in the coupons/vouchers space use the "event" markup to
describe their offers. And as much as using a discount voucher can be a very special thing, that
doesn't make coupons or vouchers events or "saleEvents". Using
[Event markup](/search/docs/appearance/structured-data/event) to describe something that
is not an event creates a bad user experience, by triggering a rich result for something that will
happen at a particular time, despite no actual event being present.

Here are some examples to illustrate the issue:

Since this creates a misleading user experience, we may take manual action on such cases. In case your website is affected by such a manual action, you will find a notification in your Search Console account. If a manual action is taken, it can result in structured data markup for the whole site not being used for search results.

While we're specifically highlighting coupons and vouchers in this blogpost, this applies to all other non-event items being annotated with "event" markup as well—or, really, for applying a type of markup to something other than the type of thing it is meant to describe.

For more information, please visit our
[developer documentation](/search/docs/appearance/structured-data/event) or stop by our
[Webmaster Forum](https://support.google.com/webmasters/go/community)
in case you have additional questions!
