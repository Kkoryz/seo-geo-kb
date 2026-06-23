---
title: "DigitalDocumentPermission"
source_url: https://schema.org/DigitalDocumentPermission
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# DigitalDocumentPermission

# DigitalDocumentPermission

A Schema.org Type

- Canonical URL: https://schema.org/DigitalDocumentPermission
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+DigitalDocumentPermission)

A permission for a particular person or group to access a particular file.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[grantee](/grantee)

[Audience](/Audience)or[ContactPoint](/ContactPoint)or[Organization](/Organization)or[Person](/Person)```
```[permissionType](/permissionType)

[DigitalDocumentPermissionType](/DigitalDocumentPermissionType)[Thing](/Thing)

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

[DigitalDocumentPermission](/DigitalDocumentPermission)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[DigitalDocument](/DigitalDocument)### Examples

[Example 1](#eg-0348)

Copied

Example notes or example HTML without markup.

A digital document everyone can read, but only one person can edit.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@type": "DigitalDocument", "name": "New schema.org types proposal", "author": "Alice", "hasDigitalDocumentPermission": [ { "@type": "DigitalDocumentPermission", "permissionType": "https://schema.org/WritePermission", "grantee": { "@type": "Person", "email": "alice@example.com" } }, { "@type": "DigitalDocumentPermission", "permissionType": "https://schema.org/ReadPermission", "grantee": { "@type": "Audience", "audienceType": "public" } } ] } </script>

Structured representation of the JSON-LD example.
