import tkinter as tk
from tkinter import messagebox
import requests

# Function to scan and display the security headers
def scan_headers():
    url = url_entry.get()  # Get the URL from the entry box

    # Check if the URL is not empty
    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return

    try:
        # Send a HEAD request to the provided URL to get the headers
        response = requests.head(url, allow_redirects=True)
        headers = response.headers

        # Check if there are any security-related headers and display them
        security_headers = [
            'Content-Security-Policy',
            'Strict-Transport-Security',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'Cache-Control',
            'X-Permitted-Cross-Domain-Policies',
            'Referrer-Policy',
            'Clear-Site-Data',
            'Cross-Origin-Embedder-Policy',
            'Cross-Origin-Opener-Policy',
            'Cross-Origin-Resource-Policy',
            'Permissions-Policy',
            'X-XSS-Protection'
        ]

        result_text.delete(1.0, tk.END)  # Clear the result area

        # Iterate through each security header and display it
        for header in security_headers:
            value = headers.get(header, 'Not Set')

            # Insert the header name with bold formatting
            result_text.insert(tk.END, f"{header}: ", "bold")

            # Insert the value without any specific formatting
            result_text.insert(tk.END, f"{value}\n")

            # Special handling for 'X-XSS-Protection' header to show deprecation notice
            if header == 'X-XSS-Protection' and value != 'Not Set':
                result_text.insert(tk.END, "(Note: X-XSS-Protection is Deprecated according to OWASP Secure Headers Project)\n", "italic")

        # Ensure the Text widget is properly updated
        result_text.config(state=tk.NORMAL)

    except requests.RequestException as e:
        messagebox.showerror("Request Error", f"Error fetching headers: {e}")

# Create the main window
root = tk.Tk()
root.title("Security Header Scanner")

# Configure the grid layout
root.grid_rowconfigure(0, weight=0)  # The first row (input section)
root.grid_rowconfigure(1, weight=1)  # The second row (result section)
root.grid_columnconfigure(0, weight=1)  # Allow the first column (main column) to expand

# Create and place the widgets
url_label = tk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

scan_button = tk.Button(root, text="Scan Headers", command=scan_headers)
scan_button.grid(row=0, column=2, padx=10, pady=5)

# Create a frame to hold the Text widget and Scrollbar
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

# Create the Text widget to display the headers
result_text = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12))
result_text.grid(row=0, column=0, sticky="nsew")

# Create a Scrollbar and attach it to the Text widget
scrollbar = tk.Scrollbar(frame, command=result_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

result_text.config(yscrollcommand=scrollbar.set)

# Create a tag for bold text and italic text
result_text.tag_configure("bold", font=("Arial", 12, "bold"))
result_text.tag_configure("italic", font=("Arial", 12, "italic"))

# Allow the Text widget to expand in both directions within the frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Run the Tkinter event loop
root.mainloop()
