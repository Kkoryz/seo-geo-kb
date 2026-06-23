---
title: "Language"
source_url: https://schema.org/Language
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Language

# Language

A Schema.org Type

- Canonical URL: https://schema.org/Language
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Language)

Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code tags expressed in

[BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag)can be used via the[alternateName](/alternateName)property. The Language type previously also covered programming languages such as Scheme and Lisp, which are now best represented using[ComputerLanguage](/ComputerLanguage).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[Language](/Language)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ContactPoint](/ContactPoint)or[Course](/Course)or[LodgingBusiness](/LodgingBusiness)or[ServiceChannel](/ServiceChannel)or[TouristAttraction](/TouristAttraction)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[inLanguage](/inLanguage).[inLanguage](/inLanguage)

[BroadcastService](/BroadcastService)or[CommunicateAction](/CommunicateAction)or[CreativeWork](/CreativeWork)or[Event](/Event)or[LinkRole](/LinkRole)or[PronounceableText](/PronounceableText)or[WriteAction](/WriteAction)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[availableLanguage](/availableLanguage).[knowsLanguage](/knowsLanguage)

[Organization](/Organization)or[Person](/Person)[Person](/Person), and less typically of an[Organization](/Organization), to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).[language](/language)

[CommunicateAction](/CommunicateAction)or[WriteAction](/WriteAction)[subtitleLanguage](/subtitleLanguage)

[BroadcastEvent](/BroadcastEvent)or[Movie](/Movie)or[ScreeningEvent](/ScreeningEvent)or[TVEpisode](/TVEpisode)[IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).### Examples

[Example 1](#eg-0169)

Copied

Example notes or example HTML without markup.

This example shows a JSON-LD description of services that do not necessarily have a direct human-oriented HTML description. It describes a GovernmentService named "Veterans Affairs Emergency Mental Health", its operator, service area and service details, such as its Veterans Crisis Line (including phone contact line hours of operation, language and other details).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GovernmentService", "name": "Veterans Affairs Emergency Mental Health", "serviceType": "Psychiatric Emergency Services", "serviceOperator": { "@type": "GovernmentOrganization", "name": "US Department of Veterans Affairs" }, "areaServed": { "@type": "AdministrativeArea", "name": "Massachusetts" }, "audience": { "@type": "Audience", "name": "Veterans" }, "availableChannel": { "@type": "ServiceChannel", "name": "Urgent Care Clinic", "availableLanguage": { "@type": "Language", "name": "Spanish", "alternateName": "es" }, "serviceLocation": { "@type": "Hospital", "name": "VA Boston -- West Roxbury", "address": { "@type": "PostalAddress", "streetAddress": "1400 VFW Parkway", "addressLocality": "West Roxbury", "addressRegion": "MA", "postalCode": "02132" } } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0369)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> We speak: <ul> <li itemprop="availableLanguage" itemscope itemtype="https://schema.org/Language"> <span itemprop="name">English</span> </li> <li itemprop="availableLanguage" itemscope itemtype="https://schema.org/Language"> <span itemprop="name">German</span> </li> </ul> </div>
