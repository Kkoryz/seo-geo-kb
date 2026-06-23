---
title: "PeopleAudience"
source_url: https://schema.org/PeopleAudience
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PeopleAudience

| Property | Expected Type | Description |
Properties from
[PeopleAudience](/PeopleAudience) |
```
```[healthCondition](/healthCondition) |
[MedicalCondition](/MedicalCondition) |
Specifying the health condition(s) of a patient, medical study, or other target audience.
|
```
```[requiredGender](/requiredGender) |
[Text](/Text) |
Audiences defined by a person's gender.
|
```
```[requiredMaxAge](/requiredMaxAge) |
[Integer](/Integer) |
Audiences defined by a person's maximum age.
|
```
```[requiredMinAge](/requiredMinAge) |
[Integer](/Integer) |
Audiences defined by a person's minimum age.
|
```
```[suggestedAge](/suggestedAge) |
[QuantitativeValue](/QuantitativeValue) |
The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
|
```
```[suggestedGender](/suggestedGender) |
[GenderType](/GenderType) or
[Text](/Text) |
The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
|
```
```[suggestedMaxAge](/suggestedMaxAge) |
[Number](/Number) |
Maximum recommended age in years for the audience or user.
|
```
```[suggestedMeasurement](/suggestedMeasurement) |
[QuantitativeValue](/QuantitativeValue) |
A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
|
```
```[suggestedMinAge](/suggestedMinAge) |
[Number](/Number) |
Minimum recommended age in years for the audience or user.
|
Properties from
[Audience](/Audience) |
```
```[audienceType](/audienceType) |
[Text](/Text) |
The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
|
```
```[geographicArea](/geographicArea) |
[AdministrativeArea](/AdministrativeArea) |
The geographic area associated with the audience.
|
Properties from
[Thing](/Thing) |
```
```[additionalType](/additionalType) |
[Text](/Text) or
[URL](/URL) |
An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the
use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org [style guide](https://schema.org/docs/styleguide.html).
|
```
```[alternateName](/alternateName) |
[Text](/Text) |
An alias for the item.
|
```
```[description](/description) |
[Text](/Text) or
[TextObject](/TextObject) |
A description of the item.
|
```
```[disambiguatingDescription](/disambiguatingDescription) |
[Text](/Text) |
A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.
|
```
```[identifier](/identifier) |
[PropertyValue](/PropertyValue) or
[Text](/Text) or
[URL](/URL) |
The identifier property represents any kind of identifier for any kind of [Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.
|
```
```[image](/image) |
[ImageObject](/ImageObject) or
[URL](/URL) |
An image of the item. This can be a [URL](/URL) or a fully described [ImageObject](/ImageObject).
|
```
```[mainEntityOfPage](/mainEntityOfPage) |
[CreativeWork](/CreativeWork) or
[URL](/URL) |
Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.
Inverse property:
[mainEntity](/mainEntity)
|
```
```[name](/name) |
[Text](/Text) |
The name of the item.
|
```
```[owner](/owner) |
[Organization](/Organization) or
[Person](/Person) |
A person or organization who owns this Thing.
Inverse property:
[owns](/owns)
|
```
```[potentialAction](/potentialAction) |
[Action](/Action) |
Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.
|
```
```[sameAs](/sameAs) |
[URL](/URL) |
URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
|
```
```[subjectOf](/subjectOf) |
[CreativeWork](/CreativeWork) or
[Event](/Event) |
A CreativeWork or Event about this Thing.
Inverse property:
[about](/about)
|
```
```[url](/url) |
[URL](/URL) |
URL of the item.
|
