---
title: "EducationalAudience"
source_url: https://schema.org/EducationalAudience
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# EducationalAudience

# EducationalAudience

A Schema.org Type

- Canonical URL: https://schema.org/EducationalAudience
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EducationalAudience)

An EducationalAudience.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[educationalRole](/educationalRole)

[Text](/Text)[Audience](/Audience)

```
```[audienceType](/audienceType)

[Text](/Text)```
```[geographicArea](/geographicArea)

[AdministrativeArea](/AdministrativeArea)[Thing](/Thing)

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

[URL](/URL)### Acknowledgements

LRMI project

[lrmi.net](http://lrmi.net)for details.

### Examples

[Example 1](#eg-0379)

Copied

Example notes or example HTML without markup.

<!-- A lesson plan for US second grade teachers. --> <div> <h1>Designing a treasure map</h1> <p>Resource type: lesson plan, learning activity</p> <p>Target audience: teachers</p> <p>Educational level: US Grade 2</p> <p>Link to lesson plan: <a href="http://example.org/lessonplan">http://example.org/lessonplan</a></p> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- A lesson plan for US second grade teachers. --> <div itemscope itemtype="https://schema.org/CreativeWork"> <h1 itemprop="name">Designing a treasure map</h1> <p>Resource type: <span itemprop="learningResourceType">lesson plan</span>, <span itemprop="learningResourceType">learning activity</span> </p> <p>Target audience: <span itemprop="audience" itemscope itemtype="https://schema.org/EducationalAudience"> <span itemprop="educationalRole">teacher</span></span>s. </p> <p itemprop="educationalLevel" itemscope itemtype="https://schema.org/DefinedTerm"> <span itemprop="inDefinedTermSet">US Grade Levels</span> <span itemprop="name">2</span> <link itemprop="url" href="http://purl.org/ASN/scheme/ASNEducationLevel/2" /> </p> <p>Link to lesson plan: <a itemprop="url" href="http://example.org/lessonplan">http://example.org/lessonplan</a></p> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- A list of the issues for a single volume of a given periodical. --> <div vocab="https://schema.org/" typeof="CreativeWork"> <h1 property="name">Designing a treasure map</h1> <p>Resource type: <span property="learningResourceType"> lesson plan</span>, <span property="learningResourceType"> learning activity</span> </p> <p>Target audience: <span rel="audience" typeof="EducationalAudience"> <span property="educationalRole">teacher</span>s </span> </p> <p rel="educationalLevel" typeof="DefinedTerm"> <span property="inDefinedTermSet">US Grade Levels</span> <span property="name">2</span> <span rel="url" resource="http://purl.org/ASN/scheme/ASNEducationLevel/2"></span> </p> <p>Link to lesson plan: <a property="url" href="http://example.org/lessonplan">http://example.org/lessonplan</a></p> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "CreativeWork", "name": "Designing a treasure map", "learningResourceType": [ "lesson plan", "learning activity" ], "audience": { "@type": "EducationalAudience", "educationalRole": "teacher" }, "educationalLevel": { "@type": "DefinedTerm", "inDefinedTermSet": "US Grade Levels", "name": "2", "url": "http://purl.org/ASN/scheme/ASNEducationLevel/2" }, "url": "http://example.org/lessonplan" } </script>

Structured representation of the JSON-LD example.
