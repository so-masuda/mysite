# mysite/middleware.py


class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        csp_policy = [
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' cdn.jsdelivr.net",
            "style-src 'self' 'unsafe-inline' cdn.jsdelivr.net",
            "font-src 'self' cdn.jsdelivr.net",
            "img-src 'self' data:",
        ]
        response["Content-Security-Policy"] = "; ".join(csp_policy)
        return response
