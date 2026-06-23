---
title: "About Schema.org"
source_url: https://schema.org/docs/faq.html
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# About Schema.org

# About Schema.org

[What is the purpose of schema.org?](faq.html#0)

[Why are Google, Bing, Yandex and Yahoo! collaborating? Aren't you competitors?](faq.html#1)

[There are lots of schemas out there. Why create a new one?](faq.html#2)

[Is schema.org a standards body like the W3C or IETF ?](faq.html#3)

[How does schema.org relate to Facebook Open Graph?](faq.html#4)

[What's coming next? How will schema.org evolve?](faq.html#5)

[How do I mark up my site using this schema?](faq.html#8)

[Why should I add markup? What will I get out of it? How will the data be used?](faq.html#9)

[This is too much work. Why can't you just extract this data automatically?](faq.html#10)

[Do I have to mark up every property?](faq.html#13)

[Why microdata? Why not RDFa or microformats?](faq.html#14)

[Why don't you support other vocabularies such as FOAF, SKOS, etc?](faq.html#15)

[Where can I give feedback, report bugs, etc.?](faq.html#16)

[Where did you get that great domain name?](faq.html#17)

[Under what terms can we reuse this documentation?](faq.html#18)

[Should we write 'https://schema.org' or 'http://schema.org' in our markup?](faq.html#19)

Q:
[What is the purpose of schema.org?]

Schema.org is a joint effort, in the spirit of sitemaps.org, to improve the web by creating a structured data markup schema supported by major search engines. On-page markup helps search engines understand the information on web pages and provide richer search results. A shared markup vocabulary makes easier for webmasters to decide on a markup schema and get the maximum benefit for their efforts. Search engines want to make it easier for people to find relevant information on the web. Markup can also enable new tools and applications that make use of the structure.

Q:
[Why are Google, Bing, Yandex and Yahoo! collaborating? Aren't you competitors?]

Currently, there are many standards and schemas for marking up different types of information on web pages. As a result, it is difficult for webmasters to decide on the most relevant and supported markup standards to use.

Creating a schema supported by all the major search engines makes it easier for webmasters to add markup, which makes it easier for search engines to create rich search features for users.

Q:
[There are lots of schemas out there. Why create a new one?]

Creating a new schema with common support benefits webmasters, search engines and users.

- Webmasters: Schema.org provides webmasters with a single place to go to learn about markup, instead of having to graft together a schema from different sources, each with its own rules, conventions and learning curves.
- Search engines: Schema.org focuses on defining the item types and properties that are most valuable to search engines. This means search engines will get the structured information they need most to improve search.
- Users: When it is easier for webmasters to add markup, and search engines see more of the markup they need, users will end up with better search results and a better experience on the web.

Q:
[Is schema.org a standards body like the W3C or IETF ?]

No.

- Schema.org is a collaboration, in the spirit of sitemaps.org, between Bing, Google, Yahoo! and Yandex to make it easier for webmasters to provide us with data so that we may better direct users to their sites.
- Schema.org is not a formal standards body. Schema.org is simply a site where we document the schemas that several major search engines will support.
- Schema.org is a collaboration between Google, Microsoft, Yahoo! and Yandex - large search engines who will use this marked-up data from web pages. Other sites - not necessarily search engines - might later join.

Q:
[How does schema.org relate to Facebook Open Graph?]

Facebook Open Graph serves its purpose well, but it doesn't provide the detailed information search engines need to improve the user experience. A single web page may have many components, and it may talk about more than one thing. If search engines understand the various components of a page, we can improve our presentation of the data. Even if you mark up your content using the Facebook Open Graph protocol, schema.org provides a mechanism for providing more detail about particular entities on the page.

For example, a page about a band could include any or all of the following:

- A list of albums
- A price for each album
- A list of songs for each album, along with a link to hear samples of each song
- A list of upcoming shows
- Bios of the band members

Q:
[What's coming next? How will schema.org evolve?]

Schema.org is a work in progress which will keep evolving over the next many years. We expect the evolution to come from two major sources.

- As we identify new kinds of structured data that we can use to provide better search results, we will extend schema.org to cover these.
- We strongly encourage schema developers to develop and evangelize their schemas. As these gain traction, we will incorporate them into schema.org.

Q:
[Who is managing schema.org on an ongoing basis? Can other websites join schema.org as partners and help decide what new schemas to support?]

The day to day operations of Schema.org, including decisions regarding the schema, are handled by a steering group, which includes representatives of the founding companies and other experts. See the [about schema.org](about.html) page for more details on how to get involved.

Q:
[Is schema.org available in multiple languages? When is that coming? What languages is the markup available in?]

Schema.org markup can be used on web pages written in any language. The site is currently available in English only, but we plan to translate to other languages soon. The markup, like HTML, is in English.

Q:
[How do I mark up my site using this schema?]

Take a look at the [getting started](gs.html) guide for an overview on microdata and schema.org. Or go to the [schemas](schemas.html) page to start looking at specific item types.

Q:
[Why should I add markup? What will I get out of it? How will the data be used?]

Search engines are using on-page markup in a variety of ways. These projects help you to surface your content more clearly or more prominently in search results. Not every type of information in schema.org will be surfaced in search results — you can refer to each company's documentation to find specific uses — but over time you can expect that more data will be used in more ways. In addition, since the markup is publicly accessible from your web pages, other organizations may find interesting new ways to make use of it as well.

Q:
[This is too much work. Why can't you just extract this data automatically?]

Automated data extraction is great when it works, but it can be error prone because different sites can represent the same information in so many different ways. Markup provides a consistent way for computers to understand the data on a page, and helps search engines display information usefully in search results.

Q:
[I have already added markup in some other format (i.e. microformats, RDFa, data-vocabulary.org, etc). Do I need to change anything on my site?]

If you are already publishing structured data markup and it is already being used by Google, Microsoft, Yandex or Yahoo!, the markup format will generally continue to be supported. Changing to the new markup format could be helpful over time because you will be switching to a standard that is accepted across several companies, but you don't have to do it.

Q:
[My website contains content that is of a type that is unsupported. Are you going to add that type? How do I mark it up in the meantime?]

If you publish content of an unsupported type, you have three options:

- Do nothing (don't mark up the content in any way). However, before you decide to do this, check to see if any of the types supported by schema.org - such as reviews, comments, images, or breadcrumbs - are relevant.
- Use a less-specific markup type. For example, schema.org has no "Professor" type. However, if you have a directory of professors in your university department, you could use the "person" type to mark up the information for every professor in the directory.
- If you are feeling ambitious, use the schema.org
[extension system](extension.html)to define a new type.

Q:
[Do I have to mark up every property?]

It is fine to mark up only some properties of an item - markup is not an all-or-nothing choice. However, marking up as much content as possible helps search engines use your information to present your page to users in the most useful way. As a general rule, you should mark up only the content that is visible to people who visit the web page and not content in hidden div's or other hidden page elements.

Q:
[Why microdata? Why not RDFa or microformats?]

Focusing on microdata seemed like a pragmatic decision at the time. For some time now we have been supporting multiple syntaxes, specifically including RDFa and JSON-LD. There are certain things that are much harder in Microdata, like mixing vocabularies, or inverting the direction of a property relationship. We are also adding code examples in all of these formats.

Q:
[Why don't you support other vocabularies such as FOAF, SKOS, etc?]

In creating schema.org, one of our goals was to create a single place where webmasters could go to figure out how to mark up their content, with reasonable syntax and style consistency across types. This way, webmasters only need to learn one thing rather than having to understand different, often overlapping vocabularies. A lot of the vocabulary on schema.org was inspired by earlier work like Microformats, FOAF, OpenCyc, etc. Many terms in schema.org came through collaborations, and we acknowledge these on the schema.org site rather than by making our markup more complex. See also our [external enumerations](https://blog.schema.org/2012/05/11/schema-org-markup-for-external-lists/) mechanism for handling enumerated lists of entities.

Q:
[Where can I give feedback, report bugs, etc.?]

Please use our [feedback](feedback.html) form.

Q:
[Where did you get that great domain name?]

We have the generosity of the [OpenDomain](http://www.opendomain.org/) project to thank for our domain name. Thanks!

Q:
[Under what terms can we reuse this documentation (and schemas, examples, software)?]

As noted in our [terms of service](https://schema.org/docs/terms.html) document, schema.org schemas
are made available under the [Creative Commons Attribution-ShareAlike License (version 3.0)](http://creativecommons.org/licenses/by-sa/3.0/).
These terms also apply to the supporting [documentation](https://schema.org/docs/documents.html) on this site and
on our [blog](http://blog.schema.org/), as well as to the markup examples used in this site. The software used for our site is also
[available](https://github.com/schemaorg/schemaorg/blob/main/software/SOFTWARE_README.md) for opensource reuse under an
[Apache 2](https://github.com/schemaorg/schemaorg/blob/main/LICENSE) license. If you have feedback on these terms please [get in touch](feedback.html).

Q:
[Should we write ]`'https://schema.org'`

or `'http://schema.org'`

in our markup?

There is a general trend towards using `'https'`

more widely, and you can already write `'https://schema.org'`

in your structured data.
We have migrated the schema.org site itself towards using `https:`

as the default version of the site and our preferred form in examples.
However 'http://schema.org' -based URLs in structured data markup will remain widely understood for the foreseeable future and there should
be no urgency about migrating existing data. This is a lengthy way of saying that both `'https://schema.org'`

and `'http://schema.org'`

are fine.
