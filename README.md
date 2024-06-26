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


**Alara Karadeniz**

Function 1:

Name: "_get_error_message"

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/c612660fde5326be83b8cc7207100d6a13241857 

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20GET_ERROR_MESSAGE%20ALARA/get_error_messageBeforeImprovement.png)

Function 2: 

Name: "_getattr_" 

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/c612660fde5326be83b8cc7207100d6a13241857 

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20_GETATTR_%20ALARA/_getattr_BeforeImprovement.png)

**Rares Stefan Dica**

Function 1:

Name: "is_ascii_encoding"

Link to commit: https://github.com/pallets/click/commit/0858e7bffd56ad7ec2fe7c8b7b7bbc855212f133

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20ASCII%20RARES/Coverage%20report%20before/coverageBeforeTests.PNG)

Function 2:

Name: "get_text_stream"

Link to commit: https://github.com/pallets/click/commit/0858e7bffd56ad7ec2fe7c8b7b7bbc855212f133

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20GET_TEXT_STREAM%20RARES/Coverage%20report%20before/coverageBeforeTests.PNG)

**Constantin-Catalin Ionascu**

Function 1:

Name: "_is_binary_reader"

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/3a6c4a6855251c8b261b1f07c62fef0db0de438f

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20IS_BINARY_READER%20CATALIN/coverageBEFORE1.png)

Function 2:

Name: "_is_binary_writer"

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/3a6c4a6855251c8b261b1f07c62fef0db0de438f

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20IS_BINARY_WRITER%20CATALIN/coverageBEFORE2.png)

**Ana-Maria Musca**

Function 1:

Name: "make_str"

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/71d46eed43359d72a335026824a2476b7a56ad5e

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20MAKE_STR%20ANA-MARIA/coverageBeforeTests.PNG)

Function 2:

Name: "should_strip_ansi"

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/71d46eed43359d72a335026824a2476b7a56ad5e 

Screenshot of instrumentation working before adding tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20SHOULD_STRIP_ANSI%20ANA-MARIA/coverageBeforeTests.PNG)

## Coverage improvement

### Individual tests


**Alara Karadeniz**

Test 1:

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/c612660fde5326be83b8cc7207100d6a13241857 

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20GET_ERROR_MESSAGE%20ALARA/get_error_messageBeforeImprovement.png)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20GET_ERROR_MESSAGE%20ALARA/get_error_messageAfterImprovement.png)

The coverage was improved by 100%, initially being 0% and now being 100%. The coverage was improved due creating 3 tests to hit each branch that exists in the function that was not hit before. 

Test 2:

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/c612660fde5326be83b8cc7207100d6a13241857 

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20_GETATTR_%20ALARA/_getattr_BeforeImprovement.png)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20_GETATTR_%20ALARA/_getattr_AfterImprovement.png)

The coverage was improved by 50%, initially being 50% and now being 100%. The coverage was improved due creating 2 tests to hit each branch that exists in the function that was not hit before. 

**Rares Stefan Dica**

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

**Constantin-Catalin Ionascu**

Test 1:

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/3a6c4a6855251c8b261b1f07c62fef0db0de438f

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20IS_BINARY_READER%20CATALIN/coverageBEFORE1.png)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20IS_BINARY_READER%20CATALIN/coverageAFTER1.png)

The coverage improvement was by 100%, initially being 50%. The coverage improved due to the new tests covering both the try and except parts of the function.

Test 2:

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/3a6c4a6855251c8b261b1f07c62fef0db0de438f

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20IS_BINARY_WRITER%20CATALIN/coverageBEFORE2.png)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20IS_BINARY_WRITER%20CATALIN/coverageAFTER2.png)

The coverage improvement was by 100%, initially being 66%. The coverage improved due to the new tests covering both the try and except parts of the function.

**Ana-Maria Musca**

Test 1:

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/71d46eed43359d72a335026824a2476b7a56ad5e

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20MAKE_STR%20ANA-MARIA/coverageBeforeTests.PNG)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%201%20MAKE_STR%20ANA-MARIA/coverageAfterTests.PNG)

The coverage improvement was by 75%, initially being 25%, now it is 100%. The coverage improved because the new test now also covers the case when the input is provided unter byte form, the try and the exception part of the function.

Test 2:

Link to commit: https://github.com/Catalin-Ionascu/clickgroup23/commit/71d46eed43359d72a335026824a2476b7a56ad5e

Screenshot of old coverage: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20SHOULD_STRIP_ANSI%20ANA-MARIA/coverageBeforeTests.PNG)

Screenshot of new coverage after tests: ![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Function%202%20SHOULD_STRIP_ANSI%20ANA-MARIA/coverageAfterTests.PNG)

The coverage improvement was by 50%, initially being 50%, now it is 100%. The coverage improved due to the new tests covering both the case when a color is provided and when a stream argument has a None value.

### Overall

Screenshots of the coverage result before:

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunProject.PNG)

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunReport1.PNG)

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20before/coverageRunReport2.PNG)

Screenshot of the coverage result after:

![alt text](https://github.com/Catalin-Ionascu/clickgroup23/blob/main/screenshotsForREADME/Coverage%20report%20PROJECT%20after/coverageAfterAllTests.PNG)

## Statement of individual contributions


**Alara Karadeniz** Contribution:

My personal contribution consisted of:
- helping in finding a relevant project
- contributing in trying to create the coverage tool
- helping in trying to organize meetings
- doing my part regarding the whole main tasks: instrumenting my functions, screenshotting the results for the before and after coverages

**Rares Dica** Contribution:

My personal contribution consisted of:
- helping in finding a relevant project
- having a big contribution in building the coverage script for calculating the coverage
- dealing with organizational matters such as structuring the repository
- doing my part regarding the whole main tasks: instrumenting my functions, screenshotting the results for the before and after coverages

**Constantin-Catalin Ionascu** Contribution:

My personal contribution consisted of:
- helping in the final moments of finding a relevant project
- forked the repository
- set up organizational rules for using the repository, such as patterns
- assisting team members in setting up different tools, such as coverage.py and lizard
- doing my part regarding the whole main tasks: instrumenting my functions, screenshotting the results for the before and after coverages

**Ana-Maria Musca** Contribution:

My personal contribution consisted of:
- helping in finding a relevant project
- mobilized the team and scheduled meetings for working on the project and checking every member's progress
- having contribution in designing our coverage tool
- doing my part regarding the whole main tasks: instrumenting my functions, screenshotting the results for the before and after coverages
