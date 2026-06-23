---
title: "ActionAccessSpecification"
source_url: https://schema.org/ActionAccessSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ActionAccessSpecification

# ActionAccessSpecification

A Schema.org Type

- Canonical URL: https://schema.org/ActionAccessSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ActionAccessSpecification)

A set of requirements that must be fulfilled in order to perform an Action.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[availabilityEnds](/availabilityEnds)

[Date](/Date)or[DateTime](/DateTime)or[Time](/Time)```
```[availabilityStarts](/availabilityStarts)

[Date](/Date)or[DateTime](/DateTime)or[Time](/Time)```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[eligibleRegion](/eligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[ineligibleRegion](/ineligibleRegion).```
```[expectsAcceptanceOf](/expectsAcceptanceOf)

[Offer](/Offer)```
```[ineligibleRegion](/ineligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[eligibleRegion](/eligibleRegion).```
```[requiresSubscription](/requiresSubscription)

[Boolean](/Boolean)or[MediaSubscription](/MediaSubscription)`true`

or `false`

(note that an earlier version had 'yes', 'no').
[Thing](/Thing)

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

[ActionAccessSpecification](/ActionAccessSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ConsumeAction](/ConsumeAction)#### Source

[https://github.com/schemaorg/schemaorg/issues/1741](https://github.com/schemaorg/schemaorg/issues/1741)

### Examples

[Example 1](#eg-0253)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "MusicRecording", "potentialAction": { "@type": "ListenAction", "actionAccessibilityRequirement": { "@type": "ActionAccessSpecification", "availabilityStarts": "2017-01-01T00:00", "availabilityEnds": "2017-12-31T00:00", "eligibleRegion": { "@type": "Country", "sameAs": "https://www.wikidata.org/wiki/Q166433", "name": "US" }, "requiresSubscription": { "@type": "MediaSubscription", "name": "ACME streaming music monthly subscription", "authenticator": { "@type": "Organization", "name": "ACME Media" } }, "expectsAcceptanceOf": { "@type": "Offer", "itemOffered": { "@type": "MusicRecording", "name": "Song I want to stream that is only available for streaming after I buy it." } } } } } </script>

Structured representation of the JSON-LD example.
