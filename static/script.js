document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('shorten-form');
    const urlInput = document.getElementById('long-url-input');
    const resultArea = document.getElementById('result-area');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default page reload

        const longUrl = urlInput.value.trim();
        resultArea.innerHTML = ''; // Clear previous results

        if (!longUrl) {
            resultArea.innerHTML = '<p class="error">Please enter a URL.</p>';
            return;
        }

        try {
            const response = await fetch('/shorten', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ long_url: longUrl }),
            });

            const data = await response.json();

            if (response.ok) { // Status codes 200-299
                const shortUrl = data.short_url;
                resultArea.innerHTML = `
                    <p>Shortened URL: <a href="${shortUrl}" target="_blank">${shortUrl}</a></p>
                    <p><small>(Click to test)</small></p>
                `;
                urlInput.value = ''; // Clear input field on success
            } else {
                // Display error message from backend
                resultArea.innerHTML = `<p class="error">Error: ${data.error || 'An unknown error occurred.'}</p>`;
            }
        } catch (error) {
            console.error('Error submitting form:', error);
            resultArea.innerHTML = '<p class="error">An error occurred while contacting the server. Please try again later.</p>';
        }
    });
});
