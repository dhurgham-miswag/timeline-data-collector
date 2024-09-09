# Timeline Data Collector

A Python-based tool that uses Selenium to automate the collection of order data from a web page, specifically the hourly timeline on `ops.miswag.co`. This script helps in gathering and calculating total orders and dispatch orders from a specific timeline page.

## Features

- **Automated Web Scraping**: Uses Selenium to automate login and data collection from a specific web page.
- **Order Data Extraction**: Collects total orders and dispatch orders from the timeline, from the last block until 4 to 5 PM.
- **Customizable Workflow**: Allows users to manually log in and set desired settings before starting the data collection process.
- **User Interaction**: Waits for user input to proceed at different steps, ensuring flexibility in the data collection process.

## Getting Started

### Prerequisites

- **For Python Script Version:**
  - Python 3.x
  - Google Chrome browser
  - [Chromedriver](https://sites.google.com/chromium.org/driver/) (make sure to match the version with your installed Chrome browser)
  - Required Python libraries: Selenium, Colorama

- **For Executable Version:**
  - No prerequisites are needed. The executable version comes bundled with all dependencies and does not require `chromedriver`.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dhurgham-miswag/timeline-data-collector.git
   cd timeline-data-collector
