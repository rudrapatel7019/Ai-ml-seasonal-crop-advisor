#  Modular Seasonal Crop Advisor (MSCA)

> A lightweight Python CLI application that instantly recommends vegetables and plants to grow based on the current season — built with a clean modular design, zero external dependencies, and robust error handling.

---

##  Problem Statement

Many novice and intermediate gardeners face difficulty tracking the correct planting windows for different crops throughout the year, leading to reduced yields and wasted resources.

**MSCA** solves this with a quick, accessible, offline terminal tool — no internet, no pip installs, no setup. Just run and get instant recommendations.

---

##  Features

-  Curated crop lists for all **4 seasons**: Spring, Summer, Autumn, Winter
-  **Case-insensitive input** — `WINTER`, `winter`, `WiNtEr` all work
-  **Robust error handling** — invalid inputs print a clear message, never crash
-  **Continuous input loop** — keeps running until you type `exit`
-  **Empty input guard** — blank entries prompt the user again cleanly
-  **Graceful exit** — terminates with a goodbye message
-  **Zero external dependencies** — uses Python standard library only (`sys`)

---

##  Modular Architecture

The application lives in a **single file** but is internally structured into three clearly separated functional modules:

| Module | Function | Responsibility |
|---|---|---|
| **Data Module** | `get_default_crop_data()` | Returns the crop dictionary — all dataset lives here |
| **Utility Module** | `suggest_crops(season, crop_data)` | Validates input, looks up and prints crop recommendations |
| **Application Module** | `main()` | Loads data, runs the input loop, handles exit and edge cases |

The crop dataset is stored as a **Python Dictionary** enabling **O(1) constant-time lookups** — efficient regardless of dataset size.

---

##  Tech Stack

| Component | Detail |
|---|---|
| Language | Python 3.x |
| Core Data Structure | Python Dictionary (O(1) key-value lookup) |
| Input Handling | `input()` with `.strip()` and `.lower()` |
| Interface | Command Line Interface (CLI) |
| External Dependencies | **None** — standard library only (`sys`) |
| Version Control | Git & GitHub |

---

##  Getting Started

### Prerequisites

- Python 3.x installed on your system
- No `pip install` required

### Installation & Run

**1. Clone the repository**
```bash
git clone https://github.com/rudrapatel7019/Seasonal_crop_advisor.git
cd Seasonal_crop_advisor
```

**2. Run the script**
```bash
python seasonal_crop_advisor.py
```

---

##  Usage Example

```
 Welcome to the Single-File Seasonal Crop Advisor!
Available seasons: Spring, Summer, Autumn, Winter.

Enter the current season (or type 'exit'): Spring

---  Crop Suggestions for Spring  ---
  1. Lettuce (Leafy Greens)
  2. Peas
  3. Radishes
  4. Spinach
  5. Broccoli (starting indoors)
  6. Potatoes
---------------------------------------------

Enter the current season (or type 'exit'): aUtUmN

---  Crop Suggestions for Autumn  ---
  1. Kale
  2. Carrots
  3. Garlic (for overwintering)
  4. Pumpkins and Winter Squash
  5. Cabbage
  6. Beets
---------------------------------------------

Enter the current season (or type 'exit'): monsoon

 Error: 'monsoon' is not a recognized season.
Please ensure you enter one of the following: Spring, Summer, Autumn, or Winter.

Enter the current season (or type 'exit'): exit
Thank you for using the Crop Advisor. Happy gardening!
```

---

##  Crop Data Reference

| Season | Crops |
|---|---|
| **Spring** | Lettuce, Peas, Radishes, Spinach, Broccoli (indoors), Potatoes |
| **Summer** | Tomatoes, Peppers, Zucchini & Squash, Corn, Cucumbers, Beans, Eggplant |
| **Autumn** | Kale, Carrots, Garlic (overwintering), Pumpkins & Winter Squash, Cabbage, Beets |
| **Winter** | Brussels Sprouts, Leeks, Hardy Kale & Spinach (under cover), Overwintered Garlic, Cover Crops |

> Note: Suggestions are general and may vary based on specific climate and region.

---

##  Testing

Manual test cases to verify all functionality:

| Test Case | Input | Expected Result |
|---|---|---|
|  Positive Test | `Spring` | Prints numbered list of 6 spring crops |
|  Edge Case (case sensitivity) | `aUtUmN` | Correctly matches autumn, prints crop list |
|  Negative Test (invalid input) | `monsoon` | Error: "is not a recognized season." |
|  Empty Input | *(blank enter)* | Prompts user again without crashing |
|  Exit Flow | `exit` | Terminates with goodbye message |

---

##  Project Structure

```
Seasonal_crop_advisor/
│
├── seasonal_crop_advisor.py   # Single-file application (data + logic + interface)
├── project_statement.py       # Project problem statement and scope
└── README.md                  # This file
```

---

##  Target Users

- Beginner and intermediate **home gardeners** needing seasonal planting guidance
- **Students** looking for a simple, accurate crop reference tool
- **Python learners** wanting a clean, functional single-file project example

---

##  Author

**Rudra Patel**
- GitHub: [@rudrapatel7019](https://github.com/rudrapatel7019)

---

##  License

This project is open source and available under the [MIT License](LICENSE).
