---
title: "inSupportOf"
source_url: https://schema.org/inSupportOf
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# inSupportOf

- Canonical URL: https://schema.org/inSupportOf
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+inSupportOf)

Qualification, candidature, degree, application that Thesis supports.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0219)

Copied

Example notes or example HTML without markup.

A Thesis. <div> <h1>Asian elephants are essential as seed dispersers in a disturbed tropical forest</h1> <h2> A Thesis</h2> <div>Author: Sekar, Nitin, Ph.D.</div> <div>Course: Conservation Biology</div> <div>School: Princeton University</div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Thesis"> <h1 itemprop="name">Asian elephants are essential as seed dispersers in a disturbed tropical forest</h1> <h2> A Thesis</h2> <div>Author: <span itemprop="author">Sekar, Nitin, Ph.D.</span></div> <div>Course: <span itemprop="inSupportOf">Conservation Biology</span></div> <div>School: <span itemprop="sourceOrganization">Princeton University</span></div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Thesis"> <h1 property="name">Asian elephants are essential as seed dispersers in a disturbed tropical forest</h1> <h2> A Thesis</h2> <div>Author: <span property="author">Sekar, Nitin, Ph.D.</span></div> <div>Course: <span property="inSupportOf">Conservation Biology</span></div> <div>School: <span property="sourceOrganization">Princeton University</span></div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": { "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfa": "http://www.w3.org/ns/rdfa#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "schema": "https://schema.org/", "xsd": "http://www.w3.org/2001/XMLSchema#" }, "@id": "", "rdfa:usesVocabulary": { "@id": "schema:" }, "@type": "schema:Thesis", "schema:author": "Sekar, Nitin, Ph.D.", "schema:inSupportOf": "Conservation Biology", "schema:name": "Asian elephants are essential as seed dispersers in a disturbed tropical forest", "schema:sourceOrganization": "Princeton University" } </script>

Structured representation of the JSON-LD example.
