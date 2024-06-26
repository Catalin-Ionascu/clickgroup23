# Report for Assignment 1

## Project chosen

Name: Click

URL: https://github.com/pallets/click

Number of lines of code and the tool used to count it: 14,037 Lizard

Programming language: Python

## Coverage measurement

### Existing tool

The coverage tool used was coverage.py with command coverage run -m pytest, coverage report and coverage html .

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunProject.PNG)

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunReport1.PNG)

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunReport2.PNG)

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

Rares Stefan Dica

Function 1:

Name: "is_ascii_encoding"

Link to commit: https://github.com/pallets/click/commit/0858e7bffd56ad7ec2fe7c8b7b7bbc855212f133

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20ASCII%20RARES/Coverage%20report%20before/coverageBeforeTests.PNG)

Function 2:

Name: "get_text_stream"

Link to commit: https://github.com/pallets/click/commit/0858e7bffd56ad7ec2fe7c8b7b7bbc855212f133

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20GET_TEXT_STREAM%20RARES/Coverage%20report%20before/coverageBeforeTests.PNG)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

Rares Stefan Dica

Test 1:

Link to commit: https://github.com/pallets/click/commit/0858e7bffd56ad7ec2fe7c8b7b7bbc855212f133

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20ASCII%20RARES/Coverage%20report%20before/coverageBeforeTests.PNG)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20ASCII%20RARES/Coverage%20report%20after/coverageAfterTests.PNG)

The coverage improvement was by 50%, initially being 50% now it is 100%. The coverage improved because the new test now also covers the exception part of the function.

Test 2:

Link to commit: https://github.com/pallets/click/commit/0858e7bffd56ad7ec2fe7c8b7b7bbc855212f133

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20GET_TEXT_STREAM%20RARES/Coverage%20report%20before/coverageBeforeTests.PNG)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20GET_TEXT_STREAM%20RARES/Coverage%20report%20after/coverageAfterTests.PNG)

The coverage improvement was by 100%, initially being 0%. The coverage improved due to the new tests covering both the try and error parts of the function.

### Overall

Screenshots of the coverage result before:

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunProject.PNG)

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunReport1.PNG)

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunReport2.PNG)

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group> TODO!!!!

## Statement of individual contributions

<Write what each group member did>

Rares Dica Contribution:

My personal contribution consisted of:
- helping in finding a relevant project
- having a big contribution in building the coverage script for calculating the coverage
- dealing with organizational matters such as structuring the repository
- doing my part regarding the whole main tasks: instrumenting my functions, screenshoting the results for the before and after coverages
