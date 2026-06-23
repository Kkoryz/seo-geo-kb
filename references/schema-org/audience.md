---
title: "Audience"
source_url: https://schema.org/Audience
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Audience

# Audience

A Schema.org Type

- Canonical URL: https://schema.org/Audience
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Audience)

Intended audience for an item, i.e. the group for whom the item was created.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[URL](/URL)Instances of

[Audience](/Audience)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CreativeWork](/CreativeWork)or[Event](/Event)or[LodgingBusiness](/LodgingBusiness)or[PlayAction](/PlayAction)or[Product](/Product)or[Service](/Service)[grantee](/grantee)

[DigitalDocumentPermission](/DigitalDocumentPermission)[permitAudience](/permitAudience)

[Permit](/Permit)[recipient](/recipient)

[AuthorizeAction](/AuthorizeAction)or[CommunicateAction](/CommunicateAction)or[DonateAction](/DonateAction)or[GiveAction](/GiveAction)or[Message](/Message)or[PayAction](/PayAction)or[ReturnAction](/ReturnAction)or[SendAction](/SendAction)or[TipAction](/TipAction)[sender](/sender)

[Message](/Message)or[ReceiveAction](/ReceiveAction)[serviceAudience](/serviceAudience)

[Service](/Service)[toRecipient](/toRecipient)

[Message](/Message)[touristType](/touristType)

[TouristAttraction](/TouristAttraction)or[TouristDestination](/TouristDestination)or[TouristTrip](/TouristTrip)#### More specific Types

### Examples

[Example 1](#eg-0301)

Copied

Example notes or example HTML without markup.

Government benefits coverage for SpecialAnnouncement pertaining to the covid-19 situation.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SpecialAnnouncement", "name": "New Paycheck Protection Program for small business", "text": "Example Administration announces a new loan that helps small businesses keep their workforce employed during the Coronavirus (COVID-19) crisis.", "datePosted": "2020-03-30T08:00", "expires": "2020-04-24T23:59", "category": "https://www.wikidata.org/wiki/Q81068910", "spatialCoverage": { "type": "Country", "name": "US" }, "governmentBenefitsInfo": { "@type": "GovernmentService", "name": "Paycheck Protection Program", "url": "https://www.sba.gov/funding-programs/loans/coronavirus-relief-options/paycheck-protection-program-ppp", "provider": { "@type": "GovernmentOrganization", "name": "US Small Business Administration" }, "serviceType": "https://schema.org/BusinessSupport", "audience": { "@type": "Audience", "name": "Small businesses" } } } </script>

Structured representation of the JSON-LD example.
