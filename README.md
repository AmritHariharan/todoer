# todoer

## About

todoer is a python script that takes your code as an input, parses it looking for comments that contain predefined tags such as `TODO:` or `FIXME:` and generates a todo list of these comments.

## Usage

```bash
$ python todoer.py INPUT_FILE (OUTPUT_FILE.md)
```

if an output filename is not specified, todoer will output to `output.md`

## Example

It takes a file like the one below:

```c++
// comment pt 1
//

using namespace std;

int main() {
	cout << "do you even #webscale bro?" << endl; // TODO: add more #buzzwords
	cout << "honestly..." << endl;
	// FIXME: this program does jack shit
	// bruh
} // main()

//end of file
```

and outputs the following markdown file.

```
# Todo list for `input.cpp`
-----
## TODO:
- [ ] line 7:  add more #buzzwords
-----
## FIXME:
- [ ] line 9:  this program does jack shit
-----
```

## Todo

## Wishlist

- [ ] get it to work with block comments (regex?)
- [x] show line numbers
- [x] markdown output
- [x] make output filename argument optional
- [ ] turn this into a VSCode extension?