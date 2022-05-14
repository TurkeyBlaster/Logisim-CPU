# Logisim-CPU
A CPU made in Logisim, bundled with tester y86 ASM and raw ROM files. Made in about 2 weeks for CSCE 312 at Texas A&M.

# Features
The CPU is a pipelined, RISC CPU that supports the [Y86 ISA](!http://web.cse.ohio-state.edu/~reeves.92/CSE2421sp13/PracticeProblemsY86.pdf).

# Usage
1. Use the script yo2rom.py found in the testcode directory to convert any .yo files into raw ROM files for Logisim:
```
$ python3 yo2rom.py <.yo_path> [<.raw_path>]
```
2. Load the raw ROM files into the CPU
    1. Open the CPU
    2. Right-click on the component labeled Instruction Memory, and select View Fetch Unit
    3. Right-click on the ROM module, and select Load Image...
    4. Select the raw ROM file
    5. Go back to the main circuit
    6. Right-click on the component labeled Data Memory, and select View Data Memory
    7. Right-click on the RAM module, and select Load Image...
    8. Select the raw ROM file
    9. Go back to the main circuit
3. Select the desired tick speed and run
    1. Simulate > Tick Frequency > ???
    2. Press Ctrl-K
    3. Press Ctrl-K again when the green wire under Halt turns bright
