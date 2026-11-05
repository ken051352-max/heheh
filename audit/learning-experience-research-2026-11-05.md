# Learning-experience research — 5 November 2026

This is a new research record for the study-path and navigation work. It does not replace the [earlier resource audit](research-2026-11-05.md). Sources were inspected using live Exa search/fetch and, for lecture artifacts, direct HTTP requests. Findings below distinguish inspected content, access checks and design judgments. No real six-week student trial was conducted.

## Decisions supported by research

### Keep one beginner lecture route; make reading selective

The [CS50P Functions and Variables page](https://cs50.harvard.edu/python/weeks/0/) exposes a lecture, notes, transcript, source, public player and downloadable video. Its actual topic list includes functions, arguments, return values, variables, numeric types and scope. A small portion can therefore support Week 0, followed by the remaining portions of the same lesson; switching courses and completing three browser projects are unnecessary before beginning the roadmap. This is a sequencing judgment, not a measured completion-rate improvement. Hosted submissions and accounts are separate from public lecture access.

[CS50 SQL Querying](https://cs50.harvard.edu/sql/weeks/0/) and [Relating](https://cs50.harvard.edu/sql/weeks/1/) were checked by retrieving their actual HTML. Both contain public video-player, MP4, audio and transcript links. The text extraction alone omitted those lecture controls, so it was insufficient to establish access. A byte-range request to each 360p MP4 returned **206, `video/mp4`, 64 bytes with an MP4 `ftypisom` signature**. This establishes an accessible video artifact at inspection time, not full playback, availability in every region or completion of the course. The small SQL project starts only after demonstrated M1 competence; a few introductory SQL lessons do not complete M8a.

### Retain the paid principal Python book and a legal free alternative

[No Starch's third-edition page](https://nostarch.com/python-crash-course-3rd-edition) identifies Eric Matthes, *Python Crash Course*, December 2022, and the chapter-level contents. It explicitly includes `pytest`, `pathlib`, exercises and projects. The [licensed O'Reilly catalogue](https://www.oreilly.com/library/view/python-crash-course/9781098156664/) exposes the detailed third-edition contents: chapter 4 includes List Comprehensions; chapter 8 includes Storing Your Functions in Modules; chapter 10 covers Files and Exceptions, including `try`/`except` and JSON; chapter 11 covers Testing Your Code; chapter 17 covers Working with APIs. The catalogue's January 2023 digital listing is not evidence of another edition. Its full book is paid; a public contents list is not free full-text access.

Independent assessments disagree in useful ways:

- [Serdar Yegulalp's InfoWorld review, 11 January 2023](https://www.infoworld.com/article/2337756/plunge-into-python-with-python-crash-course-3rd-edition.html) praises the exercises, readable explanations, projects and testing chapter, while noting sequencing reservations around exceptions and package installation.
- [Alex Armstrong's I Programmer review](https://www.i-programmer.info/bookreviews/62-python/16633-python-crash-course-3ed.html) criticizes conceptual depth, feature-by-feature teaching and reliance on following project code. This is a substantive counterpoint, not a reason to add every missing topic to the first semester.
- [Will Vincent's comparison, updated 21 August 2025](https://wsvincent.com/best-python-books/) describes *Python Crash Course* as a patient fundamentals-and-projects introduction, *Automate the Boring Stuff* as practical automation, and *Fluent Python* as a next step for an already familiar programmer. This is an individual specialist recommendation, not consensus. Metadata and technical details are checked against publishers rather than inherited from the review.

Decision: keep *Python Crash Course* as the paid principal and use selected sections alongside CS50P and original exercises. Pair reading with explanation, debugging and a changed example so copying a worked project is not mistaken for independent skill. Buying the book or completing its three large projects is not an entry gate.

[Sweigart's third-edition contents](https://automatetheboringstuff.com/3e/) and [No Starch's listing](https://nostarch.com/automate-boring-stuff-python-3rd-edition) identify *Automate the Boring Stuff with Python*, Al Sweigart, third edition, April 2025. The author supplies legal free web chapters. The contents map basics to chapters 1–8, files to 10, command-line programs to 12, SQLite to 16, and CSV/JSON/XML to 18. The [actual functions chapter](https://automatetheboringstuff.com/3e/chapter4.html) was inspected for its examples of definitions, calls, parameters, return values and scope. Use this as an alternative for the same topic, not a second book assignment. Most book chapters were not read in full, and all examples were not executed.

### Use retrieval and revisiting, with feedback and modest claims

[Dunlosky, Rawson, Marsh, Nathan and Willingham (2013)](https://journals.sagepub.com/doi/10.1177/1529100612453266) review ten study techniques across learning conditions, learner characteristics, materials and assessment tasks. The publicly accessible publisher abstract and conclusions assign high utility to practice testing and distributed practice, and moderate utility to self-explanation, elaborative interrogation and interleaving. The review discusses limitations and uneven evidence; it does not test this roadmap, prove transfer to every programming task or prescribe a universal time interval.

Decision: include a brief attempt from memory, inspect feedback, correct the error and revisit the skill in a later session. A learner who can repeat a memorized answer still needs to debug and adapt the idea. The six-week log records time and friction to adjust planning assumptions; its duration is a manageable design choice, not an experimentally established optimum.

### Scaffold procedures, then assess a changed problem

[Margulieux, Morrison and Decker (2020)](https://link.springer.com/article/10.1186/s40594-020-00222-7), *Reducing withdrawal and failure rates in introductory programming with subgoal labeled worked examples*, is an open original study of 265 students in multiple introductory programming sections. Its abstract, introduction and instructional-design discussion were inspected. The intervention improved formative quiz performance; average summative exam performance was **not statistically better**. Reported withdrawal/failure differences in those classes do not predict this learner's outcome. The instructional materials studied Java, so adapting the idea to a Python self-study repository requires judgment.

[Muldner, Jennings and Chiarelli (2022)](https://dl.acm.org/doi/full/10.1145/3560266), *A Review of Worked Examples in Programming Activities*, is a narrative review of code-tracing and code-generation examples. The author abstract and introductory/theoretical sections were inspected, not the page's separately marked AI-generated summary. It explains that benefits depend on learner experience, example design, integration and constructive engagement; examples can become less useful as experience grows. It also identifies research gaps.

Decision: give each project named stages, observable behavior, small fixtures and targeted hints, with a separate reference. Use a changed input or requirement for the final independent check. Allow experienced students to demonstrate equivalence and skip repeated instruction. A supplied reference is a learning and verification aid, not proof that a learner has implemented the skill.

## Review-driven navigation changes

Inspection found that M9–M17 already had meaningful core outcomes and projects, but large mixed core/depth topic maps appeared before the course and project. The implementation adds small first actions, direct project anchors and local contents, and folds the breadth maps into optional disclosure. Required outcomes, practical contracts and completion rubrics remain visible. The teaching material is preserved; this is a presentation judgment supported by the observed reading order, not a controlled usability result.

Course pages now expose prerequisites, one concrete first task, and completion evidence before long reference menus. The portfolio release table becomes short sections with the same inbound anchors. Book and companion pages point back to the active sequence instead of suggesting all resources are simultaneous work. Advanced modules remain later study; the first-semester path does not introduce agents or distributed infrastructure as beginner requirements.

## Access limitations and alternatives used

- Direct HTTP retrieval of No Starch's product HTML returned 403. Exa returned publisher content; the licensed O'Reilly contents supplied the missing section detail. This is source-content inspection through one route, not proof every browser or client can access the publisher page.
- An attempted general retrieval-practice guide URL returned `CRAWL_NOT_FOUND`. The decision instead uses the original published review; the failed URL was not added as a required resource.
- Search results containing unofficial full-book copies were not used. Author/publisher and licensed catalogues supplied metadata and selected public content.
- Video source links and sampled bytes were inspected, not every minute of video or the regional player behavior. Lecture access should be rechecked when reported inaccessible.
- Existing advanced references and prior technical corrections were preserved. This pass does not claim a fresh execution of every vendor integration, a reading of every book, a new employer-market forecast, or a real student pilot.

Implementation files and retained choices are listed in [the depth-review inventory](depth-review-2026-11-05.json). Fresh repository checks and visual/structural walkthroughs belong in the separate validation record.

## Final access challenge and concrete corrections

A targeted follow-up on 2026-11-05 retried the 39 warnings from the bounded external scan using native `curl` GET requests with certificate checks enabled. Six teaching pages had already succeeded in the first follow-up batch; the remaining 33 used four workers and 12-second request limits. In total, 33 warned URLs were retrieved and six original endpoints remained unverified. The external report preserves the original automated results and adds the separate follow-up; these are different observations, not a rewritten successful scan.

- Exa and native HTML retrieval both recovered the MIT 18.01SC, 18.06SC, 6.006 and 18.650 pages, Data School's pandas video page and Hyndman's FPP3 video announcement. MIT's descriptions identify their lecture resources; Data School's actual HTML exposes individual public YouTube links and Hyndman's page exposes the playlist. This confirms the resource menus and declared access, not full video playback or current compatibility of every older code example.
- The old Stanford CS145 URL returned HTTP 200 but **only an empty directory**. Searching for actual course archives led to [CS145 Fall 2020](https://cs145-fa20.github.io/). Its schedule/policies identify SQL, indexes, query optimization, transactions and design theory, public slides, fuller CS prerequisites and Canvas recordings. Its SQL Part I and Design Theory Google Slides links returned `CRAWL_EMPTY_CONTENT` through Exa. Native unauthenticated PDF and text exports succeeded instead; the design text was inspected for dependencies, BCNF/3NF and lossless decomposition, and the SQL text for its introductory query examples. M8a now uses this explicitly dated, optional slide archive. CS50 SQL remains the free lecture default; no claim of public CS145 videos or free ongoing cloud credits is made.
- Nielsen's book failed HTTPS hostname validation with native curl too. Its existing [HTTP book address](http://neuralnetworksanddeeplearning.com/) returned the book, and Exa independently extracted the author/title/chapter contents there. The book shelf now uses that working public address. No certificate verification was disabled. A guessed replacement author homepage returned a hosting placeholder and was rejected.
- The other unresolved endpoints were Observable Plot (429), Columbia's statistics blog (403), Stanford CS103 (connection reset), a NeurIPS PDF (partial download before timeout) and a journal article (403). A 200 response before an incomplete PDF transfer was **not** counted as completed retrieval. No replacement was inferred from those transport failures.

These findings justify specific navigation/access corrections; they do not establish that every linked book was read or every video watched.
