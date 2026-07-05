from bs4 import BeautifulSoup


class PerformanceChecker:
    @staticmethod
    def check(html: str) -> dict:
        """
        Detect lightweight performance indicators.
        """

        soup = BeautifulSoup(html, "html.parser")

        images = soup.find_all("img")
        scripts = soup.find_all("script")
        stylesheets = soup.find_all("link", rel=lambda x: x and "stylesheet" in x)
        lazy_images = soup.find_all("img", loading="lazy")
        inline_styles = soup.find_all(style=True)

        result = {
            "total_images": len(images),
            "lazy_loaded_images": len(lazy_images),
            "images_without_dimensions": 0,
            "large_images": 0,
            "scripts": len(scripts),
            "stylesheets": len(stylesheets),
            "inline_styles": len(inline_styles),
        }

        for img in images:
            width = img.get("width")
            height = img.get("height")

            if not width or not height:
                result["images_without_dimensions"] += 1

            src = img.get("src", "").lower()

            if any(
                src.endswith(ext)
                for ext in [
                    ".png",
                    ".jpg",
                    ".jpeg",
                    ".bmp",
                    ".tiff",
                ]
            ):
                result["large_images"] += 1

        return result


if __name__ == "__main__":

    sample_html = """
    <html>

        <head>

            <link rel="stylesheet" href="style.css">

        </head>

        <body>

            <img src="hero.jpg">

            <img
                src="logo.webp"
                width="200"
                height="100"
                loading="lazy"
            >

            <img
                src="banner.png"
                loading="lazy"
            >

            <script src="app.js"></script>

            <script src="analytics.js"></script>

            <div style="color:red;">Hello</div>

        </body>

    </html>
    """

    print(PerformanceChecker.check(sample_html))