---
title: "More on 404 | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/08/now-that-weve-bid-farewell-to-soft-404s
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-08-15
---

# More on 404 | Google Search Central Blog | Google for Developers

Friday, August 15, 2008

Now that we've
[bid farewell to soft 404 errors](/search/blog/2008/08/farewell-to-soft-404s),
in this post for

[we'll answer your burning](/search/blog/2008/08/its-404-week-at-webmaster-central)

`404`

week`404`

questions.
**How do you treat the response code 410 "Gone"?**
Just like a

`404`

.
**Do you index content or follow links from a page with a 404 response code?**

We aim to understand as much as possible about your site and its content. So while we wouldn't
want to show a hard `404`

to users in search results, we may utilize a `404`

error page's content or links if it's detected as a signal to help us better understand your site.

Keep in mind that if you want links crawled or content indexed, it's far more beneficial to
include them in a page that's not `404`

.

**What about 404 errors with a 10-second meta refresh?**


Yahoo! currently utilizes this method on their `404`

errors. They
[respond with a 404](https://www.yahoo.com/this-is-a-404),
but the

`404`

content also shows:
`<meta http-equiv="refresh" content="10;url=https://www.yahoo.com/?xxx" />`

. We feel
this technique is fine because it reduces confusion by giving users 10 seconds to make a new
selection, only offering the home page after 10 seconds without the user's input.
**Should I 301 redirect misspelled 404 errors to the correct URL?**


Redirecting with `301`

status `404`

errors is a good idea when it's helpful
to users (that is, not confusing like `soft 404`

errors). For instance, if you notice
that the
[Crawl Errors](https://support.google.com/webmasters/answer/9679690)
of Webmaster Tools shows a `404`

for a misspelled version of your URL, you can
`301`

the misspelled version of the URL to the correct version.

For example, if we saw this `404`

in Crawl Errors:

https://www.google.com/webmsters <-- typo for "webmasters"

we may first correct the typo if it exists on our own site, then `301`

the URL to the
correct version (as the broken link may occur elsewhere on the web):

https://www.google.com/webmasters

**Have you seen any good 404 errors?**

Yes, we have! (Confession: no one asked us this question, but few things are as fun to discuss as
response codes. :) We've put together a list of some of our favorite
`404`

pages. If you have more `404`

related questions, let us know, and
thanks for joining us for `404`

week!


[https://www.metrokitchen.com/nice-404-page]: "If you're looking for an item that's no longer stocked (as I was), this makes it really easy to find an alternative."

-[Riona], domestigeek

[https://www.comedycentral.com/another-404]: "Blame the robot monkeys"

-[Reid], tells really bad jokes


[https://www.splicemusic.com/and-another]: "Boost your 'Time on site' metrics with a`404`

page like this."

-[Susan], dabbler in music and Analytics


[https://www.treachery.net/wow-more-404s]: "It's not reassuring, but it's definitive."

-[Jonathan], has trained actual spiders to build websites, ants handle the`404`

errors


[https://www.apple.com/iPhone4g]: "Good with respect to usability."

[https://thcnet.net/lost-in-a-forest]: "At least there's a mailbox."

-[JohnMu], adventurous

[https://lookitsme.co.uk/404]: "It's pretty cute. :)"

-[Jessica], likes cute things

[https://www.orangecoat.com/a-404-page.html]: "Flow charts rule."

-[Sahala], internet traveller

[https://icanhascheezburger.com/iz-404-page]: "I can has useful links and even e-mail address for questions! But they could have added 'OH NOES! IZ MISSING PAGE! MAYBE TIPO OR BROKN LINKZ?' so folks'd know what's up."

-[Adam], lindy hop geek
