---
title: "ReadPermission"
source_url: https://schema.org/ReadPermission
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ReadPermission

# ReadPermission

A Schema.org Enumeration Member

- Canonical URL: https://schema.org/ReadPermission
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ReadPermission)

Permission to read or view the document.

A member value for enumeration type:

[DigitalDocumentPermissionType](/DigitalDocumentPermissionType)

### Examples

[Example 1](#eg-0348)

Copied

Example notes or example HTML without markup.

A digital document everyone can read, but only one person can edit.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@type": "DigitalDocument", "name": "New schema.org types proposal", "author": "Alice", "hasDigitalDocumentPermission": [ { "@type": "DigitalDocumentPermission", "permissionType": "https://schema.org/WritePermission", "grantee": { "@type": "Person", "email": "alice@example.com" } }, { "@type": "DigitalDocumentPermission", "permissionType": "https://schema.org/ReadPermission", "grantee": { "@type": "Audience", "audienceType": "public" } } ] } </script>

Structured representation of the JSON-LD example.
