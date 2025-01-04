# Security Header Scanner

This Python program scans a provided URL for various HTTP security headers and displays them in a graphical user interface (GUI). It helps you to check whether your website has important security headers configured to enhance its security posture. The program uses the `tkinter` library for the GUI and the `requests` library to make HTTP requests to the target URL.

## Features

- **Scan for Security Headers**: Checks for the presence of security-related HTTP headers.
- **Displays Results**: Shows whether the security headers are set, along with their values.
- **Deprecation Notice**: Special note for the `X-XSS-Protection` header, indicating that it is deprecated according to the OWASP Secure Headers Project.
- **User-Friendly Interface**: Easy-to-use GUI built with Tkinter.

## Supported Security Headers

The program checks for the following security-related HTTP headers:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Cache-Control`
- `X-Permitted-Cross-Domain-Policies`
- `Referrer-Policy`
- `Clear-Site-Data`
- `Cross-Origin-Embedder-Policy`
- `Cross-Origin-Opener-Policy`
- `Cross-Origin-Resource-Policy`
- `Permissions-Policy`
- `X-XSS-Protection` (with a deprecation note)

## Installation

### Prerequisites

Make sure you have Python installed (version 3.x recommended). You will also need to install the required dependencies:

1. **requests**: For making HTTP requests.
2. **tkinter**: For the GUI (usually comes pre-installed with Python).

You can install the required dependencies using `pip`:

`pip install requests`

**Note:** tkinter is often included by default with most Python installations. If it's not installed, you can install it via your package manager (e.g., sudo apt-get install python3-tk for Ubuntu/Debian)

### Clone the Repository

Clone this repository to your local machine:

`python SecurityHeaderScanner.pyw`

This will open a GUI where you can enter a URL and click the "Scan Headers" button to check for security headers

## How to Use

**Enter a URL:** In the input field, type the URL of the website you want to scan (e.g., https://example.com).

Click **"Scan Headers":** Press the "Scan Headers" button to send a request to the specified URL.

**View Results:** The program will display a list of security headers in the text box. Each header will show its value (or "Not Set" if it's missing). For the X-XSS-Protection header, if it is found, a special note will indicate its deprecation.

**Scroll:** If there are too many results, you can use the scrollbar to navigate through them.

### Deprecation Note

The `X-XSS-Protection header` is considered deprecated by the **OWASP Secure Headers Project** and may not provide meaningful protection against modern cross-site scripting (XSS) attacks. Therefore, the program adds a special note for this header when it is found in the response headers

### Example Output
If the headers are present:

**X-Content-Type-Options:** nosniff

**Strict-Transport-Security:** max-age=31536000; includeSubDomains

**Cache-Control:** no-store, no-cache, must-revalidate

**X-XSS-Protection:** 1; mode=block
(Note: Deprecated according to OWASP Secure Headers Project)

If the headers are not set:

**X-XSS-Protection:** Not Set

**Content-Security-Policy:** Not Set

## Troubleshooting

- If you encounter issues with the program, ensure you have a working internet connection and that the target URL is correct.
- If you receive an error message saying that the `requests` library is not installed, you can install it using `pip install requests`.
- If the program crashes or hangs, check the URL for typos or incorrect formats (e.g., missing `http://` or `https://`).

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/hadesninja/SecurityHeadersScanner/blob/master/LICENSE) file for details.
