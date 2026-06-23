---
title: "Schemas"
source_url: https://schema.org/docs/schemas.html
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Schemas

# Schemas

## Organization of Schemas

The schemas are a set of 'types', each associated with a set of properties. The types are arranged in a hierarchy.The vocabulary currently consists of 823 Types, 1529 Properties 19 Datatypes, 96 Enumerations and 535 Enumeration members.

**Browse the full hierarchy in HTML:**

**Look up a term using the Term**

*Finder*:**Or you can jump directly to a commonly used type:**

- Creative works:
[CreativeWork](/CreativeWork),[Book](/Book),[Movie](/Movie),[MusicRecording](/MusicRecording),[Recipe](/Recipe),[TVSeries](/TVSeries)... - Embedded non-text objects:
[AudioObject](/AudioObject),[ImageObject](/ImageObject),[VideoObject](/VideoObject) -
[Event](/Event) [Health and medical types](meddocs.html): notes on the health and medical types under[MedicalEntity](/MedicalEntity).-
[Organization](/Organization) -
[Person](/Person) -
[Place](/Place),[LocalBusiness](/LocalBusiness),[Restaurant](/Restaurant)... -
[Product](/Product),[Offer](/Offer),[AggregateOffer](/AggregateOffer) -
[Review](/Review),[AggregateRating](/AggregateRating) -
[Action](/Action)

See also the

[releases](releases.html)page for recent updates and project history.

We also have a small set of

[primitive data types](../DataType)for numbers, text, etc. More details about the data model, etc. are available

[here](datamodel.html).

Developer information / Download Machine Readable files (RDF, JSON-LD, etc):

## Extensions

As schema.org has grown, we have explored various mechanisms for [community extension](/docs/extension.html) as
a way of adding more detailed descriptive vocabulary that builds on the schema.org core. Some areas of Schema.org were
developed as "named extensions", and have dedicated entry pages. We previously called these "hosted" extensions, but
they are best considered simply as views into a single collection of schema definitions.

### Hosted Sections

For example, via the [auto](/docs/auto.home.html) section there is a property for [emissionsCO2](/emissionsCO2),
and via the [bib](/docs/bib.home.html) section we have a property [publisherImprint](/publisherImprint).
However, from the perspective of a publisher, these are simply schema.org properties.

We have a few of these sections:

**Note**: the 'pending' and 'meta' hosted sections are part of schema.org's schema development process.

We use the '[pending](/docs/pending.home.html)' section as a staging area for new schema.org terms that are under discussion and review.
Implementors and publishers are cautioned that terms in the [pending](/docs/pending.home.html) section
may lack consensus and that terminology and definitions could still change significantly after community and [steering group](/docs/about.html#cgsg) review.
Consumers of schema.org data who encourage use of such terms are *strongly encouraged*
to update implementations and documentation to track any evolving changes, and to share early implementation feedback with the [wider community](http://www.w3.org/community/schemaorg).

The '[meta](/docs/meta.home.html)' section is primarily for vocabulary used internally within schema.org to support technical definitions and
schema.org site functionality. These terms are not intended for general usage in the public Web.

** Attic** is a special area where terms are archived when deprecated from the core and other sections, or removed from

[pending](pending.home.html)as not accepted into the full vocabulary. References to terms in the attic area are not normally displayed unless accessed via the term identifier or via the home page. Implementors and data publishers are cautioned not to use terms in the attic area.

Unlike other core and section terms, these areas may be updated at any time without the need for a full [release](releases.html).

### External Extensions

The schema.org [steering group](about.html#cgsg) does not officially approve external extensions - they are fully independent.
We list here some notable extensions that extend schema.org in interesting and useful ways.

[GS1 Web Vocabulary](http://gs1.org/voc/)([blog post](https://blog-schema.org/2016/02/22/gs1-web-vocabulary-welcoming-the-first-schema-org-external-extension/))[Croissant](https://mlcommons.org/working-groups/data/croissant/)is an open community-built standardized metadata vocabulary for ML datasets.
