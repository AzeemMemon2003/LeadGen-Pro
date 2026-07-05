class Pricing:

    SERVICES = {

        "Technical SEO": {
            "price": 500,
            "duration": "1 Week"
        },

        "On-Page SEO": {
            "price": 400,
            "duration": "1 Week"
        },

        "Content Optimization": {
            "price": 350,
            "duration": "1 Week"
        },

        "Image SEO": {
            "price": 250,
            "duration": "2 Days"
        },

        "WordPress Maintenance": {
            "price": 300,
            "duration": "Monthly"
        },

        "Shopify Optimization": {
            "price": 700,
            "duration": "2 Weeks"
        },

        "Website Redesign": {
            "price": 2500,
            "duration": "4 Weeks"
        },

        "Lead Capture": {
            "price": 500,
            "duration": "3 Days"
        },

        "Conversion Optimization": {
            "price": 700,
            "duration": "2 Weeks"
        },

        "Google Analytics 4 Setup": {
            "price": 250,
            "duration": "1 Day"
        },

        "Google Tag Manager Setup": {
            "price": 200,
            "duration": "1 Day"
        },

        "Meta Pixel Setup": {
            "price": 200,
            "duration": "1 Day"
        },

        "Privacy Policy Implementation": {
            "price": 150,
            "duration": "1 Day"
        },

        "Local SEO": {
            "price": 900,
            "duration": "4 Weeks"
        },

        "Google Business Profile Optimization": {
            "price": 600,
            "duration": "2 Weeks"
        }

    }

    @classmethod
    def calculate(cls, services):

        items = []

        total = 0

        max_days = 0

        for service in services:

            if service not in cls.SERVICES:
                continue

            item = cls.SERVICES[service]

            items.append({

                "service": service,

                "price": item["price"],

                "duration": item["duration"]

            })

            total += item["price"]

        return {

            "items": items,

            "total": total

        }