---
title: "Role"
source_url: https://schema.org/Role
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Role

# Role

A Schema.org Type

- Canonical URL: https://schema.org/Role
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Role)

Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'.


See also

See also

[blog post](https://blog.schema.org/2014/06/16/introducing-role/).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[endDate](/endDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[roleName](/roleName)

[Text](/Text)or[URL](/URL)[namedPosition](/namedPosition).```
```[startDate](/startDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).[Thing](/Thing)

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

[URL](/URL)#### More specific Types

### Examples

[Example 1](#eg-0203)

Copied

Example notes or example HTML without markup.

A basic Role example in JSON that shows how to qualify the 'member' property by adding an intermediate Role entity.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">Cryptography Users</span> <div itemprop="member" itemscope itemtype="https://schema.org/OrganizationRole"> <div itemprop="member" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Alice</span> </div> <span itemprop="startDate">1977</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Organization"> <span property="name">Cryptography Users</span> <div property="member" typeof="OrganizationRole"> <div property="member" typeof="Person"> <span property="name">Alice</span> </div> <span property="startDate">1977</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Organization", "name": "Cryptography Users", "member": { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "Alice" }, "startDate": "1977" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0204)

Copied

Example notes or example HTML without markup.

A JSON example of an OrganizationRole being used to qualify the 'alumniOf' property (which is inverseOf 'alumni'). Note that we use startDate to indicate when the alumniOf situation began, which was the date of leaving the organization.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Delia Derbyshire</span> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Delia_Derbyshire"> <div itemprop="alumniOf" itemscope itemtype="https://schema.org/OrganizationRole"> <div itemprop="alumniOf" itemscope itemtype="https://schema.org/CollegeOrUniversity"> <span itemprop="name">University of Cambridge</span> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/University_of_Cambridge"> </div> <span itemprop="startDate">1959</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Person"> <span property="name">Delia Derbyshire</span> <link property="sameAs" href="http://en.wikipedia.org/wiki/Delia_Derbyshire"> <div property="alumniOf" typeof="OrganizationRole"> <div property="alumniOf" typeof="CollegeOrUniversity"> <span property="name">University of Cambridge</span> <link property="sameAs" href="http://en.wikipedia.org/wiki/University_of_Cambridge"> </div> <span property="startDate">1959</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "Delia Derbyshire", "sameAs": "http://en.wikipedia.org/wiki/Delia_Derbyshire", "alumniOf": { "@type": "OrganizationRole", "alumniOf": { "@type": "CollegeOrUniversity", "name": "University of Cambridge", "sameAs": "http://en.wikipedia.org/wiki/University_of_Cambridge" }, "startDate": "1959" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0205)

Copied

Example notes or example HTML without markup.

A JSON example of a PerformanceRole, in which the Role represents the acting contribution made by Bill Murray in the film Ghostbusters. The Role entity allows us to additional information, such as the character's name that he played in the film.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Movie"> <span itemprop="name">Ghostbusters</span> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Ghostbusters"/> <div itemprop="actor" itemscope itemtype="https://schema.org/PerformanceRole"> <div itemprop="actor" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Bill Murray</span> </div> <span itemprop="characterName">Dr. Peter Venkman</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Movie"> <span property="name">Ghostbusters</span> <link property="sameAs" href="http://en.wikipedia.org/wiki/Ghostbusters"/> <div property="actor" typeof="PerformanceRole"> <div property="actor" typeof="Person"> <span property="name">Bill Murray</span> </div> <span property="characterName">Dr. Peter Venkman</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Movie", "name": "Ghostbusters", "sameAs": "http://en.wikipedia.org/wiki/Ghostbusters", "actor": { "@type": "PerformanceRole", "actor": { "@type": "Person", "name": "Bill Murray" }, "characterName": "Dr. Peter Venkman" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0206)

Copied

Example notes or example HTML without markup.

A JSON example of an OrganizationRole, showing information about a 'member' of a 'SportsTeam', including time qualfiers (when he began and ended that role).

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/SportsTeam"> <span itemprop="name">San Francisco 49ers</span> <div itemprop="member" itemscope itemtype="https://schema.org/OrganizationRole"> <div itemprop="member" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Joe Montana</span> </div> <span itemprop="startDate">1979</span> <span itemprop="endDate">1992</span> <span itemprop="roleName">Quarterback</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="SportsTeam"> <span property="name">San Francisco 49ers</span> <div property="member" typeof="OrganizationRole"> <div property="member" typeof="https://schema.org/Person"> <span property="name">Joe Montana</span> </div> <span property="startDate">1979</span> <span property="endDate">1992</span> <span property="roleName">Quarterback</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "SportsTeam", "name": "San Francisco 49ers", "member": { "@type": "OrganizationRole", "member": { "@type": "Person", "name": "Joe Montana" }, "startDate": "1979", "endDate": "1992", "roleName": "Quarterback" } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0250)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Albert Einstein", "hasOccupation": [ { "@type": "Role", "hasOccupation": { "@type": "Occupation", "name": "Patent examiner", "occupationalCategory": "23-2099.00" }, "startDate": "1901", "endDate": "1906" }, { "@type": "Occupation", "name": "Professor of Physics", "educationRequirements": "PhD in Physics" } ] } </script>

Structured representation of the JSON-LD example.
