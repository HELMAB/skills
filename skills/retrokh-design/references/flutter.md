# Flutter

Copy `assets/retrokh_theme.dart` into `lib/theme/` and add `google_fonts` to `pubspec.yaml` (tested with 6.x and 9.x). For offline apps,
bundle the four fonts as assets and set `GoogleFonts.config.allowRuntimeFetching = false`.

```dart
MaterialApp(
  theme: RkTheme.light(),              // or RkTheme.light(accent: RkColors.teal)
  darkTheme: RkTheme.dark(),
  locale: const Locale('km'),
  supportedLocales: const [Locale('km'), Locale('en')],
  localizationsDelegates: GlobalMaterialLocalizations.delegates,
  home: const HomePage(),
);
```

## What the file provides

| Symbol | Purpose |
|---|---|
| `RkColors` | Raw palette (paper, ink, red, turmeric, teal, plum, night values) |
| `RkTokens` | `ThemeExtension` with semantic colours; `RkTokens.of(context)`; `withAccent()` |
| `RkShadow.s1/s2` | Hard `BoxShadow`s (offset 3 / 8, blur 0) |
| `RkText.display/numeral/body/latin` | Moul / Koulen / Battambang / Special Elite styles with Khmer-safe heights |
| `RkTheme.light/dark` | Full `ThemeData`: square shapes, zero elevation, no splash, an ink AppBar, 2px borders |
| `RkSheet` | Paper sheet with a 2px edge + 8px (or `small:` 3px) shadow |
| `RkButton` | primary / system / accent / raised / ghost, with the hard shadow and a 3px press translate |
| `RkStamp` | Rotated Koulen stamp (teal saved or red fail), excluded from semantics |
| `RkZigzag` | `PreferredSizeWidget` strip: use as `AppBar(bottom: const RkZigzag())` |
| `RkHalftone`, `RkRays` | Painted backdrops |
| `toKhmerDigits()` | ASCII → Khmer numerals |

## Recipes

```dart
Scaffold(
  appBar: AppBar(
    leading: IconButton(icon: const Icon(Icons.menu), tooltip: 'បើកបញ្ជីឯកសារ', onPressed: openDrawer),
    title: Column(children: [
      const Text('គណិតវិទ្យា'),
      Text('វិទ្យាសាស្ត្រពិត · ${toKhmerDigits(2022)}', style: RkText.body(13, color: RkColors.paperMuted)),
    ]),
    bottom: const RkZigzag(height: RkSize.zigzagPhone),
  ),
  body: RkHalftone(
    child: ListView(padding: const EdgeInsets.fromLTRB(16, 20, 24, 24), children: [
      RkSheet(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text('II.', style: RkText.numeral(20)),
        const SizedBox(height: 10),
        Text('…', style: RkText.body(16)),
      ])),
    ]),
  ),
  bottomNavigationBar: _ReaderNav(current: 133, total: 138),
);
```

Current-item tab in a list:
```dart
Container(
  height: 36, margin: const EdgeInsets.only(left: 12, right: 20), padding: const EdgeInsets.symmetric(horizontal: 12),
  alignment: Alignment.centerLeft,
  decoration: BoxDecoration(color: t.accent, boxShadow: RkShadow.s1()),
  child: Text('២. គណិតវិទ្យា', style: RkText.body(16, color: t.onAccent, bold: true)),
)
```

Ledger key column: a `Container(width: 84, decoration: BoxDecoration(border: Border(right: BorderSide(color: t.accent, width: 2))))`
containing `Text(toKhmerDigits(year), style: RkText.numeral(18, color: t.accent))`.

## Flutter-specific rules

- Material elevation shadows are blurred. Keep `elevation: 0` everywhere and draw the shadows with `RkShadow`.
- Disable ink splashes (the theme sets `NoSplash`). Feedback is the 3px press translate.
- Khmer text: keep `height` ≥1.6, avoid `maxLines: 1` on titles unless you also set `overflow: TextOverflow.ellipsis`,
  and give the line enough height. Never apply `letterSpacing` to Khmer `TextStyle`s.
- Every `IconButton` needs a Khmer `tooltip` (it becomes the semantics label).
- Leave 8px of right and bottom padding around shadowed widgets inside clipping parents (`ListView`, `Card`).
