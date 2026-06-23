---
title: "Thing"
source_url: https://schema.org/Thing
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Thing

# Thing

A Schema.org Type

- Canonical URL: https://schema.org/Thing
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Thing)

The most generic type of item.

| Property | Expected Type | Description |
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

[Thing](/Thing)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Certification](/Certification)or[CommunicateAction](/CommunicateAction)or[CreativeWork](/CreativeWork)or[DefinedTerm](/DefinedTerm)or[DefinedTermSet](/DefinedTermSet)or[Event](/Event)[actionOption](/actionOption)

[ChooseAction](/ChooseAction)[aggregateElement](/aggregateElement)

[ItemList](/ItemList)[category](/category)

[ActionAccessSpecification](/ActionAccessSpecification)or[Guide](/Guide)or[Invoice](/Invoice)or[Offer](/Offer)or[PhysicalActivity](/PhysicalActivity)or[Product](/Product)or[Recommendation](/Recommendation)or[Service](/Service)or[SpecialAnnouncement](/SpecialAnnouncement)[characterAttribute](/characterAttribute)

[Game](/Game)or[VideoGameSeries](/VideoGameSeries)[collection](/collection)

[UpdateAction](/UpdateAction)[data](/data)

[InstantaneousEvent](/InstantaneousEvent)[dataFeedElement](/dataFeedElement)

[DataFeed](/DataFeed)[defaultValue](/defaultValue)

[PropertyValueSpecification](/PropertyValueSpecification)[error](/error)

[Action](/Action)[gameItem](/gameItem)

[Game](/Game)or[VideoGameSeries](/VideoGameSeries)[gamePlatform](/gamePlatform)

[VideoGame](/VideoGame)or[VideoGameSeries](/VideoGameSeries)[video games](http://en.wikipedia.org/wiki/Category:Video_game_platforms).[instrument](/instrument)

[Action](/Action)*a pen*.[item](/item)

[DataFeedItem](/DataFeedItem)or[ListItem](/ListItem)[itemListElement](/itemListElement)

[ItemList](/ItemList)Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.

Note: The order of elements in your mark-up is not sufficient for indicating the order or elements. Use ListItem with a 'position' property in such cases.

[itemReviewed](/itemReviewed)

[AggregateRating](/AggregateRating)or[Review](/Review)[knowsAbout](/knowsAbout)

[Organization](/Organization)or[Person](/Person)[Person](/Person), and less typically of an[Organization](/Organization), to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or[JobPosting](/JobPosting)descriptions.[mainEntity](/mainEntity)

[CreativeWork](/CreativeWork)[mentions](/mentions)

[CreativeWork](/CreativeWork)[object](/object)

[Action](/Action)*a book*.[observationAbout](/observationAbout)

[Observation](/Observation)[observationAbout](/observationAbout)property identifies an entity, often a[Place](/Place), associated with an[Observation](/Observation).[option](/option)

[ChooseAction](/ChooseAction)[owns](/owns)

[Organization](/Organization)or[Person](/Person)[produces](/produces)

[Service](/Service)[quest](/quest)

[Game](/Game)or[VideoGameSeries](/VideoGameSeries)[replacee](/replacee)

[ReplaceAction](/ReplaceAction)[replacer](/replacer)

[ReplaceAction](/ReplaceAction)[requiredCollateral](/requiredCollateral)

[LoanOrCredit](/LoanOrCredit)[reservationFor](/reservationFor)

[Reservation](/Reservation)[result](/result)

[Action](/Action)*a book*.[serviceOutput](/serviceOutput)

[Service](/Service)[source](/source)

[InstantaneousEvent](/InstantaneousEvent)[targetCollection](/targetCollection)

[UpdateAction](/UpdateAction)#### More specific Types

-
[Action](/Action) -
[BioChemEntity](/BioChemEntity) -
[CreativeWork](/CreativeWork) -
[Event](/Event) -
[Intangible](/Intangible) -
[MedicalEntity](/MedicalEntity) -
[Organization](/Organization) -
[Person](/Person) -
[Place](/Place) -
[Product](/Product) -
[Taxon](/Taxon)

### Examples

[Example 1](#eg-0246)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Thing", "name": "Schema.org Ontology", "subjectOf": { "@type": "Book", "name": "The Complete History of Schema.org" } } </script>

Structured representation of the JSON-LD example.
