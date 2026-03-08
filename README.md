
SOFTWARE TESTING & RELIABILITY PROJECTS

Overview
This repository contains three projects related to software testing and reliability. 
Each project focuses on a different testing technique and applies it to real software tools or libraries. 
Detailed explanations and results are available in the reports included with each project.

1. Combinatorial Testing of csvtojson

Description
This project tests the csvtojson parser by exploring its configuration options using structured test generation.

What was done
- Modeled 18 configuration parameters of the csvtojson tool.
- Added constraints between parameters to avoid invalid combinations.
- Used ACTS (Automated Combinatorial Testing for Software) to generate t‑way interaction test cases.
- Wrote Python scripts to:
  - generate test inputs
  - produce expected outputs
  - run the tool automatically
  - compare outputs and detect differences.

Purpose
Show how combinatorial testing can explore many parameter combinations efficiently and help detect issues caused by certain parameter interactions.

2. Mutation Testing of Jsoup and Polly

Description
This project evaluates how effective existing test suites are by using mutation testing. 
Mutation testing introduces small changes (mutations) in the code to see whether the test suite detects them.

Libraries tested
- Jsoup (Java HTML parsing library)
- Polly (.NET resilience and fault-handling library)

Tools used
- PIT (PITest) for Java mutation testing
- Stryker.NET for mutation testing in .NET

What was analyzed
- Line coverage
- Mutation score
- Test strength
- Mutants that survived testing

Purpose
Show that even when code coverage is high, tests may still miss certain logical errors.

3. Coverage-Guided Fuzzing of Parser Libraries

Description
This project uses fuzz testing to check how parser libraries behave when they receive unexpected or random input.

Libraries tested
- http-parser (HTTP parser written in C)
- json-c (JSON parser written in C)

Tools used
- LibFuzzer with LLVM instrumentation
- AFL++ (American Fuzzy Lop Plus Plus)

What was done
- Built fuzzing harnesses to connect the libraries to the fuzzing tools.
- Provided seed inputs and dictionaries to guide the fuzzing process.
- Ran long fuzzing sessions to explore different execution paths.
- Reviewed coverage results after the runs.

Purpose
Test how stable these parsers are when handling many different types of inputs.

Summary
These projects explore three different testing approaches used in software development.

Combinatorial Testing
Systematically tests different configuration combinations.

Mutation Testing
Measures how strong a test suite is by introducing small faults.

Fuzz Testing
Automatically generates many inputs to test how software behaves in unusual situations.

Together, these projects demonstrate practical experience with modern software testing techniques and tools.
