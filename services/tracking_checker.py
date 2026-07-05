from bs4 import BeautifulSoup


class TrackingChecker:
    @staticmethod
    def check(html: str) -> dict:
        """
        Detect common analytics and marketing tracking tools.
        """

        soup = BeautifulSoup(html, "html.parser")

        content = html.lower()

        result = {
            "ga4": False,
            "gtm": False,
            "meta_pixel": False,
            "linkedin_insight": False,
            "hotjar": False,
            "clarity": False,
        }

        # Google Analytics 4
        ga4_patterns = [
            "gtag/js?id=g-",
            "gtag('config'",
            "google-analytics.com",
            "googletagmanager.com/gtag/js",
        ]

        if any(pattern in content for pattern in ga4_patterns):
            result["ga4"] = True

        # Google Tag Manager
        if "googletagmanager.com/gtm.js" in content or "gtm-" in content:
            result["gtm"] = True

        # Meta Pixel
        meta_patterns = [
            "connect.facebook.net",
            "fbq(",
            "facebook pixel",
        ]

        if any(pattern in content for pattern in meta_patterns):
            result["meta_pixel"] = True

        # LinkedIn Insight Tag
        if "snap.licdn.com" in content or "_linkedin_partner_id" in content:
            result["linkedin_insight"] = True

        # Hotjar
        if "hotjar" in content or "hj(" in content:
            result["hotjar"] = True

        # Microsoft Clarity
        if "clarity.ms" in content or "clarity(" in content:
            result["clarity"] = True

        return result


if __name__ == "__main__":

    sample_html = """
    <html>

        <script async src="https://www.googletagmanager.com/gtag/js?id=G-ABCDE12345"></script>

        <script>
            gtag('config','G-ABCDE12345');
        </script>

        <script>
            fbq('init','123456');
        </script>

        <script src="https://snap.licdn.com/li.lms-analytics/insight.min.js"></script>

        <script>
            (function(h,o,t,j,a,r){
                h.hj=h.hj||function(){};
            })();
        </script>

        <script type="text/javascript">
            (function(c,l,a,r,i,t,y){
                c[a]=c[a]||function(){};
            })(window, document, "clarity", "script");
        </script>

    </html>
    """

    print(TrackingChecker.check(sample_html))