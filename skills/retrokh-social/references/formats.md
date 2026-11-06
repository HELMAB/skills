# Formats and safe areas

The renderer holds these values in `FORMATS`. Text must stay inside the safe area; backgrounds and art bleed to the edge.

| Format | Size | Keep text inside | File limit used |
|---|---|---|---|
| `youtube-thumbnail` | 1280×720 | 40px margin, clear of the timestamp at bottom right | 2MB |
| `youtube-banner` | 2560×1440 | Centred 1546×423 | 6MB |
| `youtube-shorts-cover` | 1080×1920 | Centred 780×1080 | 20MB |
| `youtube-community` | 1080×1080 | 64px margin | 16MB |
| `tiktok-cover` | 1080×1920 | Centred 780×1080 | 20MB |
| `tiktok-poster` | 1080×1920 | Top 150, right 150, bottom 400, left 60 | 20MB |
| `facebook-post` | 1080×1350 | 64px margin | 30MB |
| `facebook-square` | 1080×1080 | 64px margin | 30MB |
| `facebook-story` | 1080×1920 | Top 260, bottom 340, sides 64 | 30MB |
| `facebook-link` | 1200×630 | 44px margin | 8MB |
| `facebook-event` | 1920×1005 | Top and bottom 70, sides 90 | 30MB |
| `facebook-page-cover` | 1640×924 | Top and bottom 160, sides 90, clear of the profile photo | 30MB |

## How firm these are

Checked in November 2026 against third-party guides. No official YouTube, TikTok or Meta page was consulted, so treat this as
the safest reading of sources that sometimes disagree.

- **Consistent across sources:** the YouTube banner and its safe strip, and 1080×1920 for vertical formats.
- **Sources disagree:**
  - *YouTube thumbnail:* some now recommend 3840×2160 and a higher limit. 1280×720 under 2MB uploads everywhere, so it's the default.
  - *TikTok profile grid:* described as both a 1:1 and a 3:4 crop. The safe area is the centred square, which survives both, and
    its 780px width also clears the buttons on the right.
  - *Facebook page cover:* sizes vary from 851×315 to 1920×1080, and the crop differs by device. 1640×924 keeps the 16:9 mobile
    view, and the safe band is what a wider desktop crop keeps. The profile photo's position is an estimate.
  - *Facebook event:* 1920×1005 is the usual figure, with 1920×1080 in some guides.

Tell the user to preview a page cover and TikTok cover in the platform's own upload screen before publishing.
