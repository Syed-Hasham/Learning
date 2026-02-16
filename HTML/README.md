# 🌐 HTML Learning Journey

<div align="center">

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-success?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Sigma%20Web%20Dev-orange?style=for-the-badge)

**A comprehensive repository documenting my HTML & Web Development journey**  
*Following CodeWithHarry's Sigma Web Development Course*

[🎥 Course Link]([https://www.youtube.com/@CodeWithHarry](https://www.youtube.com/watch?v=tVzUXW6siu0&list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w)) • [📝 My Notes](#-quick-reference)
</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Course Overview](#-course-overview)
- [Learning Modules](#-learning-modules)
- [Quick Reference](#-quick-reference)
- [Resources](#-resources)
- [Progress](#-progress)

---

## 🎯 About

This repository contains my complete HTML learning experience following **CodeWithHarry's Sigma Web Development Course**. Each module includes practical examples, hands-on projects, and comprehensive notes covering modern HTML5 practices.

### Why Learn HTML?
- 🌍 **Foundation of Web** - The backbone of every website
- 📱 **Responsive Design** - Build mobile-friendly pages
- 🎨 **Creative Freedom** - Design beautiful interfaces
- 🚀 **Career Ready** - Essential for web development
- 🔧 **Easy to Learn** - Beginner-friendly markup language

---

## 📚 Course Overview

**Sigma Web Development** by CodeWithHarry is a comprehensive web development course covering HTML, CSS, JavaScript, and modern web technologies.

### What I'm Learning:
- ✅ HTML5 Fundamentals
- ✅ Semantic HTML Structure
- ✅ Forms & Input Elements
- ✅ Multimedia Integration
- ✅ Best Practices & Accessibility
- ✅ Real-world Projects

---

## 📖 Learning Modules

### Module Structure
```
📦 HTML Learning
 ┣ 📂 #1 Headings & Paragraphs
 ┣ 📂 #1.1 Bookmark Manager
 ┣ 📂 #2 Image List & Tables
 ┣ 📂 #3 Forms & Input Tags
 ┣ 📂 #4 Inline & Block Elements
 ┣ 📂 #5 IDs & Classes
 ┣ 📂 #6 Video, Audio & Media
 ┣ 📂 #7 Semantic Tags
 ┗ 📂 #8 Entities, Code Tags & More
```

---

## 🔖 Quick Reference

### #1 - Headings & Paragraphs

**Headings (H1-H6)**
```html
<h1>Main Heading - Largest</h1>
<h2>Sub Heading</h2>
<h3>Section Heading</h3>
<h4>Subsection Heading</h4>
<h5>Minor Heading</h5>
<h6>Smallest Heading</h6>
```

**Paragraphs & Text Formatting**
```html
<!-- Paragraph -->
<p>This is a paragraph of text.</p>

<!-- Line Break -->
<br>

<!-- Horizontal Rule -->
<hr>

<!-- Text Formatting -->
<strong>Bold text (important)</strong>
<b>Bold text (visual)</b>
<em>Italic text (emphasis)</em>
<i>Italic text (visual)</i>
<mark>Highlighted text</mark>
<small>Smaller text</small>
<del>Deleted text</del>
<ins>Inserted text</ins>
<sub>Subscript</sub>
<sup>Superscript</sup>
```

**Best Practices:**
- Use only one `<h1>` per page
- Maintain heading hierarchy (don't skip levels)
- Use semantic tags for meaning, not just styling

---

### #1.1 - Bookmark Manager

**Links & Navigation**
```html
<!-- External Link -->
<a href="https://google.com">Visit Google</a>

<!-- Internal Link -->
<a href="about.html">About Page</a>

<!-- Email Link -->
<a href="mailto:email@example.com">Send Email</a>

<!-- Phone Link -->
<a href="tel:+1234567890">Call Us</a>

<!-- Download Link -->
<a href="file.pdf" download>Download PDF</a>

<!-- Open in New Tab -->
<a href="https://example.com" target="_blank">Open in New Tab</a>

<!-- Bookmark/Anchor Link -->
<a href="#section1">Jump to Section 1</a>
<h2 id="section1">Section 1</h2>
```

**Link Attributes:**
- `href` - Destination URL
- `target` - Where to open (`_blank`, `_self`, `_parent`, `_top`)
- `rel` - Relationship (`noopener`, `noreferrer`, `nofollow`)
- `download` - Download file instead of navigating

---

### #2 - Images, Lists & Tables

**Images**
```html
<!-- Basic Image -->
<img src="image.jpg" alt="Description of image">

<!-- Image with Size -->
<img src="photo.jpg" alt="Photo" width="300" height="200">

<!-- Responsive Image -->
<img src="image.jpg" alt="Description" style="max-width: 100%; height: auto;">

<!-- Image with Link -->
<a href="page.html">
  <img src="thumbnail.jpg" alt="Thumbnail">
</a>
```

**Lists**
```html
<!-- Unordered List (Bullets) -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

<!-- Ordered List (Numbers) -->
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>

<!-- Ordered List with Custom Start -->
<ol start="5" type="A">
  <li>Item A</li>
  <li>Item B</li>
</ol>

<!-- Nested Lists -->
<ul>
  <li>Main Item
    <ul>
      <li>Sub Item 1</li>
      <li>Sub Item 2</li>
    </ul>
  </li>
</ul>

<!-- Description List -->
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
```

**Tables**
```html
<table border="1">
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John</td>
      <td>25</td>
      <td>New York</td>
    </tr>
    <tr>
      <td>Jane</td>
      <td>30</td>
      <td>London</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="3">Total: 2 people</td>
    </tr>
  </tfoot>
</table>

<!-- Table with colspan and rowspan -->
<table>
  <tr>
    <td rowspan="2">Merged vertically</td>
    <td>Cell 1</td>
  </tr>
  <tr>
    <td>Cell 2</td>
  </tr>
  <tr>
    <td colspan="2">Merged horizontally</td>
  </tr>
</table>
```

---

### #3 - Forms & Input Tags

**Form Structure**
```html
<form action="/submit" method="POST">
  <!-- Form elements go here -->
</form>
```

**Text Inputs**
```html
<!-- Text Input -->
<label for="name">Name:</label>
<input type="text" id="name" name="name" placeholder="Enter your name" required>

<!-- Email Input -->
<label for="email">Email:</label>
<input type="email" id="email" name="email" required>

<!-- Password Input -->
<label for="password">Password:</label>
<input type="password" id="password" name="password" minlength="8" required>

<!-- Number Input -->
<label for="age">Age:</label>
<input type="number" id="age" name="age" min="0" max="120">

<!-- Date Input -->
<label for="date">Date:</label>
<input type="date" id="date" name="date">

<!-- Time Input -->
<input type="time" id="time" name="time">

<!-- URL Input -->
<input type="url" id="website" name="website" placeholder="https://">

<!-- Tel Input -->
<input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}">

<!-- Search Input -->
<input type="search" id="search" name="search" placeholder="Search...">

<!-- Color Picker -->
<input type="color" id="color" name="color">

<!-- File Upload -->
<input type="file" id="file" name="file" accept=".jpg,.png,.pdf">
```

**Other Input Types**
```html
<!-- Radio Buttons -->
<input type="radio" id="male" name="gender" value="male">
<label for="male">Male</label>

<input type="radio" id="female" name="gender" value="female">
<label for="female">Female</label>

<!-- Checkboxes -->
<input type="checkbox" id="subscribe" name="subscribe" value="yes">
<label for="subscribe">Subscribe to newsletter</label>

<!-- Dropdown/Select -->
<label for="country">Country:</label>
<select id="country" name="country">
  <option value="">Select a country</option>
  <option value="us">United States</option>
  <option value="uk">United Kingdom</option>
  <option value="ca">Canada</option>
</select>

<!-- Textarea -->
<label for="message">Message:</label>
<textarea id="message" name="message" rows="4" cols="50" placeholder="Enter your message"></textarea>

<!-- Range Slider -->
<input type="range" id="volume" name="volume" min="0" max="100" value="50">

<!-- Hidden Input -->
<input type="hidden" name="user_id" value="12345">
```

**Form Buttons**
```html
<!-- Submit Button -->
<button type="submit">Submit Form</button>
<input type="submit" value="Submit">

<!-- Reset Button -->
<button type="reset">Reset Form</button>
<input type="reset" value="Reset">

<!-- Regular Button -->
<button type="button">Click Me</button>
<input type="button" value="Click Me">
```

**Form Attributes:**
- `action` - Where to send form data
- `method` - How to send (GET/POST)
- `required` - Field must be filled
- `placeholder` - Hint text
- `maxlength` - Max characters
- `pattern` - Validation pattern (regex)
- `autocomplete` - Enable/disable autocomplete

---

### #4 - Inline & Block Elements

**Block-Level Elements**
```html
<!-- Take full width available -->
<div>Division/Container</div>
<p>Paragraph</p>
<h1>Heading</h1>
<ul><li>List</li></ul>
<section>Section</section>
<article>Article</article>
<header>Header</header>
<footer>Footer</footer>
<nav>Navigation</nav>
<form>Form</form>
<table>Table</table>
```

**Inline Elements**
```html
<!-- Only take necessary width -->
<span>Span container</span>
<a href="#">Link</a>
<img src="image.jpg" alt="Image">
<strong>Strong text</strong>
<em>Emphasized text</em>
<b>Bold text</b>
<i>Italic text</i>
<mark>Marked text</mark>
<code>Code snippet</code>
<button>Button</button>
<input type="text">
```

**Difference:**

| Block Elements | Inline Elements |
|----------------|-----------------|
| Start on new line | Continue on same line |
| Take full width | Take only needed width |
| Can contain block & inline | Can contain only inline |
| Can set width/height | Width/height ignored |
| Examples: `<div>`, `<p>`, `<h1>` | Examples: `<span>`, `<a>`, `<img>` |

**Generic Containers:**
```html
<!-- Block Container -->
<div class="container">
  <p>Content inside a div</p>
</div>

<!-- Inline Container -->
<p>This is <span style="color: red;">highlighted</span> text.</p>
```

---

### #5 - IDs & Classes

**IDs (Unique Identifier)**
```html
<!-- Only one element should have a specific ID -->
<div id="header">Header Section</div>
<p id="intro">Introduction paragraph</p>

<!-- Used in CSS -->
<style>
  #header {
    background-color: blue;
  }
</style>

<!-- Used in JavaScript -->
<script>
  document.getElementById('header');
</script>
```

**Classes (Reusable Identifier)**
```html
<!-- Multiple elements can share the same class -->
<div class="container">First container</div>
<div class="container">Second container</div>
<p class="highlight">Highlighted paragraph</p>
<p class="highlight important">Multiple classes</p>

<!-- Used in CSS -->
<style>
  .container {
    padding: 20px;
  }
  .highlight {
    background-color: yellow;
  }
</style>

<!-- Used in JavaScript -->
<script>
  document.getElementsByClassName('container');
  document.querySelectorAll('.container');
</script>
```

**Best Practices:**

| IDs | Classes |
|-----|---------|
| Unique (one per page) | Reusable (many per page) |
| Higher specificity | Lower specificity |
| Used for specific elements | Used for styling groups |
| Good for anchors/JavaScript | Good for CSS styling |
| Example: `#header`, `#nav` | Example: `.btn`, `.card` |

**Naming Conventions:**
```html
<!-- Good -->
<div class="user-profile"></div>
<div class="product-card"></div>
<button class="btn-primary"></button>

<!-- Avoid -->
<div class="UP"></div> <!-- Too short -->
<div class="user profile"></div> <!-- Spaces not allowed -->
<div class="123user"></div> <!-- Can't start with number -->
```

---

### #6 - Video, Audio & Media

**Video Element**
```html
<!-- Basic Video -->
<video src="video.mp4" controls></video>

<!-- Video with Multiple Sources -->
<video width="640" height="360" controls poster="thumbnail.jpg">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <source src="video.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>

<!-- Video with Attributes -->
<video 
  controls 
  autoplay 
  muted 
  loop 
  preload="auto"
  width="100%"
>
  <source src="video.mp4" type="video/mp4">
</video>
```

**Video Attributes:**
- `controls` - Show play/pause buttons
- `autoplay` - Start playing automatically
- `muted` - Mute audio
- `loop` - Repeat video
- `poster` - Thumbnail before play
- `preload` - none/metadata/auto
- `width`/`height` - Dimensions

**Audio Element**
```html
<!-- Basic Audio -->
<audio src="audio.mp3" controls></audio>

<!-- Audio with Multiple Sources -->
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  <source src="audio.wav" type="audio/wav">
  Your browser does not support the audio tag.
</audio>

<!-- Audio with Attributes -->
<audio controls autoplay loop muted>
  <source src="music.mp3" type="audio/mpeg">
</audio>
```

**Embedded Content**
```html
<!-- YouTube Video -->
<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/VIDEO_ID" 
  frameborder="0" 
  allowfullscreen>
</iframe>

<!-- Google Maps -->
<iframe 
  src="https://www.google.com/maps/embed?pb=..." 
  width="600" 
  height="450" 
  style="border:0;" 
  allowfullscreen>
</iframe>

<!-- Embed PDF -->
<iframe src="document.pdf" width="100%" height="600px"></iframe>

<!-- Embed External Page -->
<iframe src="https://example.com" width="800" height="600"></iframe>
```

**SVG Graphics**
```html
<!-- Inline SVG -->
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" fill="red" />
</svg>

<!-- SVG Image -->
<img src="graphic.svg" alt="SVG Image">
```

**Canvas (for JavaScript drawing)**
```html
<canvas id="myCanvas" width="400" height="200"></canvas>
```

---

### #7 - Semantic Tags

**Semantic HTML5 Elements**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Semantic HTML Example</title>
</head>
<body>
  
  <!-- Header Section -->
  <header>
    <nav>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Main Content -->
  <main>
    
    <!-- Article -->
    <article>
      <h2>Article Title</h2>
      <p>Article content...</p>
    </article>

    <!-- Section -->
    <section>
      <h2>Section Title</h2>
      <p>Section content...</p>
    </section>

    <!-- Aside (Sidebar) -->
    <aside>
      <h3>Related Links</h3>
      <ul>
        <li><a href="#">Link 1</a></li>
        <li><a href="#">Link 2</a></li>
      </ul>
    </aside>

  </main>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2024 My Website. All rights reserved.</p>
  </footer>

</body>
</html>
```

**Semantic Tags Reference:**

| Tag | Purpose | Example Use |
|-----|---------|-------------|
| `<header>` | Page/section header | Logo, nav, site title |
| `<nav>` | Navigation links | Menu, breadcrumbs |
| `<main>` | Main content | Primary page content |
| `<article>` | Independent content | Blog post, news article |
| `<section>` | Thematic grouping | Chapter, tab panel |
| `<aside>` | Side content | Sidebar, related links |
| `<footer>` | Page/section footer | Copyright, contact info |
| `<figure>` | Media with caption | Images, diagrams |
| `<figcaption>` | Figure caption | Image description |
| `<mark>` | Highlighted text | Search results |
| `<time>` | Date/time | `<time datetime="2024-01-01">` |
| `<details>` | Collapsible content | FAQ, accordion |
| `<summary>` | Details heading | Clickable title |

**Figure with Caption**
```html
<figure>
  <img src="photo.jpg" alt="Description">
  <figcaption>Photo caption goes here</figcaption>
</figure>
```

**Details/Summary (Accordion)**
```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content that appears when expanded.</p>
</details>
```

**Time Element**
```html
<p>Published on <time datetime="2024-02-17">February 17, 2024</time></p>
```

**Benefits of Semantic HTML:**
- ✅ Better SEO (Search Engine Optimization)
- ✅ Improved Accessibility (Screen readers)
- ✅ Cleaner, more readable code
- ✅ Easier maintenance
- ✅ Better browser/device compatibility

---

### #8 - Entities, Code Tags & More

**HTML Entities**
```html
<!-- Special Characters -->
&lt;        <!-- < (less than) -->
&gt;        <!-- > (greater than) -->
&amp;       <!-- & (ampersand) -->
&quot;      <!-- " (quotation mark) -->
&apos;      <!-- ' (apostrophe) -->
&nbsp;      <!-- Non-breaking space -->
&copy;      <!-- © (copyright) -->
&reg;       <!-- ® (registered) -->
&trade;     <!-- ™ (trademark) -->
&euro;      <!-- € (euro) -->
&pound;     <!-- £ (pound) -->
&yen;       <!-- ¥ (yen) -->
&cent;      <!-- ¢ (cent) -->

<!-- Usage Example -->
<p>5 &lt; 10</p>  <!-- Output: 5 < 10 -->
<p>&copy; 2024 Company Name</p>  <!-- Output: © 2024 Company Name -->
```

**Code & Preformatted Text**
```html
<!-- Inline Code -->
<p>Use the <code>console.log()</code> function to print.</p>

<!-- Code Block -->
<pre>
  <code>
    function hello() {
      console.log("Hello World");
    }
  </code>
</pre>

<!-- Keyboard Input -->
<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.</p>

<!-- Sample Output -->
<samp>Error: File not found</samp>

<!-- Variable -->
<var>x</var> = 5
```

**Quotations**
```html
<!-- Block Quote -->
<blockquote cite="https://source.com">
  <p>This is a longer quotation that spans multiple lines.</p>
</blockquote>

<!-- Inline Quote -->
<p>He said, <q>Hello World</q>.</p>

<!-- Citation -->
<cite>The Great Gatsby</cite>

<!-- Abbreviation -->
<abbr title="HyperText Markup Language">HTML</abbr>
```

**Text Direction & Language**
```html
<!-- Right-to-Left Text -->
<bdo dir="rtl">This text will be right-to-left</bdo>

<!-- Language Attribute -->
<p lang="es">Hola Mundo</p>
```

**Progress & Meter**
```html
<!-- Progress Bar -->
<progress value="70" max="100">70%</progress>

<!-- Meter/Gauge -->
<meter value="6" min="0" max="10">6 out of 10</meter>
```

**Meta Tags (in `<head>`)**
```html
<head>
  <!-- Character Encoding -->
  <meta charset="UTF-8">
  
  <!-- Viewport for Responsive Design -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Description for SEO -->
  <meta name="description" content="Page description for search engines">
  
  <!-- Keywords for SEO -->
  <meta name="keywords" content="HTML, CSS, JavaScript">
  
  <!-- Author -->
  <meta name="author" content="Your Name">
  
  <!-- Refresh Page -->
  <meta http-equiv="refresh" content="30">
  
  <!-- Open Graph (Social Media) -->
  <meta property="og:title" content="Page Title">
  <meta property="og:description" content="Page description">
  <meta property="og:image" content="image.jpg">
</head>
```

**Comments**
```html
<!-- This is a single-line comment -->

<!-- 
  This is a
  multi-line
  comment
-->
```

**Base URL**
```html
<head>
  <!-- All relative URLs will be based on this -->
  <base href="https://example.com/" target="_blank">
</head>
```

---

**Features:**
- 📚 Organized link collections
- 🔖 Category-based bookmarks
- 🎨 Clean, semantic HTML structure
- 🔗 External & internal linking

**Technologies:**
- HTML5
- Semantic Tags
- Anchor Links

---

## 📚 Resources

### Official Documentation
- [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [W3C HTML Specification](https://www.w3.org/TR/html/)
- [Can I Use](https://caniuse.com/) - Browser compatibility

### Learning Resources
- [CodeWithHarry - Sigma Web Dev Course]([https://www.youtube.com/@CodeWithHarry](https://www.youtube.com/watch?v=tVzUXW6siu0&list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w))
- [W3Schools HTML Tutorial](https://www.w3schools.com/html/)
- [FreeCodeCamp](https://www.freecodecamp.org/)

### Tools & Validators
- [HTML Validator](https://validator.w3.org/)
- [VS Code](https://code.visualstudio.com/) - Code Editor
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

### Cheat Sheets
- [HTML5 Cheat Sheet](https://htmlcheatsheet.com/)
- [Emmet Cheat Sheet](https://docs.emmet.io/cheat-sheet/)

---

## 📈 Progress

### Completed ✅
- [x] #1 - Headings & Paragraphs
- [x] #1.1 - Bookmark Manager
- [x] #2 - Images, Lists & Tables
- [x] #3 - Forms & Input Tags
- [x] #4 - Inline & Block Elements
- [x] #5 - IDs & Classes
- [x] #6 - Video, Audio & Media
- [x] #7 - Semantic Tags
- [x] #8 - Entities, Code Tags & More

---

## 💡 Key Learnings

### HTML Best Practices
1. ✅ Always use semantic HTML tags
2. ✅ Include `alt` attributes for images
3. ✅ Use proper heading hierarchy (H1 → H6)
4. ✅ Validate your HTML code
5. ✅ Keep your code clean and indented
6. ✅ Use meaningful class/ID names
7. ✅ Make your site accessible
8. ✅ Optimize images for web
9. ✅ Use external stylesheets
10. ✅ Test across different browsers

### Common Mistakes to Avoid
- ❌ Skipping DOCTYPE declaration
- ❌ Not closing tags properly
- ❌ Using deprecated tags (`<font>`, `<center>`)
- ❌ Inline styles everywhere
- ❌ Missing meta viewport tag
- ❌ Not using semantic HTML
- ❌ Forgetting alt text on images
- ❌ Improper nesting of elements

---

## 🎨 HTML5 Semantic Structure Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Page description">
    <meta name="keywords" content="HTML, CSS, Web Development">
    <meta name="author" content="Your Name">
    <title>Page Title</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    
    <!-- Header -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content -->
    <main>
        
        <!-- Hero Section -->
        <section id="home">
            <h1>Welcome to My Website</h1>
            <p>This is the hero section</p>
        </section>

        <!-- About Section -->
        <section id="about">
            <h2>About Us</h2>
            <article>
                <h3>Our Story</h3>
                <p>Content here...</p>
            </article>
        </section>

        <!-- Services Section -->
        <section id="services">
            <h2>Our Services</h2>
            <div class="service-card">
                <h3>Service 1</h3>
                <p>Description...</p>
            </div>
        </section>

        <!-- Sidebar -->
        <aside>
            <h3>Quick Links</h3>
            <ul>
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
            </ul>
        </aside>

    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 Your Name. All rights reserved.</p>
        <nav>
            <a href="#privacy">Privacy Policy</a> |
            <a href="#terms">Terms of Service</a>
        </nav>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

---

## 🤝 Contributing

Feel free to fork this repository and add your own solutions or improvements!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **CodeWithHarry** - For the amazing Sigma Web Development Course
- **MDN Web Docs** - For comprehensive documentation
- **W3C** - For HTML standards
- **Web Development Community** - For continuous support and resources

---

<div align="center">

### 🌟 Keep Learning, Keep Building!

Made with ❤️ and HTML5

⭐ Star this repo if you found it helpful!
**#SigmaWebDevelopment #CodeWithHarry #HTML5 #WebDevelopment**

</div>
