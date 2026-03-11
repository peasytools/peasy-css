"""peasy-css CLI — Generate CSS from the terminal.

Usage::

    peasy-css gradient "#ff0000" "#0000ff" --direction "to right"
    peasy-css shadow --x 2px --y 4px --blur 8px --color "rgba(0,0,0,0.2)"
    peasy-css flexbox --justify center --align center --gap 1rem
    peasy-css grid --columns "1fr 1fr 1fr" --gap 2rem
"""

from __future__ import annotations

from typing import Annotated

import typer
from rich.console import Console
from rich.syntax import Syntax

from peasy_css import engine

app = typer.Typer(
    name="peasy-css",
    help="CSS toolkit — 15 generators from peasycss.com",
    no_args_is_help=True,
)

console = Console()


def _print_css(css: str) -> None:
    """Pretty-print CSS with syntax highlighting."""
    syntax = Syntax(css, "css", theme="monokai", padding=1)
    console.print(syntax)


@app.command("gradient")
def gradient_cmd(
    colors: Annotated[list[str], typer.Argument(help="Color stops (hex or named)")],
    direction: Annotated[str, typer.Option("--direction", "-d")] = "to right",
    gradient_type: Annotated[str, typer.Option("--type", "-t")] = "linear",
    selector: Annotated[str, typer.Option("--selector", "-s")] = ".element",
) -> None:
    """Generate a CSS gradient."""
    css = engine.gradient_css(
        selector,
        colors,
        direction=direction,  # type: ignore[arg-type]
        gradient_type=gradient_type,  # type: ignore[arg-type]
    )
    _print_css(css)


@app.command("shadow")
def shadow_cmd(
    x: Annotated[str, typer.Option("--x")] = "0px",
    y: Annotated[str, typer.Option("--y")] = "4px",
    blur: Annotated[str, typer.Option("--blur")] = "6px",
    spread: Annotated[str, typer.Option("--spread")] = "0px",
    color: Annotated[str, typer.Option("--color")] = "rgba(0, 0, 0, 0.1)",
    inset: Annotated[bool, typer.Option("--inset")] = False,
    selector: Annotated[str, typer.Option("--selector", "-s")] = ".element",
) -> None:
    """Generate a box-shadow."""
    s = engine.Shadow(x=x, y=y, blur=blur, spread=spread, color=color, inset=inset)
    css = engine.box_shadow_css(selector, s)
    _print_css(css)


@app.command("flexbox")
def flexbox_cmd(
    direction: Annotated[str, typer.Option("--direction", "-d")] = "row",
    wrap: Annotated[str, typer.Option("--wrap")] = "nowrap",
    justify: Annotated[str, typer.Option("--justify", "-j")] = "flex-start",
    align: Annotated[str, typer.Option("--align", "-a")] = "stretch",
    gap: Annotated[str, typer.Option("--gap", "-g")] = "0px",
    selector: Annotated[str, typer.Option("--selector", "-s")] = ".container",
) -> None:
    """Generate flexbox layout CSS."""
    css = engine.flexbox_css(
        selector,
        direction=direction,  # type: ignore[arg-type]
        wrap=wrap,  # type: ignore[arg-type]
        justify=justify,  # type: ignore[arg-type]
        align=align,  # type: ignore[arg-type]
        gap=gap,
    )
    _print_css(css)


@app.command("grid")
def grid_cmd(
    columns: Annotated[str, typer.Option("--columns", "-c")] = "1fr 1fr 1fr",
    rows: Annotated[str, typer.Option("--rows", "-r")] = "auto",
    gap: Annotated[str, typer.Option("--gap", "-g")] = "1rem",
    selector: Annotated[str, typer.Option("--selector", "-s")] = ".container",
) -> None:
    """Generate CSS Grid layout."""
    t = engine.GridTemplate(columns=columns, rows=rows, gap=gap)
    css = engine.grid_css(selector, t)
    _print_css(css)


@app.command("border-radius")
def border_radius_cmd(
    top_left: Annotated[str, typer.Option("--tl")] = "0px",
    top_right: Annotated[str, typer.Option("--tr")] = "0px",
    bottom_right: Annotated[str, typer.Option("--br")] = "0px",
    bottom_left: Annotated[str, typer.Option("--bl")] = "0px",
    selector: Annotated[str, typer.Option("--selector", "-s")] = ".element",
) -> None:
    """Generate border-radius CSS."""
    css = engine.border_radius_css(
        selector,
        top_left=top_left,
        top_right=top_right,
        bottom_right=bottom_right,
        bottom_left=bottom_left,
    )
    _print_css(css)


@app.command("glass")
def glass_cmd(
    blur: Annotated[str, typer.Option("--blur")] = "10px",
    bg: Annotated[str, typer.Option("--bg")] = "rgba(255, 255, 255, 0.25)",
    selector: Annotated[str, typer.Option("--selector", "-s")] = ".glass",
) -> None:
    """Generate glassmorphism CSS."""
    css = engine.glassmorphism_css(selector, blur=blur, background=bg)
    _print_css(css)


@app.command("clamp")
def clamp_cmd(
    min_size: Annotated[str, typer.Option("--min")] = "1rem",
    preferred: Annotated[str, typer.Option("--preferred")] = "2.5vw",
    max_size: Annotated[str, typer.Option("--max")] = "2rem",
    selector: Annotated[str, typer.Option("--selector", "-s")] = ".heading",
) -> None:
    """Generate fluid font-size with clamp()."""
    css = engine.clamp_font_css(selector, min_size, preferred, max_size)
    _print_css(css)
