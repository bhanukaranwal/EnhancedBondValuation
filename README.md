# Enhanced Bond Valuation Calculator

[![CI](https://github.com/username/EnhancedBondValuation/actions/workflows/ci.yml/badge.svg)](https://github.com/username/EnhancedBondValuation/actions)
[![Coverage](https://codecov.io/gh/username/EnhancedBondValuation/branch/main/graph/badge.svg)](https://codecov.io/gh/username/EnhancedBondValuation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![C++ Version](https://img.shields.io/badge/c++-17%2B-blue)

A professional, feature-rich bond analytics platform inspired by Bloomberg Terminal's functionality. This tool provides comprehensive bond valuation, yield calculation, and risk analysis, blending Python's ease of use with C++'s high performance.

## ✨ Features

* **Core Analytics**: Calculate clean/dirty prices, YTM, YTC, YTW, duration, and convexity.
* **Diverse Bond Support**: Fixed-rate, zero-coupon, callable, puttable, and inflation-linked bonds.
* **Advanced Metrics**: Option-Adjusted Spread (OAS), Value-at-Risk (VaR), and credit risk modeling.
* **Bloomberg-Style Features**: BVAL-like confidence scoring, advanced bond search, and real-time data integration.
* **AI-Driven Insights**: Predict yield trends and receive bond recommendations.
* **Portfolio Management**: Aggregate portfolio metrics and perform sophisticated scenario analysis.

## 🚀 Quickstart

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/username/EnhancedBondValuation.git](https://github.com/username/EnhancedBondValuation.git)
    cd EnhancedBondValuation
    ```

2.  **Set up the environment:**
    ```bash
    # Using Conda (recommended)
    conda env create -f environment.yml
    conda activate bond-valuation

    # Or using pip
    pip install -r requirements.txt
    ```

3.  **Run a sample calculation:**
    ```bash
    python scripts/sample_run.py
    ```

4.  **Build and run C++ components:**
    ```bash
    # Ensure you have CMake and a C++ compiler
    cmake -S src/cpp -B build
    cmake --build build
    ./build/tests/test_suite
    ```

## 📊 Demo

![Dashboard](docs/examples/dashboard.gif)
*(Demo GIF placeholder)*

---

## LICENSE

```text
MIT License

Copyright (c) 2025 [Your Name or Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
