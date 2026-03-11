"""Tests for peasy_css.engine — 15 CSS generators."""

from __future__ import annotations

from peasy_css import engine

# ── Gradient ──────────────────────────────────────────────────────


class TestGradient:
    def test_linear_gradient(self) -> None:
        result = engine.gradient(["#ff0000", "#0000ff"])
        assert result == "linear-gradient(to right, #ff0000, #0000ff)"

    def test_radial_gradient(self) -> None:
        result = engine.gradient(["#ff0000", "#0000ff"], gradient_type="radial")
        assert result == "radial-gradient(circle, #ff0000, #0000ff)"

    def test_conic_gradient(self) -> None:
        result = engine.gradient(["red", "blue", "green"], gradient_type="conic")
        assert result == "conic-gradient(red, blue, green)"

    def test_repeating_gradient(self) -> None:
        result = engine.gradient(["red", "blue"], repeating=True)
        assert result.startswith("repeating-linear-gradient(")

    def test_color_stops(self) -> None:
        stops = [engine.ColorStop("red", "0%"), engine.ColorStop("blue", "100%")]
        result = engine.gradient(stops)
        assert "red 0%" in result
        assert "blue 100%" in result

    def test_gradient_css(self) -> None:
        result = engine.gradient_css(".bg", ["red", "blue"])
        assert ".bg {" in result
        assert "background:" in result

    def test_direction(self) -> None:
        result = engine.gradient(["red", "blue"], direction="to bottom")
        assert "to bottom" in result


# ── Box Shadow ────────────────────────────────────────────────────


class TestBoxShadow:
    def test_single_shadow(self) -> None:
        s = engine.Shadow(x="2px", y="4px", blur="8px", color="black")
        result = engine.box_shadow(s)
        assert result == "2px 4px 8px 0px black"

    def test_inset_shadow(self) -> None:
        s = engine.Shadow(inset=True)
        result = engine.box_shadow(s)
        assert result.startswith("inset ")

    def test_multiple_shadows(self) -> None:
        s1 = engine.Shadow(x="0px", y="2px", blur="4px")
        s2 = engine.Shadow(x="0px", y="4px", blur="8px", color="blue")
        result = engine.box_shadow(s1, s2)
        assert ", " in result

    def test_box_shadow_css(self) -> None:
        s = engine.Shadow()
        result = engine.box_shadow_css(".card", s)
        assert ".card {" in result
        assert "box-shadow:" in result


# ── Text Shadow ───────────────────────────────────────────────────


class TestTextShadow:
    def test_text_shadow(self) -> None:
        result = engine.text_shadow("2px", "2px", "4px", "gray")
        assert result == "2px 2px 4px gray"

    def test_text_shadow_css(self) -> None:
        result = engine.text_shadow_css("h1")
        assert "h1 {" in result
        assert "text-shadow:" in result


# ── Border Radius ─────────────────────────────────────────────────


class TestBorderRadius:
    def test_uniform(self) -> None:
        result = engine.border_radius(
            top_left="8px", top_right="8px", bottom_right="8px", bottom_left="8px"
        )
        assert result == "8px"

    def test_asymmetric(self) -> None:
        result = engine.border_radius(
            top_left="8px", top_right="16px", bottom_right="8px", bottom_left="0px"
        )
        assert result == "8px 16px 8px 0px"

    def test_border_radius_css(self) -> None:
        result = engine.border_radius_css(
            ".btn", top_left="4px", top_right="4px", bottom_right="4px", bottom_left="4px"
        )
        assert ".btn {" in result
        assert "border-radius: 4px;" in result


# ── Flexbox ───────────────────────────────────────────────────────


class TestFlexbox:
    def test_flexbox_defaults(self) -> None:
        result = engine.flexbox()
        assert "display: flex;" in result
        assert "flex-direction: row;" in result

    def test_flexbox_with_gap(self) -> None:
        result = engine.flexbox(gap="1rem")
        assert "gap: 1rem;" in result

    def test_flexbox_no_gap_when_zero(self) -> None:
        result = engine.flexbox(gap="0px")
        assert "gap:" not in result

    def test_flexbox_css(self) -> None:
        result = engine.flexbox_css(".flex", justify="center", align="center")
        assert ".flex {" in result
        assert "justify-content: center;" in result


# ── Grid ──────────────────────────────────────────────────────────


class TestGrid:
    def test_grid_defaults(self) -> None:
        result = engine.grid()
        assert "display: grid;" in result
        assert "grid-template-columns: 1fr 1fr 1fr;" in result

    def test_grid_custom(self) -> None:
        t = engine.GridTemplate(columns="repeat(4, 1fr)", gap="2rem")
        result = engine.grid(t)
        assert "repeat(4, 1fr)" in result
        assert "gap: 2rem;" in result

    def test_grid_auto_flow(self) -> None:
        t = engine.GridTemplate(auto_flow="dense")
        result = engine.grid(t)
        assert "grid-auto-flow: dense;" in result

    def test_grid_css(self) -> None:
        result = engine.grid_css(".grid")
        assert ".grid {" in result


# ── Animation ─────────────────────────────────────────────────────


class TestAnimation:
    def test_animation_shorthand(self) -> None:
        result = engine.animation("fadeIn", "0.5s", "ease-in")
        assert result == "fadeIn 0.5s ease-in 0s 1 normal none"

    def test_keyframes(self) -> None:
        frames = [
            engine.Keyframe("from", {"opacity": "0"}),
            engine.Keyframe("to", {"opacity": "1"}),
        ]
        result = engine.keyframes("fadeIn", frames)
        assert "@keyframes fadeIn {" in result
        assert "from { opacity: 0; }" in result
        assert "to { opacity: 1; }" in result

    def test_animation_css(self) -> None:
        result = engine.animation_css(".fade", "fadeIn")
        assert ".fade {" in result
        assert "animation:" in result


# ── Transform ─────────────────────────────────────────────────────


class TestTransform:
    def test_transform_none(self) -> None:
        result = engine.transform()
        assert result == "none"

    def test_transform_translate(self) -> None:
        result = engine.transform(translate_x="10px", translate_y="20px")
        assert "translate(10px, 20px)" in result

    def test_transform_rotate(self) -> None:
        result = engine.transform(rotate="45deg")
        assert "rotate(45deg)" in result

    def test_transform_multiple(self) -> None:
        result = engine.transform(translate_x="10px", rotate="45deg", scale_x="1.5")
        assert "translate(" in result
        assert "rotate(" in result
        assert "scale(" in result

    def test_transform_css(self) -> None:
        result = engine.transform_css(".box", rotate="90deg")
        assert ".box {" in result
        assert "transform:" in result


# ── Filter ────────────────────────────────────────────────────────


class TestFilter:
    def test_filter_none(self) -> None:
        result = engine.css_filter()
        assert result == "none"

    def test_filter_blur(self) -> None:
        result = engine.css_filter(blur="5px")
        assert result == "blur(5px)"

    def test_filter_multiple(self) -> None:
        result = engine.css_filter(blur="2px", brightness="120%", grayscale="50%")
        assert "blur(2px)" in result
        assert "brightness(120%)" in result
        assert "grayscale(50%)" in result

    def test_filter_css(self) -> None:
        result = engine.filter_css(".img", blur="3px")
        assert ".img {" in result
        assert "filter:" in result


# ── Transition ────────────────────────────────────────────────────


class TestTransition:
    def test_transition(self) -> None:
        result = engine.transition("opacity", "0.3s", "ease-in")
        assert result == "opacity 0.3s ease-in 0s"

    def test_transition_css(self) -> None:
        result = engine.transition_css(".btn", "background", "0.2s")
        assert ".btn {" in result
        assert "transition:" in result


# ── Media Query ───────────────────────────────────────────────────


class TestMediaQuery:
    def test_media_query_min_width(self) -> None:
        result = engine.media_query("768px", ".container { width: 100%; }")
        assert "@media (min-width: 768px)" in result
        assert ".container { width: 100%; }" in result

    def test_media_query_max_width(self) -> None:
        result = engine.media_query("480px", "body { font-size: 14px; }", type="max-width")
        assert "@media (max-width: 480px)" in result


# ── Typography ────────────────────────────────────────────────────


class TestTypography:
    def test_typography_defaults(self) -> None:
        result = engine.typography()
        assert "font-family:" in result
        assert "font-size: 1rem;" in result
        assert "line-height: 1.5;" in result

    def test_typography_custom(self) -> None:
        result = engine.typography(
            font_family="'Inter', sans-serif",
            font_size="1.25rem",
            letter_spacing="0.05em",
            text_transform="uppercase",
        )
        assert "'Inter', sans-serif" in result
        assert "letter-spacing: 0.05em;" in result
        assert "text-transform: uppercase;" in result

    def test_typography_css(self) -> None:
        result = engine.typography_css("body")
        assert "body {" in result


# ── Aspect Ratio ──────────────────────────────────────────────────


class TestAspectRatio:
    def test_aspect_ratio(self) -> None:
        assert engine.aspect_ratio("16 / 9") == "16 / 9"
        assert engine.aspect_ratio("1 / 1") == "1 / 1"

    def test_aspect_ratio_css(self) -> None:
        result = engine.aspect_ratio_css(".video", "16 / 9")
        assert "aspect-ratio: 16 / 9;" in result


# ── Clamp ─────────────────────────────────────────────────────────


class TestClamp:
    def test_clamp(self) -> None:
        result = engine.clamp("1rem", "2.5vw", "3rem")
        assert result == "clamp(1rem, 2.5vw, 3rem)"

    def test_clamp_font_css(self) -> None:
        result = engine.clamp_font_css("h1", "1.5rem", "4vw", "3rem")
        assert "h1 {" in result
        assert "font-size: clamp(1.5rem, 4vw, 3rem);" in result


# ── Glassmorphism ─────────────────────────────────────────────────


class TestGlassmorphism:
    def test_glassmorphism(self) -> None:
        result = engine.glassmorphism()
        assert "backdrop-filter: blur(10px);" in result
        assert "-webkit-backdrop-filter:" in result
        assert "background:" in result
        assert "border:" in result

    def test_glassmorphism_custom(self) -> None:
        result = engine.glassmorphism(blur="20px", background="rgba(0,0,0,0.5)")
        assert "blur(20px)" in result
        assert "rgba(0,0,0,0.5)" in result

    def test_glassmorphism_css(self) -> None:
        result = engine.glassmorphism_css(".modal")
        assert ".modal {" in result
