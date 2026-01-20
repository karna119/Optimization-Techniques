# 📚 Engineering Optimization Study Guide

A comprehensive, interactive web-based learning platform for Engineering Optimization based on "Engineering Optimization: Theory and Practice" by Singiresu S. Rao.

## ✨ Features

### 📖 Complete Content Coverage
- **15 Major Topics** covering all aspects of optimization
- **All images integrated** in appropriate sections
- **Interactive navigation** with sidebar menu
- **Search functionality** to find specific topics
- **Mathematical formulas** with proper formatting
- **Real-world examples** and case studies
- **Data tables** with professional styling
- **Visual illustrations** throughout

### 🎨 Beautiful Design
- Modern gradient UI with purple/violet theme
- Responsive layout for mobile and desktop
- Smooth animations and transitions
- Color-coded information boxes
- Professional typography and spacing

### 📊 Content Sections
1. 🎯 Introduction to Engineering Optimization
2. 📝 Statement of an Optimization Problem
3. 🎛️ The Design Vector
4. 🔒 Design Constraints
5. 📊 Constraint Surfaces
6. 🎯 The Objective Function
7. 🗻 Objective Function Surfaces
8. 📋 Classification of Optimization Problems
9. 📈 Single-Variable Optimization
10. ✅ Necessary and Sufficient Conditions for Optimality
11. 🔢 Multivariable Optimization Without Constraints
12. ⚖️ Multivariable Optimization with Equality Constraints
13. 🔗 Method of Lagrange Multipliers
14. ⛔ Multivariable Optimization with Inequality Constraints
15. 🎯 The Kuhn–Tucker Conditions

## 🚀 How to Use

### Option 1: Using Python HTTP Server (Recommended)

The easiest way to view the application with all images properly loaded:

```bash
# Navigate to the study guide directory
cd "c:\Users\swathikaran\Downloads\study_guide_export (1)"

# Run the Python server
python run_server.py
```

Then open your browser and go to: **http://localhost:8000**

### Option 2: Direct Browser Opening

Simply double-click `index.html` to open it in your default browser.

**Note:** When opening directly, the image paths must be relative and the file must be served, so Option 1 is recommended for full functionality.

### Option 3: Using Node.js HTTP Server

If you have Node.js installed:

```bash
cd "c:\Users\swathikaran\Downloads\study_guide_export (1)"
npx http-server
```

## 📁 File Structure

```
study_guide_export (1)/
├── index.html                 # Main application file
├── run_server.py             # Python HTTP server script
├── README.md                 # This file
├── images/                   # All illustration images
│   ├── image_point-0_0.png   # Statement of Problem illustrations
│   ├── image_point-0_1.png
│   ├── image_point-0_2.png
│   ├── image_point-1_0.png   # Design Vector illustrations
│   ├── image_point-1_1.png
│   ├── image_point-2_0.png   # Constraints illustrations
│   ├── image_point-4_0.png   # Objective Function illustrations
│   ├── image_point-4_1.png
│   ├── image_point-4_2.png
│   ├── image_point-5_0.png   # Objective Function Surfaces
│   ├── image_point-5_1.png
│   ├── image_point-5_2.png
│   ├── image_point-6_0.png   # Classification illustrations
│   ├── image_point-6_1.png
│   ├── image_point-6_2.png
│   ├── image_point-7_0.png   # Single-Variable Optimization
│   ├── image_point-7_1.png
│   ├── image_point-7_2.png
│   ├── image_point-8_0.png   # Multivariable Unconstrained
│   ├── image_point-8_1.png
│   ├── image_point-9_0.png   # Necessary & Sufficient Conditions
│   ├── image_point-9_1.png
│   ├── image_point-11_0.png  # Lagrange Multipliers
│   ├── image_point-11_1.png
│   ├── image_point-12_0.png  # Inequality Constraints
│   ├── image_point-12_1.png
│   ├── image_point-12_2.png
│   ├── image_point-13_0.png  # Kuhn-Tucker Conditions
│   └── image_point-13_1.png
└── *.md files                # Original markdown files
    ├── full_study_guide.md
    ├── statement_of_an_optimization_problem.md
    ├── design_vector.md
    ├── design_constraints.md
    ├── constraint_surface.md
    ├── objective_function.md
    ├── objective_function_surfaces.md
    ├── classification_of_optimization_problems.md
    ├── single_variable_optimization.md
    ├── necessary_and_sufficient_conditions.md
    ├── multivariable_optimization_without_constraints.md
    ├── multivariable_optimization_with_equality_constraints.md
    ├── method_of_lagrange_multipliers.md
    ├── multivariable_optimization_with_inequality_constraints.md
    └── kuhn_tucker_conditions.md
```

## 🎓 Navigation Guide

### Using the Sidebar
- Click any topic in the left sidebar to navigate to that section
- Active topic is highlighted in purple
- Sidebar remains sticky for easy navigation

### Using Search
- Enter a keyword in the search box at the top
- Click "Search" or press Enter
- The application will find and display the relevant section
- Try searching for terms like "stress", "constraint", "gradient", etc.

### Interactive Elements
- **Tabs:** Click tab buttons to switch between different explanations
- **Tables:** Hover over table rows for highlighting
- **Color-Coded Boxes:**
  - 🔵 Blue boxes: Information
  - 🟡 Yellow boxes: Highlights/Tips
  - 🟢 Green boxes: Success/Key points
  - 🔴 Red boxes: Warnings/Dangers

## 📸 Images

All images are properly integrated into their respective sections:

| Section | Images | Topics |
|---------|--------|--------|
| Statement of Problem | 3 images | Feasible region, design space, optimization |
| Design Vector | 2 images | Design space, gear pair example |
| Constraints | 1 image | Constraint surface visualization |
| Objective Function | 2 images | Maximization/Minimization, contours |
| Objective Function Surfaces | 3 images | Surface topography, contour lines, gradient |
| Classification | 3 images | Problem types, linear programming, nonlinear |
| Single-Variable Opt. | 3 images | Stationary points, elimination methods |
| Multivariable Unc. | 2 images | Hessian matrix, saddle points |
| Necessary & Sufficient | 2 images | Minima/Maxima determination, Hessian test |
| Lagrange Multipliers | 2 images | Constraint tangency, shadow prices |
| Inequality Constraints | 3 images | Active/inactive constraints, feasible regions |
| Kuhn-Tucker | 2 images | KT conditions, applications |

## 💻 Browser Compatibility

- ✅ Chrome/Chromium (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (responsive design)

## 🎨 Customization

### Changing Colors
Edit the CSS variables in the `<style>` section:
```css
header h1 { color: #667eea; }  /* Change primary color */
```

### Adjusting Font Size
Modify the font-size properties in the CSS.

### Adding More Content
Add new `<div>` elements with class `content-section` and add corresponding sidebar items.

## 📖 Content Source

All content is based on:
- **Textbook:** "Engineering Optimization: Theory and Practice"
- **Author:** Singiresu S. Rao
- **Edition:** Fourth Edition
- **Content:** Complete Chapter 1 and 2 material plus supplementary examples

## ⚠️ Notes

1. **Images:** All 29 PNG images are included and properly referenced
2. **Mathematical Notation:** Uses Unicode and mathematical symbols
3. **Responsive:** Works great on tablets and mobile devices
4. **Offline:** Once loaded, the application works without internet
5. **No Dependencies:** Pure HTML/CSS/JavaScript - no external libraries needed

## 🐛 Troubleshooting

### Images not showing?
- Make sure you're running the Python server (Option 1)
- Check that the `images/` folder contains all PNG files
- Try clearing browser cache (Ctrl+Shift+Delete)

### Content not displaying?
- Refresh the page (F5)
- Check browser console for errors (F12 → Console tab)
- Try a different browser

### Search not working?
- Make sure JavaScript is enabled
- Check browser console for JavaScript errors
- Try a shorter search term

## 🚀 Performance Tips

1. First load may take a few seconds (images loading)
2. Subsequent loads are much faster (browser caching)
3. On slow internet, wait for all images to load
4. Close unused browser tabs for better performance

## 📝 Metadata

- **Created:** January 2026
- **Language:** English
- **Subject:** Engineering Optimization
- **Level:** Advanced Undergraduate / Graduate
- **Time to Complete:** 15-20 hours of study

## 📧 Support

For questions or issues:
1. Check the README file
2. Review the content in the relevant section
3. Consult the original markdown files (*.md)
4. Refer to the textbook references

## ✅ Checklist for First Use

- [ ] Python server is running
- [ ] Browser opened to http://localhost:8000
- [ ] All 15 topics visible in sidebar
- [ ] Images loading properly
- [ ] Search functionality works
- [ ] Can navigate between sections smoothly

## 🎯 Learning Path Recommendation

**Beginner:**
1. Introduction
2. Statement of an Optimization Problem
3. Design Vector
4. Design Constraints
5. Objective Function

**Intermediate:**
6. Single-Variable Optimization
7. Necessary and Sufficient Conditions
8. Multivariable Optimization Without Constraints

**Advanced:**
9. Multivariable with Equality Constraints
10. Lagrange Multipliers
11. Multivariable with Inequality Constraints
12. Kuhn-Tucker Conditions

---

**Enjoy learning! 🎓**

*Based on Engineering Optimization: Theory and Practice by Singiresu S. Rao*
