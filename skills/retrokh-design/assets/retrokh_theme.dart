// RetroKh: Khmer 1970s print theme for Flutter.
// pubspec.yaml: google_fonts (tested with 6.x and 9.x)
// Usage: MaterialApp(theme: RkTheme.light(), darkTheme: RkTheme.dark(), locale: const Locale('km'))
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

// ───────────────────────── Tokens ─────────────────────────
abstract final class RkColors {
  static const ground = Color(0xFFEADBB8);
  static const paper = Color(0xFFF1E4C6);
  static const sheet = Color(0xFFFBF5E6);
  static const paperMuted = Color(0xFFD9C7A0);
  static const ink = Color(0xFF2A1D14);
  static const inkMuted = Color(0xFF5A4632);
  static const inkFaint = Color(0xFF6E5B45);
  static const red = Color(0xFF9E2F18);
  static const redDeep = Color(0xFF6E1F0F);
  static const turmeric = Color(0xFFE0A526);
  static const turmericLight = Color(0xFFE9B94A);
  static const teal = Color(0xFF245A57);
  static const tealHalftone = Color(0xFF2F6E6A);
  static const plum = Color(0xFF7A3E8E);
  // Night print
  static const night = Color(0xFF1C130D);
  static const nightSheet = Color(0xFFE6DCC4);
  static const nightEdge = Color(0xFF6E5B45);
  static const nightRed = Color(0xFFE2735A);
  static const nightHalftone = Color(0xFF14100C);
  static const scrim = Color(0x8C2A1D14); // rgba(42,29,20,.55)
}

abstract final class RkSize {
  static const touch = 44.0;
  static const touchPrimary = 48.0;
  static const border = 2.0;
  static const zigzag = 14.0;
  static const zigzagPhone = 10.0;
}

/// Hard print shadows: no blur, ever.
abstract final class RkShadow {
  static List<BoxShadow> s1([Color c = RkColors.ink]) =>
      [BoxShadow(color: c, offset: const Offset(3, 3), blurRadius: 0)];
  static List<BoxShadow> s2([Color c = RkColors.ink]) =>
      [BoxShadow(color: c, offset: const Offset(8, 8), blurRadius: 0)];
}

const _kmDigits = '០១២៣៤៥៦៧៨៩';
String toKhmerDigits(Object v) =>
    v.toString().replaceAllMapped(RegExp(r'[0-9]'), (m) => _kmDigits[int.parse(m[0]!)]);

/// Semantic tokens that change with brightness. Read with `RkTokens.of(context)`.
@immutable
class RkTokens extends ThemeExtension<RkTokens> {
  const RkTokens({
    required this.ground,
    required this.surface,
    required this.sheet,
    required this.text,
    required this.textMuted,
    required this.edge,
    required this.shadow,
    required this.accent,
    required this.onAccent,
    required this.primary,
    required this.onPrimary,
    required this.primaryShadow,
    required this.halftoneBase,
    required this.halftoneDot,
  });

  final Color ground, surface, sheet, text, textMuted, edge, shadow;
  final Color accent, onAccent, primary, onPrimary, primaryShadow, halftoneBase, halftoneDot;

  static const light = RkTokens(
    ground: RkColors.ground, surface: RkColors.paper, sheet: RkColors.sheet,
    text: RkColors.ink, textMuted: RkColors.inkMuted, edge: RkColors.ink, shadow: RkColors.ink,
    accent: RkColors.red, onAccent: RkColors.paper,
    primary: RkColors.ink, onPrimary: RkColors.paper, primaryShadow: RkColors.red,
    halftoneBase: RkColors.tealHalftone, halftoneDot: Color(0x40143432),
  );
  static const dark = RkTokens(
    ground: RkColors.night, surface: RkColors.ink, sheet: RkColors.nightSheet,
    text: RkColors.paper, textMuted: RkColors.paperMuted, edge: RkColors.nightEdge, shadow: Color(0xFF000000),
    accent: RkColors.nightRed, onAccent: RkColors.night,
    primary: RkColors.nightRed, onPrimary: RkColors.night, primaryShadow: Color(0xFF000000),
    halftoneBase: RkColors.nightHalftone, halftoneDot: Color(0x592F6E6A),
  );

  static RkTokens of(BuildContext context) => Theme.of(context).extension<RkTokens>() ?? light;

  RkTokens withAccent(Color accent, {Color onAccent = RkColors.paper}) => copyWith(accent: accent, onAccent: onAccent);

  @override
  RkTokens copyWith({
    Color? ground, Color? surface, Color? sheet, Color? text, Color? textMuted, Color? edge, Color? shadow,
    Color? accent, Color? onAccent, Color? primary, Color? onPrimary, Color? primaryShadow,
    Color? halftoneBase, Color? halftoneDot,
  }) =>
      RkTokens(
        ground: ground ?? this.ground, surface: surface ?? this.surface, sheet: sheet ?? this.sheet,
        text: text ?? this.text, textMuted: textMuted ?? this.textMuted, edge: edge ?? this.edge,
        shadow: shadow ?? this.shadow, accent: accent ?? this.accent, onAccent: onAccent ?? this.onAccent,
        primary: primary ?? this.primary, onPrimary: onPrimary ?? this.onPrimary,
        primaryShadow: primaryShadow ?? this.primaryShadow, halftoneBase: halftoneBase ?? this.halftoneBase,
        halftoneDot: halftoneDot ?? this.halftoneDot,
      );

  @override
  RkTokens lerp(RkTokens? other, double t) => t < .5 ? this : (other ?? this);
}

// ───────────────────────── Type ─────────────────────────
abstract final class RkText {
  /// Moul: headings ≥16px only. One weight; never bold.
  static TextStyle display(double size, {Color? color}) =>
      GoogleFonts.moul(fontSize: math.max(16, size), height: 1.6, color: color, fontWeight: FontWeight.w400);

  /// Koulen: numerals, counters, stamps.
  static TextStyle numeral(double size, {Color? color}) =>
      GoogleFonts.koulen(fontSize: size, height: 1.3, color: color, fontWeight: FontWeight.w400);

  /// Battambang: body. 400 / 700.
  static TextStyle body(double size, {Color? color, bool bold = false}) => GoogleFonts.battambang(
      fontSize: size, height: 1.7, color: color, fontWeight: bold ? FontWeight.w700 : FontWeight.w400);

  /// Special Elite: Latin-only eyebrow labels.
  static TextStyle latin({Color? color}) =>
      GoogleFonts.specialElite(fontSize: 12, height: 1.4, letterSpacing: 3, color: color);
}

// ───────────────────────── ThemeData ─────────────────────────
abstract final class RkTheme {
  static ThemeData light({Color accent = RkColors.red}) =>
      _build(Brightness.light, RkTokens.light.withAccent(accent));
  static ThemeData dark() => _build(Brightness.dark, RkTokens.dark);

  static ThemeData _build(Brightness b, RkTokens t) {
    const square = RoundedRectangleBorder(borderRadius: BorderRadius.zero);
    final edge = BorderSide(color: t.edge, width: RkSize.border);
    // Built from TextStyles only, so it works whether google_fonts targets flutter/material or material_ui.
    final textTheme = TextTheme(
      displayLarge: RkText.display(48, color: t.text),
      displayMedium: RkText.display(36, color: t.text),
      headlineLarge: RkText.display(30, color: t.text),
      headlineMedium: RkText.display(26, color: t.text),
      headlineSmall: RkText.display(22, color: t.text),
      titleLarge: RkText.display(20, color: t.text),
      titleMedium: RkText.display(16, color: t.text),
      titleSmall: RkText.body(15, color: t.text, bold: true),
      bodyLarge: RkText.body(16, color: t.text),
      bodyMedium: RkText.body(16, color: t.text),
      bodySmall: RkText.body(14, color: t.textMuted),
      labelLarge: RkText.body(16, color: t.text, bold: true),
      labelMedium: RkText.body(14, color: t.textMuted, bold: true),
      labelSmall: RkText.body(12, color: t.textMuted, bold: true),
    );

    final buttonStyle = ButtonStyle(
      shape: WidgetStatePropertyAll(square.copyWith(side: edge)),
      minimumSize: const WidgetStatePropertyAll(Size(RkSize.touch, RkSize.touch)),
      padding: const WidgetStatePropertyAll(EdgeInsets.symmetric(horizontal: 16)),
      elevation: const WidgetStatePropertyAll(0),
      textStyle: WidgetStatePropertyAll(RkText.body(16, bold: true)),
      splashFactory: NoSplash.splashFactory,
    );

    return ThemeData(
      useMaterial3: true,
      brightness: b,
      scaffoldBackgroundColor: t.ground,
      canvasColor: t.surface,
      splashFactory: NoSplash.splashFactory,
      colorScheme: ColorScheme(
        brightness: b,
        primary: t.primary, onPrimary: t.onPrimary,
        secondary: RkColors.teal, onSecondary: RkColors.paper,
        tertiary: RkColors.turmeric, onTertiary: RkColors.ink,
        error: t.accent, onError: t.onAccent,
        surface: t.surface, onSurface: t.text,
        surfaceContainerHighest: t.sheet,
        outline: t.edge, shadow: t.shadow, scrim: RkColors.scrim,
      ),
      textTheme: textTheme,
      extensions: [t],
      appBarTheme: AppBarTheme(
        backgroundColor: b == Brightness.light ? RkColors.ink : RkColors.night,
        foregroundColor: RkColors.paper,
        elevation: 0, scrolledUnderElevation: 0, centerTitle: true,
        titleTextStyle: RkText.display(20, color: RkColors.paper),
      ),
      filledButtonTheme: FilledButtonThemeData(style: buttonStyle.copyWith(
        backgroundColor: WidgetStatePropertyAll(t.primary),
        foregroundColor: WidgetStatePropertyAll(t.onPrimary),
        minimumSize: const WidgetStatePropertyAll(Size(RkSize.touchPrimary, RkSize.touchPrimary)),
      )),
      outlinedButtonTheme: OutlinedButtonThemeData(style: buttonStyle.copyWith(
        foregroundColor: WidgetStatePropertyAll(t.text),
        side: WidgetStatePropertyAll(edge),
        textStyle: WidgetStatePropertyAll(RkText.body(16)),
      )),
      textButtonTheme: TextButtonThemeData(style: buttonStyle.copyWith(
        foregroundColor: WidgetStatePropertyAll(t.accent),
        shape: const WidgetStatePropertyAll(square),
      )),
      iconButtonTheme: IconButtonThemeData(style: ButtonStyle(
        shape: WidgetStatePropertyAll(square.copyWith(side: edge)),
        minimumSize: const WidgetStatePropertyAll(Size(RkSize.touch, RkSize.touch)),
      )),
      inputDecorationTheme: InputDecorationTheme(
        filled: true, fillColor: t.sheet,
        hintStyle: RkText.body(16, color: RkColors.inkFaint),
        labelStyle: RkText.body(14, color: RkColors.inkMuted, bold: true),
        contentPadding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
        border: OutlineInputBorder(borderRadius: BorderRadius.zero, borderSide: edge),
        enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.zero, borderSide: edge),
        focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.zero,
            borderSide: BorderSide(color: t.accent, width: 3)),
        errorBorder: OutlineInputBorder(borderRadius: BorderRadius.zero,
            borderSide: BorderSide(color: t.accent, width: RkSize.border)),
      ),
      cardTheme: CardThemeData(
        color: t.sheet, elevation: 0, margin: EdgeInsets.zero, shape: square.copyWith(side: edge)),
      dialogTheme: DialogThemeData(
        backgroundColor: t.sheet, elevation: 0, shape: square.copyWith(side: edge)),
      drawerTheme: DrawerThemeData(
        backgroundColor: RkColors.paper, scrimColor: RkColors.scrim, elevation: 0,
        shape: const RoundedRectangleBorder(), width: 330),
      tabBarTheme: TabBarThemeData(
        labelColor: t.onAccent, unselectedLabelColor: t.text,
        indicator: BoxDecoration(color: t.accent),
        indicatorSize: TabBarIndicatorSize.tab,
        labelStyle: RkText.body(16, bold: true), unselectedLabelStyle: RkText.body(16, bold: true),
        dividerColor: t.edge,
      ),
      snackBarTheme: SnackBarThemeData(
        backgroundColor: RkColors.ink, contentTextStyle: RkText.body(15, color: RkColors.paper),
        shape: const RoundedRectangleBorder(), behavior: SnackBarBehavior.floating, elevation: 0),
      progressIndicatorTheme: ProgressIndicatorThemeData(
        color: t.text, linearTrackColor: RkColors.paper, linearMinHeight: 14),
      dividerTheme: DividerThemeData(color: t.edge, thickness: 2, space: 2),
      checkboxTheme: CheckboxThemeData(
        shape: const RoundedRectangleBorder(), side: edge,
        fillColor: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.selected) ? t.text : t.sheet)),
    );
  }
}

// ───────────────────────── Widgets ─────────────────────────

/// Paper sheet with a 2px edge and a hard 8px (or 3px) shadow.
class RkSheet extends StatelessWidget {
  const RkSheet({super.key, required this.child, this.padding = const EdgeInsets.all(24), this.small = false, this.color});
  final Widget child;
  final EdgeInsetsGeometry padding;
  final bool small;
  final Color? color;

  @override
  Widget build(BuildContext context) {
    final t = RkTokens.of(context);
    return Container(
      padding: padding,
      decoration: BoxDecoration(
        color: color ?? t.sheet,
        border: Border.all(color: t.edge, width: RkSize.border),
        boxShadow: small ? RkShadow.s1(t.shadow) : RkShadow.s2(t.shadow),
      ),
      child: DefaultTextStyle.merge(style: const TextStyle(color: RkColors.ink), child: child),
    );
  }
}

enum RkButtonVariant { primary, system, accent, raised, ghost }

/// Button with a hard offset shadow that "prints down" when pressed.
class RkButton extends StatefulWidget {
  const RkButton({super.key, required this.label, required this.onPressed, this.icon, this.variant = RkButtonVariant.ghost, this.iconOnly = false});
  final String label; // also the semantics label when iconOnly
  final VoidCallback? onPressed;
  final IconData? icon;
  final RkButtonVariant variant;
  final bool iconOnly;

  @override
  State<RkButton> createState() => _RkButtonState();
}

class _RkButtonState extends State<RkButton> {
  bool _down = false;

  @override
  Widget build(BuildContext context) {
    final t = RkTokens.of(context);
    final (Color bg, Color fg, Color? shadow) = switch (widget.variant) {
      RkButtonVariant.primary => (t.primary, t.onPrimary, t.primaryShadow),
      RkButtonVariant.system => (RkColors.teal, RkColors.paper, t.shadow),
      RkButtonVariant.accent => (t.accent, t.onAccent, t.shadow),
      RkButtonVariant.raised => (RkColors.sheet, RkColors.ink, t.shadow),
      RkButtonVariant.ghost => (Colors.transparent, t.text, null),
    };
    final h = widget.variant == RkButtonVariant.primary ? RkSize.touchPrimary : RkSize.touch;
    final enabled = widget.onPressed != null;
    return Semantics(
      button: true, enabled: enabled, label: widget.iconOnly ? widget.label : null,
      child: GestureDetector(
        onTapDown: enabled ? (_) => setState(() => _down = true) : null,
        onTapCancel: () => setState(() => _down = false),
        onTapUp: (_) => setState(() => _down = false),
        onTap: widget.onPressed,
        child: Opacity(
          opacity: enabled ? 1 : .45,
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 60),
            transform: Matrix4.translationValues(_down ? 3 : 0, _down ? 3 : 0, 0),
            constraints: BoxConstraints(minHeight: h, minWidth: widget.iconOnly ? h : 0),
            padding: EdgeInsets.symmetric(horizontal: widget.iconOnly ? 0 : 16),
            decoration: BoxDecoration(
              color: bg,
              border: Border.all(color: widget.variant == RkButtonVariant.primary ? bg : t.edge, width: RkSize.border),
              boxShadow: (_down || shadow == null) ? null : RkShadow.s1(shadow),
            ),
            child: Row(mainAxisSize: MainAxisSize.min, mainAxisAlignment: MainAxisAlignment.center, children: [
              if (widget.icon != null) Icon(widget.icon, size: 18, color: fg),
              if (widget.icon != null && !widget.iconOnly) const SizedBox(width: 6),
              if (!widget.iconOnly)
                Text(widget.label, style: RkText.body(16, color: fg, bold: widget.variant != RkButtonVariant.ghost)),
            ]),
          ),
        ),
      ),
    );
  }
}

/// Rotated rubber stamp. Decorative: repeat its meaning in the parent's semantics.
class RkStamp extends StatelessWidget {
  const RkStamp(this.text, {super.key, this.fail = false});
  final String text;
  final bool fail;

  @override
  Widget build(BuildContext context) {
    final c = fail ? RkTokens.of(context).accent : RkColors.teal;
    return ExcludeSemantics(
      child: Transform.rotate(
        angle: (fail ? -4 : -5) * math.pi / 180,
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: fail ? 10 : 6),
          decoration: BoxDecoration(border: Border.all(color: c, width: fail ? 3 : 2)),
          child: Text(text, style: RkText.numeral(fail ? 20 : 14, color: c).copyWith(height: 1.5)),
        ),
      ),
    );
  }
}

/// Zigzag strip: turmeric teeth on red. Place directly under the ink app bar.
class RkZigzag extends StatelessWidget implements PreferredSizeWidget {
  const RkZigzag({super.key, this.height = RkSize.zigzag});
  final double height;
  @override
  Size get preferredSize => Size.fromHeight(height);
  @override
  Widget build(BuildContext context) =>
      ExcludeSemantics(child: CustomPaint(size: Size(double.infinity, height), painter: _ZigzagPainter()));
}

class _ZigzagPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    canvas.drawRect(Offset.zero & size, Paint()..color = RkColors.red);
    final p = Paint()..color = RkColors.turmeric;
    final path = Path();
    for (double x = -10; x < size.width; x += 20) {
      path
        ..moveTo(x, 0)
        ..lineTo(x + 20, 0)
        ..lineTo(x + 10, math.min(10, size.height))
        ..close();
    }
    canvas.drawPath(path, p);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

/// Halftone backdrop: 8px dot screen on teal (night: on near-black).
class RkHalftone extends StatelessWidget {
  const RkHalftone({super.key, required this.child});
  final Widget child;
  @override
  Widget build(BuildContext context) {
    final t = RkTokens.of(context);
    return CustomPaint(painter: _HalftonePainter(t.halftoneBase, t.halftoneDot), child: child);
  }
}

class _HalftonePainter extends CustomPainter {
  _HalftonePainter(this.base, this.dot);
  final Color base, dot;
  @override
  void paint(Canvas canvas, Size size) {
    canvas.drawRect(Offset.zero & size, Paint()..color = base);
    final p = Paint()..color = dot;
    for (double y = 4; y < size.height; y += 8) {
      for (double x = 4; x < size.width; x += 8) {
        canvas.drawCircle(Offset(x, y), 1.4, p);
      }
    }
  }

  @override
  bool shouldRepaint(covariant _HalftonePainter old) => old.base != base || old.dot != dot;
}

/// Sunburst rays for splash / hero. `origin` is in fractions of the size.
class RkRays extends StatelessWidget {
  const RkRays({super.key, required this.child, this.origin = const Alignment(0, -.24)});
  final Widget child;
  final Alignment origin;
  @override
  Widget build(BuildContext context) => CustomPaint(painter: _RaysPainter(origin), child: child);
}

class _RaysPainter extends CustomPainter {
  _RaysPainter(this.origin);
  final Alignment origin;
  @override
  void paint(Canvas canvas, Size size) {
    final c = origin.alongSize(size);
    final r = size.longestSide * 1.5;
    canvas.drawRect(Offset.zero & size, Paint()..color = RkColors.turmericLight);
    final p = Paint()..color = RkColors.turmeric;
    const step = math.pi / 10; // 18°
    for (int i = 0; i < 20; i++) {
      final a = i * step;
      canvas.drawPath(
        Path()
          ..moveTo(c.dx, c.dy)
          ..lineTo(c.dx + r * math.cos(a), c.dy + r * math.sin(a))
          ..lineTo(c.dx + r * math.cos(a + step / 2), c.dy + r * math.sin(a + step / 2))
          ..close(),
        p,
      );
    }
  }

  @override
  bool shouldRepaint(covariant _RaysPainter old) => old.origin != origin;
}
