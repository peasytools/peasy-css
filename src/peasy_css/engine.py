"""peasy-css — Pure Python CSS code generator.

15 CSS utilities: gradient, box-shadow, text-shadow, border-radius,
flexbox, grid, animation, transform, filter, transition, media-query,
typography, aspect-ratio, clamp, and glass-morphism.

Zero dependencies. All functions return CSS strings.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

# ── Types ────────────────────────────────────────────────────────────

GradientDirection = Literal[
    "to right",
    "to left",
    "to top",
    "to bottom",
    "to top right",
    "to top left",
    "to bottom right",
    "to bottom left",
]

GradientType = Literal["linear", "radial", "conic"]

FlexDirection = Literal["row", "row-reverse", "column", "column-reverse"]
FlexWrap = Literal["nowrap", "wrap", "wrap-reverse"]
FlexJustify = Literal[
    "flex-start", "flex-end", "center", "space-between", "space-around", "space-evenly"
]
FlexAlign = Literal["flex-start", "flex-end", "center", "stretch", "baseline"]

GridAutoFlow = Literal["row", "column", "dense", "row dense", "column dense"]

TimingFunction = Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"]

FontWeight = Literal["100", "200", "300", "400", "500", "600", "700", "800", "900"]


@dataclass(frozen=True)
class ColorStop:
    """A color stop in a gradient."""

    color: str
    position: str | None = None


@dataclass(frozen=True)
class Shadow:
    """A single shadow layer."""

    x: str = "0px"
    y: str = "4px"
    blur: str = "6px"
    spread: str = "0px"
    color: str = "rgba(0, 0, 0, 0.1)"
    inset: bool = False


@dataclass(frozen=True)
class GridTemplate:
    """CSS Grid template configuration."""

    columns: str = "1fr 1fr 1fr"
    rows: str = "auto"
    gap: str = "1rem"
    auto_flow: GridAutoFlow = "row"


@dataclass(frozen=True)
class Keyframe:
    """A single keyframe step."""

    offset: str  # e.g. "0%", "50%", "100%", "from", "to"
    properties: dict[str, str] = field(default_factory=dict)


# ── Gradient ─────────────────────────────────────────────────────────


def gradient(
    colors: list[str] | list[ColorStop],
    *,
    direction: GradientDirection = "to right",
    gradient_type: GradientType = "linear",
    repeating: bool = False,
) -> str:
    """Generate a CSS gradient value.

    Returns the full ``background`` property value, e.g.:
    ``linear-gradient(to right, #ff0000, #0000ff)``
    """
    stops: list[str] = []
    for c in colors:
        if isinstance(c, ColorStop):
            stops.append(f"{c.color} {c.position}" if c.position else c.color)
        else:
            stops.append(c)

    prefix = "repeating-" if repeating else ""

    if gradient_type == "linear":
        return f"{prefix}linear-gradient({direction}, {', '.join(stops)})"
    if gradient_type == "radial":
        return f"{prefix}radial-gradient(circle, {', '.join(stops)})"
    # conic
    return f"{prefix}conic-gradient({', '.join(stops)})"


def gradient_css(
    selector: str,
    colors: list[str] | list[ColorStop],
    *,
    direction: GradientDirection = "to right",
    gradient_type: GradientType = "linear",
    repeating: bool = False,
) -> str:
    """Generate a complete CSS rule with gradient background."""
    value = gradient(colors, direction=direction, gradient_type=gradient_type, repeating=repeating)
    return f"{selector} {{\n  background: {value};\n}}"


# ── Box Shadow ───────────────────────────────────────────────────────


def box_shadow(*shadows: Shadow) -> str:
    """Generate a ``box-shadow`` CSS value.

    Multiple shadows are comma-separated.
    """
    parts: list[str] = []
    for s in shadows:
        inset = "inset " if s.inset else ""
        parts.append(f"{inset}{s.x} {s.y} {s.blur} {s.spread} {s.color}")
    return ", ".join(parts)


def box_shadow_css(selector: str, *shadows: Shadow) -> str:
    """Generate a complete CSS rule with box-shadow."""
    value = box_shadow(*shadows)
    return f"{selector} {{\n  box-shadow: {value};\n}}"


# ── Text Shadow ──────────────────────────────────────────────────────


def text_shadow(
    x: str = "1px",
    y: str = "1px",
    blur: str = "2px",
    color: str = "rgba(0, 0, 0, 0.3)",
) -> str:
    """Generate a ``text-shadow`` CSS value."""
    return f"{x} {y} {blur} {color}"


def text_shadow_css(
    selector: str,
    x: str = "1px",
    y: str = "1px",
    blur: str = "2px",
    color: str = "rgba(0, 0, 0, 0.3)",
) -> str:
    """Generate a complete CSS rule with text-shadow."""
    value = text_shadow(x, y, blur, color)
    return f"{selector} {{\n  text-shadow: {value};\n}}"


# ── Border Radius ────────────────────────────────────────────────────


def border_radius(
    *,
    top_left: str = "0px",
    top_right: str = "0px",
    bottom_right: str = "0px",
    bottom_left: str = "0px",
) -> str:
    """Generate a ``border-radius`` CSS value (4-corner shorthand)."""
    if top_left == top_right == bottom_right == bottom_left:
        return top_left
    return f"{top_left} {top_right} {bottom_right} {bottom_left}"


def border_radius_css(
    selector: str,
    *,
    top_left: str = "0px",
    top_right: str = "0px",
    bottom_right: str = "0px",
    bottom_left: str = "0px",
) -> str:
    """Generate a complete CSS rule with border-radius."""
    value = border_radius(
        top_left=top_left,
        top_right=top_right,
        bottom_right=bottom_right,
        bottom_left=bottom_left,
    )
    return f"{selector} {{\n  border-radius: {value};\n}}"


# ── Flexbox ──────────────────────────────────────────────────────────


def flexbox(
    *,
    direction: FlexDirection = "row",
    wrap: FlexWrap = "nowrap",
    justify: FlexJustify = "flex-start",
    align: FlexAlign = "stretch",
    gap: str = "0px",
) -> str:
    """Generate flexbox CSS properties as a multi-line block."""
    lines = [
        "display: flex;",
        f"flex-direction: {direction};",
        f"flex-wrap: {wrap};",
        f"justify-content: {justify};",
        f"align-items: {align};",
    ]
    if gap != "0px":
        lines.append(f"gap: {gap};")
    return "\n".join(f"  {line}" for line in lines)


def flexbox_css(
    selector: str,
    *,
    direction: FlexDirection = "row",
    wrap: FlexWrap = "nowrap",
    justify: FlexJustify = "flex-start",
    align: FlexAlign = "stretch",
    gap: str = "0px",
) -> str:
    """Generate a complete CSS rule with flexbox layout."""
    props = flexbox(direction=direction, wrap=wrap, justify=justify, align=align, gap=gap)
    return f"{selector} {{\n{props}\n}}"


# ── Grid ─────────────────────────────────────────────────────────────


def grid(template: GridTemplate | None = None) -> str:
    """Generate CSS Grid properties as a multi-line block."""
    t = template or GridTemplate()
    lines = [
        "display: grid;",
        f"grid-template-columns: {t.columns};",
        f"grid-template-rows: {t.rows};",
        f"gap: {t.gap};",
    ]
    if t.auto_flow != "row":
        lines.append(f"grid-auto-flow: {t.auto_flow};")
    return "\n".join(f"  {line}" for line in lines)


def grid_css(selector: str, template: GridTemplate | None = None) -> str:
    """Generate a complete CSS rule with grid layout."""
    props = grid(template)
    return f"{selector} {{\n{props}\n}}"


# ── Animation / Keyframes ────────────────────────────────────────────


def animation(
    name: str,
    duration: str = "1s",
    timing: TimingFunction = "ease",
    delay: str = "0s",
    iteration: str = "1",
    direction: str = "normal",
    fill_mode: str = "none",
) -> str:
    """Generate an ``animation`` CSS shorthand value."""
    return f"{name} {duration} {timing} {delay} {iteration} {direction} {fill_mode}"


def keyframes(name: str, frames: list[Keyframe]) -> str:
    """Generate a ``@keyframes`` CSS block."""
    lines = [f"@keyframes {name} {{"]
    for frame in frames:
        props = "; ".join(f"{k}: {v}" for k, v in frame.properties.items())
        lines.append(f"  {frame.offset} {{ {props}; }}")
    lines.append("}")
    return "\n".join(lines)


def animation_css(
    selector: str,
    name: str,
    duration: str = "1s",
    timing: TimingFunction = "ease",
    delay: str = "0s",
    iteration: str = "1",
    direction: str = "normal",
    fill_mode: str = "none",
) -> str:
    """Generate a CSS rule with animation shorthand."""
    value = animation(name, duration, timing, delay, iteration, direction, fill_mode)
    return f"{selector} {{\n  animation: {value};\n}}"


# ── Transform ────────────────────────────────────────────────────────


def transform(
    *,
    translate_x: str = "0",
    translate_y: str = "0",
    rotate: str = "0deg",
    scale_x: str = "1",
    scale_y: str = "1",
    skew_x: str = "0deg",
    skew_y: str = "0deg",
) -> str:
    """Generate a ``transform`` CSS value."""
    parts: list[str] = []
    if translate_x != "0" or translate_y != "0":
        parts.append(f"translate({translate_x}, {translate_y})")
    if rotate != "0deg":
        parts.append(f"rotate({rotate})")
    if scale_x != "1" or scale_y != "1":
        parts.append(f"scale({scale_x}, {scale_y})")
    if skew_x != "0deg" or skew_y != "0deg":
        parts.append(f"skew({skew_x}, {skew_y})")
    return " ".join(parts) if parts else "none"


def transform_css(selector: str, **kwargs: str) -> str:
    """Generate a complete CSS rule with transform."""
    value = transform(**kwargs)
    return f"{selector} {{\n  transform: {value};\n}}"


# ── Filter ───────────────────────────────────────────────────────────


def css_filter(
    *,
    blur: str = "0px",
    brightness: str = "100%",
    contrast: str = "100%",
    grayscale: str = "0%",
    hue_rotate: str = "0deg",
    invert: str = "0%",
    opacity: str = "100%",
    saturate: str = "100%",
    sepia: str = "0%",
) -> str:
    """Generate a ``filter`` CSS value from individual filter functions."""
    parts: list[str] = []
    if blur != "0px":
        parts.append(f"blur({blur})")
    if brightness != "100%":
        parts.append(f"brightness({brightness})")
    if contrast != "100%":
        parts.append(f"contrast({contrast})")
    if grayscale != "0%":
        parts.append(f"grayscale({grayscale})")
    if hue_rotate != "0deg":
        parts.append(f"hue-rotate({hue_rotate})")
    if invert != "0%":
        parts.append(f"invert({invert})")
    if opacity != "100%":
        parts.append(f"opacity({opacity})")
    if saturate != "100%":
        parts.append(f"saturate({saturate})")
    if sepia != "0%":
        parts.append(f"sepia({sepia})")
    return " ".join(parts) if parts else "none"


def filter_css(selector: str, **kwargs: str) -> str:
    """Generate a complete CSS rule with filter."""
    value = css_filter(**kwargs)
    return f"{selector} {{\n  filter: {value};\n}}"


# ── Transition ───────────────────────────────────────────────────────


def transition(
    property: str = "all",
    duration: str = "0.3s",
    timing: TimingFunction = "ease",
    delay: str = "0s",
) -> str:
    """Generate a ``transition`` CSS shorthand value."""
    return f"{property} {duration} {timing} {delay}"


def transition_css(
    selector: str,
    property: str = "all",
    duration: str = "0.3s",
    timing: TimingFunction = "ease",
    delay: str = "0s",
) -> str:
    """Generate a complete CSS rule with transition."""
    value = transition(property, duration, timing, delay)
    return f"{selector} {{\n  transition: {value};\n}}"


# ── Media Query ──────────────────────────────────────────────────────


def media_query(
    breakpoint: str,
    css_block: str,
    *,
    type: str = "min-width",
) -> str:
    """Wrap CSS in a media query.

    Example::

        media_query("768px", ".container { width: 100%; }")
        # → @media (min-width: 768px) { .container { width: 100%; } }
    """
    indented = "\n".join(f"  {line}" for line in css_block.strip().split("\n"))
    return f"@media ({type}: {breakpoint}) {{\n{indented}\n}}"


# ── Typography ───────────────────────────────────────────────────────


def typography(
    *,
    font_family: str = "system-ui, -apple-system, sans-serif",
    font_size: str = "1rem",
    font_weight: FontWeight = "400",
    line_height: str = "1.5",
    letter_spacing: str = "normal",
    text_transform: str = "none",
) -> str:
    """Generate typography CSS properties as a multi-line block."""
    lines = [
        f"font-family: {font_family};",
        f"font-size: {font_size};",
        f"font-weight: {font_weight};",
        f"line-height: {line_height};",
    ]
    if letter_spacing != "normal":
        lines.append(f"letter-spacing: {letter_spacing};")
    if text_transform != "none":
        lines.append(f"text-transform: {text_transform};")
    return "\n".join(f"  {line}" for line in lines)


def typography_css(selector: str, **kwargs: str) -> str:
    """Generate a complete CSS rule with typography."""
    props = typography(**kwargs)  # type: ignore[arg-type]
    return f"{selector} {{\n{props}\n}}"


# ── Aspect Ratio ─────────────────────────────────────────────────────


def aspect_ratio(ratio: str = "16 / 9") -> str:
    """Generate an ``aspect-ratio`` CSS value."""
    return ratio


def aspect_ratio_css(selector: str, ratio: str = "16 / 9") -> str:
    """Generate a CSS rule with aspect-ratio."""
    return f"{selector} {{\n  aspect-ratio: {ratio};\n}}"


# ── Clamp ────────────────────────────────────────────────────────────


def clamp(min_val: str, preferred: str, max_val: str) -> str:
    """Generate a CSS ``clamp()`` value for fluid typography/spacing."""
    return f"clamp({min_val}, {preferred}, {max_val})"


def clamp_font_css(
    selector: str,
    min_size: str = "1rem",
    preferred: str = "2.5vw",
    max_size: str = "2rem",
) -> str:
    """Generate a CSS rule with fluid font-size using clamp()."""
    value = clamp(min_size, preferred, max_size)
    return f"{selector} {{\n  font-size: {value};\n}}"


# ── Glass Morphism ───────────────────────────────────────────────────


def glassmorphism(
    *,
    blur: str = "10px",
    background: str = "rgba(255, 255, 255, 0.25)",
    border_color: str = "rgba(255, 255, 255, 0.18)",
    border_width: str = "1px",
) -> str:
    """Generate glassmorphism CSS properties as a multi-line block."""
    lines = [
        f"background: {background};",
        f"backdrop-filter: blur({blur});",
        f"-webkit-backdrop-filter: blur({blur});",
        f"border: {border_width} solid {border_color};",
    ]
    return "\n".join(f"  {line}" for line in lines)


def glassmorphism_css(
    selector: str,
    *,
    blur: str = "10px",
    background: str = "rgba(255, 255, 255, 0.25)",
    border_color: str = "rgba(255, 255, 255, 0.18)",
    border_width: str = "1px",
) -> str:
    """Generate a CSS rule with glassmorphism effect."""
    props = glassmorphism(
        blur=blur, background=background, border_color=border_color, border_width=border_width
    )
    return f"{selector} {{\n{props}\n}}"
