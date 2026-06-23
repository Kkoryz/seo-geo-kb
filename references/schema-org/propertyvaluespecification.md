---
title: "PropertyValueSpecification"
source_url: https://schema.org/PropertyValueSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PropertyValueSpecification

| Property | Expected Type | Description |
Properties from
[PropertyValueSpecification](/PropertyValueSpecification) |
```
```[defaultValue](/defaultValue) |
[Text](/Text) or
[Thing](/Thing) |
The default value of the input. For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values.
|
```
```[maxValue](/maxValue) |
[Number](/Number) |
The upper value of some characteristic or property.
|
```
```[minValue](/minValue) |
[Number](/Number) |
The lower value of some characteristic or property.
|
```
```[multipleValues](/multipleValues) |
[Boolean](/Boolean) |
Whether multiple values are allowed for the property. Default is false.
|
```
```[readonlyValue](/readonlyValue) |
[Boolean](/Boolean) |
Whether or not a property is mutable. Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form.
|
```
```[stepValue](/stepValue) |
[Number](/Number) |
The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification.
|
```
```[valueMaxLength](/valueMaxLength) |
[Number](/Number) |
Specifies the allowed range for number of characters in a literal value.
|
```
```[valueMinLength](/valueMinLength) |
[Number](/Number) |
Specifies the minimum allowed range for number of characters in a literal value.
|
```
```[valueName](/valueName) |
[Text](/Text) |
Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML's input@name.
|
```
```[valuePattern](/valuePattern) |
[Text](/Text) |
Specifies a regular expression for testing literal values according to the HTML spec.
|
```
```[valueRequired](/valueRequired) |
[Boolean](/Boolean) |
Whether the property must be filled in to complete the action. Default is false.
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
