# Profile
"A program for creating a profile of a MSA"

This program based on the sequences of the MSA it gets, creates a profile. Moreover, it can return the maximum sequence of a given sequence which matchs with the given one.
* I assumed pseudocount = 1 to avoid log(0) occurance. You can change it in the program.
* I also wrote this code for proteins; therefore, the value "B" is equal to 20 which the number of different types of naturally occurring amino acidss. You can change it to 4 for DNA and RNA, as well. (That is, the value "B" is equal to the number of different type of unit which make the sequence.)

## Input
- line 1: n =  size of MSA
- line 2, ..., n + 1: MSA
- line n + 2: sequence for matiching with profile

## Output
A sequence, part of the given sequence, that has the maximum score with the profile of MSA.

## Example
![image](https://user-images.githubusercontent.com/47606879/143487430-6624144f-23a7-47cf-885c-10eb3931f539.png)
