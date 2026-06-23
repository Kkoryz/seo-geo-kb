---
title: "GovernmentService"
source_url: https://schema.org/GovernmentService
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# GovernmentService

# GovernmentService

A Schema.org Type

- Canonical URL: https://schema.org/GovernmentService
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+GovernmentService)

A service provided by a government organization, e.g. food stamps, veterans benefits, etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[jurisdiction](/jurisdiction)

[AdministrativeArea](/AdministrativeArea)or[Text](/Text)```
```[serviceOperator](/serviceOperator)

[Organization](/Organization)[Service](/Service)

```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[availableChannel](/availableChannel)

[ServiceChannel](/ServiceChannel)```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[broker](/broker)

[Organization](/Organization)or[Person](/Person)[bookingAgent](/bookingAgent).```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasOfferCatalog](/hasOfferCatalog)

[OfferCatalog](/OfferCatalog)```
```[hoursAvailable](/hoursAvailable)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[isRelatedTo](/isRelatedTo)

[Product](/Product)or[Service](/Service)```
```[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[providerMobility](/providerMobility)

[Text](/Text)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[serviceOutput](/serviceOutput)

[Thing](/Thing)[produces](/produces).```
```[serviceType](/serviceType)

[GovernmentBenefitsType](/GovernmentBenefitsType)or[Text](/Text)```
```[slogan](/slogan)

[Text](/Text)```
```[termsOfService](/termsOfService)

[Text](/Text)or[URL](/URL)[Thing](/Thing)

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

[GovernmentService](/GovernmentService)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[SpecialAnnouncement](/SpecialAnnouncement)### Examples

[Example 1](#eg-0168)

Copied

Example notes or example HTML without markup.

<div> NYC Food Service Establishment Permit, issued by Department of Health and Mental Hygiene. (issued through NYC Food Service Establishment Permit Service; valid in New York for 1 year). </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/GovernmentPermit"> <span itemprop="name">NYC Food Service Establishment Permit</span> <div itemprop="issuedBy" itemscope itemtype="https://schema.org/GovernmentOrganization"> <span itemprop="name">Department of Health and Mental Hygiene"</span> </div> <div itemprop="issuedThrough" itemscope itemtype="https://schema.org/GovernmentService"> <span itemprop="name">NYC Food Service Establishment Permit Service</span> </div> <div itemprop="validIn" itemscope itemtype="https://schema.org/AdministrativeArea"> <span itemprop="name">New York</span> </div> <time itemprop="validFor" datetime="P1Y">1 year</time> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="GovernmentPermit"> <span property="name">NYC Food Service Establishment Permit</span> <div property="issuedBy" typeof="GovernmentOrganization"> <span property="name">Department of Health and Mental Hygiene"</span> </div> <div property="issuedThrough" typeof="GovernmentService"> <span property="name">NYC Food Service Establishment Permit Service</span> </div> <div property="validIn" typeof="AdministrativeArea"> <span property="name">New York</span> </div> <time property="validFor" datetime="P1Y">1 Year</time> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GovernmentPermit", "issuedBy": { "@type": "GovernmentOrganization", "name": "Department of Health and Mental Hygiene\"" }, "issuedThrough": { "@type": "GovernmentService", "name": "NYC Food Service Establishment Permit Service" }, "name": "NYC Food Service Establishment Permit", "validFor": "P1Y", "validIn": { "@type": "AdministrativeArea", "name": "New York" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0169)

Copied

Example notes or example HTML without markup.

This example shows a JSON-LD description of services that do not necessarily have a direct human-oriented HTML description. It describes a GovernmentService named "Veterans Affairs Emergency Mental Health", its operator, service area and service details, such as its Veterans Crisis Line (including phone contact line hours of operation, language and other details).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "GovernmentService", "name": "Veterans Affairs Emergency Mental Health", "serviceType": "Psychiatric Emergency Services", "serviceOperator": { "@type": "GovernmentOrganization", "name": "US Department of Veterans Affairs" }, "areaServed": { "@type": "AdministrativeArea", "name": "Massachusetts" }, "audience": { "@type": "Audience", "name": "Veterans" }, "availableChannel": { "@type": "ServiceChannel", "name": "Urgent Care Clinic", "availableLanguage": { "@type": "Language", "name": "Spanish", "alternateName": "es" }, "serviceLocation": { "@type": "Hospital", "name": "VA Boston -- West Roxbury", "address": { "@type": "PostalAddress", "streetAddress": "1400 VFW Parkway", "addressLocality": "West Roxbury", "addressRegion": "MA", "postalCode": "02132" } } } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0301)

Copied

Example notes or example HTML without markup.

Government benefits coverage for SpecialAnnouncement pertaining to the covid-19 situation.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SpecialAnnouncement", "name": "New Paycheck Protection Program for small business", "text": "Example Administration announces a new loan that helps small businesses keep their workforce employed during the Coronavirus (COVID-19) crisis.", "datePosted": "2020-03-30T08:00", "expires": "2020-04-24T23:59", "category": "https://www.wikidata.org/wiki/Q81068910", "spatialCoverage": { "type": "Country", "name": "US" }, "governmentBenefitsInfo": { "@type": "GovernmentService", "name": "Paycheck Protection Program", "url": "https://www.sba.gov/funding-programs/loans/coronavirus-relief-options/paycheck-protection-program-ppp", "provider": { "@type": "GovernmentOrganization", "name": "US Small Business Administration" }, "serviceType": "https://schema.org/BusinessSupport", "audience": { "@type": "Audience", "name": "Small businesses" } } } </script>

Structured representation of the JSON-LD example.
