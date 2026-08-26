# HTML & CSS Profile Lab

## Overview

This lab was about creating a simple **personal profile webpage** using HTML and CSS.

The project helped us practice:

* HTML page structure
* Headings and paragraphs
* Images
* Ordered and unordered lists
* Forms and form controls
* HTML attributes
* CSS selectors
* CSS properties
* Classes and IDs
* Hover effects
* External CSS files
* Basic JavaScript with `onclick`

---

## 1. HTML Page Structure

We learned how to create the basic structure of an HTML document:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
</head>

<body>

</body>

</html>
```

### Important elements

* `<!DOCTYPE html>` tells the browser that the document uses HTML5.
* `<html>` is the root element.
* `<head>` contains information about the webpage.
* `<title>` sets the browser tab title.
* `<body>` contains the visible content.

---

## 2. Linking an External CSS File

Instead of putting all CSS inside the HTML file, we connected an external stylesheet:

```html
<link rel="stylesheet" href="css/style.css">
```

This keeps the HTML and CSS separate and makes the project easier to organize.

Our structure can look like:

```text
project/
│
├── index.html
│
└── css/
    └── style.css
```

---

## 3. Images

We learned how to display an image using `<img>`:

```html
<img width="300"
     src="image-url"
     alt="">
```

Important attributes:

* `src` specifies the image location.
* `alt` provides alternative text.
* `width` controls the image width.

---

## 4. Headings and Paragraphs

We used different heading levels:

```html
<h1>Mada</h1>
<h2>Goal</h2>
<h2>Hobbies</h2>
```

We also used paragraphs:

```html
<p>trying to make it to the next day</p>
```

The headings help organize the content and show the importance of each section.

---

## 5. Classes and IDs

We learned that HTML elements can have classes and IDs.

### Class

```html
<p class="note">Trying to make it to the next day</p>
```

A class can be reused on multiple elements.

CSS:

```css
.note {
    color: blue;
}
```

### ID

```html
<p id="main-note">Trying to make it to the next day</p>
```

An ID identifies a specific element.

CSS:

```css
#main-note {
    color: blueviolet;
}
```

---

## 6. CSS Selectors

We learned three important types of selectors.

### Element selector

```css
p {
    color: blue;
}
```

This applies to all `<p>` elements.

### Class selector

```css
.note {
    color: blue;
}
```

This applies to elements with `class="note"`.

### ID selector

```css
#main-note {
    color: blueviolet;
}
```

This applies to the element with `id="main-note"`.

---

## 7. CSS Styling

We learned how to change the appearance of the webpage.

For example:

```css
body {
    font-size: 1.3rem;
    font-family: sans-serif;
    line-height: 2rem;
}
```

We also changed:

* Font size
* Font family
* Line height
* Text alignment
* Font weight
* Text color
* Borders
* Margins
* Padding
* Width

Example:

```css
p {
    text-align: left;
    font-weight: bold;
    font-size: 4rem;
    color: rgb(0, 140, 255);
}
```

---

## 8. Hover Effects

We learned how to change an element when the mouse moves over it.

Example:

```css
#main-note:hover {
    color: palevioletred;
}
```

The paragraph changes color when the user hovers over it.

We also used `transform`:

```css
#feedback:hover {
    transform: scale(1.5);
}
```

This makes the feedback button become larger when the mouse is over it.

---

## 9. Forms

We created a simple form:

```html
<form action="">
```

The form contains different input controls.

### Email input

```html
<label for="email">Email</label>

<input type="email"
       name="email"
       id="email">
```

The `type="email"` creates an email input.

---

## 10. Select Dropdown

We learned how to create a dropdown menu:

```html
<select name="color" id="color">

    <option value="">Red</option>
    <option value="">Blue</option>

</select>
```

The user can select one option from the list.

---

## 11. Checkboxes

We learned how to create checkboxes:

```html
<input type="checkbox"
       name="yes"
       class="ch"
       id="ch">

<label for="yes">Yes</label>
```

Checkboxes allow users to select options.

We also created a special CSS class for the checkboxes:

```css
.ch {
    width: 10%;
    margin: 0;
    padding: 0;
}
```

---

## 12. Textarea

We used `<textarea>` for larger text input:

```html
<textarea name="message" id="message"></textarea>
```

This is useful when the user needs to enter a message or feedback.

---

## 13. Buttons

We created buttons using:

```html
<button>Send</button>
```

And styled them with CSS:

```css
button {
    padding: 10px 32px;
    margin: 2rem;
    cursor: pointer;
}
```

The `cursor: pointer` makes the mouse cursor change when hovering over the button.

---

## 14. Form Styling

We learned how to style the entire form:

```css
form {
    border: thick double #664ca8;
}
```

We also applied the same styles to multiple form elements:

```css
input,
select,
textarea {
    width: 90%;
    padding: 12px;
    margin: 10px 0;
}
```

This is an example of grouping selectors.

---

## 15. Inline CSS

We also practiced writing CSS directly inside an HTML element.

For example:

```html
<body style="display: flex;
             justify-content: center;
             flex-direction: column;
             align-items: center;">
```

And:

```html
<main style="width: 500px;
             text-align: center;">
```

Inline CSS works, but using an external stylesheet is generally easier to maintain when a project becomes larger.

---

## 16. Basic JavaScript

We used a small amount of JavaScript with the Feedback button:

```html
<button id="feedback"
        onclick="window.history.back()">
    Feedback
</button>
```

When the button is clicked:

```javascript
window.history.back()
```

takes the user back to the previous page.

---

# What I Learned

By completing this lab, I learned how to:

* Build a basic HTML webpage
* Structure content using HTML elements
* Add images to a webpage
* Use headings and paragraphs
* Create ordered and unordered lists
* Create forms
* Use email inputs
* Create dropdown menus
* Create checkboxes
* Create textareas
* Create buttons
* Use classes and IDs
* Connect HTML to an external CSS file
* Style HTML elements with CSS
* Use CSS selectors
* Use the `:hover` pseudo-class
* Use CSS `transform`
* Use margins and padding
* Add borders
* Use basic Flexbox
* Add simple JavaScript behavior with `onclick`

---

# Main Concepts Practiced

```text
HTML
 ├── Page structure
 ├── Headings
 ├── Paragraphs
 ├── Images
 ├── Lists
 ├── Forms
 ├── Inputs
 ├── Select
 ├── Checkboxes
 ├── Textarea
 └── Buttons

CSS
 ├── Selectors
 ├── Classes
 ├── IDs
 ├── Colors
 ├── Fonts
 ├── Borders
 ├── Margins
 ├── Padding
 ├── Flexbox
 ├── Hover
 └── Transform

JavaScript
 └── onclick + window.history.back()
```

# Final Result

The final project is a simple **personal profile page** containing:

1. A profile image
2. A name
3. A personal note
4. A goal
5. Hobbies
6. Learning progress
7. An email form
8. A favorite-color dropdown
9. Yes/No checkboxes
10. A message textarea
11. A Send button
12. A Feedback button with basic JavaScript behavior
