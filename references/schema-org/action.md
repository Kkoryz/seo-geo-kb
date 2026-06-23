---
title: "Action"
source_url: https://schema.org/Action
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Action

# Action

A Schema.org Type

- Canonical URL: https://schema.org/Action
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Action)

An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.


See also

See also

[blog post](https://blog.schema.org/2014/04/16/announcing-schema-org-actions/)and[Actions overview document](https://schema.org/docs/actions.html).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[actionProcess](/actionProcess)

[HowTo](/HowTo)```
```[actionStatus](/actionStatus)

[ActionStatusType](/ActionStatusType)```
```[agent](/agent)

[Organization](/Organization)or[Person](/Person)*John*wrote a book.```
```[endTime](/endTime)

[DateTime](/DateTime)or[Time](/Time)*December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

```
```[error](/error)

[Thing](/Thing)```
```[instrument](/instrument)

[Thing](/Thing)*a pen*.```
```[location](/location)

[Place](/Place)or[PostalAddress](/PostalAddress)or[Text](/Text)or[VirtualLocation](/VirtualLocation)```
```[object](/object)

[Thing](/Thing)*a book*.```
```[participant](/participant)

[Organization](/Organization)or[Person](/Person)*Steve*.```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[result](/result)

[Thing](/Thing)*a book*.```
```[startTime](/startTime)

[DateTime](/DateTime)or[Time](/Time)*January*to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

```
```[target](/target)

[EntryPoint](/EntryPoint)or[URL](/URL)[Thing](/Thing)

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

[Action](/Action)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[InteractionCounter](/InteractionCounter)[LikeAction](/LikeAction). For down votes use[DislikeAction](/DislikeAction). Otherwise, use the most specific Action.[potentialAction](/potentialAction)

[Thing](/Thing)#### More specific Types

-
[AchieveAction](/AchieveAction) -
[AssessAction](/AssessAction) -
[ConsumeAction](/ConsumeAction) -
[ControlAction](/ControlAction) -
[CreateAction](/CreateAction) -
[FindAction](/FindAction) -
[InteractAction](/InteractAction) -
[MoveAction](/MoveAction) -
[OrganizeAction](/OrganizeAction) -
[PlayAction](/PlayAction) -
[SearchAction](/SearchAction) -
[SeekToAction](/SeekToAction) -
[SolveMathAction](/SolveMathAction) -
[TradeAction](/TradeAction) -
[TransferAction](/TransferAction) -
[UpdateAction](/UpdateAction)

### Acknowledgements

Hydra project

[Hydra project](http://purl.org/hydra/)'s community group.

### Examples

[Example 1](#eg-0032)

Copied

Example notes or example HTML without markup.

John listened to Pink with Steve at Anna's apartment on his iPod.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John listened to Pink with Steve at Anna's apartment on his iPod. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ListenAction", "agent": { "@type": "Person", "name": "John" }, "object": { "@type": "MusicGroup", "name": "Pink!" }, "participant": { "@type": "Person", "name": "Steve" }, "location": { "@type": "Residence", "name": "Ann's apartment" }, "instrument": { "@type": "Product", "name": "iPod" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0033)

Copied

Example notes or example HTML without markup.

John created an exercise plan with Steve.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- John created an exercise plan with Steve. --> <script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CreateAction", "agent": { "@type": "Person", "name": "John" }, "result": { "@type": "ExercisePlan", "name": "John's weight loss plan" }, "participant": { "@type": "Person", "name": "Steve" } } </script>

Structured representation of the JSON-LD example.
