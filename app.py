import string
import random
from flask import Flask, request, redirect, jsonify, send_from_directory, abort

app = Flask(__name__, static_folder='static')

# In-memory storage for URL mappings {short_code: long_url}
url_map = {}

def generate_short_code(length=6):
    """Generates a random alphanumeric short code."""
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if short_code not in url_map: # Ensure uniqueness
            return short_code

@app.route('/')
def serve_index():
    """Serves the main HTML page."""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serves other static files (CSS, JS)."""
    # This is needed to serve style.css and script.js correctly
    # It prevents Flask from interpreting them as short codes
    if path.endswith(('.css', '.js')):
        return send_from_directory(app.static_folder, path)
    
    # If it's not CSS or JS, assume it's a short code attempt
    short_code = path
    long_url = url_map.get(short_code)
    if long_url:
        # Add http:// if missing, required for redirect
        if not long_url.startswith(('http://', 'https://')):
            long_url = 'http://' + long_url
        return redirect(long_url, code=302)
    else:
        # If the short code is not found, return 404
        abort(404, description="Short URL not found")


@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Creates a short URL."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    long_url = data.get('long_url')

    if not long_url:
        return jsonify({"error": "Missing 'long_url' parameter"}), 400

    # Optional: Basic validation if it looks like a URL (can be improved)
    if '.' not in long_url:
         return jsonify({"error": "Invalid URL format provided"}), 400

    # Check if URL already shortened (optional, avoids duplicates)
    # for code, url in url_map.items():
    #     if url == long_url:
    #         short_url = request.host_url + code
    #         return jsonify({"short_url": short_url}), 200

    short_code = generate_short_code()
    url_map[short_code] = long_url

    # Construct the full short URL to return
    # request.host_url gives the base URL (e.g., http://127.0.0.1:5000/)
    short_url = request.host_url + short_code
    return jsonify({"short_url": short_url}), 201 # 201 Created

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    # You can return a custom HTML page here if you want
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible on the network (needed for Docker)
    # Use a common port like 5000 or 8080. Render might inject PORT env var.
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) # Turn debug=False for production
