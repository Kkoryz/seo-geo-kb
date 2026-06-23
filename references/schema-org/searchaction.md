---
title: "SearchAction"
source_url: https://schema.org/SearchAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# SearchAction

# SearchAction

A Schema.org Type

- Canonical URL: https://schema.org/SearchAction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SearchAction)

The act of searching for an object.


Related actions:



Related actions:

[FindAction](/FindAction): SearchAction generally leads to a FindAction, but not necessarily.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[query](/query)

[Text](/Text)[Action](/Action)

```
```[actionProcess](/actionProcess)

[HowTo](/HowTo)```
```[actionStatus](/actionStatus)

[ActionStatusType](/ActionStatusType)```
```[agent](/agent)

[Organization](/Organization)or[Person](/Person)*John*wrote a book.```
```[endTime](/endTime)

[DateTime](/DateTime)or[Time](/Time)*December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

```
```[error](/error)

[Thing](/Thing)```
```[instrument](/instrument)

[Thing](/Thing)*a pen*.```
```[location](/location)

[Place](/Place)or[PostalAddress](/PostalAddress)or[Text](/Text)or[VirtualLocation](/VirtualLocation)```
```[object](/object)

[Thing](/Thing)*a book*.```
```[participant](/participant)

[Organization](/Organization)or[Person](/Person)*Steve*.```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[result](/result)

[Thing](/Thing)*a book*.```
```[startTime](/startTime)

[DateTime](/DateTime)or[Time](/Time)*January*to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

```
```[target](/target)

[EntryPoint](/EntryPoint)or[URL](/URL)[Thing](/Thing)

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

[URL](/URL)### Examples

[Example 1](#eg-0138)

Copied

Example notes or example HTML without markup.

John searched for 'What is the answer to life the universe and everything?'.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John searched for 'What is the answer to life the universe and everything?'.--> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SearchAction", "agent": { "@type": "Person", "name": "John" }, "query": "What is the answer to life the universe and everything?" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0139)

Copied

Example notes or example HTML without markup.

John searched for hotels.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John searched for hotels.--> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SearchAction", "agent": { "@type": "Person", "name": "John" }, "query": "Hotels" } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0457)

Copied

Example notes or example HTML without markup.

<p>(A WebSite describing its search options)</p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/WebSite"> <link itemprop="url" href="http://www.example.com/"/> <form itemprop="potentialAction" itemscope itemtype="https://schema.org/SearchAction"> <meta itemprop="target" content="http://example.com/search?q={query}"/> <input itemprop="query" type="text" name="query"/> <input type="submit"/> </form> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="WebSite"> <link property="url" href="http://www.example.com/"/> <form property="potentialAction" typeof="https://schema.org/SearchAction"> <meta property="target" content="http://www.example.com/search?q={query}"/> <input property="query" type="text" name="query"> <input type="submit"> </form> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WebSite", "url": "http://example.com/", "potentialAction": { "@type": "SearchAction", "target": "http://example.com/search?&q={query}", "query": "required" } } </script>

Structured representation of the JSON-LD example.
