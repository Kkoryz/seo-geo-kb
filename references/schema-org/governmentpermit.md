---
title: "GovernmentPermit"
source_url: https://schema.org/GovernmentPermit
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# GovernmentPermit

# GovernmentPermit

A Schema.org Type

- Canonical URL: https://schema.org/GovernmentPermit
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+GovernmentPermit)

A permit issued by a government agency.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[issuedBy](/issuedBy)

[Organization](/Organization)[Permit](/Permit),[Ticket](/Ticket), or[Certification](/Certification).```
```[issuedThrough](/issuedThrough)

[Service](/Service)```
```[permitAudience](/permitAudience)

[Audience](/Audience)```
```[validFor](/validFor)

[Duration](/Duration)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validIn](/validIn)

[AdministrativeArea](/AdministrativeArea)[Permit](/Permit), a[Certification](/Certification), or an[EducationalOccupationalCredential](/EducationalOccupationalCredential).```
```[validUntil](/validUntil)

[Date](/Date)[Thing](/Thing)

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
