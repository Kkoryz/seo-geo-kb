---
title: "ContactPoint"
source_url: https://schema.org/ContactPoint
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ContactPoint

# ContactPoint

A Schema.org Type

- Canonical URL: https://schema.org/ContactPoint
-
Equivalent Class: vcard:VCard

Equivalent Class: fibo-fnd-org-org:ContactPoint

Equivalent Class: gs1:ContactPoint [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ContactPoint)

A contact point—for example, a Customer Complaints department.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[availableLanguage](/availableLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[inLanguage](/inLanguage).```
```[contactOption](/contactOption)

[ContactPointOption](/ContactPointOption)```
```[contactType](/contactType)

[Text](/Text)```
```[email](/email)

[Text](/Text)```
```[faxNumber](/faxNumber)

[Text](/Text)```
```[hoursAvailable](/hoursAvailable)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[productSupported](/productSupported)

[Product](/Product)or[Text](/Text)```
```[telephone](/telephone)

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

[ContactPoint](/ContactPoint)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[JobPosting](/JobPosting)[bccRecipient](/bccRecipient)

[Message](/Message)[ccRecipient](/ccRecipient)

[Message](/Message)[contactPoint](/contactPoint)

[HealthInsurancePlan](/HealthInsurancePlan)or[Organization](/Organization)or[Person](/Person)[contactPoints](/contactPoints)

[Organization](/Organization)or[Person](/Person)[grantee](/grantee)

[DigitalDocumentPermission](/DigitalDocumentPermission)[homeLocation](/homeLocation)

[Person](/Person)[recipient](/recipient)

[AuthorizeAction](/AuthorizeAction)or[CommunicateAction](/CommunicateAction)or[DonateAction](/DonateAction)or[GiveAction](/GiveAction)or[Message](/Message)or[PayAction](/PayAction)or[ReturnAction](/ReturnAction)or[SendAction](/SendAction)or[TipAction](/TipAction)[servicePhone](/servicePhone)

[ServiceChannel](/ServiceChannel)[serviceSmsNumber](/serviceSmsNumber)

[ServiceChannel](/ServiceChannel)[toRecipient](/toRecipient)

[Message](/Message)[workLocation](/workLocation)

[Person](/Person)#### More specific Types

### Examples

[Example 1](#eg-0169)

Copied

Example notes or example HTML without markup.

This example shows a JSON-LD description of services that do not necessarily have a direct human-oriented HTML description. It describes a GovernmentService named "Veterans Affairs Emergency Mental Health", its operator, service area and service details, such as its Veterans Crisis Line (including phone contact line hours of operation, language and other details).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GovernmentService", "name": "Veterans Affairs Emergency Mental Health", "serviceType": "Psychiatric Emergency Services", "serviceOperator": { "@type": "GovernmentOrganization", "name": "US Department of Veterans Affairs" }, "areaServed": { "@type": "AdministrativeArea", "name": "Massachusetts" }, "audience": { "@type": "Audience", "name": "Veterans" }, "availableChannel": { "@type": "ServiceChannel", "name": "Urgent Care Clinic", "availableLanguage": { "@type": "Language", "name": "Spanish", "alternateName": "es" }, "serviceLocation": { "@type": "Hospital", "name": "VA Boston -- West Roxbury", "address": { "@type": "PostalAddress", "streetAddress": "1400 VFW Parkway", "addressLocality": "West Roxbury", "addressRegion": "MA", "postalCode": "02132" } } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0199)

Copied

Example notes or example HTML without markup.

Example specifying one customer service phone number.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Organization", "url" : "http://www.your-company-site.com", "contactPoint" : [ { "@type" : "ContactPoint", "telephone" : "+1-401-555-1212", "contactType" : "customer service" } ] } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0200)

Copied

Example notes or example HTML without markup.

A fuller example that illustrates multiple contact numbers for a company, including US toll-free numbers, a hearing-impaired number, and several contact categories.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Organization", "url" : "http://www.t-mobile.com", "contactPoint" : [ { "@type" : "ContactPoint", "telephone" : "+1-877-746-0909", "contactType" : "customer service", "contactOption" : "TollFree", "areaServed" : "US" } , { "@type" : "ContactPoint", "telephone" : "+1-505-998-3793", "contactType" : "customer service" } , { "@type" : "ContactPoint", "telephone" : "+1-877-296-1018", "contactType" : "customer service", "contactOption" : ["HearingImpairedSupported","TollFree"] , "areaServed" : "US" } , { "@type" : "ContactPoint", "telephone" : "+1-877-453-1304", "contactType" : "technical support", "contactOption" : "TollFree", "areaServed" : ["US","CA"], "availableLanguage" : ["English","French"] } , { "@type" : "ContactPoint", "telephone" : "+1-877-453-1304", "contactType" : "bill payment", "contactOption" : "TollFree", "areaServed" : ["US","CA"] } ] } </script>

Structured representation of the JSON-LD example.
