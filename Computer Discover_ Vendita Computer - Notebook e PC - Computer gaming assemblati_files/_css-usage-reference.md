# CSS Files Usage Reference - Computer Discover

This document catalogs CSS files and their usage in the Computer Discover section.

## Core Style Files

### all.min.css
- Main stylesheet combining multiple components
- Used across entire site

### style.min.css (and variants)
- Theme-specific styling
- Component-specific overrides

## Framework Components

### Frontend Styles
- `frontend.min.css`: Core frontend styling
- `e-animation-grow.min.css`: Animation effects
- `e-swiper.min.css`: Slider/carousel styling

### WooCommerce Components
- `woocommerce.min.css`: Core shop styling
- `woo-quick-view.min.css`: Product quick view popup
- `woo-mini-cart.min.css`: Mini cart widget
- `woo-star-font.min.css`: Product rating stars

## Widget Styles

### Core Widgets
- `widget-spacer.min.css`: Spacing control
- `widget-social-icons.min.css`: Social media icons
- `widget-image.min.css`: Image widget styling
- `widget-image-carousel.min.css`: Image slider
- `widget-image-box.min.css`: Image with text boxes

### Special Components
- `preloader.min.css`: Loading animations
- `simple-line-icons.min.css`: Icon font
- `smartslider.min.css`: Smart Slider styling

## Utility Styles

### System Components
- `apple-webkit.min.css`: WebKit-specific fixes
- `cleantalk-public.min.css`: Anti-spam styling
- `cleantalk-email-decoder.min.css`: Email protection

### Typography
- `dmsans.css`: DM Sans font styles
- `roboto.css`: Roboto font styles
- `robotoslab.css`: Roboto Slab font styles
- `redhatdisplay.css`: Red Hat Display font

## Common Classes and Their Usage

### Layout Classes
- `.site-header`: Main header styling
- `.site-content`: Content area
- `.site-footer`: Footer styling
- `.container`: Width constraints
- `.row`: Grid system

### Component Classes
- `.product`: Product display
- `.widget`: Widget containers
- `.menu-item`: Navigation items
- `.btn`: Button styles
- `.card`: Card components

### State Classes
- `.active`: Active states
- `.hover`: Hover effects
- `.disabled`: Disabled states
- `.loading`: Loading states

### Responsive Classes
Media queries handle these breakpoints:
- Desktop: 1200px+
- Tablet: 768px-1199px
- Mobile: <768px

## Special Notes
- All minified files (.min.css) are production-ready versions
- Font files provide typography system
- Widget files contain isolated component styles
- Responsive design implemented across all components