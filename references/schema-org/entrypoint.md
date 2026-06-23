---
title: "EntryPoint"
source_url: https://schema.org/EntryPoint
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# EntryPoint

# EntryPoint

A Schema.org Type

- Canonical URL: https://schema.org/EntryPoint
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EntryPoint)

An entry point, within some Web-based protocol.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[actionApplication](/actionApplication)

[SoftwareApplication](/SoftwareApplication)[application](/application).```
```[actionPlatform](/actionPlatform)

[DigitalPlatformEnumeration](/DigitalPlatformEnumeration)or[Text](/Text)or[URL](/URL)```
```[contentType](/contentType)

[Text](/Text)```
```[encodingType](/encodingType)

[Text](/Text)```
```[httpMethod](/httpMethod)

[Text](/Text)```
```[urlTemplate](/urlTemplate)

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

[EntryPoint](/EntryPoint)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Action](/Action)### Acknowledgements

Hydra project

[Hydra project](http://purl.org/hydra/)'s community group.

### Examples

[Example 1](#eg-0188)

Copied

Example notes or example HTML without markup.

A Restaurant named "Tartine Bakery" with a ViewAction as a potentialAction, with several target endpoints including the simple url http://example.com/player?id=123 and full EntryPoint descriptions for Windows and iOS SoftwareApplication apps.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Restaurant", "name": "Tartine Bakery", "potentialAction": { "@type": "ViewAction", "target": [ "http://www.urbanspoon.com/r/6/92204", { "@type": "EntryPoint", "urlTemplate": "http://api.urbanspoon.com/r/6/92204", "contentType": "application/json+ld" }, "android-app://com.urbanspoon/http/www.urbanspoon.com/r/6/92204", { "@type": "EntryPoint", "urlTemplate": "urbanspoon://r/6/92204", "actionApplication": { "@type": "SoftwareApplication", "@id": "284708449", "name": "Urbanspoon iPhone & iPad App", "operatingSystem": "iOS" } }, { "@type": "EntryPoint", "urlTemplate": "urbanspoon://r/6/92204", "actionApplication": { "@type": "SoftwareApplication", "@id": "5b23b738-bb64-4829-9296-5bcb59bb0d2d", "name": "Windows Phone App", "operatingSystem": "Windows Phone 8" } } ] } } </script>

Structured representation of the JSON-LD example.
