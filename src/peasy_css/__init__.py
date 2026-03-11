"""peasy-css — Pure Python CSS code generator.

15 CSS utilities for generating gradients, shadows, borders, flexbox, grid,
animations, transforms, filters, transitions, media queries, typography,
aspect-ratio, clamp, and glassmorphism.

Zero dependencies.
"""

from __future__ import annotations

from peasy_css.engine import (
    ColorStop,
    FlexAlign,
    FlexDirection,
    FlexJustify,
    FlexWrap,
    FontWeight,
    GradientDirection,
    GradientType,
    GridAutoFlow,
    GridTemplate,
    Keyframe,
    Shadow,
    TimingFunction,
    animation,
    animation_css,
    aspect_ratio,
    aspect_ratio_css,
    border_radius,
    border_radius_css,
    box_shadow,
    box_shadow_css,
    clamp,
    clamp_font_css,
    css_filter,
    filter_css,
    flexbox,
    flexbox_css,
    glassmorphism,
    glassmorphism_css,
    gradient,
    gradient_css,
    grid,
    grid_css,
    keyframes,
    media_query,
    text_shadow,
    text_shadow_css,
    transform,
    transform_css,
    transition,
    transition_css,
    typography,
    typography_css,
)

__version__ = "0.1.0"

__all__ = [
    # Types
    "ColorStop",
    "FlexAlign",
    "FlexDirection",
    "FlexJustify",
    "FlexWrap",
    "FontWeight",
    "GradientDirection",
    "GradientType",
    "GridAutoFlow",
    "GridTemplate",
    "Keyframe",
    "Shadow",
    "TimingFunction",
    # Animation
    "animation",
    "animation_css",
    # Aspect Ratio
    "aspect_ratio",
    "aspect_ratio_css",
    # Border
    "border_radius",
    "border_radius_css",
    # Shadows
    "box_shadow",
    "box_shadow_css",
    # Clamp
    "clamp",
    "clamp_font_css",
    # Filter
    "css_filter",
    "filter_css",
    # Layout
    "flexbox",
    "flexbox_css",
    # Glassmorphism
    "glassmorphism",
    "glassmorphism_css",
    # Gradient
    "gradient",
    "gradient_css",
    "grid",
    "grid_css",
    "keyframes",
    # Media Query
    "media_query",
    "text_shadow",
    "text_shadow_css",
    # Transform
    "transform",
    "transform_css",
    # Transition
    "transition",
    "transition_css",
    # Typography
    "typography",
    "typography_css",
]
