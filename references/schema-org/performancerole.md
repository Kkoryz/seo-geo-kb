---
title: "PerformanceRole"
source_url: https://schema.org/PerformanceRole
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PerformanceRole

# PerformanceRole

A Schema.org Type

- Canonical URL: https://schema.org/PerformanceRole
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PerformanceRole)

A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[characterName](/characterName)

[Text](/Text)[Role](/Role)

```
```[endDate](/endDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[roleName](/roleName)

[Text](/Text)or[URL](/URL)[namedPosition](/namedPosition).```
```[startDate](/startDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).[Thing](/Thing)

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

[Example 1](#eg-0205)

Copied

Example notes or example HTML without markup.

A JSON example of a PerformanceRole, in which the Role represents the acting contribution made by Bill Murray in the film Ghostbusters. The Role entity allows us to additional information, such as the character's name that he played in the film.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Movie"> <span itemprop="name">Ghostbusters</span> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Ghostbusters"/> <div itemprop="actor" itemscope itemtype="https://schema.org/PerformanceRole"> <div itemprop="actor" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Bill Murray</span> </div> <span itemprop="characterName">Dr. Peter Venkman</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Movie"> <span property="name">Ghostbusters</span> <link property="sameAs" href="http://en.wikipedia.org/wiki/Ghostbusters"/> <div property="actor" typeof="PerformanceRole"> <div property="actor" typeof="Person"> <span property="name">Bill Murray</span> </div> <span property="characterName">Dr. Peter Venkman</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Movie", "name": "Ghostbusters", "sameAs": "http://en.wikipedia.org/wiki/Ghostbusters", "actor": { "@type": "PerformanceRole", "actor": { "@type": "Person", "name": "Bill Murray" }, "characterName": "Dr. Peter Venkman" } } </script>

Structured representation of the JSON-LD example.
