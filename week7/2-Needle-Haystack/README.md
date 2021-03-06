# Needle Haystack

Implement a program which finds all the indices of occurrence
of a given substring(needle) inside a larger string(haystack).

## Input

The first line will contain the haystack.
The second line will contain the needle.

## Output

On separate lines, output the indices of occurrence of the needle.

## Limits

```
1 <= haystack_len <= 5000000
2 <= needle_len <= 100
```

## Example

Input:

```
<<<<<<< HEAD
The quick brown fox jumps over the lazy dog. The dog was not amused.
=======
thequickbrownfoxjumpsoverthelazydogthedogwasnotamused
>>>>>>> upstream/master
dog
```

Output:

```
<<<<<<< HEAD
40
49
=======
32
38
>>>>>>> upstream/master
```
