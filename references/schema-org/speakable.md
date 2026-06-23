---
title: "speakable"
source_url: https://schema.org/speakable
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# speakable

# speakable

A Schema.org Property

- Canonical URL: https://schema.org/speakable
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+speakable)

Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.


The


1.)


2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the


3.) XPaths - addresses content via XPaths (assuming an XML view of the content). Use the


For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this we define a supporting type,

The

*speakable*property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.)

*id-value*URL references - uses*id-value*of an element in the page being annotated. The simplest use of*speakable*has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the

[cssSelector](/cssSelector)property.3.) XPaths - addresses content via XPaths (assuming an XML view of the content). Use the

[xpath](/xpath)property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this we define a supporting type,

[SpeakableSpecification](/SpeakableSpecification)which is defined to be a possible value of the*speakable*property.### Values expected to be one of these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1389](https://github.com/schemaorg/schemaorg/issues/1389)

### Examples

[Example 1](#eg-0237)

Copied

Example notes or example HTML without markup.

An example of 'speakable' markup (JSON-LD only, initially).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "WebPage", "name": "Jane Doe's homepage", "speakable": { "@type": "SpeakableSpecification", "cssSelector": ["headline", "summary"] }, "url": "http://www.janedoe.com" }

Structured representation of the JSON-LD example.

[Example 2](#eg-0238)

Copied

Example notes or example HTML without markup.

An example of speakable markup in Microdata in HTML head section.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!DOCTYPE html> <html> <head rel="home" href="/" itemid="" itemscope itemtype="https://schema.org/SpeakableSpecification"> <title>Example showing complex structures in HTML head</title> <meta itemprop="cssSelector" content=".title" /> <meta itemprop="xpath" content="/html/body/h3" /> </head> <body> <h1 class="title">Complex Microdata in HTML head</h1> <p>...</p> </body> </html>

[Example 3](#eg-0474)

Copied

Example notes or example HTML without markup.

An example of 'speakable' markup (JSON-LD only, initially).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "WebPage", "name": "Jane Doe's homepage", "speakable": [ "#myhead1", "#thesummary"], "url": "http://www.janedoe.com" }

Structured representation of the JSON-LD example.
