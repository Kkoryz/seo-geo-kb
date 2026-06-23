---
title: "ProgramMembership"
source_url: https://schema.org/ProgramMembership
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ProgramMembership

# ProgramMembership

A Schema.org Type

- Canonical URL: https://schema.org/ProgramMembership
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ProgramMembership)

Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[hostingOrganization](/hostingOrganization)

[Organization](/Organization)```
```[member](/member)

[Organization](/Organization)or[Person](/Person)[musicGroupMember](/musicGroupMember),[members](/members).Inverse property:

[memberOf](/memberOf)```
```[membershipNumber](/membershipNumber)

[Text](/Text)```
```[membershipPointsEarned](/membershipPointsEarned)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[program](/program)

[MemberProgram](/MemberProgram)[MemberProgram](https://schema.org/MemberProgram)associated with a[ProgramMembership](https://schema.org/ProgramMembership).```
```[programName](/programName)

[Text](/Text)[:program](https://schema.org/program)instead.[Thing](/Thing)

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

[ProgramMembership](/ProgramMembership)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Organization](/Organization)or[Person](/Person)[programMembershipUsed](/programMembershipUsed)

[Reservation](/Reservation)### Examples

[Example 1](#eg-0269)

Copied

Example notes or example HTML without markup.

An email message describing the points earned.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@type": "ProgramMembership", "name": "ACME customer rewards", "membershipPointsEarned": { "@type": "QuantitativeValue", "unitText": "Starpoints", "value": 500 } } </script>

Structured representation of the JSON-LD example.
