# Logo Design

## Overview

This project includes a simple HTML and CSS setup to create a visually appealing logo design. The design features a diamond shape with four differently colored sides and centered text. This layout demonstrates the use of CSS positioning, transformations, and styling to create a modern logo appearance.

## Project Structure

- `index.html` - The HTML file containing the structure of the logo and text.
- `styles.css` - The CSS file providing styling for the diamond shape and text.

## Features

- **Centered Diamond Shape**: A diamond shape created by rotating a square using CSS transforms.
- **Colorful Sides**: Four sides of the diamond with different colors to enhance visual appeal.
- **Centered Text**: The logo text is centrally positioned within the diamond shape.
- **Responsive Layout**: The design is centered within the viewport, ensuring it is well-positioned on various screen sizes.

## Files

### `index.html`

Contains the basic HTML structure of the logo and text:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logo Design</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="logo-container">
        <div class="diamond">
            <div class="side top-left"></div>
            <div class="side top-right"></div>
            <div class="side bottom-left"></div>
            <div class="side bottom-right"></div>
        </div>
        <div class="logo-text">
            <h1>HTML<span class="ampersand">&</span>CSS</h1>
            <p>design and build websites</p>
        </div>
    </div>
</body>
</html>
