# Week 5 Day 4 — HTML & CSS

## 📚 What We Learned

Today we focused on **CSS Flexbox, CSS Grid, and Responsive Design**. We applied these concepts to a personal profile page and practiced how to make a webpage adapt to different screen sizes.

---

## 1. CSS Flexbox

Flexbox is useful for arranging elements in a row or column.

We used:

```css
display: flex;
```

For example, the header uses Flexbox:

```css
header {
    display: flex;
    justify-content: space-around;
    align-items: center;
    gap: 1rem;
}
```

### Important Flexbox properties

* `display: flex` — turns an element into a flex container.
* `justify-content` — controls alignment along the main axis.
* `align-items` — controls alignment along the cross axis.
* `flex-direction` — controls whether items are arranged in a row or column.
* `gap` — adds space between flex items.

We also used Flexbox for the navigation:

```css
nav {
    display: flex;
    justify-content: space-between;
    width: 30%;
}
```

---

## 2. CSS Grid

CSS Grid is useful when we need to organize content into **rows and columns**.

We used Grid for the About Me section:

```css
.aboutme {
    display: grid;
    height: 100vh;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

### Important Grid concepts

#### `display: grid`

Makes an element a grid container.

#### `grid-template-columns`

Defines the columns in the grid.

For example:

```css
grid-template-columns: repeat(2, 1fr);
```

creates two equal columns.

#### `1fr`

`fr` means **fraction of the available space**.

For example:

```css
grid-template-columns: 1fr 1fr;
```

means each column gets half of the available space.

---

## 3. Responsive Grid

One of the useful techniques we learned was:

```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```

This helps the grid automatically adjust based on the available screen width.

### How it works

* `repeat()` repeats the columns.
* `auto-fit` automatically fits as many columns as possible.
* `minmax(250px, 1fr)` means each column should be at least `250px` wide but can grow to use available space.

This allows the layout to work on different screen sizes without manually defining every screen width.

---

## 4. Responsive Design

Responsive design means creating webpages that work well on:

* 💻 Desktop
* 💻 Laptop
* 📱 Tablet
* 📱 Mobile

We used a **media query** to change the layout for smaller screens:

```css
@media (max-width: 768px) {
    nav {
        flex-direction: column;
    }
}
```

When the screen width is **768px or smaller**, the navigation changes from a row to a column.

This is an example of making a desktop layout adapt to smaller devices.

---

## 5. Flexbox vs Grid

We learned that Flexbox and Grid have different strengths.

### Flexbox

Best for **one-dimensional layouts**:

```text
→ → →
```

or

```text
↓
↓
↓
```

For example:

* Navigation bars
* Headers
* Buttons
* Aligning items

### Grid

Best for **two-dimensional layouts**:

```text
┌───────┬───────┐
│       │       │
├───────┼───────┤
│       │       │
└───────┴───────┘
```

For example:

* Page sections
* Card layouts
* Image + text layouts
* Multiple columns

---

## 6. Combining Flexbox and Grid

A webpage does not have to use only Flexbox or only Grid.

In this project, we used:

* **Flexbox** for the header and navigation.
* **Grid** for the About Me section.
* **Media queries** to make the layout responsive.

Using both tools allows us to choose the best layout method for each part of the page.

---

## 7. Responsive Images

We also practiced controlling images with CSS:

```css
header img {
    width: 80px;
    object-fit: cover;
    border: 4px solid #F8E948;
    border-radius: 20px;
}
```

### Properties we used

* `width` — controls image size.
* `object-fit: cover` — keeps the image contained within its dimensions while maintaining its proportions.
* `border` — adds a border around the image.
* `border-radius` — rounds the corners.
* `box-shadow` — adds a shadow around the image.

---

## 8. What I Practiced

In this profile page, I practiced:

* Creating a page layout with HTML.
* Using CSS Flexbox.
* Using CSS Grid.
* Creating responsive layouts.
* Using `auto-fit` and `minmax()`.
* Using `fr` units.
* Creating media queries.
* Changing Flexbox direction on smaller screens.
* Aligning elements with `justify-content` and `align-items`.
* Creating responsive navigation.
* Combining Grid and Flexbox in the same webpage.

---

## 🎯 Main Takeaway

The main lesson from today was that **Flexbox and Grid make it much easier to create organized and responsive layouts**.

Flexbox is especially useful for arranging items in one direction, while Grid is useful for creating rows and columns. Combined with **media queries**, they allow a webpage to adapt to different screen sizes.

> **Flexbox → one-dimensional layout**
> **Grid → two-dimensional layout**
> **Media Query → responsive behavior**
