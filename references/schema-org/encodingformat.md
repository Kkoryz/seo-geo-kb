---
title: "encodingFormat"
source_url: https://schema.org/encodingFormat
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# encodingFormat

# encodingFormat

A Schema.org Property

- Canonical URL: https://schema.org/encodingFormat
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+encodingFormat)

Media type typically expressed using a MIME format (see


In cases where a


Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.

[IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)and[MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.In cases where a

[CreativeWork](/CreativeWork)has several media type representations,[encoding](/encoding)can be used to indicate each[MediaObject](/MediaObject)alongside particular[encodingFormat](/encodingFormat)information.Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.

### Used on these types


| Supersedes |
|---|
```
``` |

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

[Example 2](#eg-0176)

Copied

Example notes or example HTML without markup.

<img src="png" alt="standards. toothbrushes. don't ask" longdesc="927desc.html">

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<figure itemscope itemtype="https://schema.org/CreativeWork"> <meta itemprop="accessibilityFeature" content="alternativeText"> <meta itemprop="accessibilityFeature" content="longDescription"> <meta itemprop="accessibilityHazard" content="noFlashingHazard"> <meta itemprop="accessibilityHazard" content="noMotionSimulationHazard"> <meta itemprop="encodingFormat" content="image/png"> <img src="png" alt="standards. toothbrushes. don't ask" longdesc="927desc.html"> </figure>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<figure vocab="https://schema.org/" typeof="CreativeWork"> <meta property="accessibilityFeature" content="alternativeText"> <meta property="accessibilityFeature" content="longDescription"> <meta property="accessibilityHazard" content="noFlashingHazard"> <meta property="accessibilityHazard" content="noMotionSimulationHazard"> <meta property="encodingFormat" content="image/png"> <img src="png" alt="standards. toothbrushes. don't ask" longdesc="927desc.html"> </figure>

[Example 3](#eg-0177)

Copied

Example notes or example HTML without markup.

[A basic presentation in HTML]

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<main itemscope itemtype="https://schema.org/CreativeWork"> <meta itemprop="accessibilityHazard" content="flashing"/> <meta itemprop="accessibilityHazard" content="noMotionSimulationHazard"/> <meta itemprop="accessibilityHazard" content="noSoundHazard"/> <meta itemprop="accessibilityFeature" content="longDescription"/> <meta itemprop="accessibilityFeature" content="alternativeText"/> <meta itemprop="encodingFormat" content="text/html"/> <meta itemprop="encodingFormat" content="image/png"/> <meta itemprop="encodingFormat" content="text/css"/> <meta itemprop="encodingFormat" content="text/javascript"/> <meta itemprop="accessibilityAPI" content="ARIA"/> <meta itemprop="accessibilityAPI" content="UIAccessibility"/> <meta itemprop="accessibilityControl" content="fullKeyboardControl"/> <meta itemprop="accessibilityControl" content="fullKeyboardControl"/> <meta itemprop="accessibilityControl" content="fullKeyboardControl"/> <meta itemprop="accessibilityControl" content="fullMouseControl"/> <!--...slide content...--> </main>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CreativeWork"> <meta property="accessibilityHazard" content="flashing"/> <meta property="accessibilityHazard" content="noMotionSimulationHazard"/> <meta property="accessibilityHazard" content="noSoundHazard"/> <meta property="accessibilityFeature" content="longDescription"/> <meta property="accessibilityFeature" content="alternativeText"/> <meta property="encodingFormat" content="text/html"/> <meta property="encodingFormat" content="image/png"/> <meta property="encodingFormat" content="text/css"/> <meta property="encodingFormat" content="text/javascript"/> <meta property="accessibilityAPI" content="ARIA"/> <meta property="accessibilityAPI" content="UIAccessibility"/> <meta property="accessibilityControl" content="fullKeyboardControl"/> <meta property="accessibilityControl" content="fullKeyboardControl"/> <meta property="accessibilityControl" content="fullKeyboardControl"/> <meta property="accessibilityControl" content="fullMouseControl"/> <!--...slide content...--> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org/" , "@type" : "CreativeWork" , "accessibilityHazard" : [ "flashing" , "noSoundHazard" , "noMotionSimulationHazard" ] , "accessibilityFeature" : [ "alternativeText" , "longDescription" ] , "encodingFormat" : [ "text/html" , "image/png" , "text/javascript" , "text/css" ] , "accessibilityAPI" : [ "ARIA" , "UIAccessibility" ], "accessibilityControl" : [ "fullKeyboardControl" , "fullTouchControl" , "fullVoiceControl" , "fullMouseControl" ] } </script>

Structured representation of the JSON-LD example.
