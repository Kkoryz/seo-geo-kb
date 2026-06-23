---
title: "How to start a multilingual site | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/08/how-to-start-multilingual-site
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-08-07
---

# How to start a multilingual site | Google Search Central Blog | Google for Developers

Thursday, August 07, 2008

Have you ever thought of creating one or several sites in different languages? Let's say you want to start a travel site about backpacking in Europe, and you want to offer your content to English, German, and Spanish speakers. You'll want to keep in mind factors like site structure, geographic as well as language targeting, and content organization.

## Site structure

The first thing you'll want to consider is if it makes sense for you to buy country-specific
top-level domains (TLD) for all the countries you plan to serve. So your domains might be
`ilovebackpacking.co.uk`

, `ichlieberucksackreisen.de`

, and
`irdemochilero.es`

. This option is beneficial if you want to target the countries that
each TLD is associated with, a method known as geo targeting. Note that this is different from
language targeting, which we will get into a little more later. Let's say your German content is
specifically for users from Germany and not as relevant for German-speaking users in Austria or
Switzerland. In this case, you'd want to register a domain on the `.de`

TLD. German users
will identify your site as a local one they are more likely to trust. On the other hand, it can
be pretty expensive to buy domains on the country-specific TLDs, and it's more of a pain to update
and maintain multiple domains. So if your time and resources are limited, consider buying one
non-country-specific domain, which hosts all the different versions of your website. In this
case, we recommend either of these two options:

-
Put the content of every language in a different subdomain. For our example, you would have
`en.example.com`

,`de.example.com`

, and`es.example.com`

. -
Put the content of every language in a different subdirectory. This is easier to handle when
updating and maintaining your site. For our example, you would have
`example.com/en/`

,`example.com/de/`

, and`example.com/es/`

.

Matt Cutts wrote a substantial post on
[subdirectories and subdomains](https://www.mattcutts.com/blog/subdomains-and-subdirectories/),
which may help you decide which option to go with.

## Geographic targeting vs. Language targeting

As mentioned above, if your content is especially targeted towards a particular region in the
world, you can use the
[Set Geographic Target tool in Webmaster Tools](https://www.google.com/support/webmasters/bin/answer.py?answer=62399).
It allows you to set different geographic targets for different subdirectories or subdomains (for
example, `/de/`

for Germany).

If you want to reach all speakers of a particular language around the world, you probably don't want to limit yourself to a specific geographic location. This is known as language targeting, and in this case, you don't want to use the geographic target tool.

## Content organization

The same content in different languages is not considered duplicate content. Just make sure you keep things organized. If you follow one of the site structure recommendations mentioned above, this should be pretty straightforward. Avoid mixing languages on each page, as this may confuse Googlebot as well as your users. Keep navigation and content in the same language on each page.

If you want to check how many of your pages are recognized in a certain language, you can perform
a language-specific site search. For example, if you go to
[google.de](https://google.de/)
and do a site search on google.com, choose the option below the search box to only display German
results.

If you have more questions on this topic, you can join our
[Webmaster Help Group](https://support.google.com/webmasters/community)
to get more advice.
