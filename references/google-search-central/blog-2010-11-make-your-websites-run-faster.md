---
title: "Make your websites run faster, automatically—try mod_pagespeed for Apache | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/11/make-your-websites-run-faster
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-11-03
---

# Make your websites run faster, automatically—try mod_pagespeed for Apache | Google Search Central Blog | Google for Developers

Wednesday, November 03, 2010

Last year, as part of Google's initiative to make the web faster, we introduced
[Page Speed](/speed),
a tool that gives developers suggestions to speed up web pages. It's usually pretty
straightforward for developers and webmasters to implement these suggestions by updating their
web server configuration, HTML, JavaScript, CSS and images. But we thought we could make it even
easier—ideally these optimizations should happen with minimal developer and webmaster
effort.

So today, we're introducing a module for the Apache HTTP Server called
[ mod_pagespeed](/speed/pagespeed/module)
to perform many speed optimizations automatically. We're starting with more than 15 on-the-fly
optimizations that address various aspects of web performance, including optimizing caching,
minimizing client-server round trips and minimizing payload size. We've seen mod_pagespeed reduce
page load times by up to 50% (an average across a rough sample of sites we tried)—in other
words, essentially speeding up websites by about 2x, and sometimes even faster.

Here are a few simple optimizations that are a pain to do manually, but that
`mod_pagespeed`

excels at:

- Making changes to the pages built by the Content Management Systems (CMS) with no need to make changes to the CMS itself,
- Recompressing an image when its HTML context changes to serve only the bytes required (typically tedious to optimize manually), and
- Extending the cache lifetime of the logo and images of your website to a year, while still allowing you to update these at any time.

We're working with
[Go Daddy](https://www.godaddy.com/)
to get `mod_pagespeed`

running for many of its 8.5 million customers. Warren Adelman,
President and COO of Go Daddy, says:

```
Go Daddy is continually looking for ways to provide our customers the best user experience
possible. That's the reason we partnered with Google on the 'Make the Web Faster' initiative.
Go Daddy engineers are seeing a dramatic decrease in load times of customers' websites using
````mod_pagespeed`

and other technologies provided. We hope to provide the technology to
our customers soon - not only for their benefit, but for their website visitors as well.

We're also working with
[Cotendo](https://www.cotendo.com/)
to integrate the core engine of `mod_pagespeed`

as part of their Content Delivery
Network (CDN) service.

`mod_pagespeed`

integrates as a module for the Apache HTTP Server, and we've released
it as open-source for Apache for many Linux distributions. Download
[mod_pagespeed](/speed/pagespeed/module)
for your platform and let us know what you think on the project's
[mailing list](https://groups.google.com/group/mod-pagespeed-discuss).
We hope to work with the hosting, developer and webmaster community to improve
`mod_pagespeed`

and make the web faster.
