# mysite/middleware.py
import secrets


def generate_nonce(length=16):
    """Generate a random nonce."""
    return secrets.token_hex(length)


class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        nonce = generate_nonce()
        request.csp_nonce = nonce
        response = self.get_response(request)
        csp_policy = [
            "default-src 'self'",
            "frame-ancestors 'self'",
            f"script-src 'self' 'nonce-{nonce}' 'strict-dynamic' cdn.jsdelivr.net",
            f"style-src 'self' 'nonce-{nonce}' cdn.jsdelivr.net",
            "font-src 'self' cdn.jsdelivr.net",
            "img-src 'self' data:",
        ]
        response["Content-Security-Policy"] = "; ".join(csp_policy)
        response["Referrer-Policy"] = "strict-origin-when-cross-origin"
        permissions_policy = [
            "accelerometer=()",
            "ambient-light-sensor=()",
            "autoplay=()",
            "battery=()",
            "camera=()",
            "display-capture=()",
            "document-domain=()",
            "encrypted-media=()",
            "fullscreen=()",
            "gamepad=()",
            "geolocation=()",
            "gyroscope=()",
            "layout-animations=()",
            "legacy-image-formats=()",
            "magnetometer=()",
            "microphone=()",
            "midi=()",
            "oversized-images=()",
            "payment=()",
            "picture-in-picture=()",
            "publickey-credentials-get=()",
            "speaker-selection=()",
            "sync-xhr=()",
            "unoptimized-images=()",
            "unsized-media=()",
            "usb=()",
            "screen-wake-lock=()",
            "web-share=()",
            "xr-spatial-tracking=()",
        ]
        response["Permissions-Policy"] = ", ".join(permissions_policy)
        return response
