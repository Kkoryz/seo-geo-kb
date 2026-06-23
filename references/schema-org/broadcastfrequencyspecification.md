---
title: "BroadcastFrequencySpecification"
source_url: https://schema.org/BroadcastFrequencySpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# BroadcastFrequencySpecification

# BroadcastFrequencySpecification

A Schema.org Type

- Canonical URL: https://schema.org/BroadcastFrequencySpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+BroadcastFrequencySpecification)

The frequency in MHz and the modulation used for a particular BroadcastService.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[broadcastFrequencyValue](/broadcastFrequencyValue)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[broadcastSignalModulation](/broadcastSignalModulation)

[QualitativeValue](/QualitativeValue)or[Text](/Text)```
```[broadcastSubChannel](/broadcastSubChannel)

[Text](/Text)[Thing](/Thing)

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

[BroadcastFrequencySpecification](/BroadcastFrequencySpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[BroadcastChannel](/BroadcastChannel)or[BroadcastService](/BroadcastService)#### Source

[https://github.com/schemaorg/schemaorg/issues/1004](https://github.com/schemaorg/schemaorg/issues/1004)

### Examples

[Example 1](#eg-0319)

Copied

Example notes or example HTML without markup.

A radio station on 107.9 FM.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WXKS-FM</span> <span itemprop="broadcastDisplayName">Kiss 108</span> <div itemprop="broadcastFrequency" itemscope itemtype="https://schema.org/BroadcastFrequencySpecification"> <meta itemprop="broadcastFrequencyValue" content="107.9" /> <meta itemprop="broadcastSignalModulation" content="FM" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="BroadcastService"> <span property="name">WXKS-FM</span> <span property="broadcastDisplayName">Kiss 108</span> <div property="broadcastFrequency" typeof="BroadcastFrequencySpecification"> <meta property="broadcastFrequencyValue" content="107.9" /> <meta property="broadcastSignalModulation" content="FM" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name": "WXKS-FM", "broadcastDisplayName": "Kiss 108", "broadcastFrequency": { "@type": "BroadcastFrequencySpecification", "broadcastFrequencyValue": 107.9, "broadcastSignalModulation": "FM" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0320)

Copied

Example notes or example HTML without markup.

A radio station on 1030 AM.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WBZ-AM</span> <span itemprop="broadcastDisplayName">WBZ NewsRadio</span> <div itemprop="broadcastFrequency" itemscope itemtype="https://schema.org/BroadcastFrequencySpecification"> <meta itemprop="broadcastFrequencyValue" content="1030" /> <meta itemprop="broadcastSignalModulation" content="AM" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="BroadcastService"> <span property="name">WBZ-AM</span> <span property="broadcastDisplayName">WBZ NewsRadio</span> <div property="broadcastFrequency" typeof="BroadcastFrequencySpecification"> <meta property="broadcastFrequencyValue" content="1030" /> <meta property="broadcastSignalModulation" content="AM" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name": "WBZ-AM", "broadcastDisplayName": "WBZ NewsRadio", "broadcastFrequency": { "@type": "BroadcastFrequencySpecification", "broadcastFrequencyValue": 1030, "broadcastSignalModulation": "AM" } } </script>

Structured representation of the JSON-LD example.
