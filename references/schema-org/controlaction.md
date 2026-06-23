---
title: "ControlAction"
source_url: https://schema.org/ControlAction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ControlAction

| Property | Expected Type | Description |
Properties from
[Action](/Action) |
```
```[actionProcess](/actionProcess) |
[HowTo](/HowTo) |
Description of the process by which the action was performed.
|
```
```[actionStatus](/actionStatus) |
[ActionStatusType](/ActionStatusType) |
Indicates the current disposition of the Action.
|
```
```[agent](/agent) |
[Organization](/Organization) or
[Person](/Person) |
The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote a book.
|
```
```[endTime](/endTime) |
[DateTime](/DateTime) or
[Time](/Time) |
The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
|
```
```[error](/error) |
[Thing](/Thing) |
For failed actions, more information on the cause of the failure. Consider using the Error type.
|
```
```[instrument](/instrument) |
[Thing](/Thing) |
The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.
|
```
```[location](/location) |
[Place](/Place) or
[PostalAddress](/PostalAddress) or
[Text](/Text) or
[VirtualLocation](/VirtualLocation) |
The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
|
```
```[object](/object) |
[Thing](/Thing) |
The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). E.g. John read *a book*.
|
```
```[participant](/participant) |
[Organization](/Organization) or
[Person](/Person) |
Other co-agents that participated in the action indirectly. E.g. John wrote a book with *Steve*.
|
```
```[provider](/provider) |
[Organization](/Organization) or
[Person](/Person) |
The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
Supersedes
[carrier](/carrier).
|
```
```[result](/result) |
[Thing](/Thing) |
The result produced in the action. E.g. John wrote *a book*.
|
```
```[startTime](/startTime) |
[DateTime](/DateTime) or
[Time](/Time) |
The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
|
```
```[target](/target) |
[EntryPoint](/EntryPoint) or
[URL](/URL) |
Indicates a target EntryPoint, or url, for an Action.
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
