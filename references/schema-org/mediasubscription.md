---
title: "MediaSubscription"
source_url: https://schema.org/MediaSubscription
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MediaSubscription

# MediaSubscription

A Schema.org Type

- Canonical URL: https://schema.org/MediaSubscription
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MediaSubscription)

A subscription which allows a user to access media including audio, video, books, etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[authenticator](/authenticator)

[Organization](/Organization)```
```[expectsAcceptanceOf](/expectsAcceptanceOf)

[Offer](/Offer)[Thing](/Thing)

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

[MediaSubscription](/MediaSubscription)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ActionAccessSpecification](/ActionAccessSpecification)or[MediaObject](/MediaObject)`true`

or `false`

(note that an earlier version had 'yes', 'no').
#### Source

[https://github.com/schemaorg/schemaorg/issues/1741](https://github.com/schemaorg/schemaorg/issues/1741)

### Examples

[Example 1](#eg-0253)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "MusicRecording", "potentialAction": { "@type": "ListenAction", "actionAccessibilityRequirement": { "@type": "ActionAccessSpecification", "availabilityStarts": "2017-01-01T00:00", "availabilityEnds": "2017-12-31T00:00", "eligibleRegion": { "@type": "Country", "sameAs": "https://www.wikidata.org/wiki/Q166433", "name": "US" }, "requiresSubscription": { "@type": "MediaSubscription", "name": "ACME streaming music monthly subscription", "authenticator": { "@type": "Organization", "name": "ACME Media" } }, "expectsAcceptanceOf": { "@type": "Offer", "itemOffered": { "@type": "MusicRecording", "name": "Song I want to stream that is only available for streaming after I buy it." } } } } } </script>

Structured representation of the JSON-LD example.
