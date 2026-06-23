---
title: "Video Schema: What It Is & How to Implement It"
source_url: https://www.semrush.com/blog/video-schema/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2023-11-03
---

# Video Schema: What It Is & How to Implement It

## What Is Video Schema?

Video schema markup is code that helps search engines understand and display your video content in search results.

Adding video schema markup to your webpages supplies additional details about your videos. For example, the title, description, thumbnail, video duration, and upload date.

Google uses this information to generate rich results. Here is an example:

In this example, Google shows the thumbnail, title, description, upload date, and uploader information.

This feature makes the video result stand out on search engine results pages (SERPs) and often generates more clicks.

In this post, you’ll learn everything you need to know about using video schema markup.

Let’s get started.

## What Are the Benefits of Using Video Schema?

Using video schema is not a direct ranking factor. But it provides indirect SEO benefits.

Video schema markup makes your video eligible for an immersive, rich snippet format. This often includes a thumbnail, the video duration, and other relevant information. It stands out more than standard search results.

When users see these rich snippets, they are more likely to click. This can improve your overall click-through rate (CTR).

For example, see this video in a rich snippet format:

Compare it to the plain blue link result:

Which would you click? Probably the first one.

Another benefit of video schema is that it helps Google understand your video’s content. This may make it more likely that Google will rank your video for relevant search queries.

## Examples of Schema Markup for Videos

Video schema markup comes in different forms. But they all use VideoObject schema as the foundation.

VideoObject schema marks up your video and defines its properties. It can appear as JSON-LD or Microdata. JSON-LD is placed inside a <script> element that can go anywhere on the webpage. Microdata relies on specific HTML tags to embed structured data in the code.

Google supports both formats but prefers JSON-LD, so that’s what we’ll focus on here.

Below are examples showing how different properties change your video’s appearance in search results.

### Standard Video

This screenshot shows a video result that uses standard VideoObject schema:

Here is the markup code powering this snippet:

`<script type = "application/ld+json" > `

{

"@context": "https://schema.org",

"@type": "VideoObject",

"name": "Action Recap: Pakistan vs India",

"description": "Watch the best moments from the Asia Cup 2023 match between Pakistan and India",

"thumbnailUrl": ["https://img1.hotstarext.com/image/upload/f_auto,t_hcdl/sources/r1/cms/prod/9889/1589889-h-655968c7423d"],

"uploadDate": "2023-09-10T15:13:40.000Z",

"duration": "PT0H9M51S",

"embedUrl": "https://www.hotstar.com/in/sports/cricket/asia-cup-2023/708507/match-clips/action-recap-pakistan-vs-india/1540024271",

"regionsAllowed": [{

"@type": "Place",

"name": "IN"

}],

"publication": {

"@type": "BroadcastEvent",

"isLiveBroadcast": false,

"startDate": "2023-09-10T15:13:40.000Z"

}

}

</script>

This markup helps Google display the video in a rich snippet and makes the result stand out.

### Live-Streamed Video

For livestream videos, you can add BroadcastEvent properties to show when a live event is happening. Google then displays a LIVE badge on the video snippet.

Here’s how a snippet using BroadcastEvent properties appears:

Here is sample code:

`<script type="application/ld+json">`

{

"@context": "https://schema.org",

"@type": "VideoObject",

"name": "Super 4s: PAK vs IND",

"description": "Watch live stream of Asia Cup 2023 Super 4s match between Pakistan and India.",

"thumbnailUrl": ["https://img1.hotstarext.com/image/upload/f_auto,t_hcdl/sources/r1/cms/prod/8563/1588563-h-364f2ca5f332"],

"uploadDate": "2023-09-11T07:30:00.000Z",

"embedUrl": "https://www.hotstar.com/in/sports/cricket/super-4s-pakistan-vs-india/1540025325",

"contentUrl": "https://www.hotstar.com/stream/super-4s-pakistan-vs-india",

"regionsAllowed": ["IN"],

"publication": {

"@type": "BroadcastEvent",

"isLiveBroadcast": true,

"startDate": "2023-09-11T07:40:10.000Z"

}

}

</script>

Use this markup for live events such as news programs, award shows, or sports events.

Google recommends calling its indexing API to request crawling when the live video starts and ends. This ensures the LIVE badge appears promptly.

### Video Clips

You can also add Clip properties to indicate important moments in your video. Google can use them to display timestamps and labels.

Here is a snippet example that uses Clip properties:

And here is a sample code:

`<script type="application/ld+json">`

{

"@context": "https://schema.org",

"@type": "VideoObject",

"name": "How to Meditate 🙏🏼",

"description": "Meditation is a practice that can benefit your health and wellness in so many ways.",

"thumbnailUrl": ["https://i.ytimg.com/vi/oq6j9uWrcfg/maxresdefault.jpg"],

"uploadDate": "2016-09-21",

"duration": "PT4M10S",

"embedUrl": "https://www.youtube.com/embed/oq6j9uWrcfg",

"genre": "Howto & Style",

"author": {

"@type": "Person",

"name": "Lavendaire"

},

"interactionStatistic": {

"@type": "InteractionCounter",

"interactionType": { "@type": "WatchAction" },

"userInteractionCount": 2054538

},

"hasPart": [

{

"@type": "Clip",

"name": "Purpose of Meditation",

"startOffset": 30,

"endOffset": 45,

"url": "https://www.youtube.com/watch?v=oq6j9uWrcfg&t=30"

},

{

"@type": "Clip",

"name": "Benefits of Meditation",

"startOffset": 50,

"endOffset": 120,

"url": "https://www.youtube.com/watch?v=oq6j9uWrcfg&t=50"

}

]

}

</script>

This helps users jump to a specific moment in the video directly from Google.

## Recommended and Required Properties for Video Schema

Properties are video attributes you define in markup (e.g., name, thumbnail image source, etc.).

VideoObject supports [many properties](https://schema.org/VideoObject), but not all are necessary. Google says three properties are required for a rich snippet:

**name**: The title or name of the video**thumbnailUrl**: The source of the thumbnail image**uploadDate**: The date when you uploaded the video

Google can’t extract the video’s information if any of these are missing.

Depending on the video type, you may need other properties. This table summarizes all video schema properties. (Properties marked with * are required.)

|
| |
|
|
|
| name* | Name or title of the video |
| thumbnailUrl* | URL of the video thumbnail image |
| uploadDate* | Publish date of the video |
| contentUrl | URL of the actual video file |
| description | Video description |
| duration | Video duration in ISO 8601 format |
| embedUrl | URL of the video player where the video is embedded |
| expires | Expiration date of the video |
| hasPart | Used to nest the Clip properties |
| interactionStatistic | Number of total views the video has |
| regionsAllowed | Places where the video is allowed |
|
| |
| publication* | Used to nest BroadcastEvent properties when the video is live |
| publication.endDate* | Date/time when the live stream ends |
| publication.isLiveBroadcast* | Boolean value that defines if the video is live or has ended |
| publication.startDate* | Date/time when the live stream starts |
|
| |
| name* | Name of the clip |
| startOffset* | Start time for the clip |
| endOffset | End time for the clip |
| url* | URL of the video that points to the starting of the clip |

Learn more from [Google’s documentation on schema markup for videos](https://developers.google.com/search/docs/appearance/structured-data/video#video-object).

## How to Implement Video Schema

Implementing video schema markup is straightforward.

There are multiple ways to do it. The simplest approach is to write the code manually and add it to the webpage.

Here’s how:

### 1. Create the Video Schema Markup Code

Create your video schema markup code in JSON-LD format.

Use a text editor and start with this template:

`<script type="application/ld+json"> `

{

"@context": "https://schema.org/",

"@type": "VideoObject",

"name": "Name of the Video",

"thumbnailUrl": "https://example.com/thumbnail.jpg",

"uploadDate": "2024-01-28"

}

</script>

Change the video name, thumbnail image URL, and upload date to fit your content. Then copy the code.

### 2. Validate Your Schema Markup Code

Visit [Google’s Rich Results Test](https://search.google.com/test/rich-results).

Switch to the "**Code**" mode on the main screen and paste your markup code.

Click the "**Test Code**" button.

After validation, the results will appear:

If there are no errors, the markup is ready for implementation.

### 3. Add the Video Schema Markup Code to the Webpage

Open your content management system (CMS) and find the webpage where you want to add schema markup.

In WordPress, you can follow these steps:

From your WordPress admin dashboard, go to "**Posts**."

Locate the post you want to add schema to.

Then click "**Edit**."

The WordPress block editor will open up.

In the editor, click the "**+**" sign (anywhere in the page) and create a new "**Custom HTML**" block.

Now, paste the code in the HTML box as shown below. And click "**Update**."

### 4. Perform a Rich Results Test

After implementing your markup, test it with the [Rich Results Test](https://search.google.com/test/rich-results). Or you can use [Site Audit](https://www.semrush.com/siteaudit/) to scan for multiple schema types, including video schema.

Create a new project in Site Audit:

Enter your domain and project name, then click "**Create project**."

Follow the setup instructions.

In the last configuration step, you can set a schedule for recurring audits.

Then, click "**Start Site Audit**."

When the audit is complete, go to the "**Issues**" tab and type "structured data" into the search bar.

You’ll then be able to see any problems with your structured data, and you’ll get advice for fixing them.

## Best Practices for Video Schema Markup

Using schema for videos can boost your organic marketing strategy if you implement it correctly.

Here are some best practices for successful video schema implementation:

- Insert keywords naturally in properties like the name and description
- Ensure you have all required properties from Google
- Update the markup code whenever the video changes
- Validate your markup before implementing it
- Audit your site regularly to spot new schema issues
- Verify the thumbnail image link is accessible to Google
- Track the performance of your video rich snippets

## Measuring the Impact of Video Schema on SEO

Video schema can expand your organic reach. But measuring your performance is essential.

Use [Google Search Console](https://search.google.com/search-console) to see how your site’s video results perform.

Go to the "**Performance**" section and click "**Search results**."

Scroll to the table and select “**SEARCH APPEARANCE**.”

The "Videos" row shows how many clicks and impressions you get from video results.

Click "**Videos**" to filter the performance report for video results.

Adjust the date range to see how your video schema implementation performs over time.

Another way to track the impact of video schema is to use [Position Tracking](https://www.semrush.com/position-tracking/).

Go to the Position Tracking tool and click “**Create project**.”

Enter your website domain and click "**Create Project**."

In the "**Targeting**" section, select "**Google**," then choose your device, location, and language. Click "**Continue To Keywords**."

Add the keywords you want to track and click "**Start Tracking**."

After setup, go to the "**Overview**" tab, click "**SERP Features**," and choose "**Video**."

Then select "**SERP Features**" again and set it to "**your-domain.com ranks**."

This view shows all keywords for which your site ranks with a video result.

That's how easy it is to track video schema results using the Position Tracking tool.
