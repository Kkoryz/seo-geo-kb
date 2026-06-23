---
title: "description"
source_url: https://schema.org/description
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# description

# description

A Schema.org Property

- Canonical URL: https://schema.org/description
-
Equivalent Property: gs1:description

Equivalent Property: dcterms:description

Equivalent Property: og:description [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+description)

A description of the item.

### Values expected to be one of these types


### Used on these types


#### Sub-properties

### Examples

[Example 1](#eg-0006)

Copied

Example notes or example HTML without markup.

<b>12oclock_girona.mp3</b> Total Time: 0m:15s - Recorded on a terrace of Girona a sunday morning composed by Roger <script type="text/javascript"> var fo = new FlashObject("http://google.com/flash/preview-player.swf", "flashPlayer_719", "358", "16", "6", "#FFFFFF");fo.addVariable("url", "http://media.freesound.org/data/0/previews/719__elmomo__12oclock_girona_preview.mp3");fo.addVariable("autostart", "0");fo.write("flashcontent_719"); </script>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/AudioObject"> <span itemprop="name"><b>12oclock_girona.mp3</b></span> <script type="text/javascript"> var fo = new FlashObject("http://google.com/flash/preview-player.swf", "flashPlayer_719", "358", "16", "6", "#FFFFFF");fo.addVariable("url","http://media.freesound.org/data/0/previews/719__elmomo__12oclock_girona_preview.mp3");fo.addVariable("autostart", "0");fo.write("flashcontent_719"); </script> <meta itemprop="encodingFormat" content="audio/mpeg" /> <meta itemprop="contentUrl" content="http://media.freesound.org/data/0/previews/719__elmomo__12oclock_girona_preview.mp3" /> <span class="description"> <meta itemprop="duration" content="T0M15S" /> <span itemprop="description">Recorded on a terrace of Girona a sunday morning</span> </span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="AudioObject"> <span property="name"><b>12oclock_girona.mp3</b></span> <script type="text/javascript"> var fo = new FlashObject("http://google.com/flash/preview-player.swf", "flashPlayer_719", "358", "16", "6", "#FFFFFF");fo.addVariable("url","http://media.freesound.org/data/0/previews/719__elmomo__12oclock_girona_preview.mp3");fo.addVariable("autostart", "0");fo.write("flashcontent_719"); </script> <meta property="encodingFormat" content="audio/mpeg" /> <meta property="contentUrl" content="http://media.freesound.org/data/0/previews/719__elmomo__12oclock_girona_preview.mp3" /> <span class="description"> <meta property="duration" content="T0M15S" /> <span property="description">Recorded on a terrace of Girona a sunday morning</span> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "AudioObject", "contentUrl": "http://media.freesound.org/data/0/previews/719__elmomo__12oclock_girona_preview.mp3", "description": "Recorded on a terrace of Girona a sunday morning", "duration": "T0M15S", "encodingFormat": "audio/mpeg", "name": "12oclock_girona.mp3" } </script>

Structured representation of the JSON-LD example.
