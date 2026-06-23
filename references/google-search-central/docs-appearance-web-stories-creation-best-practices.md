---
title: "Best Practices for Creating Web Stories | Google Search Central | Documentation | Google for Developers"
source_url: https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2026-03-02
---

# Best Practices for Creating Web Stories | Google Search Central | Documentation | Google for Developers

# Best practices for creating Web Stories

To keep your readers engaged, follow our best practices for creating
[Web Stories](/search/docs/appearance/enable-web-stories). We recommend
focusing on the critical tasks first. If you have more time, follow the recommended best
practices too.

## Storytelling

Critical storytelling best practices |
|
|---|---|
| Video first | Video is more engaging than text or images. Use as much video as possible, and supplement with images and text. |

### More storytelling best practices

Recommended storytelling best practices |
|
|---|---|
| Bring your perspective | Go beyond the facts. Share your opinions. Be the protagonist of your own story. Make it relatable. |
| Have a narrative arc | Create suspense in your story from one page to another. Bring the user along in the journey by providing context and narrative. Deliver payoff for sticking with you to the end. |

## Design

Critical design best practices |
|
|---|---|
| Reduce your character count | Avoid including multiple pages with walls of text. Consider reducing text to approximately 280 characters per page (the length of a tweet). |
| Don't block text | Make sure text is not blocked by other content on the page. Avoid burned in text; by not using burned in text, you prevent text from being blocked when it gets resized to fit various device sizes. |
| Keep text within bounds | Ensure that all text in your Web Story is visible to the reader. Avoid burned in text; by not using burned in text, you prevent text from overflowing when it gets resized to fit various device sizes. |
| Use animations mindfully | Bring your stories to life with animations. Avoid distracting or repetitive animations which can cause fatigue. |

### More design best practices

Recommended design best practices |
|
|---|---|
| Use Web Stories-specific call to action | When re-creating stories that were originally created for a social platform like Instagram, Snapchat or YouTube, be sure to remove any reader call-to-action specific to a certain platform. Make sure that users are able to follow any actions suggested in your Web Story. |
| Use full bleed videos and images | Include full bleed assets in your stories to create a more immersive experience for readers. |
| Avoid low resolution or distorted images and videos | Use high-quality images, and take care when resizing images to portrait. |
| Add a logo to your cover page | Include a high-resolution logo that represents your brand. |
| Shorten video length | We recommend videos that are less than 15 seconds per page, or 60 seconds maximum. |
| Include audio | Use high-quality audio clips that are at least 5 seconds long with balanced volume, and ensure speech is audible. |
| Consider auto advance for video-only stories | Auto-advanced experience for video-based Web Stories could work well for a laid back experience. |

## SEO

Critical SEO best practices |
|
|---|---|
| Provide high-quality content |
Like any web page, providing high-quality content that is useful and interesting to your
readers the most important thing you can do. Include a complete narrative and follow the
|

`noindex`

attribute in your story; this attribute
blocks Google from indexing the page and prevents it from appearing on Google. Additionally,
add your Web Stories to your sitemap. You can check to see if Google can find your Web
Stories with the [Index Coverage Report](https://support.google.com/webmasters/answer/7440203)and[Sitemaps Report](https://support.google.com/webmasters/answer/7451001)in Search Console.[to itself. For example:](https://amp.dev/documentation/guides-and-tutorials/optimize-and-measure/discovery/)`link rel="canonical"`

`<link rel="canonical" href="https://www.example.com/url/to/webstory.html">`

Make sure that your Web Stories follow the
[AMP story
metadata guidelines](https://amp.dev/documentation/components/amp-story/#metadata-guidelines). Include markup that you would normally include on a web page, such as:

and`title`

`description`

`meta`

tags[Structured data](/search/docs/appearance/structured-data/intro-structured-data)[OGP](https://ogp.me/)-
[Twitter card](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards)

### More SEO best practices

Recommended SEO best practices |
|
|---|---|
| Include structured data |
We recommend
|

We recommend integrating Web Stories into your website, such as linking them from your
home page or category pages where applicable. For example, if your Web Story is about a travel
destination and you have a page that lists all your travel articles, then also link the Web
Stories on that category page. An additional special landing page like
`www.example.com/stories`

(which would then be linked from key pages
like your home page) might also make sense.

[AMP story page attachments](https://amp.dev/documentation/components/amp-story-page-attachment/)can be used to present additional information alongside your Web Story. This can be useful to provide extra detail, deep dives, or onward journeys for the content presented in your Web Story.[captions to your video](https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video)to help readers better understand your story. Avoid captions that are burned into the video to ensure that they don't overlap with other content or flow off the screen.
We recommend that you use semantic HTML to build your Web Story. However, some Web Story editor
tools may instead export a story that formats each slide as a video file that bakes in all
the text into the video. In this case, we recommend that you add the precise text displayed
inside of the video as a `title`

attribute on the
[ amp-video](https://amp.dev/documentation/components/amp-video/?format=stories) element. Again, only do this if you can't use semantic markup in your Web Stories.

[support for landscape displays](https://amp.dev/documentation/examples/style-layout/desktop_and_landscape_mode_support/).## Technical

Critical technical best practices |
|
|---|---|
| Make the story valid |
Web Stories must be valid AMP pages. To avoid invalid AMP issues, test your Story using the
|

`<amp-story> poster-portrait-src`

attribute is at least 640x853px and use an aspect ratio of 3:4.
`<amp-story> publisher-logo-src`

attribute is at least 96x96 px and aspect ratio of 1:1.
### More technical best practices

Recommended technical best practices |
|
|---|---|
Include `og:image`
|
We recommend including `og:image` in your
`<meta>` tags to improve your story's discoverability.
|

## Other resources

[Web Stories on Google](https://creators.google/en-us/content-creation-products/own-your-content/web-stories/): Creator-focused resources to making Web Stories.[Enable Web Stories on Google Search](/search/docs/appearance/enable-web-stories): Developer-oriented guide on building Web Stories that meet the technical guidelines required to appear on Google Search.[AMP stories website](https://amp.dev/about/stories/): Developer-focused Web Stories format capabilities.[Web accessibility](/web/fundamentals/accessibility): Tips to help ensure your Web Story is accessible to all users.[Structured data guidelines](/search/docs/appearance/structured-data/sd-policies): Details on adding structured data to help Google Search understand your content.
