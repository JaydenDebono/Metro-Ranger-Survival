# Technical Reflection: Metro Ranger Survival

1.Using SEC level Computing to create a custom project
I used my Computing notes from year 9 to year 11 to build this project, I also learned a few extra things like how to forget labels and update the UI
through Youtube tutorials

2. State Management in GUI Development
Working with Tkinter, I discovered that UI labels don't always clear themselves automatically between game sessions. I had to learn how to manage "Global States" effectively.
The Solution: I developed a reset protocol that clears old labels (encounters, loot, and status) before a new game begins. This prevents "ghosting" where information from a previous death appears in a new life.

3. Feature Triaging and Deadlines
With a strict deadline for the SSWES submission, I had to make the professional decision to prioritize Stability over Complexity. 
The Lesson: I learned that in the games industry, a perfectly functional core loop(Movement and Survival) is more valuable than a wide range of buggy features. I focused on polishing the movement and resource-taxing logic to ensure a bug-free experience for the reviewer.

