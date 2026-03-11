# peasy-css

[![PyPI](https://img.shields.io/pypi/v/peasy-css)](https://pypi.org/project/peasy-css/)
[![Python](https://img.shields.io/pypi/pyversions/peasy-css)](https://pypi.org/project/peasy-css/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/peasy-css/)

Pure Python CSS generator — gradients, shadows, flexbox, grid, animations, transforms, filters, glassmorphism, and more. Zero dependencies, type-safe, with CLI, MCP server, and REST API client.

Built from [PeasyCSS](https://peasycss.com), the interactive CSS tools platform with 200+ generators and references.

> **Try the interactive tools at [peasycss.com](https://peasycss.com)** — [CSS Tools](https://peasycss.com/), [CSS Glossary](https://peasycss.com/glossary/)

<p align="center">
  <img src="demo.gif" alt="peasy-css demo — CSS gradient, box shadow, and flexbox generation in Python REPL" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Gradients](#gradients)
  - [Box Shadows](#box-shadows)
  - [Flexbox Layouts](#flexbox-layouts)
  - [CSS Grid](#css-grid)
  - [Animations & Keyframes](#animations--keyframes)
  - [Transforms](#transforms)
  - [CSS Filters](#css-filters)
  - [Glassmorphism](#glassmorphism)
  - [Fluid Typography](#fluid-typography)
  - [Media Queries](#media-queries)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About CSS](#learn-more-about-css)
- [Peasy Developer Tools](#peasy-developer-tools)
- [License](#license)

## Install

```bash
# Core library (zero dependencies)
pip install peasy-css

# With CLI
pip install "peasy-css[cli]"

# With MCP server for AI assistants
pip install "peasy-css[mcp]"

# With REST API client
pip install "peasy-css[api]"

# Everything
pip install "peasy-css[all]"
```

## Quick Start

```python
from peasy_css import gradient, box_shadow, Shadow, flexbox, glassmorphism

# Generate a linear gradient
css = gradient(["#ff6b35", "#f7c948", "#2ec4b6"])
# → "linear-gradient(to right, #ff6b35, #f7c948, #2ec4b6)"

# Create a box shadow
shadow = Shadow(x="0px", y="4px", blur="12px", color="rgba(0,0,0,0.15)")
css = box_shadow(shadow)
# → "0px 4px 12px 0px rgba(0,0,0,0.15)"

# Flexbox layout
css = flexbox(direction="row", justify="center", align="center", gap="1rem")
# → "display: flex;\nflex-direction: row;\njustify-content: center;\nalign-items: center;\ngap: 1rem;"

# Glassmorphism effect
css = glassmorphism(blur="20px", background="rgba(255,255,255,0.1)")
# → backdrop-filter, background, border — frosted glass effect
```

## What You Can Do

### Gradients

CSS gradients create smooth color transitions — linear (directional), radial (circular), and conic (angular). The `gradient()` function supports all three types with optional repeating patterns and precise color stops.

| Type | CSS Function | Use Case |
|------|-------------|----------|
| Linear | `linear-gradient()` | Backgrounds, buttons, headers |
| Radial | `radial-gradient()` | Spotlight effects, circular highlights |
| Conic | `conic-gradient()` | Pie charts, color wheels |
| Repeating | `repeating-*-gradient()` | Striped patterns, progress bars |

```python
from peasy_css import gradient, gradient_css, ColorStop

# Linear gradient with direction
gradient(["#e66465", "#9198e5"], direction="to bottom")
# → "linear-gradient(to bottom, #e66465, #9198e5)"

# Radial gradient
gradient(["#fff", "#000"], gradient_type="radial")
# → "radial-gradient(circle, #fff, #000)"

# Precise color stops
stops = [ColorStop("red", "0%"), ColorStop("yellow", "50%"), ColorStop("green", "100%")]
gradient(stops)
# → "linear-gradient(to right, red 0%, yellow 50%, green 100%)"

# Complete CSS rule
gradient_css(".hero", ["#667eea", "#764ba2"])
# → ".hero {\n  background: linear-gradient(to right, #667eea, #764ba2);\n}"
```

Learn more: [PeasyCSS](https://peasycss.com/) · [CSS Gradient Glossary](https://peasycss.com/glossary/gradient/)

### Box Shadows

Box shadows add depth and elevation to elements. Multiple shadows can be layered for complex effects like material design elevation or neumorphism.

```python
from peasy_css import box_shadow, box_shadow_css, Shadow

# Single shadow
s = Shadow(x="0px", y="4px", blur="6px", spread="0px", color="rgba(0,0,0,0.1)")
box_shadow(s)
# → "0px 4px 6px 0px rgba(0,0,0,0.1)"

# Inset shadow (inner shadow)
s = Shadow(x="0px", y="2px", blur="4px", color="rgba(0,0,0,0.2)", inset=True)
box_shadow(s)
# → "inset 0px 2px 4px 0px rgba(0,0,0,0.2)"

# Multiple layered shadows
s1 = Shadow(y="2px", blur="4px", color="rgba(0,0,0,0.1)")
s2 = Shadow(y="8px", blur="16px", color="rgba(0,0,0,0.1)")
box_shadow(s1, s2)
# → "0px 2px 4px 0px rgba(0,0,0,0.1), 0px 8px 16px 0px rgba(0,0,0,0.1)"
```

Learn more: [PeasyCSS](https://peasycss.com/) · [Box Shadow Glossary](https://peasycss.com/glossary/box-shadow/)

### Flexbox Layouts

Flexbox is a one-dimensional layout model for distributing space and aligning items. It handles both horizontal (row) and vertical (column) layouts with powerful alignment controls.

| Property | Values | Default |
|----------|--------|---------|
| `direction` | row, row-reverse, column, column-reverse | row |
| `wrap` | nowrap, wrap, wrap-reverse | nowrap |
| `justify` | flex-start, flex-end, center, space-between, space-around, space-evenly | flex-start |
| `align` | stretch, flex-start, flex-end, center, baseline | stretch |

```python
from peasy_css import flexbox, flexbox_css

# Centered content
flexbox(justify="center", align="center")

# Responsive card layout
flexbox(wrap="wrap", gap="1.5rem", justify="space-between")

# Complete CSS rule
flexbox_css(".navbar", direction="row", justify="space-between", align="center")
# → ".navbar {\n  display: flex;\n  flex-direction: row;\n  ..."
```

Learn more: [PeasyCSS](https://peasycss.com/) · [Flexbox Glossary](https://peasycss.com/glossary/flexbox/)

### CSS Grid

CSS Grid is a two-dimensional layout system for rows and columns simultaneously. It excels at complex page layouts, card grids, and dashboard designs.

```python
from peasy_css import grid, grid_css, GridTemplate

# Default 3-column grid
grid()
# → "display: grid;\ngrid-template-columns: 1fr 1fr 1fr;\ngap: 1rem;"

# Custom grid template
t = GridTemplate(columns="repeat(4, 1fr)", rows="auto 1fr auto", gap="2rem")
grid(t)

# Dense auto-flow (fill gaps automatically)
t = GridTemplate(columns="repeat(auto-fill, minmax(250px, 1fr))", auto_flow="dense")
grid(t)
```

Learn more: [PeasyCSS](https://peasycss.com/) · [CSS Grid Glossary](https://peasycss.com/glossary/grid/)

### Animations & Keyframes

CSS animations bring elements to life with multi-step transitions. The `animation()` function generates the shorthand property, while `keyframes()` creates `@keyframes` rules.

```python
from peasy_css import animation, animation_css, keyframes, Keyframe

# Animation shorthand
animation("fadeIn", "0.5s", "ease-in")
# → "fadeIn 0.5s ease-in 0s 1 normal none"

# Keyframes definition
frames = [
    Keyframe("from", {"opacity": "0", "transform": "translateY(-20px)"}),
    Keyframe("to", {"opacity": "1", "transform": "translateY(0)"}),
]
keyframes("fadeIn", frames)
# → "@keyframes fadeIn {\n  from { opacity: 0; transform: translateY(-20px); }\n  to { ... }\n}"
```

Learn more: [PeasyCSS](https://peasycss.com/) · [CSS Animation Glossary](https://peasycss.com/glossary/animation/)

### Transforms

CSS transforms modify the visual rendering of elements — translate, rotate, scale, and skew without affecting document flow.

```python
from peasy_css import transform, transform_css

# Single transform
transform(rotate="45deg")
# → "rotate(45deg)"

# Combined transforms
transform(translate_x="10px", translate_y="20px", rotate="45deg", scale_x="1.5")
# → "translate(10px, 20px) rotate(45deg) scale(1.5, 1)"

# No transforms applied
transform()
# → "none"
```

Learn more: [PeasyCSS](https://peasycss.com/) · [CSS Transform Glossary](https://peasycss.com/glossary/transform/)

### CSS Filters

CSS filters apply graphical effects like blur, brightness, contrast, and grayscale to elements — commonly used for image effects and hover states.

```python
from peasy_css import css_filter, filter_css

# Single filter
css_filter(blur="5px")
# → "blur(5px)"

# Multiple filters
css_filter(blur="2px", brightness="120%", grayscale="50%")
# → "blur(2px) brightness(120%) grayscale(50%)"
```

Learn more: [PeasyCSS](https://peasycss.com/) · [CSS Filter Glossary](https://peasycss.com/glossary/filter/)

### Glassmorphism

Glassmorphism creates a frosted glass effect using backdrop-filter, semi-transparent backgrounds, and subtle borders. It's widely used in modern UI design (iOS, Windows 11).

```python
from peasy_css import glassmorphism, glassmorphism_css

# Default glassmorphism
glassmorphism()
# → "backdrop-filter: blur(10px);\n-webkit-backdrop-filter: blur(10px);\nbackground: rgba(255, 255, 255, 0.25);\nborder: 1px solid rgba(255, 255, 255, 0.18);"

# Custom glass effect
glassmorphism(blur="20px", background="rgba(0, 0, 0, 0.3)")

# Complete CSS rule
glassmorphism_css(".modal", blur="15px")
```

Learn more: [PeasyCSS](https://peasycss.com/) · [CSS Glossary](https://peasycss.com/glossary/)

### Fluid Typography

CSS `clamp()` enables fluid typography that scales smoothly between viewport sizes — replacing complex media query breakpoints with a single declaration.

```python
from peasy_css import clamp, clamp_font_css

# Fluid value
clamp("1rem", "2.5vw", "3rem")
# → "clamp(1rem, 2.5vw, 3rem)"

# Fluid font-size CSS rule
clamp_font_css("h1", "1.5rem", "4vw", "3rem")
# → "h1 {\n  font-size: clamp(1.5rem, 4vw, 3rem);\n}"
```

Learn more: [PeasyCSS](https://peasycss.com/) · [CSS Clamp Glossary](https://peasycss.com/glossary/clamp/)

### Media Queries

Media queries enable responsive design by applying CSS rules at specific viewport breakpoints.

```python
from peasy_css import media_query

# Min-width (mobile-first)
media_query("768px", ".sidebar { display: block; }")
# → "@media (min-width: 768px) {\n  .sidebar { display: block; }\n}"

# Max-width (desktop-first)
media_query("480px", "body { font-size: 14px; }", type="max-width")
# → "@media (max-width: 480px) {\n  body { font-size: 14px; }\n}"
```

Learn more: [PeasyCSS](https://peasycss.com/) · [Media Query Glossary](https://peasycss.com/glossary/media-query/)

## Command-Line Interface

```bash
# Generate a gradient
peasy-css gradient --colors "#ff6b35" "#f7c948" "#2ec4b6"

# Box shadow
peasy-css shadow --x 0px --y 4px --blur 12px --color "rgba(0,0,0,0.15)"

# Flexbox layout
peasy-css flexbox --direction row --justify center --align center --gap 1rem

# CSS Grid
peasy-css grid --columns "repeat(3, 1fr)" --gap 2rem

# Glassmorphism
peasy-css glass --blur 20px --background "rgba(255,255,255,0.1)"

# Fluid font size
peasy-css clamp --min 1rem --preferred 2.5vw --max 3rem
```

## MCP Server (Claude, Cursor, Windsurf)

Start the MCP server for AI-assisted CSS generation:

```bash
uvx --from "peasy-css[mcp]" python -m peasy_css
```

### Claude Desktop

```json
{
  "mcpServers": {
    "peasy-css": {
      "command": "uvx",
      "args": ["--from", "peasy-css[mcp]", "python", "-m", "peasy_css"]
    }
  }
}
```

### Cursor / Windsurf

```json
{
  "mcpServers": {
    "peasy-css": {
      "command": "uvx",
      "args": ["--from", "peasy-css[mcp]", "python", "-m", "peasy_css"]
    }
  }
}
```

**Available MCP tools:** `css_gradient`, `css_box_shadow`, `css_flexbox`, `css_grid`, `css_animation`, `css_transform`, `css_glassmorphism`, `css_clamp_font`, `css_media_query`

## REST API Client

```python
from peasy_css.api import PeasyCssAPI

api = PeasyCssAPI()

# List all CSS tools
tools = api.list_tools()

# Get a specific tool
tool = api.get_tool("gradient-generator")

# Search tools and glossary
results = api.search("flexbox")

# OpenAPI specification
spec = api.openapi_spec()
```

## API Reference

### CSS Generators

| Function | Description |
|----------|-------------|
| `gradient(colors, ...)` | Generate CSS gradient value |
| `gradient_css(selector, colors, ...)` | Complete gradient CSS rule |
| `box_shadow(*shadows)` | Generate box-shadow value |
| `box_shadow_css(selector, *shadows)` | Complete box-shadow CSS rule |
| `text_shadow(x, y, blur, color)` | Generate text-shadow value |
| `text_shadow_css(selector, ...)` | Complete text-shadow CSS rule |
| `border_radius(...)` | Generate border-radius value |
| `border_radius_css(selector, ...)` | Complete border-radius CSS rule |
| `flexbox(...)` | Generate flexbox properties |
| `flexbox_css(selector, ...)` | Complete flexbox CSS rule |
| `grid(template)` | Generate grid properties |
| `grid_css(selector, template)` | Complete grid CSS rule |
| `animation(name, duration, timing)` | Generate animation shorthand |
| `animation_css(selector, name, ...)` | Complete animation CSS rule |
| `keyframes(name, frames)` | Generate @keyframes rule |
| `transform(...)` | Generate transform value |
| `transform_css(selector, ...)` | Complete transform CSS rule |
| `css_filter(...)` | Generate filter value |
| `filter_css(selector, ...)` | Complete filter CSS rule |
| `transition(prop, duration, timing)` | Generate transition value |
| `transition_css(selector, ...)` | Complete transition CSS rule |
| `media_query(breakpoint, css, type)` | Wrap CSS in @media rule |
| `typography(...)` | Generate typography properties |
| `typography_css(selector, ...)` | Complete typography CSS rule |
| `aspect_ratio(ratio)` | Generate aspect-ratio value |
| `aspect_ratio_css(selector, ratio)` | Complete aspect-ratio CSS rule |
| `clamp(min, preferred, max)` | Generate clamp() value |
| `clamp_font_css(selector, ...)` | Complete fluid font-size CSS rule |
| `glassmorphism(...)` | Generate glassmorphism properties |
| `glassmorphism_css(selector, ...)` | Complete glassmorphism CSS rule |

### Types

| Type | Fields |
|------|--------|
| `ColorStop` | `color: str`, `position: str` |
| `Shadow` | `x`, `y`, `blur`, `spread`, `color`, `inset` |
| `GridTemplate` | `columns`, `rows`, `gap`, `auto_flow` |
| `Keyframe` | `selector: str`, `properties: dict[str, str]` |

## Learn More About CSS

- **Tools**: [PeasyCSS Tools](https://peasycss.com/)
- **Reference**: [CSS Glossary](https://peasycss.com/glossary/)
- **API**: [REST API Docs](https://peasycss.com/developers/) · [OpenAPI Spec](https://peasycss.com/api/openapi.json)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install peasy-css` | [npm](https://www.npmjs.com/package/peasy-css) |
| **MCP** | `uvx --from "peasy-css[mcp]" python -m peasy_css.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Peasy Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| peasy-pdf | [PyPI](https://pypi.org/project/peasy-pdf/) | — | PDF merge, split, compress, encrypt — [peasypdf.com](https://peasypdf.com) |
| peasy-image | [PyPI](https://pypi.org/project/peasy-image/) | [npm](https://www.npmjs.com/package/peasy-image) | Image resize, crop, convert, watermark — [peasyimage.com](https://peasyimage.com) |
| peasytext | [PyPI](https://pypi.org/project/peasytext/) | [npm](https://www.npmjs.com/package/peasytext) | Text case, slug, encode, diff — [peasytext.com](https://peasytext.com) |
| **peasy-css** | **[PyPI](https://pypi.org/project/peasy-css/)** | **[npm](https://www.npmjs.com/package/peasy-css)** | **CSS gradient, shadow, flexbox, grid — [peasycss.com](https://peasycss.com)** |
| peasy-compress | [PyPI](https://pypi.org/project/peasy-compress/) | — | Archive & compression — gzip, zip, tar — [peasytools.com](https://peasytools.com) |
| peasy-document | [PyPI](https://pypi.org/project/peasy-document/) | — | Document conversion — Markdown, CSV, HTML — [peasytools.com](https://peasytools.com) |
| peasy-audio | [PyPI](https://pypi.org/project/peasy-audio/) | — | Audio trim, merge, convert, normalize — [peasyaudio.com](https://peasyaudio.com) |
| peasy-video | [PyPI](https://pypi.org/project/peasy-video/) | — | Video trim, resize, GIF, thumbnails — [peasyvideo.com](https://peasyvideo.com) |
| peasy-convert | [PyPI](https://pypi.org/project/peasy-convert/) | — | Unified CLI: `peasy pdf merge a.pdf b.pdf` — [peasytools.com](https://peasytools.com) |
| peasy-mcp | [PyPI](https://pypi.org/project/peasy-mcp/) | — | Unified MCP hub for AI assistants — [peasytools.com](https://peasytools.com) |

## License

MIT
