# Maughan Library Book Finder

This is a simple web-based tool to help users find the location of books in the Maughan Library by their classmark.

## How to Run

Because web browsers have security restrictions that prevent loading local files directly, you need to run a simple local web server to use this tool. Here’s how:

**1. Open a terminal or command prompt.**

**2. Navigate to this project's directory.**
   ```bash
   cd path/to/this/folder
   ```

**3. Start a simple web server.**

*   **If you have Python 3:**
    ```bash
    python3 -m http.server
    ```

*   **If you have Python 2:**
    ```bash
    python -m SimpleHTTPServer
    ```

*   **If you have Node.js:**
    First, install the `http-server` package if you don't have it:
    ```bash
    npm install -g http-server
    ```
    Then, run the server:
    ```bash
    http-server
    ```

**4. Open the website in your browser.**
   Once the server is running, open your web browser and go to:
   [http://localhost:8000](http://localhost:8000)

Now, the book finder should load correctly and you can start searching for classmarks.
