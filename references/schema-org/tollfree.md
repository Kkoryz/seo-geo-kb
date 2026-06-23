---
title: "TollFree"
source_url: https://schema.org/TollFree
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# TollFree

# TollFree

A Schema.org Enumeration Member

- Canonical URL: https://schema.org/TollFree
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+TollFree)

The associated telephone number is toll free.

A member value for enumeration type:

[ContactPointOption](/ContactPointOption)

### Examples

[Example 1](#eg-0200)

Copied

Example notes or example HTML without markup.

A fuller example that illustrates multiple contact numbers for a company, including US toll-free numbers, a hearing-impaired number, and several contact categories.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Organization", "url" : "http://www.t-mobile.com", "contactPoint" : [ { "@type" : "ContactPoint", "telephone" : "+1-877-746-0909", "contactType" : "customer service", "contactOption" : "TollFree", "areaServed" : "US" } , { "@type" : "ContactPoint", "telephone" : "+1-505-998-3793", "contactType" : "customer service" } , { "@type" : "ContactPoint", "telephone" : "+1-877-296-1018", "contactType" : "customer service", "contactOption" : ["HearingImpairedSupported","TollFree"] , "areaServed" : "US" } , { "@type" : "ContactPoint", "telephone" : "+1-877-453-1304", "contactType" : "technical support", "contactOption" : "TollFree", "areaServed" : ["US","CA"], "availableLanguage" : ["English","French"] } , { "@type" : "ContactPoint", "telephone" : "+1-877-453-1304", "contactType" : "bill payment", "contactOption" : "TollFree", "areaServed" : ["US","CA"] } ] } </script>

Structured representation of the JSON-LD example.
