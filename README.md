# Software Testing & Reliability Projects

This repository contains three projects focused on **software testing and reliability techniques**.  
Each project applies a different testing approach to real software tools or libraries.  
Detailed results and analysis are included in the reports for each project.

# 1. Combinatorial Testing – csvtojson

## Description
This project tests the **csvtojson** parser by modeling its configuration space and generating systematic test cases.

## What I Did
- Modeled **18 configuration parameters** of the csvtojson tool.
- Added **constraints between parameters** to avoid invalid combinations.
- Used **ACTS (Automated Combinatorial Testing for Software)** to generate **t-way interaction test cases**.
- Built Python scripts to:
  - Generate test inputs
  - Produce expected outputs (oracle)
  - Run the tool automatically
  - Compare outputs and detect mismatches.

## Purpose
Demonstrates how **combinatorial testing** can efficiently explore large configuration spaces and detect issues caused by parameter interactions.


# 2. Mutation Testing – Jsoup & Polly

## Description
This project evaluates how effective existing test suites are using **mutation testing**.  
Mutation testing introduces small changes (mutants) into the source code to see whether the test suite detects them.

## Libraries Tested
- **Jsoup** – Java HTML parsing library  
- **Polly** – .NET resilience and fault-handling library

## Tools Used
- **PIT (PITest)** for Java mutation testing
- **Stryker.NET** for mutation testing in .NET

## What I Analyzed
- Line coverage
- Mutation coverage
- Test strength
- Surviving mutants

## Purpose
Shows that **high code coverage does not always mean strong tests**, and mutation testing helps reveal gaps in existing test suites.


# 3. Coverage-Guided Fuzzing – http-parser & json-c

## Description
This project uses **coverage-guided fuzz testing** to check how parser libraries behave when they receive unexpected or random input.

## Libraries Tested
- **http-parser** – C HTTP request/response parser
- **json-c** – C library for JSON parsing

## Tools Used
- **LibFuzzer** with LLVM instrumentation
- **AFL++ (American Fuzzy Lop Plus Plus)**

## What I Did
- Built **fuzzing harnesses** to connect the libraries to the fuzzing tools.
- Provided **seed inputs and dictionaries** to guide fuzzing.
- Ran long fuzzing sessions to explore different execution paths.
- Analyzed coverage results after fuzzing.

## Purpose
Used fuzz testing to evaluate how stable these parsers are when handling many different input cases.


# Summary

These projects explore three different testing approaches:

| Method | Focus |
|------|------|
| Combinatorial Testing | Systematically explores configuration combinations |
| Mutation Testing | Evaluates the strength of test suites |
| Fuzz Testing | Tests software behavior with random inputs |

Together, these projects demonstrate practical experience with **modern software testing tools and reliability techniques**.
