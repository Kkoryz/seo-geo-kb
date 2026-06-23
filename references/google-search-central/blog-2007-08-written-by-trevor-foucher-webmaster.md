---
title: "Register non-English domain names with Webmaster Tools | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2007/08/written-by-trevor-foucher-webmaster
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2007-08-27
---

# Register non-English domain names with Webmaster Tools | Google Search Central Blog | Google for Developers

Monday, August 27, 2007

I'm happy to announce that Webmaster Tools is expanding support for webmasters outside of the
English-speaking world, by supporting
[Internationalizing Domain Names in Applications (IDNA)](https://www.ietf.org/rfc/rfc3490.txt).
IDNA provides a way for site owners to have domains that go beyond the domain name system's
limitations of English letters and numbers. Prior to IDNA, Internet host names could only be in
the 26 letters of the English alphabet, the numbers 0-9, and the hyphen character. With IDNA
support, you'll now be able to add your sites that use other character sets, and organize them
easily on your Webmaster Tools Dashboard.

Let's say you wanted to add `https://北京大学.cn/`

(Peking University) to your Webmaster
Tools account before we launched IDNA support. If you typed that in to the "Add Site" box, you'd
get back an error message that looks like this:

Some webmasters discovered a workaround. Internally, IDNA converts nicely encoded
`https://北京大学.cn/`

to a format called
[Punycode](https://www.ietf.org/rfc/rfc3492.txt),
which looks like `https://xn--1lq90ic7fzpc.cn/`

. This allowed them to diagnose and view
information about their site, but it looked pretty ugly. Also, if they had more than one IDNA
site, you can imagine it would be pretty hard to tell them apart.

Since we now support IDNA throughout Webmaster Tools, all you need to do is type in the name of
your site, and we will add it correctly. Here is what it looks like if you attempt to add
`https://北京大学.cn/`

to your account:

If you are one of the webmasters who discovered the workaround previously (that is, you have had
sites listed in your account that look like `https://xn--1lq90ic7fzpc.cn/`

), those sites
will now automatically display correctly.

We'd love to hear your questions and feedback on this new feature; you can post in the
[Google Webmaster Tools](https://support.google.com/webmasters/community)
section of our Webmaster Help Group. We'd also appreciate suggestions for other ways we can
improve our international support.
