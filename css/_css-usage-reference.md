# CSS Usage Reference

This file documents the usage of CSS classes and IDs from style.css and bootstrap.min.css files in this directory.

## bootstrap.min.css
Bootstrap is a comprehensive CSS framework. The minified version includes standard Bootstrap classes for:

- Grid system (col-*, row, container)
- Typography (h1-h6, p, etc.)
- Components (btn, card, nav, etc.)
- Utilities (mt-*, p-*, text-*, etc.)

For full reference see: https://getbootstrap.com/docs/

## style.css
Custom styles specific to this site. Key selectors and their usage:

### Layout Classes
- `.aktexts`
  - Purpose: Main container for product text content
  - Usage: Wraps all product descriptions
  - Properties: Sets max-width, centers content, adds padding

- `.aktexts-inner`
  - Purpose: Inner content container
  - Usage: Contains the actual product description paragraphs
  - Properties: Adds white background, padding, and subtle shadow

### Typography
- `.aktexts-inner p`
  - Purpose: Paragraph styling within content area
  - Usage: Applied to all product description paragraphs
  - Properties: Sets consistent margin and padding

### Responsive Design
The CSS includes mobile-friendly adjustments for screens under 768px:
- Reduces padding on `.aktexts` and `.aktexts-inner`
- Maintains readability on smaller devices
