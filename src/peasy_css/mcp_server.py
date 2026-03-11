"""peasy-css MCP server — CSS generation tools for AI assistants.

Start the server::

    uvx --from "peasy-css[mcp]" python -m peasy_css
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from peasy_css import engine

mcp = FastMCP(
    "peasy-css",
    instructions="CSS generation tools: gradients, shadows, flexbox, grid, animations, and more.",
)


@mcp.tool()
def css_gradient(
    colors: list[str],
    direction: str = "to right",
    gradient_type: str = "linear",
    selector: str = ".element",
) -> str:
    """Generate CSS gradient. Returns complete CSS rule."""
    return engine.gradient_css(
        selector,
        colors,
        direction=direction,  # type: ignore[arg-type]
        gradient_type=gradient_type,  # type: ignore[arg-type]
    )


@mcp.tool()
def css_box_shadow(
    x: str = "0px",
    y: str = "4px",
    blur: str = "6px",
    spread: str = "0px",
    color: str = "rgba(0, 0, 0, 0.1)",
    inset: bool = False,
    selector: str = ".element",
) -> str:
    """Generate CSS box-shadow. Returns complete CSS rule."""
    s = engine.Shadow(x=x, y=y, blur=blur, spread=spread, color=color, inset=inset)
    return engine.box_shadow_css(selector, s)


@mcp.tool()
def css_flexbox(
    direction: str = "row",
    wrap: str = "nowrap",
    justify: str = "flex-start",
    align: str = "stretch",
    gap: str = "0px",
    selector: str = ".container",
) -> str:
    """Generate CSS flexbox layout. Returns complete CSS rule."""
    return engine.flexbox_css(
        selector,
        direction=direction,  # type: ignore[arg-type]
        wrap=wrap,  # type: ignore[arg-type]
        justify=justify,  # type: ignore[arg-type]
        align=align,  # type: ignore[arg-type]
        gap=gap,
    )


@mcp.tool()
def css_grid(
    columns: str = "1fr 1fr 1fr",
    rows: str = "auto",
    gap: str = "1rem",
    selector: str = ".container",
) -> str:
    """Generate CSS Grid layout. Returns complete CSS rule."""
    t = engine.GridTemplate(columns=columns, rows=rows, gap=gap)
    return engine.grid_css(selector, t)


@mcp.tool()
def css_animation(
    name: str,
    duration: str = "1s",
    timing: str = "ease",
    selector: str = ".element",
) -> str:
    """Generate CSS animation shorthand. Returns complete CSS rule."""
    return engine.animation_css(
        selector,
        name,
        duration=duration,
        timing=timing,  # type: ignore[arg-type]
    )


@mcp.tool()
def css_transform(
    translate_x: str = "0",
    translate_y: str = "0",
    rotate: str = "0deg",
    scale_x: str = "1",
    scale_y: str = "1",
    selector: str = ".element",
) -> str:
    """Generate CSS transform. Returns complete CSS rule."""
    return engine.transform_css(
        selector,
        translate_x=translate_x,
        translate_y=translate_y,
        rotate=rotate,
        scale_x=scale_x,
        scale_y=scale_y,
    )


@mcp.tool()
def css_glassmorphism(
    blur: str = "10px",
    background: str = "rgba(255, 255, 255, 0.25)",
    selector: str = ".glass",
) -> str:
    """Generate glassmorphism CSS. Returns complete CSS rule."""
    return engine.glassmorphism_css(selector, blur=blur, background=background)


@mcp.tool()
def css_clamp_font(
    min_size: str = "1rem",
    preferred: str = "2.5vw",
    max_size: str = "2rem",
    selector: str = ".heading",
) -> str:
    """Generate fluid font-size with clamp(). Returns CSS rule."""
    return engine.clamp_font_css(selector, min_size, preferred, max_size)


@mcp.tool()
def css_media_query(
    breakpoint: str,
    css_block: str,
    query_type: str = "min-width",
) -> str:
    """Wrap CSS in a media query. Returns @media rule."""
    return engine.media_query(breakpoint, css_block, type=query_type)
