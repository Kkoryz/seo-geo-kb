---
title: "SpeakableSpecification"
source_url: https://schema.org/SpeakableSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# SpeakableSpecification

# SpeakableSpecification

A Schema.org Type

- Canonical URL: https://schema.org/SpeakableSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SpeakableSpecification)

A SpeakableSpecification indicates (typically via

[xpath](/xpath)or[cssSelector](/cssSelector)) sections of a document that are highlighted as particularly[speakable](/speakable). Instances of this type are expected to be used primarily as values of the[speakable](/speakable)property.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[cssSelector](/cssSelector)

[CssSelectorType](/CssSelectorType)[SpeakableSpecification](/SpeakableSpecification)or[WebPageElement](/WebPageElement). In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".```
```[xpath](/xpath)

[XPathType](/XPathType)[SpeakableSpecification](/SpeakableSpecification)or[WebPageElement](/WebPageElement). In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".[Thing](/Thing)

```
```[additionalType](/additionalType)

[Text](/Text)or[URL](/URL)[style guide](https://schema.org/docs/styleguide.html).```
```[alternateName](/alternateName)

[Text](/Text)```
```[description](/description)

[Text](/Text)or[TextObject](/TextObject)```
```[disambiguatingDescription](/disambiguatingDescription)

[Text](/Text)```
```[identifier](/identifier)

[PropertyValue](/PropertyValue)or[Text](/Text)or[URL](/URL)[Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See[background notes](/docs/datamodel.html#identifierBg)for more details.```
```[image](/image)

[ImageObject](/ImageObject)or[URL](/URL)[URL](/URL)or a fully described[ImageObject](/ImageObject).```
```[mainEntityOfPage](/mainEntityOfPage)

[CreativeWork](/CreativeWork)or[URL](/URL)[background notes](/docs/datamodel.html#mainEntityBackground)for details.Inverse property:

[mainEntity](/mainEntity)```
```[name](/name)

[Text](/Text)```
```[owner](/owner)

[Organization](/Organization)or[Person](/Person)Inverse property:

[owns](/owns)```
```[potentialAction](/potentialAction)

[Action](/Action)```
```[sameAs](/sameAs)

[URL](/URL)```
```[subjectOf](/subjectOf)

[CreativeWork](/CreativeWork)or[Event](/Event)Inverse property:

[about](/about)```
```[url](/url)

[URL](/URL)Instances of

[SpeakableSpecification](/SpeakableSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Article](/Article)or[WebPage](/WebPage)The

*speakable*property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.)

*id-value*URL references - uses*id-value*of an element in the page being annotated. The simplest use of*speakable*has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the

[cssSelector](/cssSelector)property.3.) XPaths - addresses content via XPaths (assuming an XML view of the content). Use the

[xpath](/xpath)property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this we define a supporting type,

[SpeakableSpecification](/SpeakableSpecification)which is defined to be a possible value of the*speakable*property.#### Source

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
